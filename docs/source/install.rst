Get API key
=========

Go to this link and get your API key to use:
https://upgrade.yubico.com/getapikey/

Install Django
==========

Install Django on your VM: pip install Django==1.8 (Version 1.8
because this sample uses request.REQUEST.get which is deprecated in
1.9)

Install The following

.. prompt:: bash

	pip install django-otp==0.3.4
	pip install yubico-client==1.9.1
	pip install django_yubico

Some code
=========

Make this section use git clone

Unzip the attached file using 

.. prompt:: bash

      tar xvzf yubi.tar.gz

Configuration
===========

Yubikey uses a Database called `DjangoYubicoYubicokey`. To check if
this is installed use this command:

.. prompt:: bash

   	python manage.py inspectdb

if it is not installed then use: 

.. prompt:: bash

   python manage.py makemigrations
   python manage.py migrate

Cretae a user
^^^^^^^^^^^

Once you confirm that `DjangoYubicoYubicokey` is installed make sure
that you have created an admin user for django portal.
To create admin user in django:

.. prompt:: bash

   python manage.py createsuperuser

follow the instructions to create credentials.

Run the django by: (There are only 2 url patterns as of now. /admin/ &
/yubico/)

.. prompt:: bash

	python manage.py runserver

go to:

* http://127.0.0.1:8000/admin/ 

login using the credetials that you just created.  you will see a site administration page with Yubico Yubikeys.

If you see the database by clicking the link you will see that there are no yubikeys stored.

To add yubikeys click on +Add link and follow the
instructions. Generally you'll be asked to give these information:
Device ID, Client ID, Secret Key and the User.  Yubikey supports
multiple user authentication with just one key. (Advantage)

To get the details:

#. Device ID: open a text editor, connect your yubikey, press the
    button on top of yubikey. Generates a random
    string. First 12 characters is  constant for a device & that is the device ID
#. Client ID: when you registered in the link earlier with the getapikey you'll get the Client ID and the secret key.
#. Secret Key: Generated when you registered in the getapikey link.

Enter all the details as mentioned and this will give a user access to login using yubikey. 


Test the key:

go to:

* http://127.0.0.1:8000/yubico/

You'll be asked for your username and otp key.  enter your username,
click on the otp and press the otp to generate the otp key.  If
success then you'll be redirected to page to enter your password.  On
which if you succeed you'll be taken to `/account/profile` (this has not
been created so you'll get an error but it still means that you were
able to login using yubikey)

Usually I faced like 2 issues so far with just the login after successfull installation of yubikey database:

#. NO_VALID_ANSWERS, https://github.com/Kami/python-yubico-client/issues/6
#. Any other error related to Database. In this case follow this link
    to resolve it:

    * http://stackoverflow.com/questions/29888046/django-1-8-create-initial-migrations-for-existing-schema

This is an initial draft to test django with yubikey using a sample
code. This will be updated as and when we test it against other
systems.
