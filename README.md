"# Visitor-Management-System" 

Manages the check in and check out information of the visitors. Sends mail to the visitor's about their checkin and checkout details.

To Run The code :

Change the settings in settings.py:

EMAIL_HOST_USER = 'abc@gmail.com'  # 'your email address' 

EMAIL_HOST_PASSWORD = 'abcpassword'  # 'your email password'

for the first time:

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

After completing the above steps run:

python manage.py runserver

You can see the images in the in 'images' folder for outline of the project.

