"""
Data module for storing static content
Used to initialize the database or provide fallback data
"""

def get_education():
    """Return education information"""
    return [
        {
            'degree': 'Bachelor of Technology',
            'field': 'Artificial Intelligence and Data Science',
            'institution': 'Velagapudi Ramakrishna Siddhartha Engineering College, Vijayawada',
            'period': '2023 - Present',
            'gpa': '8.93'
        },
        {
            'degree': 'Diploma',
            'field': 'Computer Engineering',
            'institution': 'Adsumlu Aswardha Narayana Muurthi & Valluripalli Venkata Rama Seshadri Rao College',
            'period': '2020 - 2023',
            'gpa': '89.17%'
        },
        {
            'degree': 'Secondary School Certificate (SSC)',
            'field': '',
            'institution': 'Padmavathi EM High School, Vidyanagar, Krosuru',
            'period': '2019 - 2020',
            'gpa': '9.2'
        }
    ]

def get_skills():
    """Return skills information"""
    return [
        {'category': 'Programming Languages', 'items': ['Java', 'Python', 'C', 'JavaScript', 'R']},
        {'category': 'Web Development', 'items': ['HTML', 'CSS', 'JavaScript', 'React.js']},
        {'category': 'Data Science', 'items': ['Machine Learning', 'Data Analysis', 'Data Visualization', 'Deep Learning', 'AI']},
        {'category': 'Backend', 'items': ['SQL', 'MongoDB', 'Django', 'Flask']},
        {'category': 'Other', 'items': ['Photography', 'Sports', 'Computer Programming', 'Software Development']}
    ]

def get_tools():
    """Return tools information"""
    return ['GitHub', 'Jupyter', 'Colab', 'Visual Studio Code', 'Windows OS']

def get_projects():
    """Return projects information"""
    return [
        {
            'title': 'Health Insurance Fraud Detection Using Machine Learning',
            'description': 'AI-powered fraud detection for health insurance claims',
            'details': 'Developed a machine learning model using XGBoost and SVM for fraud detection. Implemented data preprocessing, anomaly detection, and feature engineering, integrating it into a web dashboard for real-time analysis, which reduced financial losses.',
            'tech_stack': 'Python, Machine Learning, XGBoost, SVM, Web Dashboard',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/2329/2329087.png',
            'github_url': '#',
            'date': 'Present'
        },
        {
            'title': 'Smart Helmet for Coal Mine Workers',
            'description': 'IoT-based safety solution for coal mine workers',
            'details': 'I developed a smart helmet that incorporates Arduino, gas sensors, GPS, and an SMS alert system to detect methane (CH4) and carbon monoxide (CO) in coal mines. The helmet features LoRa/GSM communication, allowing for real-time, long-range alerts to both workers and control rooms, thereby enhancing workplace safety.',
            'tech_stack': 'Arduino, IoT, LoRa, Gas Sensors, GPS, SMS Alert System',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/2421/2421988.png',
            'github_url': '#',
            'date': '2023'
        },
        {
            'title': 'Resume Building Tool',
            'description': 'AI-powered resume-building platform',
            'details': 'Created a web-based platform featuring templates, real-time suggestions, and AI-driven feedback for professionally optimized resumes.',
            'tech_stack': 'Web Development, AI, Template Engine',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/3135/3135731.png',
            'github_url': '#',
            'date': '2022'
        },
        {
            'title': 'E-commerce Product Recommendation System',
            'description': 'ML-based recommendation system for e-commerce platforms',
            'details': 'Built a collaborative filtering recommendation system for e-commerce platforms using machine learning algorithms to suggest products based on user behavior, browsing history, and purchase patterns. Implemented content-based filtering to enhance recommendation accuracy.',
            'tech_stack': 'Python, Scikit-learn, Collaborative Filtering, Content-based Filtering',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/2830/2830284.png',
            'github_url': '#',
            'date': '2022'
        }
    ]

def get_achievements():
    """Return achievements information"""
    return [
        {
            'title': 'First Place - Innovation Day Celebration',
            'description': 'Won 1st place for the "Smart Helmet for Coal Mine Workers," an AIoT safety solution for detecting harmful gases in coal mines.',
            'organization': 'Velagapudi Ramakrishna Siddhartha Engineering College',
            'date': '2023',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/2583/2583344.png'
        },
        {
            'title': 'Top 8 Startup and Innovation Ideas',
            'description': 'Recognized for my startup idea, "Robotics for Bomb Detection and Disposal." I presented this concept at an MSME-sponsored innovation event, where it received industry acclaim for its focus on AI-driven optimization in logistics. I received the award for best startup idea.',
            'organization': 'AIC ALEAP WE Hub & MSME Minister, Andhra Pradesh',
            'date': '2022',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/1642/1642322.png'
        },
        {
            'title': '₹3 Lakh Funding',
            'description': '₹3 lakhs in funding for the development of an AIoT-based smart helmet to monitor harmful gases in real-time. The project aims to enhance coal mine workers\' safety through early detection of hazardous gases and real-time alerts. The funding will support research, hardware integration, and system deployment.',
            'organization': 'RVR & JC Engineering College',
            'date': '2024',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/3176/3176293.png'
        }
    ]

