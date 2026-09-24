🍽️ Saffron & Sage Bistro
A full-stack restaurant website built with Django — featuring a homepage, an interactive menu ordering system, and a table reservation form. Built as a portfolio project to demonstrate full-stack development skills.

🔗 GitHub: https://github.com/Keerthi-3009/restaurant-project
🌐 Live Demo: _add your live link here once deployed_

Features

* Homepage with hero banner, tagline, and quick-access buttons (View Menu, Book Table)
* Browse restaurant menu items by category (e.g. Tandoor Specials, Paneer Specials)
* Select item quantities and see them added to the order in real time
* Running order total and selected-items summary
* Place Order button to submit the order
* Book a Table reservation form (name, email, phone, date, time)
* Django admin dashboard for managing menu items

Tech Stack

* Backend: Python, Django
* Database: SQLite
* Frontend: HTML, CSS, Bootstrap
* Tools: VS Code, Git/GitHub

Screenshots
Homepage
![Homepage](screenshots/homepage.png)

Menu Order Page
![Menu Order](screenshots/menu-order.png)

Book a Table
![Book a Table](screenshots/book-a-table.png)

Setup Instructions

1. Clone the repository

​```
git clone https://github.com/Keerthi-3009/restaurant-project.git
cd restaurant-project
​```

2. Create and activate a virtual environment

​```
python -m venv venv
venv\Scripts\activate
​```

3. Install dependencies

​```
pip install django
​```

4. Run migrations

​```
python manage.py makemigrations
python manage.py migrate
​```

5. Create a superuser (optional, for admin access)

​```
python manage.py createsuperuser
​```

6. Run the server

​```
python manage.py runserver
​```

Visit `http://127.0.0.1:8000/` for the site, `http://127.0.0.1:8000/admin/` for the admin dashboard.

Future Improvements

* User authentication and order history
* Payment integration
* Live deployment

Author
Built by Keerthi as part of a full-stack development portfolio.