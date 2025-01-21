# WOOFSPOT

![Website Mock Up](readme/woofspot_mockup.png)

## Table of Contents

- [Project Description](#project-description)
  - [Purpose](#purpose)
  - [User Demographics](#user-demographics)
- [UX Design](#ux-design)
  - [User Stories](#user-stories)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
- [Technical Overview](#technical-overview)
  - [Flowcharts](#flowcharts)
  - [Data Model](#data-model)
- [Technologies](#technologies)
- [Deployment](#deployment)
  - [Github](#github)
  - [Heroku](#heroku)
- [Testing](#testing)
  - [User Stories Testing](#user-stories-testing)
  - [Manual Testing](#manual-testing)
  - [Code Validation Testing](#code-validation-testing)
  - [Known Issues](#known-issues)
- [Credits](#credits)
  - [Media](#media)
  - [Code](#code)
- [Acknowledgments](#acknowledgments)

---

# Project Description

## Purpose

The Woofspot App is designed to bring pet owners and enthusiasts together through fun and engaging pet-friendly events.
Whether you're looking to host, join, or review events, Woofspot makes it easy to connect with like-minded individuals
in your local pet-loving community.

With a focus on simplicity and usability, Woofspot offers features like:

- Creating, editing, viewing, and deleting events
- Browsing and searching for events
- Leaving reviews and ratings for past events
- Engaging with events through likes and reservations

Built using Django, Woofspot combines robust functionality with a clean, responsive design. Tools like Cloudinary,
Bootstrap, and Rive ensure smooth performance and an engaging user experience. Hosted on Heroku, the platform is
reliable and accessible to users around the globe.

## User Demographics

Woofspot is tailored for anyone who loves pets and wants to be part of a vibrant community. Here’s who will benefit most:

- Pet Owners: Looking for dog meetups, pet-friendly outings, or training sessions.
- Event Organizers: Planning and managing gatherings for pet lovers.
- Pet Enthusiasts: Animal lovers who want to participate in pet-friendly events, even if they don’t own a pet.

The platform is designed to be intuitive and accessible, making it easy for users of all experience levels
to explore events and connect with others.

[Back to top](#table-of-contents)

---

# Technologies

## Languages

- Python
- HTML5
- CSS
- JavaScript

## Frameworks, Libraries, Apps

| Name                                                             | Purpose                                             |
| :--------------------------------------------------------------- | :-------------------------------------------------- |
| [Django](https://www.djangoproject.com/)                         | Build the app's backend and manages the database    |
| [Django Allauth](https://docs.allauth.org/en/latest/)            | Accounts registration and authentication            |
| [Django Summernote](https://pypi.org/project/django-summernote/) | Provide WYSIWYG editing                             |
| [Gunicorn](https://gunicorn.org/)                                | Use as WSGI server that handles web requests        |
| [Whitenoise](https://whitenoise.readthedocs.io/en/latest/#)      | Work with static files                              |
| [Gitpod](https://www.gitpod.io/)                                 | Serves as cloud-based development environment       |
| [Heroku](heroku.com)                                             | Deploy and Host the application                     |
| Google API                                                       | Sign In with Google feature                         |
| [Bootstrap5](https://getbootstrap.com/)                          | Enables responsive design and ready-made components |
| [Neon Console](https://console.neon.tech/)                       | View and manage Woofspot database                   |
| [Psycopg2](https://pypi.org/project/psycopg2/)                   | Connects Django to PostgreSQL                       |
| [Cloudinary](https://cloudinary.com/)                            | Store images                                        |
| [Font Awesome](https://fontawesome.com/)                         | Add icons to enhance user experience                |
| [Balsamiq](https://balsamiq.com/)                                | Create the wireframes                               |
| [Photopea](https://www.photopea.com/)                            | Work with images (resize, convert, etc)             |
| [Vmake.ai](https://vmake.ai/image-outpainting)                   | Expand the image                                    |
| [Inkscape](https://inkscape.org/)                                | Create Woofspot logo and action picture pages       |
| [Rive](https://rive.app/)                                        | Animate dog for action picture pages                |
| [Websitemockupgenerator](https://websitemockupgenerator.com)     | Create the README Mockup image                      |
| [LucidChart](https://lucid.app)                                  | Create flowcharts                                   |
| [Figma](https://www.figma.com)                                   | Create architecture abstraction layers image        |
| Git                                                              | Use for version control                             |
| [GitHub](https://github.com/)                                    | Store the source code                               |
| [Pep8ci.herokuapp](https://pep8ci.herokuapp.com)                 | Validate Python code                                |
| [W3C HTML Markup Validator](https://validator.w3.org/)           | Validate HTML code                                  |
| [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)        | Validate CSS code                                   |

> [!NOTE]
> A complete list of project dependencies is available in the requirements.txt file.

[Back to top](#table-of-contents)

---

# Deployment

> [!NOTE]
> Before starting the deployment process, please note that you need two files in your repository:
>
> 1. `requirements.txt` with all actual dependencies.
> 2. `env.py` file with environment variables, it's needed for deployment on Heroku and for local deployment as well. Sample `env.py` file:
>
> ```
> import os
>
> os.environ.setdefault(
>    "DATABASE_URL", "<USER_VALUE>")
> os.environ.setdefault("SECRET_KEY", "<USER_VALUE>")
>
> os.environ.setdefault("CLOUDINARY_CLOUD_NAME", "<USER_VALUE>")
> os.environ.setdefault("CLOUDINARY_API_KEY", "<USER_VALUE>")
> os.environ.setdefault("CLOUDINARY_API_SECRET", "<USER_VALUE>")
>
> os.environ.setdefault("EMAIL_HOST_USER", "<USER_VALUE>")
> os.environ.setdefault("EMAIL_HOST_PASSWORD", "<USER_VALUE>")
>
> os.environ.setdefault("DEFAULT_IMAGE", "https://res.cloudinary.com/....webp")
> ```
>
> Also please note that the `DEBUG` flag in settings.py should be `False`.

## How to clone

1. Head over to the [Woofspot repository](https://github.com/tayapro/woofspot) on GitHub.
2. Click the **Code** button (located on the right side of the page), select **HTTPS**, and copy the provided link.
3. Open your terminal and navigate to the folder where you want to save the repository.
4. In the terminal, type `git clone`, paste the copied URL, and hit **Enter** to start cloning.

> [!NOTE]
> To update requirements.txt with all actual dependencies, run: \
> `pip3 freeze > requirements.txt` \
> Check `DEBUG` flag in settings.py, should be `False`. \
> \
> Then commit the changes to GitHub, if needed.

## Neon PostgeSQL Database

This project uses Neon Console for PostgreSQL. The `DATABASE_URL` can be found in the Dashboard tab under Connection Details, as Connection string value:

<img src="readme/Neon_database_url.png" width="500" alt="Neon DB url image">

To use your own database, set it up and configure the `DATABASE_URL`.

## Cloudinary API

This project uses the Cloudinary API to store media files, as Heroku doesn’t support persistent storage for this type of data.

To get started with Cloudinary:

1. Create an account and log in.
2. Head to the settings page.
3. Click the **"Generate new API key"** button to create your own API credentials.

<img src="readme/Cloudinary_api_key.png" width="500" alt="Cloudinary API key image">

### Heroku Deployment

Heroku, a cloud platform that enables easy application building, deployment, and management, was chosen for the Woofspot project. \
Follow these steps to deploy the Woofspot app on Heroku:

1. **Fork or Clone the Repository**  
   Start by forking or cloning the [Woofspot repository](https://github.com/tayapro/woofspot) to your local machine.

2. **Log in to Heroku**  
   Access your Heroku account or create one if you don’t have it yet.

3. **Set Up a New Application**  
   Create a new application on Heroku and name it as desired.

4. **Configure Settings**

   - Go to the **Settings** tab in your Heroku dashboard.

   - In the **Config Vars** section, add the following environment variables with your own values:

     - `CLOUDINARY_API_KEY`: Cloudinary API key, see the "Cloudinary API" section above.
     - `CLOUDINARY_API_SECRET`: Cloudinary API secret, see the "Cloudinary API" section above.
     - `CLOUDINARY_CLOUD_NAME`: Cloudinary cloud name, see the "Cloudinary API" section above.
     - `DATABASE_URL`: database connection URL, see the "Neon PostgeSQL Database" section above.
     - `DEFAULT_IMAGE`: URL for a default image.
     - `EMAIL_HOST_USER`: Google email address, in current configuration _woofspot.app@gmail.com_.
     - `EMAIL_HOST_PASSWORD`: Password to send emails using Google API, for more details how to set up it,
       see [](https://www.geeksforgeeks.org/setup-sending-email-in-django-project/)
     - `SECRET_KEY`: secret key.

   - In the **Buildpacks** section, add the **Python** buildpack.

5. **Deploy the Application**
   - Navigate to the **Deploy** tab.
   - Under **App connected to GitHub**, link your GitHub repository.
   - In the **Manual deploy** section, select the `main` branch and click **Deploy Branch** to deploy your app.

> [!NOTE]
> To update requirements.txt with all actual dependencies, run: \
> `pip3 freeze > requirements.txt` \
> Check `DEBUG` flag in settings.py, should be `False`. \
> \
> Then commit the changes to GitHub.

[Back to top](#table-of-contents)

---

# Testing

## User Stories Testing

This section shows the connection between [Features](#features) and [UX design](#ux-design) sections.

## Code Validation Testing

### HTML

The W3C Markup Validation Service was used to validate the website's HTML.

> [!NOTE]
> The Django Allauth templates in `templates\account`, `templates\allauth`, `templates\mfa`, `templates\openid`,
> `templates\socialaccount`, `templates\tests`, and `templates\usersessions` remain unmodified and were not validated.
> Only the customized templates (`templates\account\login.html`, `templates\account\logout.html`,
> and `templates\account\signup.html`) were validated. Results are shown below.

<details><summary><code>XXXXX.html</code> page passed without any errors or warnings.</summary>
<img src="readme/W3HTML_validation_XXXXX.png" width="500" alt="W3C XXXXXX.html validation image">
</details>

### Python

All files passed without any errors or warnings on [CI Python Linter](https://pep8ci.herokuapp.com/).

#### event_app

<details><summary><code>forms.py</code> page passed without any errors or warnings.</summary>
<img src="readme/PEP8_event_app_forms.png" width="500" alt="PEP8 event_app forms validation image">
</details>

<details><summary><code>models.py</code> page passed without any errors or warnings.</summary>
<img src="readme/PEP8_event_app_models.png" width="500" alt="PEP8 event_app models validation image">
</details>

<details><summary><code>urls.py</code> page passed without any errors or warnings.</summary>
<img src="readme/PEP8_event_app_urls.png" width="500" alt="PEP8 event_app urls validation image">
</details>

#### user_app

<details><summary><code>forms.py</code> page passed without any errors or warnings.</summary>
<img src="readme/PEP8_user_app_forms.png" width="500" alt="PEP8 user_app forms validation image">
</details>

<details><summary><code>views.py</code> page passed without any errors or warnings.</summary>
<img src="readme/PEP8_user_app_views.png" width="500" alt="PEP8 user_app views validation image">
</details>

<details><summary><code>urls.py</code> page passed without any errors or warnings.</summary>
<img src="readme/PEP8_user_app_urls.png" width="500" alt="PEP8 user_app urls validation image">
</details>

#### woofspot_project

<details><summary><code>settings.py</code> page passed without any errors or warnings.</summary>
<img src="readme/PEP8_woofspot_project_settings.png" width="500" alt="PEP8 woofspot_project settings validation image">
</details>

<details><summary><code>views.py</code> page passed without any errors or warnings.</summary>
<img src="readme/PEP8_woofspot_project_views.png" width="500" alt="PEP8 woofspot_project views validation image">
</details>

<details><summary><code>urls.py</code> page passed without any errors or warnings.</summary>
<img src="readme/PEP8_woofspot_project_urls.png" width="500" alt="PEP8 woofspot_project urls validation image">
</details>

[Back to top](#table-of-contents)
