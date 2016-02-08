Django Portal Yubikey
===========================

To use yubikey, you will need Client ID & Secret Key.
Steps to get your yubikey api key:

#. Go to link: https://upgrade.yubico.com/getapikey/
#. Please enter your email id.
#. Click on the next input box, plug in your yubikey to USB port of your computer, press the button at the center of the yubikey to generate one-time password.
#. You will be redirected to another page with Client ID & Secret Key. 
#. Copy paste both the Client ID & Secret key to a notepad.


Download the code from github
==============================

Repository: https://github.com/cloudmesh/yubikey

Get Source

.. prompt:: bash
	    
  git clone git@github.com:cloudmesh/yubikey.git
  cd yubikey


Install Dependencies
============================

Use the following commands to install the dependencies for using 
yubikey:

.. prompt:: bash
	    
  make r
  make dbmigrate 
  make admin
  make run


`make r` will install all the dependencies that is used for yubikey.
`make dbmigrate` will migrate the required db from the previously installed 
packages.
`make admin` will ask you to create a superuser. Please continue to 
fill in your username, email and password.
`make run` will run the local server, open the browser and go to 
https://localhost:8000/admin/


Configuration - Verification
===============

Yubikey uses a Database called `django_yubico_yubicokey` and model
named `DjangoYubicoYubicokey`. To check if this is installed use this
command:

.. prompt:: bash
	    
  make inspect
	

Add your Yubikey to Django Database:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Go to:

* http://127.0.0.1:8000/admin/ 

Login using the credetials that you just created. You will see a site 
administration page with Yubico Yubikeys.

If you see the database by clicking the link you will see that there
are no yubikeys stored.

#. Click on +Add link and follow the instructions. 
#. Generally you'll be asked to give these information.
	* Device ID, Client ID, Secret Key and the User.  Yubikey supports multiple user 
	authentication with just one key. (Advantage)

To get the details:

#. Device ID: open a text editor, connect your yubikey to usb port to the machine, press the
    button on top of yubikey. This generates a random
    string. First 12 characters is constant for a device & that is the device ID.
#. Client ID: when you registered in the link earlier with the getapikey you'll get the Client ID and the secret key.
#. Secret Key: Generated when you registered in the getapikey link.


Enter all the details as mentioned and this will give a user access to login using yubikey. 

Test the key:

go to:

* http://127.0.0.1:8000/yubico/login/

Enter your username, Click on OTP input box and connect your yubikey to the usb port.
Press the center of the yubikey to generate the otp. Click on login, you will be taken
to the next page to enter your password. Enter the password and you will be taken 
to the accounts/profile/ page. Don't worry, you have just logged in.


Possible Issues that one will face
===============
Usually I faced like 2 issues so far with just the login after
successfull installation of yubikey database:

#. NO_VALID_ANSWERS, https://github.com/Kami/python-yubico-client/issues/6
#. Any other error related to Database. In this case follow this link
    to resolve it:

    * http://stackoverflow.com/questions/29888046/django-1-8-create-initial-migrations-for-existing-schema


This document will be maintained by @tbindi , & will be constantly
updated as and when it is tested on different set of machines.
