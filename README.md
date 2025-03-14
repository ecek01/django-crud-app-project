## Game Logo

<img src="https://github.com/ecek01/django-crud-app-project/blob/main/djandocalendar.png">

# Library App - MEN Stack Crud App Project

## **Description**

<p>This project is a Django-based web application that allows users to manage events, tasks, and to-dos using a calendar interface. Users can add, edit, and delete events, track their tasks, and view upcoming deadlines. The application also features user authentication, allowing users to register, log in, and manage their events securely.</p>

## **Github Repo**

<p><a href="https://github.com/ecek01/django-crud-app-project/tree/main">Django Calendar CRUD App GitHub Repo</a></p>

## **Deployment Link**

<p><a href="https://django-calendar-app-p4-05ddabefc58a.herokuapp.com/">Django Calendar CRUD App Deployment Link</a></p>

## **Timeframe & Working Team**

- **Timeframe**: 2 weeks
- **Team**: Solo project

## **Technologies Used**

- **Back End**: Django, Python, PostgreSQL
- **Front End**: HTML, CSS, JavaScript, Bootstrap
- **Tools**: Git, GitHub, Django ORM, FullCalendar.js

## **Brief**

<p>The goal of this project was to build a full CRUD (Create, Read, Update, Delete) web application where users can manage their personal events, tasks, and to-dos within a calendar interface. Users should be able to: Register and login, create events with details, edit or delete events, filter and view upcoming tasks and logout.</p>

## **Planning**

- Wireframes were designed to plan the user interface, focusing on a clean and intuitive layout.
- User stories and application flow were mapped to ensure all CRUD operations were implemented.
- Database schema was structured using Django models and migrations.
- [Project planning material](https://trello.com/b/MwQ3moo4/django-crud-app-project)

## **Build/Code Process**

1. **Database Setup**: Configured PostgreSQL as the database using Django's ORM.

2. **Authentication**: Implemented user registration, login, and logout using Django's built-in authentication.

3. **CRUD Functionality**: Created models and views for managing events and tasks.

4. **Front-End Design**: Styled with Bootstrap and FullCalendar.js for an interactive calendar experience.

5. **Logout Redirection**: Ensured users are redirected to the home page after logout instead of Django’s default.


## **Attributions**

- FullCalendar.js - Interactive event calendar.
- Bootstrap - Used for styling and responsive UI.

## **Challenges**

- Fixing logout redirection: By default, Django redirects to /accounts/profile/. This was fixed by setting LOGIN_REDIRECT_URL = "event_list" in settings.py
- Integrating FullCalendar.js with Django: Ensuring event data was dynamically loaded from the database into the front-end calendar.

## **Wins**

- Successfully implemented full CRUD functionality for events.
- Integrated authentication to personalize event management for different users.
- Created a modern and responsive UI using Bootstrap.

## **Key Learnings/Takeaways**

- Improved Django skills: Learned to structure Django projects efficiently.
- Gained experience with PostgreSQL and Django ORM for database management.
- Improved front-end integration: Worked with FullCalendar.js to enhance user experience.

## **Bugs**

- Logout issues: Fixed redirection errors by manually setting a logout redirect.
- Event display bugs: Some events were not appearing correctly due to incorrect date formatting.


## **Future Improvements**

- Enhance mobile responsiveness</li>
- Add event categories with colour-coding.</li>
- Enable event reminders via email notifications.
