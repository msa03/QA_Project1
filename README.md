# QA-DevOps-SFIA_1-Project

* Project Introduction
* Project Design
* CI Pipeline
* Risk Assessment
* My App
* Project Review/Analysis
* Future Improvements

### Project Introduction
---
For this project, I was asked to create an online application using a Flask framework. It needed to have CRUD funtionality, meaning that a user should be able to create, read, update and delete user input data. The data itself had to be stored externally in a MySQL database, an RDS instance in AWS, and should include at least two tables that share a one-to-many relationship.

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

For project management, I used Trello to create a tracking board that allowed me to allocate user stories and specific tasks to achieve them. By implementing MoSCow prioritisation, I was able to determine which tasks were absolutely necessary for the MVP (must have) and the tasks/functionalities that would be an addition to the MVP (should have's and could have's). On Trello, I was able to show this with different coloured labels. Here is what my Trello board looked like at the start of my project:
![alt text](image.jpg)

For version source control I used git and stored my entire project structure and all my source code on GitHub. The benefit of using GitHub is that I would be able to make changes and commit them to update my repository but also be able to revert back to previous versions of my source code as all commits are tracked and saved. This is incredibly useful in the case that we accidentally push broken code up to our repository. As this allows me store my repository externally from my server, if the server did crash, I would be able to create a new server and clone down my repository to recreate the project infrastructure. My host connection dropped several times throughout the course of my project, so to ensure I always saved my current progress, I regularly pushed my commits up to my GitHub account.

I used python code in Visual Studio Code for the development of my app, specifically the Flask extension for python. This was all done on a Ubuntu 18.04 virtual machine. I installed a venv (virtual environment) for pip installs as this would ensure there were no conflicts between existing pip installs on the virtual machine (or local machine if you were working locally).

For the build and automated testing, Jenkins was the proposed server. Jenkins would allow me to clone my project repository into it and then initiate an automatic build from within it. This would also be the same for automated testing. As the application is an ongoing process, I would never be able to achieve a 100% build. For the build to be 100%, I would need to run the app using a systemd service so that the build would not hang. One useful function of using Jenkins is that it allows webhooks via GitHub to run a build every time a push is made to the main branch of the repository. Again, this is to allow a fully automated build. Here is an illustration of the CI Pipeline I am implementing:
![alt text](image.jpg)

### Risk Assessment
---
Before I started with the actual development of the app, I needed to produce an extensive risk assessment do identify the possible risks and areas that could prevent me from achieving my MVP, and then propose countermeasures to reduce the likelihood of the risks. I created my risk assessment in an excel spreadsheet which is shown below:
![alt text](image.jpg)

I updated the risk assessment with some of my own responses to the risks as the project progressed. This can be seen in the figure above.

### My App:
---
When a user navigates to the app, they can see the homepage where they are also able to view a list of the manufacturers added, if they exist. Otherwise they can follow the links to add one:
![alt text](image.jpg)

Upon clicking **Add Manufacturer** the user is taken to the corresponding page where they can add a manufacturer and specify its specialty:
![alt text](image.jpg)

Once the user submits their input they are redirected to the **Add Item** page where they can add an item for the selected manufacturer and specify its colour:
![alt text](image.jpg)

Once an item has been added, the user can view, update or delete their current manufacturers. If a manufacturer is deleted, all associated items will also be deleted:
![alt text](image.jpg)

### Project Review/Analysis
---
Upon completion of my project, there are a few things that I would like to reflect on. The majority of the coding and HTML was both fun and very challenging. As I was entirely a beginner in the python language, I initially struggled to grasp the logic of pythonic coding. I had to do a lot of extensive research for building a Flask app; this took up a lot of my project time to actually learn how to formulate working functions and also how to reference these within the HTML pages. 

As mentioned earlier, I had very little understanding about how to translate a database with a many-to-many relationship into working code so I quickly had to abandon my initial proposed project idea. As a result, I had to redo all of my models, forms and routes to reflect the changes in my subsequent database relationship. I was then able to produce a working application with full CRUD functionality.

I had a lot of issues with my Ubuntu server, specifically losing connection to the remote host from within Visual Studio Code very frequently. This greatly hindered my progress and added a heavier time constraint on my project every time it occurred. I encountered this problem right up until the day before the submission deadline. My only current solution for bypassing that obstacle was to restart the instance each time from within AWS and also having to update my configuration file with the new public DNS. At one point I decided to create a new instance altogether because my current one was not working, however I didn't need to use it in the end.

### Future Improvements
---
For future iterations of my project, I would like to add more columns to each database table or even a third table linkig to one of the intial two tables so that the app can be expanded upon. I also would like be able to create an app based off my inital project idea as it would be very beneficial for my own understanding to learn how to code a many-to-many relationship into an app. Finally I could put a bit more emphasis for making the front end more aesthetically pleasing for the end user as this could affect repeat usability for the user.

In terms of project management, I think I could definitely improve my time management. A large portion of the time I had was spent struggling and worrying about not being able to code the way I wanted, so I would focus on being able to break down any issues so that it is easier to deal with and move forward at the same time.