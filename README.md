# django-app-project

This is the first formal project after django practice

## Run Locally

**OS**: Ubuntu  
**Editor**: Visual Studio Code

Clone the project

```bash
git clone git@github.com:noumanrafi0/django-app-project.git
```

Go to the project directory

```bash
cd my-cd django-app-project/
code .
```

Install environment and activate

```bash
python3 -m venv env
source env/bin/activate
```

Install packages

```bash
pip install -r requirements.txt
```

Make log directory, make migrations, migrate and runserver

```bash
mkdir log
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```

### TASK_1

Django Application with Django Form, Authentication (Signup, Login, Logout, Edit Profile), Using Custom Django Templates (one base template and others inherit from it) and proper Exception Handlings

### TASK_2

Create a `Profile` model with 1-1 relation with `User` model and its edit view. In edit view(`Edit Profile API`), edit user profile information that can have phone number (validate number in backend), address (simple text field) and profile photo (image field, for now image can be saved in a media folder)
