from django.db import IntegrityError
from rest_framework import serializers
from dislikes.models import Dislike


class DislikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Dislike
        fields = ['id', 'created_at', 'owner', 'post']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntregrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
