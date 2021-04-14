#!/usr/bin/env bash
# Task 0

sudo apt update
sudo apt -y install nginx

sudo mkdir -p /data
sudo mkdir -p /data/web_static
sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test

test="<html>
  <head>
  </head>
  <body>
    Holberton School Test HTML
  </body>
</html>"

sudo touch /data/web_static/releases/test/index.html
sudo echo "$test" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data

sudo sed -i '/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default

sudo service nginx restart
