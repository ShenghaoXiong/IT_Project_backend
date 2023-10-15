# Flask Application README

## Description

This is a Flask application that serves as a backend for a farmbot web application. The application is configured to connect to a MySQL database and is CORS enabled. It is designed to be deployed on Google Cloud with specific runtime and scaling configurations.

## Installation

1. Clone the repository
   ```sh
   git clone https://github.com/ShenghaoXiong/IT_Project_backend.git
   cd https://github.com/ShenghaoXiong/IT_Project_backend.git
   ```

2. Install dependencies
   The `supports.txt` file lists all the required packages for this project. Install them using pip:
   ```sh
   pip install -r supports.txt
   ```

## Environment Variables

The application requires the following environment variables (as seen in `app.yaml`):

- `HOSTNAME`: The hostname of the MySQL database.
- `PORT`: The port number for the MySQL database.
- `USERNAME`: The username for the MySQL database.
- `PASSWORD`: The password for the MySQL database.
- `DATABASE`: The name of the MySQL database.
- `SECRET_KEY`: The secret key for the Flask application.

## Running the Application

### Locally

You can run the application locally using the following command:

```sh
flask run
```

### On Google Cloud

The `app.yaml` file contains the configuration for deploying the application to Google Cloud. Follow the [official documentation](https://cloud.google.com/appengine/docs/standard) for deploying Python applications on App Engine Standard Environment.

## Dependencies

- Flask: The Python micro framework for building web applications.
- Flask-SQLAlchemy: An extension for Flask that adds support for SQLAlchemy to the application.
- Flask-Marshmallow: An object serialization/deserialization library for Flask.
- Flask-CORS: A Flask extension for handling Cross-Origin Resource Sharing (CORS).
- SQLAlchemy: The Python SQL toolkit and Object-Relational Mapping (ORM) system.
- Marshmallow: An object serialization/deserialization library for Python.
- PyMySQL: A library to connect to MySQL databases from Python applications.
- Werkzeug: A comprehensive WSGI web application library.
