# Tab-Tracker-Server

This is the server side code for the web application Tab Tracker. 

The codebase comes with pre-built fixtures with some initial data for the app, as well as models for the different tpes of data the server will be recieving, and functions that handle different requests from the client as well as handiling authentiation of users. 

To begin seed the data base by running these commands in your terminal to load your models:
- python3 manage.py makemigrations tabtrackerpapi
- python3 manage.py migrate

Once your models have been migrated, establish a connection with a databse, then you can seed your data using these commands in your terminal:
- python3 manage.py loaddata lessons
- python3 manage.py loaddata routines
- python3 manage.py loaddata exercises

After this your all set to run the sever for Tab Tracker, to do so use this command in your terminal:
- python3 manage.py runserver
