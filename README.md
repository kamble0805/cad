# Civilian CAD System – Under Development

This project is a submodule of a larger **Computer Aided Dispatch (CAD)** platform, focused on the **Civilian CAD System**. It facilitates the onboarding and profile management of civilians within the CAD infrastructure. The solution also includes an administrative interface for managing civilian records and access.

## Key Features

- 🔐 **Civilian Registration and Authentication**
- 📄 **User Profile Management**
- 🛠️ **Admin Panel for System Oversight**
- 📁 **Structured Django Back-End**
- 💻 **Ready for Future CSS and UI Enhancements**

---

## Technologies Used

- **Python 3.13.1**
- **Django 5.2**
- **SQLite3 (Development DB)**
- **HTML, CSS (Styling to be finalized)**
- **Gunicorn & Whitenoise** for production deployments

---

## Local Development Setup

### Prerequisites

- Python 3.10+
- Git
- Virtualenv (optional but recommended)

### Steps to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/kamble0805/cad.git
cd cad

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver
