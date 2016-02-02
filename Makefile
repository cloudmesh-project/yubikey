UNAME := $(shell uname)

BROWSER=firefox
ifeq ($(UNAME), Darwin)
BROWSER=open
endif
ifeq ($(UNAME), Windows)
BROWSER=/cygdrive/c/Program\ Files\ \(x86\)/Google/Chrome/Application/chrome.exe
endif
ifeq ($(UNAME), CYGWIN_NT-6.3)
BROWSER=/cygdrive/c/Program\ Files\ \(x86\)/Google/Chrome/Application/chrome.exe
endif



doc: 
	cd docs; make html

publish:
	ghp-import -n -p docs/build/html

view:
	$(BROWSER) docs/build/html/index.html

man: cloudmesh
	cm man > docs/source/man/man.rst

log:
	gitchangelog | fgrep -v ":dev:" | fgrep -v ":new:" > ChangeLog
	git commit -m "chg: dev: Update ChangeLog" ChangeLog
	git push

######################################################################
# INSTALL AND RUN
######################################################################

r:
	pip install -r requirements.txt

install:
	cd sample_yubi; python manage.py makemigrations
	cd sample_yubi; python manage.py migrate
	cd sample_yubi; python manage.py inspectdb

admin:
	cd sample_yubi; python manage.py createsuperuser

run:
	cd sample_yubi; python manage.py runserver

open:
	open http://127.0.0.1:8000/admin/ 


######################################################################
# CLEANING
######################################################################

clean:
	python setup.py clean

######################################################################
# TAGGING
######################################################################

tag: log
	python setup.py tag

rmtag:
	python setup.py rmtag

