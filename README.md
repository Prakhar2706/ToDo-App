# ToDo App

Welcome to the ToDo App! This Django project allows users to manage their tasks efficiently with a variety of features. Whether you need to create tasks, set priorities, or manage your user profile, this app has you covered.

![image](https://github.com/user-attachments/assets/844aa9b4-a1ac-479d-a9b8-cef1880d843a)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Prakhar2706/ToDo-App.git
   cd ToDo-App
2. Create a virtual environment (optional but recommended):
    
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:

   ```bash
   pip install Django==5.0.7 django-crispy-forms==1.9.2 django-widget-tweaks==1.4.8 Pillow==10.1.0
   
4. Create migrations for your models:

   ```bash
   python manage.py makemigrations

5. Apply migrations:

   ```bash
   python manage.py migrate

6. Create a superuser (optional, for admin access):

   ```bash
   python manage.py createsuperuser

7. Run the development server:

   ```bash
   python manage.py runserver

8. Open your web browser and go to http://127.0.0.1:8000/ to access the ToDo App.

## Look

![image](https://github.com/user-attachments/assets/64ea1d41-539c-4be8-915b-75a610c77f94)
![image](https://github.com/user-attachments/assets/fdb71749-16d2-4ebc-b6b1-ccd25d6a8b44)
![image](https://github.com/user-attachments/assets/68a594fe-2e30-4a2a-9222-3b1a015fecf2)
![image](https://github.com/user-attachments/assets/844aa9b4-a1ac-479d-a9b8-cef1880d843a)
![image](https://github.com/user-attachments/assets/a473de07-de70-4109-b897-6eab3a01665a)
![image](https://github.com/user-attachments/assets/60fc697f-eee8-4315-a750-743a9662395e)

## Features

- User creation
- Task management (create, edit, delete, complete tasks)
- Schedule priority tasks
- User authentication
- Edit user profile
- Filter tasks
- Search bar for quick task lookup
- Attach files to specific tasks
- Schedule tasks according to date and time
- Sort tasks based on priority and due date

## Requirements

To run this project, you need to have the following packages installed:

- Django==5.0.7
- django-crispy-forms==1.9.2
- django-widget-tweaks==1.4.8
- Pillow==10.1.0

## Usage

* Register a new user or log in with an existing account.
* Create new tasks and set their priority.
* Edit or delete tasks as needed.
* Use the search bar to quickly find tasks.
* Attach files to tasks if necessary.
* Schedule tasks by date and time, and sort them accordingly.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.
