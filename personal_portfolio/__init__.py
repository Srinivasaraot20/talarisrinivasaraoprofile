import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_mail import Mail

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create SQLAlchemy base class
class Base(DeclarativeBase):
    pass

# Create db instance
db = SQLAlchemy(model_class=Base)
mail = Mail()

def create_app():
    # Create Flask app
    app = Flask(__name__)
    
    # Load configuration
    from personal_portfolio.config import DevelopmentConfig
    app.config.from_object(DevelopmentConfig)
    app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")
    
    # Initialize extensions
    db.init_app(app)
    mail.init_app(app)
    
    # Import and register blueprints/routes
    from personal_portfolio.routes import init_routes
    init_routes(app)
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app