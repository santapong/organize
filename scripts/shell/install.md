# Update Linux command
sudo apt update
sudo apt upgrade

# Install Project
export project_path=[to my path]
cd $project_path
git clone https://github.com/santapong/Organize # Clone Git

# Move config to nginx path
sudo chown 755 $project_path/scripts/nginx/nginx.conf 
sudo mv $project_path/scripts/nginx/nginx.conf /etc/nginx/conf.d/nginx.conf

# Move .service to systemd
sudo chown 755 $project_path/scripts/systemd/organize.service
sudo mv $project_path/scripts/systemd/organize.service /etc/systemd/organize.service

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