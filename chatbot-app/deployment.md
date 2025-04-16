# Deployment Guide

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- A valid Gemini API key

## Setup Steps

1. **Clone the Repository**
```bash
git clone <repository-url>
cd chatbot-app
```

2. **Set Up Environment**
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

3. **Configure Environment Variables**
```bash
# Copy the example env file
cp .env.example .env

# Edit .env file with your actual values
# IMPORTANT: Set FLASK_ENV=production
```

4. **Database Setup**
The SQLite database will be automatically created when the application starts.

## Running in Production

1. **Using Gunicorn (Recommended for Production)**
```bash
gunicorn --bind 0.0.0.0:$PORT app:app --workers 4
```

2. **Using Flask Development Server (Not Recommended for Production)**
```bash
python app.py
```

## Monitoring

- Application logs are written to `app.log`
- Monitor the Gunicorn process using your system's process manager
- Consider setting up application monitoring using tools like New Relic or Datadog

## Security Considerations

1. **API Key Protection**
   - Never commit the `.env` file
   - Regularly rotate the Gemini API key
   - Use environment variables for sensitive data

2. **Database Security**
   - Ensure proper file permissions on the SQLite database
   - Regularly backup the database

3. **Network Security**
   - Configure proper firewall rules
   - Use HTTPS if exposed to the internet
   - Consider using a reverse proxy like Nginx

## Maintenance

1. **Regular Updates**
   - Keep dependencies updated using `pip-audit`
   - Monitor for security advisories
   - Regularly update the Python runtime

2. **Backup Strategy**
   - Implement regular backups of the SQLite database
   - Store backups in a secure location