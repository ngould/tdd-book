Provisioning a new site
=======================

# Required packages:

* nginx
* Python 2.7
* Git
* pip
* virtualenv

e.g., on Ubuntu:

  sudo apt-get install nginx git python python-pip
  sudo pip install virtualenv

## Nginx Virtual Host Config

* see nginx.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

## Upstart job

* see gunicorn-upstart.template.conf
* replace SITENAME with, e.g., stagin.my-domain.com

## Folder structure
Assume we have a user account at /home/username

/home/username
|---sites
    |---SITENAME
        |---database
        |---source
        |---static
        |---virtualenv

