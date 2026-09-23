# Horse Ranch Management Software

A web-based software to manage access and operations for a horse ranch.
The system provides different access levels for customers, staff, and managers/owners.

Built based on real-world operational needs drawn from hands-on ranch management experience.

---

## Tech Stack

This project is built with:

- **Backend:** Python & Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (development) / PostgreSQL (production-ready)
- **Optional:** Node.js for frontend build tools

---

## Features

- User authentication with different roles:
  - Customer
  - Staff
  - Admin/Manager
- Role-based access control (RBAC)
- Frontend interface for easy interaction
- Responsive design for desktop and mobile
- Secure handling of user data
- Horse and stall assignment tracking
- Scheduling for lessons, boarding, and vet visits
- Billing/invoicing for boarding customers
- Inventory tracking (feed, supplies)

##> Some features above are planned/in progress. See [Roadmap](#roadmap--future-improvements) for status.

---

## Getting Started

### Prerequisites

- Python 3.11+
- pip (Python package manager)
- Node.js & npm (optional, if using frontend build tools)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/horse-ranch-management.git
   cd horse-ranch-management
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin/manager account)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open the app**
   Visit `http://127.0.0.1:8000/` in your browser.

---

## Screenshots

> _Add screenshots or a short GIF here showing the login screen, dashboard, and key features once available._

---

## Project Structure

```
horse-ranch-management/
├── ranch_app/          # Core Django app (models, views, urls)
├── templates/           # HTML templates
├── static/               # CSS, JS, images
├── docs/                 # Project documentation (SRS, MVP scope, planning)
├── requirements.txt
├── manage.py
└── README.md
```

---

## Documentation

##Project planning and process documentation is available in the [`/docs`](./docs) folder, including:

- Software Requirements Specification (SRS)
- MVP scope and feature prioritization
- Development workflow (Scrum/Kanban board overview)

---

## Roadmap / Future Improvements

- [ ] Vet visit and health record tracking
- [ ] Automated billing reminders
- [ ] Customer-facing booking calendar
- [ ] Staff scheduling module
- [ ] Reporting dashboard for owners/managers
- [ ] API endpoints for mobile app integration

---

## License

##This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.

---

## Contact

Built by David — [GitHub Profile](https://github.com/david7zr) | [LinkedIn](https://www.linkedin.com/in/david-estrada-b06373316/)
