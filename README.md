# Django Practise

## Usefull commands related to Django
1. To install Django : `pip install Django`
2. Check if django is installed or not : `python -m django --version`
3. To create Django Project :  `django-admin startproject projectname`
4. To start/run django project created:  `python manage.py runserver`. Usually it runs at 127.0.0.1:8000/.
5. To create Django app :  `python manage.py startapp appname`. Here "appname" is user-defined so you can write anything instead of this word. Make sure you are inside the terminal at the same level as manage.py while running this command. 
6. If you create any changes to models or app. For example, adding new column to a model then after making changes you need to execute two commands in terminal that are `python manage.py makemigrations <app-name>` and `python manage.py migrate`. [Link](https://stackoverflow.com/questions/50603258/django-how-can-i-add-delete-fields-in-sqlite3-database)


## List of Projects

1. Deploy ML in Django ([View](DeployML_in_Django/))
   * This project is an example of how to use your ML model and deploy it. In this a website is designed where user is required to enter relevant input and then a ML model           predicting category of Glass is used to showcase the output on website page.
2. Feedback Analysis Website using Django ([View](FeedbackAnalysis/))
   * In this user will submit some text and then the website will show sentiment analysis of the text submitted on website.
