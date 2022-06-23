# pictures
# Picture-Globe  
## Author  

>[David Njagi](https://github.com/poldiee)  
  
# Description  
Django application for personal gallery that allows user to upload images for other to see and be able to to share by copying the image link.

##  Live Link  
 Click [View Site](https://.herokuapp.com/)  to visit the site

## Screenshots  

## User Story  

* View different photos that interest them  
* Click a single image to expand it and view the details of that photo  
* Search for different categories   
* Copy a link to the photo to share with my friends.  
* View photos based on the location they were taken.  

## BDD  



## Setup and Installation  
To get the code..  

##### Cloning the repository:  
 ```bash 
 https://github.com/poldiee/pictures.git 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd pictures pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations pictures 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  


## Technology used  

* [Python3.8](https://www.python.org/)  
* [Django 4](https://docs.djangoproject.com/en/)  
* [Heroku](https://heroku.com)  


## Known Bugs  
*  

## Contact Information   
If you have any question or contributions, please email me at [nessidave@gmail.com]  

## License 

* MIT License
* Copyright (c) 2022 **poldiee**
