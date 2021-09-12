# QA-DevOps-SFIA_1-Project

### Project Introduction
---
For this project, I was asked to create an online application using a Flask framework. It needed to have CRUD funtionality, meaning that a user should be able to create, read, update and delete user input data. The data itself had to be stored externally in a MySQL database and should include at least two tables that share a one-to-many relationship.

### Project Design
---
I initially decided to make a shopping list app whereby a user could create a custom list and then add items to that list. The user could also update the lists and items and delete them too if desired. I created an ERD (Entity-Relationship Diagram) in an online [draw.io](https://app.diagrams.net/) app that allowed me to illustrate the connections between the tables - in my case, a many-to-many relationship. See below:
![alt text](image.jpg)

In my case of a many-to-many relationship, I needed to create a join or link table to separate it into two one-to-many relationships. When I began coding for the app, I had a lot of issues with trying to reference foreign keys and using backrefs, so to ensure I would have an MVP and because of time-constraints I had to completely change my idea. I settled on an app where a user could specify (add) a manufacturer and add items to that manufacturer. A similar concept to my first idea, but this would be a one-to-many relationship. See the new ERD below:
![alt text](image.jpg)

### CI Pipeline
---
The stages of the CI (Continuos Integration) Pipeline that I had to implement were:
* Project Management/Tracking
* Version Source Control
* Development
* Build/Testing
![alt text](image.jpg)

For project management, I used Trello to create a tracking board that allowed me to allocate user stories and specific tasks to achieve them. By implementing MoSCow prioritisation, I was able to determine which tasks were absolutely necessary for the MVP (must have) and the tasks/functionalities that would be an addition to the MVP (should have's and could have's). On Trello, I was able to show this with different coloured labels. Here is what my Trello board looked like at the start of my project:
![alt text](image.jpg)

For version source control I used git and stored my entire project structure and all my source code on GitHub. The benefit of using GitHub is that I would be able to make changes and commit them to update my repository but also be able to revert back to previous versions of my source code as all commits are tracked and saved. This is incredibly useful in the case that we accidentally push broken code up to our repository. As this allows me store my repository externally from my server, if the server did crash, I would be able to create a new server and clone down my repository to recreate the project infrastructure. My host connection dropped several times throughout the course of my project, so to ensure I always saved my current progress, I regularly pushed my commits up to my GitHub account.

I used python code in Visual Studio Code for the development of my app, specifically the Flask extension for python. This was all done on a Ubuntu 18.04 virtual machine. I installed a venv (virtual environment) for pip installs as this would ensure there were no conflicts between existing pip installs on the virtual machine (or local machine if you were working locally).