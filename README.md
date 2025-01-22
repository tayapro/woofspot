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
  - [Code Validation](#code-validation)
  - [Performance](#performance)
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

# Features

## Existing Features

### F01 Navigation Bar

The Woofspot pages feature a sticky navbar with an eye-catching colored Woofspot logo text.
The layout includes a search section with different options for registered and unregistered users,
plus a hamburger menu with popover functionality.
On screens smaller than 665px, the search section appears at the bottom of the screen.

_Screen more than 665px:_

<img src="readme/f01_desktop.png" width="500" alt="navbar desktop image"/>

_Screen less than 665px:_

<img src="readme/f01_mobile1.png" width="300" alt="navbar mobile image"/> <br>
<img src="readme/f01_mobile2.png" width="300" alt="navbar mobile image"/>

### F02 Popover menu

The menu is accessible on all device sizes, featuring a hamburger icon and popover functionality.
Users can find important links such as "Home," "Username" (Profile), "My Events" (where users
can view events they're hosting, attending, or have previously attended), and "Logout." Each
link has a hover effect that slightly enlarges the text for a smooth interaction.

<img src="readme/f02.png" width="300" alt="navbar mobile image"/>

To close the popover menu, the user can click the circular "X" button in the top-right corner of the screen.

### F03 Icons container

Each Woofspot event card includes an Icons section where users can view various icons:

- Status Icons: These indicate the user’s connection to the event:

  - Host
  - Attendee

- Interaction Icons:
  - Hosts can edit or delete upcoming events.
  - Registered users can like an event. Clicking the heart icon toggles between solid and regular heart icons. If a non-registered user clicks the like icon, the app will redirect them to the Login page. \
    **Note**: This feature is implemented using htmx, allowing it to work without re-rendering the entire page.
  - Rating Star: The star rating appears in read-only mode for hosts and non-attendees, showing the score. For attendees, the star is a clickable link that redirects to the Review page, where they can leave a review and set a rating score.

#### Icon sets examples:

<table>
<tr>
<td><img src="readme/f03_non_registered_icons.png" width="35" alt="Icon set for past attendee event"></td>
<td>
Non registered user's future event 
</td>
</tr>
<tr>
<td><img src="readme/f03_future_host_icons.png" width="35" alt="Icon set for past attendee event"></td>
<td>
User's future event where they are marked as a host
</td>
</tr>
<tr>
<td><img src="readme/f03_past_attendee_icons.png" width="50" alt="Icon set for past attendee event"></td>
<td>
User's past event where they are marked as an attendee
</td>
</tr>
<tr>
<td><img src="readme/f03_future_attendee_icons.png" width="45" alt="Icon set for past attendee event"></td>
<td>
User's future event where they are marked as an attendee
</td>
</tr>
</table>

Each icon (except like) has a tooltip with a short, clear explanation for every screen size.

<img src="readme/f03_tooltip.png" width="200" alt="tooltip for icon image"/>

### F04 RIVE animated dog

In the Woofspot project, a playful and engaging RIVE animated dog is featured across multiple pages,
including the login, signup, logout, event creation, event editing, event deletion, reservation cancellation,
and leave rating pages. This animated dog serves as a dynamic and visually appealing element to enhance
the user experience.

<img src="readme/f04_animated_doggy.gif" width="200" alt="Animated doggy gif">

Particularly on mobile screens, where users may struggle to distinguish between various static pet images due
to size constraints or color differences, the animated dog provides a fun and effective solution. Its lively
animation draws attention and ensures a consistent and engaging experience for users across all devices.

### F05 Home page - Image with Tagline

The first thing users see when they visit Woofspot is a bright, colorful photo featuring excited dogs.
What are they waiting for? Probably just a good ol' unleashed run or something exciting from their human.

<img src="readme/f05_big_image.png" width="500" alt="Photo with dogs">

This image perfectly captures the playful spirit of the site, instantly drawing users in with a sense of
anticipation and joy. It sets the tone for the whole experience, echoing the fun and adventurous nature
of spending time with a four-legged friend. Whether it's discovering new pet-friendly events or simply
exploring the platform, the vibrant image hints at all the exciting adventures Woofspot has in store.

### F06 Home page - Event Calendar Link and Upcoming Events Carousel

Since Woofspot is all about pet-friendly events, users can easily find a link to the event calendar,
where they can explore all upcoming and past events.

<img src="readme/f06_carousel.png" width="500" alt="Photo with stretch cat">

The attention-grabbing carousel of event cards showcases the next four weeks of events, giving users
a sneak peek into the variety of activities they can join. It's a fun and interactive way to highlight
just a few of the many exciting events Woofspot has to offer.

The event titles act as links that take users to the event's detailed view page, where they can find
all the related information.

### F07 Home page - Everything You Need to Know accordion and Contact Us form

What if a user has a few questions and wants more information about Woofspot’s event rules—like how to attend,
or what to do if they have a great idea for the next event? The "Everything You Need to Know" section,
presented in a simple and clear accordion format, provides all the answers in an easy-to-digest way.

<img src="readme/f07_everything_you_need_to_know.png" width="500" alt="Everything you need to know">

And if, after reading through the "Everything You Need to Know" section, users still have questions,
they can reach out to the Woofspot team via the Contact Us form. Even if the user is already registered
on Woofspot, they’ll need to fill out the email field, just in case we need to get in touch through
a different contact email.

<img src="readme/f07_contact_us.png" width="500" alt="Contact us form">

### F08 Event Calendar page

Let’s dive into the event calendar page! This page is accessible to everyone and is divided into two sections:
future events and past events.
All events features various icon sets (for more details, see _F03 Icons container_ above).

<img src="readme/f08_future_events.png" width="500" alt="Future events">

The design is clean and straightforward, with bright images for each event and clickable titles that make
navigation easy. It’s simple, yet functional, ensuring users can quickly find the events they’re looking for.

<img src="readme/f08_past_events.png" width="500" alt="Past events">

Each card has a hover effect that slightly enlarges it, creating a smooth and interactive experience.

### F09 My Events page

The "My Events" page is a personalized place available to every registered user.
It’s divided into three sections:

- **Hosted by Me**: Here, users can manage their existing events and create new ones by clicking the "Host New Event" button.

  <img src="readme/f09_hosted_by_me.png" width="500" alt="Hosted by me section">

- **Planning to Attend**: In this section, users can see the events they’ve registered for (marked with a "ticket" icon).
  They also have the option to cancel their reservation by clicking the "X" icon.

  <img src="readme/f09_planning_to_attend.png" width="500" alt="Planning to attend section">

- **Past Events**: This section includes events the user has attended, either as a host or an attendee.
  Attendees can leave a review for events they’ve participated in.

  <img src="readme/f09_past_events.png" width="500" alt="Past events section">

If any section has an empty list of events, the user will see a friendly message, such as:

- For Hosted by Me: "You’re not organizing any events yet."
- For Planning to Attend: "You haven’t reserved a spot for any future events yet."
- For Past Events: "You haven’t hosted any events or made any reservations yet."

These messages help guide the user and keep the page informative, even when no events are present.

### F10 Event Reservation Submit

When the user clicks the plus icon (labeled "Join the event" in the tooltip) on an event card,
whether on the Landing page, Event Calendar page, or Event View page, they’ll see a modal window with
a "Reservation Confirmed" message.

<img src="readme/f10_join_button.png" width="300" alt="Join button">

<img src="readme/f10_reservation_message.png" width="300" alt="Reservation message">

They’ll also receive an email from the Woofspot team with their
reservation details and can continue exploring Woofspot.

### F11 Event Reservation Cancel

If for any reason the user wants to cancel their reservation, they can do so by clicking the "X" (Cancel Reservation)
icon. They will then be redirected to the "Reservation Cancel" page, where they’ll be asked again to confirm
their cancellation.

<img src="readme/f11_reservation_cancel_button.png" width="300" alt="Reservation cancel button">

On the desktop version, the screen is divided into two panels: on the left, there’s a photo featuring a curious cat
and dog, seemingly asking, "Are you sure?" On the right, the user will see a simple form with a question and two
buttons: "Cancel Spot" and "No".

<p float="left">
<img src="readme/f11_reservation_cancel_desktop.png" width="350" alt="Reservation cancel desktop">
<img src="readme/f11_reservation_cancel_mobile.png" width="150" alt="Reservation cancel mobile">
</p>

On mobile devices, only the right-hand side panel with the buttons will be visible, offering a streamlined
experience.

By clicking "Cancel Spot" the user will see a modal window with a "Reservation cancelled" message.

<img src="readme/f11_reservation_cancel_message.png" width="300" alt="Reservation cancel message">

They’ll also receive an email from the Woofspot team with their reservation cancel confirmation and
can continue exploring Woofspot.

### F12 Event Review

### F13 Event Management (CRUD)

#### CREATE

On the "My Events" page, every user can create a new event by clicking the "Host New Event" button.
They will then be redirected to the Event Create page.

On the desktop version, the screen is split into two panels: on the left, there’s a bright photo of a
bulldog, and on the right, the user will see:

- A gentle reminder about the format: English text, JPG, JPEG, or PNG images under 2MB.
- A form with pre-filled fields ready for the user to edit, such as title, description, location, date, and time.
- A field to choose a picture if desired (this is optional; if no image is chosen, a default image will be
  added automatically).

<p float="left">
<img src="readme/f13_event_create_desktop.png" width="350" alt="Event create desktop">
<img src="readme/f13_event_create_mobile.png" width="150" alt="Event create mobile">
</p>

When the user clicks "Submit," they will see a modal window with a "Event Created" message.

<img src="readme/f13_event_create_message.png" width="300" alt="Event create message">

If there are any form validation errors, the user will see a detailed description of the errors, such as:

- Please use only Latin/accented characters.
- Event start time cannot be between 21:00 and 09:00.
- Please make sure the event is no longer than three hours.

The user will also receive an email from the Woofspot team confirming the event creation.

#### READ

Each Woofspot event is showcased on a card that includes a vibrant photo, an engaging title, the
event date and time, the location, and a short description to give users a quick overview. To make
navigation even easier, each card features a set of icons that represent available actions (such as
joining the event or liking it) and show the status related to the user's involvement. These icons
help users quickly identify whether they are already registered for an event, whether they can edit
or cancel their reservation, or whether there are any additional actions they can take, enhancing
the overall user experience.

<p float="left">
<img src="readme/f13_event_view_desktop.png" width="350" alt="Event view desktop">
<img src="readme/f13_event_view_mobile.png" width="150" alt="Event view mobile">
</p>

The event description is initially displayed with a brief summary. By clicking the "Show More" link,
the user can expand it to view the full description.
The "Back" button will take the user to the previous page.

#### UPDATE

An event has already been created but the user wants to make changes, they can do so by clicking
the "pen to square" (Edit) icon. This will take them to the Event Edit page.

On the desktop version, the screen is split into two panels: on the left, there’s a photo of a dog,
and on the right, the user will see:

A gentle reminder about the format: English text, JPG, JPEG, or PNG images under 2MB.\
A form with fields that can be edited, including the title, description, location, date, and time.\
Information about the current event image: This event has an image, and feel free to upload a new one.\
A field to choose a new picture, if desired.

<p float="left"> 
<img src="readme/f13_event_edit_desktop.png" width="350" alt="Event edit desktop page"> 
<img src="readme/f13_event_edit_mobile.png" width="150" alt="Event edit mobile page"> 
</p>

When the user clicks "Save Changes," they will see a modal window with a "Event Updated" message.

<img src="readme/f13_event_edit_message.png" width="300" alt="Event edit message">

In case of any form validation errors, the user will be informed with an error message
displayed above the form, helping them correct any issues.

<img src="readme/f13_event_edit_errors.png" width="250" alt="Event edit errors">

Both the user and all event attendees will also receive an email from the Woofspot team notifying
them of the event changes.

#### DELETE

If a user in the host role wants to delete their event, they can click the "bucket" (Delete) icon.
This will take them to the Event Delete page.

On the desktop version, the screen is split into two panels: on the left, there’s a photo of a sad dog,
seemingly asking, "Are you sure about this?" On the right, the user will see a simple form with a
question about the selected event and two options: "Delete Event" and "No".

On mobile devices, only the right-hand panel with the buttons will be displayed, providing a
streamlined experience.

<p float="left">
<img src="readme/f13_event_delete_desktop.png" width="350" alt="Event delete desktop page"> 
<img src="readme/f13_event_delete_mobile.png" width="150" alt="Event delete mobile page"> 
</p>

When the user clicks "Delete Event," they will see a modal window with a "Event Deleted" message.

<img src="readme/f13_event_delete_message.png" width="300" alt="Event edit message">

The user will also receive an email from the Woofspot team confirming the event deletion.

> [!NOTE]
> If something goes wrong during the process of saving changes for Create/Edit/Delete or sending emails,
> the user will be informed through a modal window displaying the error(s). This ensures the user is
> aware of any issues and can take the necessary steps to resolve them.

### F14 User Access and Logout pages

### F15 Profile page

The profile page displays the user's "username" and "email" in a read-only format.

<img src="readme/f15_profile.png" width="300" alt="Profile">

### F16 Email Notifications

### F17 Spinner

### F18 Woofspot Navigation though app

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
| [Ezgif](https://ezgif.com/)                                      | Conver video to gif                                 |
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

## Code Validation

### HTML

The W3C Markup Validation Service was used to validate the website's HTML.

> [!NOTE]
> The Django Allauth templates in `templates\account`, `templates\allauth`, `templates\mfa`, `templates\openid`,
> `templates\socialaccount`, `templates\tests`, and `templates\usersessions` remain unmodified and were not validated.
> Only the customized templates (`templates\account\login.html`, `templates\account\logout.html`, `templates\account\password_reset.html`
> and `templates\account\signup.html`) were validated. Results are shown below.

> [!NOTE]
> Received the following warning for the WOOFSPOT element (logo and landing page link) in the navigation bar.
> Warning: Consider using the h1 element as a top-level heading only
>
> The Popover API has been choosen to enhance the user experience by providing dynamic and interactive
> content in a way that’s intuitive and accessible.
> Although some custom attributes were flagged in validation, these are crucial for targeting specific
> elements and triggering popover functionality in Woofspot project:
> Error: Attribute popovertarget not allowed on element button at this point.
> Error: Attribute popover not allowed on element nav at this point.
> Error: Attribute popovertarget not allowed on element button at this point.
> Error: Attribute popovertargetaction not allowed on element button at this point.
>
> While integrating HTMX functionality into the Woofspot project, encountered the following validation issues:
> Error: Attribute hx-swap not allowed on element div at this point.
> Error: Attribute hx-post not allowed on element div at this point.
> Error: Attribute hx-headers not allowed on element div at this point.
> These warnings occur because certain HTMX attributes, such as hx-swap, hx-post, and hx-headers, are
> applied to the <div> element that may not be considered valid targets for these attributes in some
> contexts, based on HTML validation rules.
> In Woofspot project, these attributes are used to enhance dynamic content loading and interaction without
> reloading the page. Although these attributes may not be strictly validated for use on <div>,
> they are functional within the HTMX framework and contribute to the interactive behavior of the platform.
>
> For now, validation warnings (Popover API & HTMX) are not critical and do not affect the functionality,
> but future versions of the project may involve further refinement of element usage to ensure full compatibility
> with validation standards.

<details><summary><code>XXXXX.html</code></summary>
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

## Performance

Google Lighthouse in Google Chrome Developer Tools was used to check the website performance.

### Home

<details><summary>Home desktop</summary>
<img src="readme/landing_page_desktop.png" width="500px">
</details>

<img src="readme/landing_page_desktop_numbers.png" width="300px" alt="Landing desktop numbers">

<details><summary>Home mobile</summary>
<img src="readme/landing_page_mobile.png" width="500px">
</details>

<img src="readme/landing_page_mobile_numbers.png" width="300px" alt="Landing mobile numbers">

### Event Calendar page

<details><summary>Event Calendar desktop</summary>
<img src="readme/event_calendar_page_desktop.png" width="500px">
</details>

<img src="readme/event_calendar_page_desktop_numbers.png" width="300px" alt="Event Calendar desktop numbers">

<details><summary>Event Calendar mobile</summary>
<img src="readme/event_calendar_page_mobile.png" width="500px">
</details>

<img src="readme/event_calendar_page_mobile_numbers.png" width="300px" alt="Event Calendar mobile numbers">

### My Events page

<details><summary>My Events desktop</summary>
<img src="readme/my_events_page_desktop.png" width="500px">
</details>

<img src="readme/my_events_page_desktop_numbers.png" width="300px" alt="My Events desktop numbers">

<details><summary>My Events mobile</summary>
<img src="readme/my_events_page_mobile.png" width="500px">
</details>

<img src="readme/my_events_page_mobile_numbers.png" width="300px" alt="My Events mobile numbers">

### Search Results page

<details><summary>Search Results desktop</summary>
<img src="readme/search_results_page_desktop.png" width="500px">
</details>

<img src="readme/search_results_page_desktop_numbers.png" width="300px" alt="Search Results desktop numbers">

<details><summary>Search Results mobile</summary>
<img src="readme/search_resultspage_mobile.png" width="500px">
</details>

<img src="readme/search_results_page_mobile_numbers.png" width="300px" alt="Search Results mobile numbers">

### No Search Results page

<details><summary>No Search Results desktop</summary>
<img src="readme/no_search_results_page_desktop.png" width="500px">
</details>

<img src="readme/no_search_results_page_desktop_numbers.png" width="300px" alt="No Search Results desktop numbers">

<details><summary>Search Results mobile</summary>
<img src="readme/no_search_resultspage_mobile.png" width="500px">
</details>

<img src="readme/no_search_results_page_mobile_numbers.png" width="300px" alt="No Search Results mobile numbers">

### Event Create page

<details><summary>Event Create desktop</summary>
<img src="readme/event_create_page_desktop.png" width="500px">
</details>

<img src="readme/event_create_page_desktop_numbers.png" width="300px" alt="Event Create desktop numbers">

<details><summary>Event Create mobile</summary>
<img src="readme/event_create_page_mobile.png" width="500px">
</details>

<img src="readme/event_create_page_mobile_numbers.png" width="300px" alt="Event Create mobile numbers">

### Event View page

<details><summary>Event View desktop</summary>
<img src="readme/event_view_page_desktop.png" width="500px">
</details>

<img src="readme/event_view_page_desktop_numbers.png" width="300px" alt="Event View desktop numbers">

<details><summary>Event View mobile</summary>
<img src="readme/event_view_page_mobile.png" width="500px">
</details>

<img src="readme/event_view_page_mobile_numbers.png" width="300px" alt="Event View mobile numbers">

### Event Edit page

<details><summary>Event Edit desktop</summary>
<img src="readme/event_edit_page_desktop.png" width="500px">
</details>

<img src="readme/event_edit_page_desktop_numbers.png" width="300px" alt="Event Edit desktop numbers">

<details><summary>Event Edit mobile</summary>
<img src="readme/event_edit_page_mobile.png" width="500px">
</details>

<img src="readme/event_edit_page_mobile_numbers.png" width="300px" alt="Event Edit mobile numbers">

### Event Delete page

<details><summary>Event Delete desktop</summary>
<img src="readme/event_delete_page_desktop.png" width="500px">
</details>

<img src="readme/event_delete_page_desktop_numbers.png" width="300px" alt="Event Delete desktop numbers">

<details><summary>Event Delete mobile</summary>
<img src="readme/event_delete_page_mobile.png" width="500px">
</details>

<img src="readme/event_delete_page_mobile_numbers.png" width="300px" alt="Event Delete mobile numbers">

### Rating Submit page

<details><summary>Rating Submit desktop</summary>
<img src="readme/rating_submit_page_desktop.png" width="500px">
</details>

<img src="readme/rating_submit_page_desktop_numbers.png" width="300px" alt="Rating Submit desktop numbers">

<details><summary>Rating Submit mobile</summary>
<img src="readme/rating_submit_page_mobile.png" width="500px">
</details>

<img src="readme/rating_submit_page_mobile_numbers.png" width="300px" alt="Rating Submit mobile numbers">

### Reservation Cancelled page

<details><summary>Reservation Cancelled desktop</summary>
<img src="readme/reservation_cancelled_page_desktop.png" width="500px">
</details>

<img src="readme/reservation_cancelled_page_desktop_numbers.png" width="300px" alt="Reservation Cancelled desktop numbers">

<details><summary>Reservation Cancelled mobile</summary>
<img src="readme/reservation_cancelled_page_mobile.png" width="500px">
</details>

<img src="readme/reservation_cancelled_page_mobile_numbers.png" width="300px" alt="Reservation Cancelled mobile numbers">

### Signup page

<details><summary>Signup desktop</summary>
<img src="readme/signup_page_desktop.png" width="500px">
</details>

<img src="readme/signup_page_desktop_numbers.png" width="300px" alt="Signup desktop numbers">

<details><summary>Signup mobile</summary>
<img src="readme/signup_page_mobile.png" width="500px">
</details>

<img src="readme/signup_page_mobile_numbers.png" width="300px" alt="Signup mobile numbers">

### Login page

<details><summary>Login desktop</summary>
<img src="readme/login_page_desktop.png" width="500px">
</details>

<img src="readme/login_page_desktop_numbers.png" width="300px" alt="Login desktop numbers">

<details><summary>Login mobile</summary>
<img src="readme/login_page_mobile.png" width="500px">
</details>

<img src="readme/login_page_mobile_numbers.png" width="300px" alt="Login mobile numbers">

### Logout page

<details><summary>Logout desktop</summary>
<img src="readme/logout_page_desktop.png" width="500px">
</details>

<img src="readme/logout_page_desktop_numbers.png" width="300px" alt="Logout desktop numbers">

<details><summary>Logout mobile</summary>
<img src="readme/logout_page_mobile.png" width="500px">
</details>

<img src="readme/logout_page_mobile_numbers.png" width="300px" alt="Logout mobile numbers">

### Password Reset page

<details><summary>Password Reset desktop</summary>
<img src="readme/password_reset_page_desktop.png" width="500px">
</details>

<img src="readme/password_reset_page_desktop_numbers.png" width="300px" alt="Password Reset desktop numbers">

<details><summary>Password Reset mobile</summary>
<img src="readme/password_reset_page_mobile.png" width="500px">
</details>

<img src="readme/password_reset_page_mobile_numbers.png" width="300px" alt="Password Reset mobile numbers">

### Profile page

<details><summary>Profile desktop</summary>
<img src="readme/profile_page_desktop.png" width="500px">
</details>

<img src="readme/profile_page_desktop_numbers.png" width="300px" alt="Profile desktop numbers">

<details><summary>Profile mobile</summary>
<img src="readme/profile_page_mobile.png" width="500px">
</details>

<img src="readme/profile_page_mobile_numbers.png" width="300px" alt="Profile mobile numbers">

### 403 Error page

<details><summary>403 desktop</summary>
<img src="readme/403_page_desktop.png" width="500px">
</details>

<img src="readme/403_page_desktop_numbers.png" width="300px" alt="403 desktop numbers">

<details><summary>403 mobile</summary>
<img src="readme/403_page_mobile.png" width="500px">
</details>

<img src="readme/403_page_mobile_numbers.png" width="300px" alt="403 mobile numbers">

### 404 Error page

<details><summary>404 desktop</summary>
<img src="readme/404_page_desktop.png" width="500px">
</details>

<img src="readme/404_page_desktop_numbers.png" width="300px" alt="404 desktop numbers">

<details><summary>404 mobile</summary>
<img src="readme/404_page_mobile.png" width="500px">
</details>

<img src="readme/404_page_mobile_numbers.png" width="300px" alt="404 mobile numbers">

[Back to top](#table-of-contents)

---

# Credits

## Content

- The fonts used were imported from Google Fonts.
- The icons were taken from Font Awesome.
- [Google icon](https://icons8.com/icons/set/google) for "Sign in with Google" button.

## Media

- [Running puppy](https://unsplash.com/photos/a-small-white-teddy-bear-is-running-down-the-street-6_kWa9NvvCg?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Freya Song](https://unsplash.com/@freyasong).
- [Brown puppy on bed](https://unsplash.com/photos/brown-puppy-on-bed-V6G2m3D9IDI) photo by [Roberto Nickson](https://unsplash.com/@rpnickson).
- [Bernese Mountain Dog and friend during warm days](https://unsplash.com/photos/black-white-and-brown-bernese-mountain-dog-lying-on-white-textile-sJgucUmcaKE?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Louis-Philippe Poitras](https://unsplash.com/@lppoitras).
- [A crocheted Googlebot and Crawley](https://unsplash.com/photos/a-crocheted-stuffed-animal-next-to-a-crocheted-vase-M7ZuRWaaevw?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Lizzi Sassman](https://unsplash.com/@okaylizzi).
- [Dachshund resting on white hanged fabric](https://unsplash.com/photos/dachshund-resting-on-white-hanged-fabric-D1wiHCovGJ0?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Erda Estremera](https://unsplash.com/@erdaest).
- [Small brown dog sitting on white floor](https://unsplash.com/photos/a-small-brown-dog-sitting-on-top-of-a-white-floor-rermv-4qZsI?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Petar Acanski](https://unsplash.com/@petaracanski).
- [Happy french bulldog](https://unsplash.com/photos/brown-short-coated-dog-wearing-red-and-white-santa-costume-BVqQNu5J7qI?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by []().
- [Dog sleeping on floor](https://unsplash.com/photos/dog-sleeping-on-floor-LTQMgx8tYqM?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Minh Pham](https://unsplash.com/@minhphamdesign).
- [Long walks in the desert](https://unsplash.com/photos/person-walking-on-brown-sand-near-body-of-water-during-daytime-11ZynBe_DRA?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Karsten Winegeart](https://unsplash.com/@karsten116).
- [Combination lock](https://unsplash.com/photos/closeup-photo-of-round-gray-combination-padlock-atW3fbSy_9Y?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Debby Hudson](https://unsplash.com/@hudsoncrafted).
- [Night park bench](https://unsplash.com/photos/a-park-bench-sitting-on-the-side-of-a-path-YL2NV6GjXFA?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [sq lim](https://unsplash.com/@sql).
- [Wooden fence near body of water](https://unsplash.com/photos/brown-wooden-fence-near-body-of-water-nIhScs1bRYg?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Jaleel Akbash](https://unsplash.com/@jaleel_akbash).
- [Dog sits in green grass field](https://unsplash.com/photos/short-coated-tan-dog-sits-in-green-grass-field-during-daytime-r1q76Rut5t8?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Reed Shepherd](https://unsplash.com/@reed_shepherd1).
- [Photo dog with hoomans](https://unsplash.com/photos/man-in-black-and-white-striped-shirt-beside-woman-in-black-and-white-stripe-shirt-RRh6wyEU_4Q?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Chewy](https://unsplash.com/@chewy).
- [Yoga cat](https://unsplash.com/photos/russian-blue-cat-lying-on-brown-woven-chair-5ieFKjviwL8?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Hana Oliver](https://unsplash.com/@hanako87).
- [Pet clinic](https://unsplash.com/photos/white-and-black-short-coated-dog-wearing-white-and-black-polka-dot-shirt-loJL4ijUobg?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Karsten Winegeart](https://unsplash.com/@karsten116).
- [Exotic animal](https://unsplash.com/photos/a-green-lizard-sitting-on-top-of-a-tree-branch-uWRGj2zhQJI?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Viktoriia Kondratiuk](https://unsplash.com/@viktoriia_kondratiuk).
- [Sad cat](https://unsplash.com/photos/selective-focus-photography-of-brown-tabby-cat-DM2Gr9U7lHo?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Anna Ogiienko](https://unsplash.com/@panafotkas).
- [Party dogs](https://unsplash.com/photos/white-long-coated-dog-sitting-on-brown-tree-log-during-daytime-cnBQdL559mY?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Karolina Wv](https://unsplash.com/@karolinawv).
- [Grumpy cat](https://unsplash.com/photos/orange-and-white-tabby-cat-sitting-on-brown-wooden-table-in-kitchen-room-w2DsS-ZAP4U?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Paul Hanaoka](https://unsplash.com/@plhnk).
- [Sunset dog](https://unsplash.com/photos/white-long-coated-dog-on-green-grass-field-during-daytime-cLZQ9KHuTos?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Massimo Negrello](https://unsplash.com/@massimonegrello).
- [Mountains dog](https://unsplash.com/photos/black-dog-with-red-collared-standing-on-gray-stone-during-cloudy-day-nk_uvN_b-w8?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Patrick Hendry](https://unsplash.com/@worldsbetweenlines).
- [Art studio cat](https://unsplash.com/photos/a-cat-sitting-on-a-desk-in-a-room-tNjJeDf6hJs?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Sindy Süßengut](https://unsplash.com/@sindy_suessengut).
- [Market dog](https://unsplash.com/photos/a-dog-is-sitting-on-a-table-in-a-flower-shop-mHw2MVxI8fM?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Travis Leery](https://unsplash.com/@jersey_photos).
- [Beach dogs](https://unsplash.com/photos/two-dogs-running-on-the-beach-with-a-teddy-bear-hZE7CNo8cdo?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Lisa Anderson](https://unsplash.com/@lisaaandy).
- [Kittens on books shelf](https://unsplash.com/photos/a-couple-of-cats-laying-on-top-of-a-book-shelf-txzw_LiGa4w?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Duygu Güngör](https://unsplash.com/@duygug).
- [Puppy on bed](https://unsplash.com/photos/brown-short-coated-dog-on-brown-wicker-basket-oeND26pmdNs?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Jordan Bigelow](https://unsplash.com/@jordanbigs).
- [Woman with a dog in a kitchen](https://unsplash.com/photos/a-woman-standing-in-a-kitchen-with-a-dog-GF0RhSNQ5n8?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Luzelle Cockburn](https://unsplash.com/@luzelle).
- [Dog sitting in front of book](https://unsplash.com/photos/dog-sitting-in-front-of-book-Zqy-x7K5Qcg?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash) photo by [Jamie Street](https://unsplash.com/@jamie452).

## Code

- Popover menu is adapted from the [Everything you need to know about the Popover API](https://codepen.io/web-dot-dev/pen/vYbadaJ).
- The Rive integration in this web app is adapted from [the Web (JS) implementation for Rive](https://rive.app/community/doc/web-js/docvlgbnS1mp).
- Understanding of [Bootstrap Carousel](https://getbootstrap.com/docs/5.0/components/carousel/).
- Knowledge of sending email in Django with [StackOverflow django-email questions](https://stackoverflow.com/questions/tagged/django-email?tab=Frequent).
- Understanding of [Django-Browser-Reload](https://medium.com/@appseed.us/django-hot-reload-templates-and-static-4d74a774b26f).
- Knowledge of Sign In with Google for Web with [Django Allauth social account Google](https://docs.allauth.org/en/dev/socialaccount/providers/google.html).
- Understanding of Django with [Django documentation](https://docs.djangoproject.com/en/5.1/).

[Back to top](#table-of-contents)

---

# Acknowledgments

Special thanks to my mentors, Ronan McClelland and Jubril Akolade, for their invaluable guidance and support.\
Thanks to the amazing Slack Community and their extensive knowledge base, which helped resolve issues
throughout this project's development.

[Back to top](#table-of-contents)
