## SIMPLE CALCULATOR
The web application used for AWS EC2 Server for Django Implementation is "Simple Calculator"
 
### WORKING:
The users enter two numeric values. The calculator performs addition, subtraction, multiplication and division based on the button pressed in the calculator
 
#### EXAMPLE:
If users enter '10','5' and +, result is '15
 
#### TECHNOLOGIES USED:
HTML/Inline CSS are used for the front end and styling.
Validation is done using .js file.
Python is used for back end calculations.
 
### DETAILS:
Simple Calculator


1.	Setting up the project on Git-hub


2.	Git-clone the project in the server


3.	Follow below steps for installing python, Django framework, gunicorn and nginx
```
sudo apt-get install python


sudo apt-get install python-pip
sudo apt-get install Django==1.11.9

pip install gunicorn
sudo apt-get install nginx;
```
Add below nginx configuration at /etc/nginx/sites-enabled/nginx.conf;
```
server {

listen 80;

server_name ip.adress; # substitute by your FQDN and machine's IP address
charset utf-8;

client_max_body_size 75M; # adjust to taste


location /media {
alias /var/www/path/to/your/project/media; # your Django project's media
files
}
location /assets {
alias /var/www/path/to/your/project/static; # your Django project's
static files
}

location / {
proxy_pass http://127.0.0.1:8000;
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}
}
```
4.	Running gunicorn and nginx with wsgi and https
```
pip install gunicorn
gunicorn -bind 0.0.0.0:8000 mystic.wsgi <from main folder>

brew install nginx

sudo /etc/init.d/nginx reload;
sudo /etc/init.d/nginx restart;
```
 
### LINKS:
* Public App URL: https://18.217.251.194
* Code URL: https://github.uc.edu/bundeyyn/calculator
* Doc URL: https://github.uc.edu/bundeyyn/calculator/blob/master/README.md
