#!/bin/bash

nginx_config="/etc/nginx/sites-enabled/default"
redirect_block="location /redirect_me {
    return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
}"

# Check if the Nginx configuration file exists
if [ ! -e "$nginx_config" ]; then
    echo "Error: Nginx configuration file not found at $nginx_config."
    exit 1
fi

# Check if the redirection block already exists
if grep -q "location /redirect_me" "$nginx_config"; then
    echo "Redirection block already exists in the Nginx configuration. Exiting."
    exit 0
fi

# Add the redirection block to the Nginx configuration
echo "$redirect_block" | sudo tee -a "$nginx_config" > /dev/null

# Test the Nginx configuration
sudo nginx -t

# Restart Nginx if the configuration test is successful
if [ $? -eq 0 ]; then
    sudo service nginx restart
    echo "Nginx restarted successfully."
else
    echo "Error: Nginx configuration test failed. Please check the configuration manually."
fi
