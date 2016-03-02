Provisioning a new site
=======================

## Required packages:

* nginx
* Python3
* Git
* pip
* virtualenv

e.g.,, on RHEL:
    	- sudo yum install nginx

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, e.g., www.seanapsys.com

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, e.g., www.seanapsys.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
└ ─ ─ sites
      └ ─ ─ SITENAME
             ├ ─ ─ database
             ├ ─ ─ source
             ├ ─ ─ static
             └ ─ ─ virtualenv

