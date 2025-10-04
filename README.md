Setup:

# Navigate to project
cd /home/ubuntu/portfolio-website/flask-website

# Pull latest changes
git pull origin main

# Restart the service
sudo systemctl restart portfolio

# If nginx config changed, restart that too
sudo systemctl restart nginx
