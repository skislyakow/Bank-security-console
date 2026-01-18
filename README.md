# Bank security console

This is an internal repository for Siyanie Bank employees. If you've accessed this repository by accident, you won't be able to run it because you don't have access to the database. However, you can freely use the markup code or view how the database queries are implemented.

The Security Console is a website that can be connected to a remote database containing visits and access cards for our bank's employees.

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Configuration (Environment Variables)
The project uses environment variables to store sensitive information and database configurations.
Create a file named .env in the root directory of the project.
Copy the following variables into your .env file and set your own values:

```env
# Django Security
SECRET_KEY=your-secret-key-goes-here

# Database Settings
DB_ENGINE=django.db.backends.postgresql
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=127.0.0.1
DB_PORT=5432
```

Reference Table
```
Variable	Description										Example

SECRET_KEY	Django's secret key for cryptographic signing.	django-insecure-xxx...
DB_ENGINE	Database backend engine.						django.db.backends.postgresql
DB_NAME	    The name of your database.						my_db
DB_USER	    Database user login.							postgres
DB_PASSWORD	Password for the database user.					mypassword
DB_HOST	    Database server address.						localhost
DB_PORT	    Port number for the database.					5432
```






### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).