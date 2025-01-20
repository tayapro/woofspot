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

# Testing

## User Stories Testing

This section shows the connection between [Features](#features) and [UX design](#ux-design) sections.

## Code Validation Testing

### HTML

The W3C Markup Validation Service was employed to check the HTML of the website.
Only `layout.html` has been slightly changed.

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
