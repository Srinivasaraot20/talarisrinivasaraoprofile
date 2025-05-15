from datetime import datetime
from personal_portfolio.app import db

class Project(db.Model):
    """Project model for storing portfolio projects"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    details = db.Column(db.Text, nullable=False)
    tech_stack = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    github_url = db.Column(db.String(200))
    demo_url = db.Column(db.String(200))
    date = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Project {self.title}>'

class Achievement(db.Model):
    """Achievement model for storing awards and recognitions"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    organization = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Achievement {self.title}>'

class Certification(db.Model):
    """Certification model for storing professional certifications"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    issuer = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    credential_url = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Certification {self.title}>'