def get_certifications():
    """Return certifications information"""
    return [
        {
            'title': 'Java Programming Fundamentals',
            'issuer': 'GalileoX (Universidad Galileo)',
            'date': '2023',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/226/226777.png',
            'credential_url': '#'
        },
        {
            'title': 'Foundation of R Software',
            'issuer': 'IIT Madras (NPTEL)',
            'date': '2022',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/2103/2103665.png',
            'credential_url': '#'
        },
        {
            'title': 'Artificial Intelligence with Python - Heuristic Search',
            'issuer': 'Infysos',
            'date': '2022',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/1693/1693746.png',
            'credential_url': '#'
        },
        {
            'title': 'Hardware and Operating Systems',
            'issuer': 'IBM',
            'date': '2021',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/5453/5453855.png',
            'credential_url': '#'
        },
        {
            'title': 'Introduction to Data Science with Python',
            'issuer': 'HarvardX (Harvard University)',
            'date': '2023',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/2721/2721287.png',
            'credential_url': '#'
        },
        {
            'title': 'Ethical Hacking',
            'issuer': 'IIT Kharagpur (NPTEL)',
            'date': '2022',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/2450/2450879.png',
            'credential_url': '#'
        },
        
        {
            'title': 'Introduction to Deep Learning',
            'issuer': 'Infysos',
            'date': '2023',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/8637/8637922.png',
            'credential_url': '#'
        },
        {
            'title': 'Introduction to MongoDB for Students',
            'issuer': 'MongoDB',
            'date': '2022',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/8297/8297437.png',
            'credential_url': '#'
        },
        {
            'title': 'Production Machine Learning Systems',
            'issuer': 'Google Cloud (Coursera)',
            'date': '2023',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/2875/2875383.png',
            'credential_url': '#'
        },
        {
            'title': 'Introduction to Networks',
            'issuer': 'Cisco Networking Academy',
            'date': '2021',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/2885/2885417.png',
            'credential_url': '#'
        }
    ]

def get_internships():
    """Return internship information"""
    return [
     
        {
            'position': 'AI-ML Virtual Internship',
            'company': 'Eduskills',
            'period': '2023',
            'description': 'Gained hands-on experience with machine learning algorithms, data preprocessing, and model evaluation using Python and libraries like TensorFlow.',
            'type': 'Virtual'
        },
        {
            'position': 'SQL Internship',
            'company': 'DevSkillHub Training & Consultancy',
            'period': '2022',
            'description': 'Worked on database management, SQL query writing, and optimizing relational databases for efficient data retrieval.',
            'type': 'In-person'
        },
        {
            'position': 'Full Stack Development Training & Internship (Python, Django)',
            'company': 'Lineysha and Thevan Software Technologies',
            'period': '2023',
            'description': 'Developed full-stack web applications using Python, Django, and REST APIs for both front-end and back-end tasks.',
            'type': 'Hybrid'
        },
        {
            'position': 'Cloud Virtual Internship',
            'company': 'Eduskills',
            'period': '2022',
            'description': 'Gained experience in cloud infrastructure, AWS and Azure services, and cloud-based development tools for app deployment.',
            'type': 'Virtual'
        },
        {
            'position': 'Web Development Internship',
            'company': 'Coding Raja Technologies',
            'period': '2023',
            'description': 'Contributed to web projects using HTML, CSS, JavaScript, and backend integration to build dynamic websites.',
            'type': 'Remote'
        }
    ]

def get_gallery_images():
    """Return gallery images information"""
    return [

        {
            'title': 'Innovation Day - First Place Award',
            'category': 'Award Ceremonies',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/3557/3557232.png',
            'description': 'Receiving the first place award at Innovation Day for the Smart Helmet project'
        },
        {
            'title': 'Smart Helmet Project Demo',
            'category': 'Project Demos',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/2059/2059464.png',
            'description': 'Demonstrating the Smart Helmet for Coal Mine Workers project'
        },
        {
            'title': 'MSME Startup Pitch',
            'category': 'Presentations',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/1205/1205526.png',
            'description': 'Pitching the Robotics for Bomb Detection concept at MSME event'
        },
        {
            'title': 'Team Hackathon - 2023',
            'category': 'Hackathons',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/7641/7641727.png',
            'description': 'Working with the team during a 24-hour hackathon event'
        },
        {
            'title': 'VIT-AP Award Ceremony',
            'category': 'Award Ceremonies',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/3176/3176283.png',
            'description': 'Receiving the Appreciation Award at Innovation Acquisition Summit'
        },
        {
            'title': 'Project Exhibition',
            'category': 'Project Demos',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/4252/4252296.png',
            'description': 'Displaying projects at the college technical exhibition'
        },
        {
            'title': 'NSS Volunteer Work',
            'category': 'Team Events',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/3588/3588652.png',
            'description': 'Participating in the NSS blood donation camp'
        },
        {
            'title': 'Web Development Workshop',
            'category': 'Team Events',
            'image_url': 'https://cdn-icons-png.flaticon.com/512/3049/3049387.png',
            'description': 'Leading a workshop on modern web development techniques'
        },
        {
            'title': '"₹3 Lakh Funding Award"',
            'category': 'Achievements',
            'src': '/static/images/smart_helmet_award.jpg',
            'description': 'Secured ₹3 lakhs in funding from RVR & JC Engineering College for developing an AIoT-based smart helmet to monitor harmful gases in real-time and enhance coal mine workers'
        }
        

    ]
