from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '1t547321ipol'

db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    technologies = db.Column(db.String(200))
    github_url = db.Column(db.String(200))
    live_url = db.Column(db.String(200))
    image_url = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Project {self.title}>'

@app.route("/")
def home():
    projects = Project.query.order_by(Project.created_at.desc()).limit(3).all()
    return render_template('index.html', projects=projects)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/projects")
def projects():
    all_projects = Project.query.order_by(Project.created_at.desc()).all()
    return render_template('projects.html', projects=all_projects)

@app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)