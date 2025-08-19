# Woodstone Festival 2025 - Admin Portal

This repository contains the Flask admin portal for Woodstone Festival 2025, a sacred content management system with user authentication and document management capabilities.

## Quick Setup (Automated)

The easiest way to get started is using the automated setup script:

```bash
./setup_woodstone_admin.sh
```

This script will automatically:
1. Extract `woodstone_festival_2025_euystacio_warp_full_ready_admin.tar.gz`
2. Set up a Python virtual environment
3. Install all required dependencies (Flask, markdown, requests, werkzeug)
4. Start the Flask application

## Manual Setup

If you prefer to set up manually:

```bash
# 1. Extract the admin portal
tar -xzf woodstone_festival_2025_euystacio_warp_full_ready_admin.tar.gz

# 2. Change to the extracted directory
cd woodstone_festival_2025_euystacio_warp

# 3. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 4. Install dependencies
pip install flask markdown requests werkzeug

# 5. Start the application
cd app
python3 app.py
```

## Access Information

Once the server is running, you can access the admin portal at:

- **URL**: http://localhost:5000/connect
- **Username**: woodstone  
- **Password**: threefold-zes
- **Role**: admin

## Features

- User authentication and role-based access control
- Content management system with pulse submission
- Sacred document management (Golden Bible, Rütli Declaration, etc.)
- Markdown support for rich text content
- SQLite database backend
- Responsive web interface

## Requirements

- Python 3.6+
- Flask framework
- SQLite (included with Python)
- Modern web browser

## Directory Structure

```
woodstone_festival_2025_euystacio_warp/
├── app/
│   ├── app.py              # Main Flask application
│   ├── cms.py              # Content management system
│   ├── templates/          # HTML templates
│   └── static/             # CSS and static files
├── pages-clean/            # Sacred document markdown files
└── README.md               # Additional documentation
```

## Development Notes

The admin user is automatically created when the application starts for the first time with the credentials listed above. The application uses SQLite for data persistence and includes password hashing for security.

For production deployment, ensure to:
- Change the Flask secret key
- Use a production-grade web server (e.g., Gunicorn)
- Configure proper logging and monitoring
- Set up secure HTTPS connections