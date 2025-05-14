# Update Linux command
sudo apt update
sudo apt upgrade


# Install Project
export project_path=[to my path]
cd $project_path
git clone https://github.com/santapong/Organize # Clone Git

# Move nginx config to nginx path
sudo mv $project_path/scripts/nginx/nginx.conf /etc/nginx/conf.d/nginx.conf

# Install Nginx
sudo apt install nginx
sudo systemctl enable nginx
sudo systemctl start nginx

# Start Backend
Some code

[Healt Check]

# Start Frontend
Some code

[Healt Check]