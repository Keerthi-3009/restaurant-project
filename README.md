# Real Estate Property Listing Portal

A web-based property listing platform built with Django, allowing users to browse property listings, search and filter by criteria, and contact agents directly — built as a portfolio project to demonstrate full-stack development skills.

## Features

- Browse property listings with details (price, location, type, etc.)
- Search and filter properties by criteria
- View individual property details
- Contact agent for a listed property

## Tech Stack

- **Backend:** Python, Django
- **Database:** MySQL (via MySQL Workbench)
- **Frontend:** HTML, CSS, Bootstrap
- **Tools:** VS Code, Git/GitHub

## Getting Started

### Prerequisites

- Python 3.x installed
- pip (Python package manager)
- MySQL Server and MySQL Workbench installed

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/Keerthi-3009/real-estate-portal.git
   cd real-estate-portal
   ```

2. Install dependencies
   ```bash
   pip install django mysqlclient
   ```

3. Set up your MySQL database and update the database credentials in `settings.py`

4. Run database migrations
   ```bash
   python manage.py migrate
   ```

5. Start the development server
   ```bash
   python manage.py runserver
   ```

6. Open your browser and go to
   ```
   http://127.0.0.1:8000/
   ```

## Project Structure

```
real_estate_project/
├── real_estate/          # Main app (models, views, templates)
├── real_estate_project/  # Project settings and configuration
├── manage.py
```

## Screenshots

_Add a screenshot of the property listing page here, e.g._
```
![Property Listings](screenshots/listings-page.png)
```

## Future Improvements

- User authentication for buyers and agents
- Favorites/saved listings
- Map-based property search
- Live deployment

## Author

Built by Keerthi as part of a full-stack development portfolio.