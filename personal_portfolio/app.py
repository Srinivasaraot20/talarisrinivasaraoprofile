import os
import logging
from flask import Flask, render_template, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_mail import Mail
from personal_portfolio.config import DevelopmentConfig
from personal_portfolio.forms import ContactForm
import personal_portfolio.data as data

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create SQLAlchemy base class
class Base(DeclarativeBase):
    pass

# Create Flask app
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

# Initialize database
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Initialize mail
mail = Mail(app)

# Import models after db initialization to avoid circular imports
from personal_portfolio.models import Project, Achievement, Certification

@app.context_processor
def inject_globals():
    """Inject global variables to all templates"""
    return {
        'name': 'Srinivasa Rao Talari',
        'email': 'srininvast20@gmail.com',
        'phone': '+91-8341492762',
        'github': 'https://github.com/Srinivasaraot20',
        'linkedin': 'https://www.linkedin.com/in/srinivasa-rao-talari-a87723289/'
    }

@app.route('/')
def index():
    """Home page route"""
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    """About page route"""
    education = data.get_education()
    skills = data.get_skills()
    tools = data.get_tools()
    internships = data.get_internships()
    return render_template('about.html', title='About Me', 
                          education=education, skills=skills, 
                          tools=tools, internships=internships)

@app.route('/projects')
def projects():
    """Projects page route"""
    # Get projects from database or initialize with data if empty
    projects_data = Project.query.all()
    if not projects_data:
        for project in data.get_projects():
            new_project = Project(
                title=project['title'],
                description=project['description'],
                details=project['details'],
                tech_stack=project['tech_stack'],
                image_url=project['image_url'],
                github_url=project.get('github_url', ''),
                demo_url=project.get('demo_url', ''),
                date=project['date']
            )
            db.session.add(new_project)
        db.session.commit()
        projects_data = Project.query.all()
        
    return render_template('projects.html', title='Projects', projects=projects_data)

@app.route('/achievements')
def achievements():
    """Achievements page route"""
    # Get achievements from database or initialize with data if empty
    achievements_data = Achievement.query.all()
    if not achievements_data:
        for achievement in data.get_achievements():
            new_achievement = Achievement(
                title=achievement['title'],
                description=achievement['description'],
                organization=achievement['organization'],
                date=achievement['date'],
                image_url=achievement['image_url']
            )
            db.session.add(new_achievement)
        db.session.commit()
        achievements_data = Achievement.query.all()
        
    return render_template('achievements.html', title='Achievements', achievements=achievements_data)

@app.route('/certifications')
def certifications():
    """Certifications page route"""
    # Get certifications from database or initialize with data if empty
    certifications_data = Certification.query.all()
    if not certifications_data:
        for certification in data.get_certifications():
            new_certification = Certification(
                title=certification['title'],
                issuer=certification['issuer'],
                date=certification['date'],
                image_url=certification['image_url'],
                credential_url=certification.get('credential_url', '')
            )
            db.session.add(new_certification)
        db.session.commit()
        certifications_data = Certification.query.all()
        
    return render_template('certifications.html', title='Certifications', certifications=certifications_data)

@app.route('/resume')
def resume():
    """Resume page route"""
    return render_template('resume.html', title='Resume')

@app.route('/gallery')
def gallery():
    """Gallery page route"""
    gallery_images = data.get_gallery_images()
    return render_template('gallery.html', title='Gallery', images=gallery_images)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page route with form handling"""
    form = ContactForm()
    
    if form.validate_on_submit():
        try:
            from flask_mail import Message
            msg = Message(
                subject=f"Portfolio Contact: {form.subject.data}",
                sender=app.config['MAIL_DEFAULT_SENDER'],
                recipients=[app.config['MAIL_DEFAULT_RECIPIENT']],
                body=f"""
                From: {form.name.data} <{form.email.data}>
                
                Message:
                {form.message.data}
                """
            )
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('contact'))
        except Exception as e:
            app.logger.error(f"Error sending email: {str(e)}")
            flash('An error occurred while sending your message. Please try again later.', 'danger')
    
    return render_template('contact.html', title='Contact Me', form=form)

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('404.html', title='Page Not Found'), 404

# Create tables
with app.app_context():
    db.create_all()
