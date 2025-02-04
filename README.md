Install Required Libraries

pip install django mysqlclient

If you are using pipenv or virtualenv, activate it first before running the above command.

2. Clone or Download the Project
If you have the project stored in a repository, clone it using:
git clone <repository_url>
cd DjangoCRUD

3. Configure Database (MySQL)
Make sure MySQL is installed and running on your system.


4. Apply Migrations
Run the following commands to create necessary database tables:

python manage.py makemigrations
python manage.py migrate

5. Create a Superuser (Optional for Admin Panel)
If your project has a Django admin panel, create a superuser:

python manage.py createsuperuser
Follow the prompts to set up a username, email, and password.

6. Run the Development Server
Start the Django development server with:
python manage.py runserver

7. Access the Application
