Django Portal Yubikey
=========

First thing to do after you get a yubikey is to get api key:
https://upgrade.yubico.com/getapikey/
This link provides you Client ID & Secret Key

Plug in your yubikey to your machine, when asked for keyboard config. Skip & manually select the keyboard.
Please go to that link, enter your email id & press the center of the key to generate OTP.

Install Dependencies
==========

Install The following on your virtual machine: (I have used Virtual Env)

.. prompt:: bash

	pip install Django==1.9
	pip install django-otp==0.3.4
	pip install yubico-client==1.9.1
	pip install django_yubico

This code supports both Django version 1.8 & 1.9

Download the code from github
=========

Download at: https://github.com/cloudmesh/yubikey

Or use git clone.

Configuration:
===========

Yubikey uses a Database called `django_yubico_yubicokey` and model named `DjangoYubicoYubicokey`. To check if
this is installed use this command:

.. prompt:: bash
	cd sample_yubikey/
   	python manage.py inspectdb

if it is not installed then use: 

.. prompt:: bash

   python manage.py makemigrations
   python manage.py migrate

If you are still unable to find that in your database follow these steps:

.. prompt:: bash

	python manage.py migrate --fake
	python manage.py makemigrations
	python manage.py --fake-initial
	

Add your Yubikey to Django Database:
^^^^^^^^^^^

Once you confirm that `DjangoYubicoYubicokey` is installed make sure
that you have created an admin user for django portal.
To create admin user in django:

.. prompt:: bash

   python manage.py createsuperuser

follow the instructions to create credentials.

Time to run Django and store your keys,run

.. prompt:: bash

	python manage.py runserver

go to:

* http://127.0.0.1:8000/admin/ 

login using the credetials that you just created.  you will see a site administration page with Yubico Yubikeys.

If you see the database by clicking the link you will see that there are no yubikeys stored.

#. Click on +Add link and follow the instructions. 
#. Generally you'll be asked to give these information.
	* Device ID, Client ID, Secret Key and the User.  Yubikey supports multiple user 
	authentication with just one key. (Advantage)

To get the details:

#. Device ID: open a text editor, connect your yubikey to the machine, press the
    button on top of yubikey. This generates a random
    string. First 12 characters is constant for a device & that is the device ID.
#. Client ID: when you registered in the link earlier with the getapikey you'll get the Client ID and the secret key.
#. Secret Key: Generated when you registered in the getapikey link.

Enter all the details as mentioned and this will give a user access to login using yubikey. 


Test the key:

go to:

* http://127.0.0.1:8000/yubico/login/

You'll be asked for your username and otp key.  enter your username,
click on the otp and press the otp to generate the otp key.  If
success then you'll be redirected to page to enter your password.  On
which if you succeed you'll be taken to `/account/profile` (Don't Worry!! This has not
been created so you'll get an error. It means that you were
able to login using yubikey)


Usually I faced like 2 issues so far with just the login after successfull installation of yubikey database:

#. NO_VALID_ANSWERS, https://github.com/Kami/python-yubico-client/issues/6
#. Any other error related to Database. In this case follow this link
    to resolve it:

    * http://stackoverflow.com/questions/29888046/django-1-8-create-initial-migrations-for-existing-schema


This document will be maintained by @tbindi , & will be constantly updated as and when it is tested on different 
set of machines.
