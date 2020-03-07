# Visitor-Management-System

Manages the check in and check out information of the visitors. 

# Manager(admin):

-> Can see all visitors checkin and checkout details

-> Can remove access to any visitor

# Visitor(user):

-> Creates an account in the system

-> Can update his/her profile

-> Can view his all Checkin/Checkout information

-> Recieves mails related to his Checkin/Checkout


# To Run The code :

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

