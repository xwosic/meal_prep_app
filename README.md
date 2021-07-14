># meal_prep_app
>>## description
>>This is web application project about preparing meals for all week. In this app user can
>>* create recipes
>>* group them
>>* export gathered recipes to shopping list
>>
>>## installation
>>### follow these commands to set up environment and project:
>>* first make sure that your Python is 3.6 or greater
>>    * python --version
>>
>>* clone repo to selected folder
>>    * git clone https://github.com/xwosic/meal_prep_project.git
>>
>>* in folder where you clone repo create virtual environment
>>    * python -m venv venv
>>
>>* activate the venv
>>    * on unix: source venv/bin/activate
>>    * on windows: source venv/Scripts/activate 
>>    
>>* go to meal_prep_project
>>    * cd meal_prep_project
>>  
>>* there should be requirements.txt file in it use it to install all packages
>>    * python -m pip install -r requirements.txt
>>
>>* migrate project to create database
>>    * python manage.py migrate
>>
>>* run project and enter url
>>    * python manage.py runserver
