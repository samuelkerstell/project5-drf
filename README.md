# Golf Shot API
## Project goals
This project is the Django Rest Framework API for the Golf Shot Web App.


Golf Shot is a social media website where golfers all over the world can share their golf life!
The primary goal of this project is to develop a user-friendly web application that allows image sharing among users. The platform aims to create a golf community where golfers can upload their images and interact through likes and comments on those images shared by others.



## Table of contents
- [Golf Shot](#golf-shot)
  * [Project goals](#project-goals)
  * [Table of contents](#table-of-contents)
  * [Planning](#planning)
    + [Data models](#data-models)
      - [**Profile**](#--profile--)
  * [API endpoints](#api-endpoints)
  * [Frameworks, libraries and dependencies](#frameworks--libraries-and-dependencies)
    + [django-cloudinary-storage](#django-cloudinary-storage)
    + [dj-allauth](#dj-allauth)
    + [dj-rest-auth](#dj-rest-auth)
    + [djangorestframework-simplejwt](#djangorestframework-simplejwt)
    + [dj-database-url](#dj-database-url)
    + [psychopg2](#psychopg2)
    + [python-dateutil](#python-dateutil)
    + [django-recurrence](#django-recurrence)
    + [django-filter](#django-filter)
    + [django-cors-headers](#django-cors-headers)
  * [Testing](#testing)
    + [Manual testing](#manual-testing)
    + [Python validation](#python-validation)
    + [Resolved bugs](#resolved-bugs)
      - [Bugs found while testing the API in isolation](#bugs-found-while-testing-the-api-in-isolation)
      - [Bugs found while testing the React front-end](#bugs-found-while-testing-the-react-front-end)
    + [Unresolved bugs](#unresolved-bugs)
  * [Deployment](#deployment)
  * [Credits](#credits)


## Planning
User stories were made in the frontend [repository](https://github.com/samuelkerstell/project5-react/issues)

The project's structure was influenced by the [drf-api walkthrough](https://github.com/Code-Institute-Solutions/drf-api), primarily due to time constraints and the specific requirements outlined in Project 5 assessments. I expanded upon this foundation by adding a dislike model with logic in the frontend to fluidily coexist with the like model.


### Data models
#### The following models have been created for this project:
  - User
  - Profile( automatically created when creating a User)
  - Post (to display and create posts)
  - Comment (to display and create comments on posts)
  - Like (to like a post)
  - Dislike (to dislike a post)
  - Follower (to follow other users)


Custom models implemented for Golf Shot are:
#### Entity Relationship Diagram
![diagram](/readme-asset/Blankdiagram(1).png)

## API endpoints


## Frameworks, libraries and dependencies
The TribeHub API is implemented in Python using [Django](https://www.djangoproject.com) and [Django Rest Framework](https://django-filter.readthedocs.io/en/stable/).

The following additional utilities, apps and modules were also used.

### django-cloudinary-storage
https://pypi.org/project/django-cloudinary-storage/


### dj-allauth
https://django-allauth.readthedocs.io/en/latest/


### dj-rest-auth
https://dj-rest-auth.readthedocs.io/en/latest/introduction.html


### djangorestframework-simplejwt
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/


### dj-database-url
https://pypi.org/project/dj-database-url/


### psychopg2
https://pypi.org/project/psycopg2/


### python-dateutil
https://pypi.org/project/python-dateutil/


### django-filter
https://django-filter.readthedocs.io/en/stable/


### django-cors-headers
https://pypi.org/project/django-cors-headers/


## Testing
### Manual testing
* #### User
    * Logged out users can create an account ✓
    * Logged in users can sign in with their created account ✓


* #### Profiles App
    * Logged out users can list profiles ✓
    * Logged out user can retrieve profiles with a valid id ✓
    * Logged out user can't retrieve profiles with an invalid id ✓
    * Logged in users can change Name of the profile they own ✓
    * Logged in users can't change Name of a profile they don't own ✓
    * Logged out users can't change Name of a profile ✓
    * Logged in users can change content/bio of the profile they own ✓
    * Logged in users can't change content/bio of a profile they don't own ✓
    * Logged out users can't change content/bio of a profile ✓
    * Logged in users can change image of the profile they own ✓
    * Logged in users can't change image of a profile they don't own ✓
    * Logged out users can't change image of a profile ✓


* #### Posts App
    * Logged out users can list posts ✓
    * Logged out users can't create a post ✓
    * Logged out users can retrieve a post with a valid id ✓
    * Logged out users can't retrieve a post with an invalid id ✓
    * Logged in users can create a post ✓
    * Logged in users can update a post they own ✓
    * Logged in users can delete a post they own ✓
    * Logged in users can't update a post they don't own ✓
    * Logged in users can't delete a post they don't own ✓


* #### Comments App
    * Logged out users can list comments ✓
    * Logged out users can't create a comment ✓
    * Logged out users can retrieve a comment with a valid id ✓
    * Logged out users can't retrieve a comment with an invalid id ✓
    * Logged in users can create a comment ✓
    * Logged in users can update a comment they own ✓
    * Logged in users can delete a comment they own ✓
    * Logged in users can't update a comment they don't own ✓
    * Logged in users can't delete a comment they don't own ✓


* #### Followers App
    * Logged out users can list followers ✓
    * Logged out users can't create a follow ✓
    * Logged out users can retrieve a follower with a valid id ✓
    * Logged out users can't retrieve a follower with an invalid id ✓
    * Logged in users can create a follow ✓
    * Logged in users can delete a follow ✓
    * Logged in users can't delete a follow they don't own ✓


* #### Likes App
    * Logged out users can list likes ✓
    * Logged out users can't create a like ✓
    * Logged out users can retrieve a like with a valid id ✓
    * Logged out users can't retrieve a like with an invalid id ✓
    * Logged in users can create a like ✓
    * Logged in users can delete a like ✓
    * Logged in users can't delete a like they don't own ✓


* #### Dislikes App
    * Logged out users can list dislikes ✓
    * Logged out users can't create a dislike ✓
    * Logged out users can retrieve a dislike with a valid id ✓
    * Logged out users can't retrieve a dislike with an invalid id ✓
    * Logged in users can create a dislike ✓
    * Logged in users can delete a dislike ✓
    * Logged in users can't delete a dislike they don't own ✓

    

### Python validation

Code errors and style issues were detected using the Pylance linter in VSCode, and immediately fixed throughout development.
All files containing custom Python code were then validated using the [Code Institute Python Linter](https://pep8ci.herokuapp.com/):


### Resolved bugs

#### Bugs found while testing the API in isolation


#### Bugs found while testing the React front-end
dj-rest-auth/registration/ - fixed by adding trailing slash


## Deployment
The Golf Shot API is deployed to Heroku, using an ElephantSQL Postgres database.
To duplicate deployment to Heroku, follow these steps:

- Fork or clone this repository in GitHub.
- You will need a Cloudinary account to host user profile images.
- Login to Cloudinary.
- Select the 'dashboard' option.
- Copy the value of the 'API Environment variable' from the part starting `cloudinary://` to the end. You may need to select the eye icon to view the full environment variable. Paste this value somewhere for safe keeping as you will need it shortly (but destroy after deployment).
- Log in to Heroku.
- Select 'Create new app' from the 'New' menu at the top right.
- Enter a name for the app and select the appropriate region.
- Select 'Create app'.
- Select 'Settings' from the menu at the top.
- Login to ElephantSQL.
- Click 'Create new instance' on the dashboard.
- Name the 'plan' and select the 'Tiny Turtle (free)' plan.
- Select 'select region'.
- Choose the nearest data centre to your location.
- Click 'Review'.
- Go to the ElephantSQL dashboard and click on the 'database instance name' for this project.
- Copy the ElephantSQL database URL to your clipboard (this starts with `postgres://`).
- Return to the Heroku dashboard.
- Select the 'settings' tab.
- Locate the 'reveal config vars' link and select.
- Enter the following config var names and values:
    - `CLOUDINARY_URL`: *your cloudinary URL as obtained above*
    - `DATABASE_URL`: *your ElephantSQL postgres database URL as obtained above*
    - `SECRET_KEY`: *your secret key*
    - `ALLOWED_HOST`: *the url of your Heroku app (but without the `https://` prefix)*
- Select the 'Deploy' tab at the top.
- Select 'GitHub' from the deployment options and confirm you wish to deploy using GitHub. You may be asked to enter your GitHub password.
- Find the 'Connect to GitHub' section and use the search box to locate your repo.
- Select 'Connect' when found.
- Optionally choose the main branch under 'Automatic Deploys' and select 'Enable Automatic Deploys' if you wish your deployed API to be automatically redeployed every time you push changes to GitHub.
- Find the 'Manual Deploy' section, choose 'main' as the branch to deploy and select 'Deploy Branch'.
- Your API will shortly be deployed and you will be given a link to the deployed site when the process is complete.

## Credits
- [Django documentation](https://www.djangoproject.com)
- [Django Rest Framework documentation](https://www.django-rest-framework.org)
- [django-filter documentation](https://django-filter.readthedocs.io/en/stable/)
- [django-recurrence documentation](https://django-recurrence.readthedocs.io/en/latest/)
- [Python datetime documentation](https://docs.python.org/3/library/datetime.html)
- [dateutil documentation](https://dateutil.readthedocs.io/en/stable/index.html)

These official Django & Python documents were researched to get a greater understanding before pursuing this project.
