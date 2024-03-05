# Django CRUD Web Application

This Django web application is a simple CRUD (Create, Read, Update, Delete) project that allows users to manage user records with ease. Users can perform the following operations:

- Create new user records.
- View a list of all user records.
- Edit existing user records.
- Delete user records.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Creating a User](#creating-a-user)
  - [Viewing User Records](#viewing-user-records)
  - [Editing User Records](#editing-user-records)
  - [Deleting User Records](#deleting-user-records)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [License](#license)

## Getting Started

## Prerequisites

### Before running the application, make sure you have the following prerequisites installed:

- Python (3.7 or higher)
- Django
- Virtual environment (optional but recommended)

### Creating a User

- Visit the home page at http://localhost:8000/.
1. Click the "Create User" button.
2. Fill in the user details in the registration form.
3. click the "Create" button to submit the form.

### Viewing User Records
-  Visit the home page at http://localhost:8000/.
1. Click the "View User List" button to see a list of all user records.
2. Click on a user's name to view their details.

### Editing User Records
- Visit the home page at http://localhost:8000/.
1. Click the "View User List" button.
2. Click the "Edit" link next to the user you want to edit.
3. Update the user's information in the edit form.
4. Click the "Update" button to save the changes.

### Deleting User Records
- Visit the home page at http://localhost:8000/.
1. Click the "View User List" button.
2. Click the "Delete" link next to the user you want to delete.
3. Confirm the deletion when prompted.

## Project Structure
#### The project structure is organized as follows:

- crud_app/: The Django app containing models, views, forms, and templates.
- media/: Directory for storing user profile photos (media files).
- static/: Directory for static files (CSS, JavaScript).
- templates/: HTML templates for rendering pages.
- manage.py: Django's command-line tool for managing the project.
- requirements.txt: List of project dependencies.
- README.md: This documentation file.


### Technologies Used
- Python
- Django
- Bootstrap (for styling)
- HTML5
- CSS3

