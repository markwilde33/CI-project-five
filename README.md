# Interstellar Issue Tracker 

### Code Institute: Full Stack Frameworks Milestone Project

<a href="https://interstellar-issue-tracker.herokuapp.com/" target="_blank"> Click here to view website</a>

*Developer: Mark Wilde*

-----------------------



## Index


1. [Project Instructions](#instructions-from-code-institute)
2. [Issue Tracker Information](#issuetracker-information)
3. [UX](#ux)
    * [Design](#design)
    * [User Stories](#user-stories)
4. [Features](#features)
5. [Technologies](#technologies-used)
6. [Testing](#testing)
    * [User Stories](#user-stories)
    * [Manual Testing](#manual-testing)
    * [Other](#other)
7. [Deployment](#deployment)
8.  [Installation](#installation)
9. [Credits](#credits)



## Instructions From Code Institute



Guidelines for project development:


- Build a web app that fulfills some actual (or imagined) real-world need. This can be of your choosing and may be domain specific.
- Write a README.md file for your project that explains what the project does and the need that it fulfills. It should also describe the functionality of the project, as well as the technologies used. Detail how the project was deployed and tested and if some of the work was based on other code, explain what was kept and how it was changed to fit your need. A project submitted without a README.md file will FAIL.
- The project must be a brand new Django project, composed of multiple apps (an app for each reusable component in your project).
- The project should include an authentication mechanism, allowing a user to register and log in, and there should be a good reason as to why the users would need to do so. e.g., a user would have to register to persist their shopping cart between sessions (otherwise it would be lost).
- At least one of your Django apps should contain some e-commerce functionality using Stripe. This may be a shopping cart checkout, subscription-based payments or single payments, etc.
- Include at least one form with validation that will allow users to create and edit models in the backend (in addition to the authentication mechanism).
- The project will need to connect to a database (e.g., sqlite or Postgres) using Django’s ORM
- The UI should be responsive, use either media queries or a responsive framework such as Bootstrap to make sure that the site looks well on all commonly-used devices.
- As well as having a responsive UI, the app should have a great user experience.
- The frontend should contain some JavaScript logic to enhance the user experience.
- Whenever relevant, the backend should integrate with third-party Python/Django packages, such as Django Rest Framework, etc. Strive to choose the best tool for each purpose and avoid reinventing the wheel, unless your version of the wheel is shinier (and if so, consider also releasing your wheel as a standalone open source project).
- Make sure to test your project extensively. In particular, make sure that no unhandled exceptions are visible to the users, under any circumstances. Use automated Django tests wherever possible. For your JavaScript code, consider using Jasmine tests.
- Use Git & GitHub for version control. Each new piece of functionality should be in a separate commit.
- Deploy the final version of your code to a hosting platform such as Heroku.



## Issue Tracker Information


- This project is a Django driven responsive design web application that allows users to create tickets. 
- Tickets specify a bug that a user would like fixed or a feature which a user would like implemented.
- Users can read, create, edit, delete, upvote, pay for, comment on, and view the current status of tickets.
- This project used the Stripe API to handle payment processing and harnesses Django's built-in user authentication features.
- There is a data visualization page provided so that users can view data in chart form, such as most popular features and the ratio of tickets to users.
- The project was developed with the purpose of providing a platform which can be utilized by an existing project/website, so that it's development team have access to constructive criticism and suggestions from their customers; and as such, can make the recommended improvements to their product.



## UX



### Design


- Development of the website adhered to a mobile first approach, it implements a simplistic design with minimal content. 

- The Bootstrap (version 4.3.1) framework underpins the project and was implemented as per convention. 
  
- Users are asked to register or login before being granted access to the website.

- All pages share the same navbar and footer except for the homepage which has a separate footer to provide information about the website.

- Each page has a clear purpose and some unique functionality.
  
- An outer space theme was utilized which ties in with the websites name. The images used by the website were chosen in an attempt to increase its visual appeal. 
 
- The color scheme was chosen to provide contrast against the dark background and is consistent across the website.



### User Stories


Several user stories were considered before development began:

1. "I want to be able to share bugs I have found with the websites development team."
2. "I want to be able to recommend potential features I feel would improve the website, with the websites development team."
3. "I want to be able to view, comment on, upvote or make a donation towards other tickets."
4. "I want other users to be able to view comment on, upvote or make a donation towards my tickets."
5. "I want to be kept up to date with the status of tickets, the date and time of ticket status changes should be provided."
6. "I would like to be provided with data visualization charts or graphs, that show worthwhile ticket information."
7. "I want all of my created tickets available for viewing in one place, such as a personal profile page."
8. "I want to be able to edit and delete my tickets."
9. "There are some websites I visit which I feel could benefit from providing an issue tracker app for their users, and would like to be able to recommend a good issue tracker to them."



## Existing Features



| Page          |                                                                                                                                                                                     Description                                                                                                                                                                                      |
| :------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Index         |  This is the landing page. It is a basic page with a background image, some quotes from our customers, website information in the footer and links for the registration and login pages in the navbar.                                                                                                                                                                               |
| Tickets       |  This page displays user tickets in a table format. Pagination is used to show five tickets per page. The information displayed includes the ticket title, author, description, upvotes, status, date created, type and a link to view the ticket in more detail. There is a simple footer and navbar which is used across all other pages also, except the index page.              |
| New Ticket    |  This page provides a simple form for users to add a ticket. Users are asked to specify the ticket title, description and type before submitting.                                                                                                                                                                                                                                     |
| Ticket View   |  This page provides detailed information about an individual ticket, including the ticket title, author, description, upvotes, status, date created, type, status last updated, comments from other users, a comment box to make a new comment, an upvote/donate button and button links to the tickets and user profile page.                                                        |
| Profile       |  This page displays the users collection of created tickets from newest to oldest using a table format. Users can also view, edit and delete their tickets from here.                                                                                                                                                                                                                |
| Dashboard     |  This is a data visualization page were users can view some of the most important information from the database, in chart form.                                                                                                                                                                                                                                                      |
| Admin         |  When signed in as admin, the admin panel can be accessed directly from a link in the navbar.                                                                                                                                                                                                                                                                                        |
| Make Payment  |  A simple page from which a user can confirm they want to donate €9.99 towards their chosen feature, and then make the donation using stripe.                                                                                                                                                                                                                                        |
| Miscellaneous |  When a user is signed in, the navbar provides links to the tickets, new ticket, Profile and dashboard pages, as well as a link to log them out. The footer provides a link to the projects github page.                                                                                                                                                                             |



This project also uses custom Django authentication templates to manage URL paths and provide user authentication functionality including;

* **Password Reset Form** - A form allowing users to enter an email and receive a link to reset their password
* **Password Reset Done** - A page that confirms an email has been sent to reset password
* **Password Reset Email** - An email template that provides the password reset link and instructions for the user
* **Password Reset Confirm** - A form allowing users to confirm their new password
* **Password Reset Complete** - A page that confirms password has been successfully reset 



## Future Technologies


- The data visualization page is static at present, it would be better if the charts were responsive in real time. This can be implemented in a future update. 
  
- Users might like to upload their own personal avatars to be displayed in the comments section, this could also be implemented in a future update.



## Technologies Used


### Integrated Development Environment


- [Cloud9](https://aws.amazon.com/cloud9/?origin=c9io)
    - The project was developed using the **Cloud9** Integrated Development Environment.



### Front end


- [HTML](https://www.w3schools.com/html/default.asp)
    - The project uses **HTML** to create the pages.

- [CSS](https://www.w3schools.com/css/default.asp)
    - The project uses **CSS** to style the pages.

- [Bootstrap](https://getbootstrap.com/)
    - The project uses **Bootstrap** for styling and responsive design.

- [Font Awesome](https://fontawesome.com/)
    - The project uses **Font Awesome** for various icons across the website.

- [Google Fonts](https://fonts.google.com/)
    - The project uses **Google Fonts** roboto style.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** for responsiveness.
    
- [Chart js](https://www.chartjs.org/)
    - The project uses **Chart js** for data visualization.
  
- [JavaScript](https://developer.mozilla.org/bm/docs/Web/JavaScript)
    - The project uses **JavaScript** for responsiveness.
  


### Back end


- [Python](https://www.python.org/)
    - The project uses **Python** to write the websites logic.
  
- [Django](https://www.djangoproject.com/)
    - The project was built using the **Django** framework.
  
- [Stripe](https://stripe.com/docs/payments/checkout)
    - The project uses **Stripe** for handling online payments.
    
- [PostgreSQL](https://www.heroku.com/postgres)
    - The project uses a **PostgreSQL** database as recommended by Heroku.
    


### Version Control


- The project uses [Git](https://git-scm.com) as it's version control system.
  
- The project uses  a  [Github](https://github.com/markwilde33) repository.



### Hosting Platform


- [Heroku](https://devcenter.heroku.com/)
    - The project uses the **Heroku** cloud platform for hosting the website.



## Testing


<details>
      <summary><strong><em>User Story Tests</em></strong></summary>

## User Tests:

1. Verify that users can share bugs and recommend features with the websites development team.
2. Verify that all users can view, comment on, upvote or make a donation towards other tickets.
3. Verify that users are kept up to date with the status of current tickets.
4. Verify that data charts are provided for users to view at their leisure.
5. Verify that users each have their own profile page, where they can view, edit and delete their tickets.

</details> 


<details>
      <summary><strong><em>Manual Tests</em></strong></summary>

## Manual Tests:
  

#### Index Page:
   
1. Open the app.
2. Try to submit the empty register form and verify that an error message about the required fields appears.
3. Try to submit the empty login form and verify that an error message about the required fields appears.
4. Try to submit the login form without first registering and verify that an error message appears.
5. Click on the forgot password link and verify that the reset password pages are functioning correctly, and that a user receives an email to reset their password.
6. For the registration form, verify a user receives a warning message if they enter a user name that has already been chosen by another user.
7. For the login form, verify a user receives a warning message if they enter an incorrect user name and/or password.
8. Verify that the 'Sign In' link on the register page is functioning as intended, i.e., a user will be taken to the login page when they click it.
9. When a user successfully registers verify they have access to the full site and receive a welcome message.
10. When a user successfully logs in verify they have access to the full site and receive a welcome message.
11. Verify that the user block quotes and footer information are/is displaying correctly. 

#### Navbar:

1. Click on the "Interstellar Issue Tracker" link, verify the homepage is loaded.
2. Click on the "Tickets" link, verify the tickets page is loaded.
3. Click on the "New Ticket" link, verify the My new ticket page is loaded.
4. Click on the "Account" drop down link, verify the user can click on the profile page by clicking on the profile link, or log out by clicking on the log out link.
5. Click on the "Dashboard" link, verify the dashboard page is loaded.
6. Verify all information is displaying as intended with no grammatical errors.

#### Footer:

1. On the index page, verify the footer is displaying website information.
2. On all other pages, click on the "Mark Wilde" link, and verify the github repository of the website is opened on a separate page.
3. Verify all information is displaying as intended with no grammatical errors.
   
#### Tickets:

1. Verify that the table is displaying all relevant ticket details (as previously documented in the information section) correctly.
2. Verify the view ticket button is functioning correctly, when clicked users are taken to a full page view of the ticket.
3. Verify the page pagination is functioning correctly, five tickets are displayed per page.
4. Verify all information is displaying as intended with no grammatical errors.

#### New Ticket:

1. Verify that the ticket form is rendering on the page.
2. Try to submit the empty login form and verify that an error message about the required fields appears.
3. Verify the submit button is functioning correctly, when clicked users are taken to the tickets page were they can view the ticket they have created.
4. Verify users receive a message informing them their ticket has been updated when they edit or create a ticket and click the submit button.
5. Verify the return to tickets page link is functioning correctly, when clicked a user is taken to the tickets page.
6. Verify all information is displaying as intended with no grammatical errors.

#### View Ticket Page:
   
1. Verify that the page is displaying all relevant ticket details and functionality (as previously documented in the information section) correctly.
2. Verify all information is displaying as intended with no grammatical errors.

#### Profile Page:
   
1. Verify any ticket a user adds or edits is displayed here.
2. Verify that the table is displaying all relevant ticket details (as previously documented in the information section) correctly.
3. Verify users can view, edit or delete a ticket by clicking the buttons labeled same. 
4. Verify the view, delete and edit ticket buttons are functioning correctly.
5. Verify users receive a message asking them to confirm a ticket deletion when they click the ticket delete button.
6. verify users are taken to the ticket view page when they click the view button.
7. Verify users are taken to the ticket form page when they click the edit button.
8. Verify the page pagination is functioning correctly, five tickets are displayed per page.
9. Verify all information is displaying as intended with no grammatical errors.

#### Dashboard:

1. Verify that all charts are rendering as intended and are mobile responsive.
2. Verify all information is displaying as intended with no statistic or grammatical errors.


#### Make Payment Page:

1. Verify user are informed of their payment amount and the make payment button is functioning correctly.
2. Verify a stripe payment form pops up when users click the make payment button.
3. Verify the users donation is confirmed when they correctly enter their payment details, and that they are returned to the tickets page.
4. Verify error messages are shown if users enter incorrect details in the stripe payment form.
5. Verify the 'return to tickets' link is functioning correctly and takes a user back to the tickets page when clicked.
6. Verify all information is displaying as intended with no grammatical errors.

 
</details> 


<details>
      <summary><strong><em>Other</em></strong></summary>


### Further Testing

- Google chrome developer tools where used at every stage of production to
isolate issues and improve mobile responsiveness.
- The app has been tested on various browsers, including Chrome, Firefox, Opera, and Safari.
- The app was tested across many screen sizes, from very small to very large.
- Some family members tested the app on their own devices and reported no issues with functionality and responsiveness.
- It is displaying as intended across various devices and in different browsers.


### Issues

- The author is not yet proficient in automated testing, and as such, was unable to adhere to a test driven development approach.
- When a user makes a donation towards a feature an upvote is not added to the ticket. Admin can check stripe payment history and add the upvote after the fact. Obviously this is not ideal, and needs to be rectified. An upvote should be added automatically to a feature when a donation payment is confirmed. This could be fixed in future versions of the application.
- Users can currently upvote bugs multiple times. Each bug should only receive a maximum of one upvote per user, this could be fixed in future versions of the application.



## Deployment


The website has been deployed to [Heroku](https://www.heroku.com) and can be accessed [here](https://interstellar-issue-tracker.herokuapp.com/)

#### With thanks to kimpea
[found at](https://raw.githubusercontent.com/kimpea/us-issue-tracker/master/README.md)

### To run this locally...

1. Create a new workspace in C9 with a workspace name and description, and use `https://github.com/markwilde33/CI-project-five.git` in the 'Clone from Git' field.
2. Create a virtual environment with `wget -q https://git.io/v77xs -O /tmp/setup-workspace.sh && source /tmp/setup-workspace.sh`.
3. Activate this virtual environment with `mkvirtualenv [name of virtual environment]`.
4. Install requirements with `pip3 install -r requirements.txt`. 
5. Create an env.py file with the following: 

```
import os

os.environ.setdefault('STRIPE_PUBLISHABLE', "")
os.environ.setdefault('STRIPE_SECRET', "")
os.environ.setdefault('SECRET_KEY', '')
#os.environ.setdefault('DATABASE_URL', '')
```

6. Make sure you uncomment `#import env` in settings.py.
7. You will need to generate your own SECRET_KEY. You will need to set up a Stripe account and use their testing API keys. Once you have a database set up (you can use Postgres for database on Heroku) you can uncomment
os.environ.setdefault('DATABASE_URL', '') and use the key that PostgreSQL generates for you in Heroku's Config Vars.
8. Make migrations with `python3 manage.py makemigrations`.
9. Migrate with `python3 manage.py migrate`.
10. Create a super user with `python3 manage.py createsuperuser` and follow instructions in your terminal.
11. To run the application locally, type in `python3 manage.py runserver $IP:$C9_PORT`.
12. Please note that the database will be empty, therefore there will be no reported bugs or requested features on display. This also means the graphs will not be showing until data is submitted into the database. 



**Heroku Deployment**


1. Create an [Heroku](https://www.heroku.com) account.

2. Create a new app 'Interstellar Issue Tracker' on heroku.com

3. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli):
    ``` 
    $ brew install heroku/brew/heroku
    ``` 
4. Login to heroku:
    ``` 
    $ heroku login
    ``` 
5. Check app has been created by heroku:
    ``` 
    $ heroku apps
    ``` 
6. Add heroku remote:
    ``` 
    $ heroku git:remote -a Interstellar Issue Tracker
    ``` 
#### With thanks to kimpea
[found at](https://raw.githubusercontent.com/kimpea/us-issue-tracker/master/README.md)

7. Use `git status`to outline all staged and unstaged files. Use `git add` to stage all files.
8. Add env.py to .gitignore with `echo env.py >> .gitignore` so that secret keys are not pushed to GitHub or Heroku.
9. Use `git commit -m [message]` to commit changes.
10. Use `git push -u origin master` to push these changes to GitHub.
11. Log into Heroku and Create New App. Create a unique name and region (USA or Europe, whichever is closest to you).
12. Navigate to Resources and search for 'PostgreSQL' - choose 'Hobby Dev - Free' and select 'Provision'.
13.Go to Settings and Reveal Config Vars - copy and paste the SECRET_KEY, STRIPE_PUBLISHABLE and STRIPE_SECRET into the fields.
14. In env.py, uncomment DATABASE_URL and use the key generated from PostgreSQL in Heroku's Config Vars. 
15. In Config Vars, add DISABLE_COLLECTSTATIC = 1.
16. Run `python3 manage.py makemigrations` and `python3 manage.py migrate`.
17. Create a new super user for the production database with `python3 manage.py createsuperuser` and follow instructions in the terminal.
18. `pip3 freeze > requirements.txt` to make sure requirements.txt is up to date. Remove pygobject and unattended upgrades.
19. Create a Procfile and add `web: gunicorn tracker.wsgi:application`
20. In settings.py, comment out `import env` and set `DEBUG = False`.
21. In Heroku, go to Deploy and select GitHub as a deployment method. Find your repository. Manually deploy the master branch. Activate automatic deploys.
22. Add the deployed Heroku link to ALLOWED_HOSTS in settings.py and `git push origin master`. The Heroku app should now be working.
  


### Development vs Deployed Version

- In the development version, Debug is set to True and the env.py file is imported into settings.py. However, in the deployed version, Debug is set to False and env.py is commented out. Also, the env.py file is not pushed to GitHub or Heroku as this contains keys which need to remain hidden from other users. The deployed version uses Heroku's PostgreSQL database whereas the development version uses SQLite. 



## Credits


[Code Institute](https://codeinstitute.net/)

The Html Fundamentals module, CSS Fundamentals module, Python Fundamentals module,Practical Python module and the Fullstack Frameworks module were used for guidance.



### Media

- [Google Images](https://www.google.ie/imghp) was used for to find website images.



### Acknowledgements


- I received inspiration for this project from [Code Institute](https://codeinstitute.net/), [The Net Ninja](https://www.thenetninja.co.uk), [Brad Traversy](https://www.traversymedia.com/) and [Corey Schafer](https://www.youtube.com/user/schafer5/featured).