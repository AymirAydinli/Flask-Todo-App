# Flask-Todo-App
 This Flask application is a modular web application demonstrating the use of Flask in creating robust web services. It is structured into various components for configuration, form handling, database models, and routing.

 # Flask Application

This Flask application is a modular web application demonstrating the use of Flask in creating robust web services. It is structured into various components for configuration, form handling, database models, and routing.

## Components

### `config.py`

- **Purpose**: Contains configuration settings for the Flask application. It includes parameters such as database URI, secret keys, and other environment-specific settings.

### `forms.py`

- **Purpose**: Defines the form classes using Flask-WTF. It is used for creating and validating user input forms in the application.

### `models.py`

- **Purpose**: Contains the SQLAlchemy model definitions. This file defines the structure of the database tables and their relationships.

### `routes.py`

- **Purpose**: Manages the URL routes and view functions. This file contains the logic that responds to requests on different endpoints.

## Setup and Running the Application

1. **Environment Setup**:
   - Ensure Python is installed on your system.
   - It's recommended to use a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```

2. **Install Dependencies**:
   - Install required packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Configuration**:
   - Set up the necessary configuration in `config.py`.
   - Ensure the database URI and other environment variables are correctly set.

4. **Initialize Database** (if applicable):
   - Run database migrations or setup scripts as required.

5. **Running the Application**:
   - Start the server:
     ```bash
     flask run
     ```

6. **Accessing the Application**:
   - The application will be accessible at `http://127.0.0.1:5000/` or the configured port.





 
[screen-capture (7).webm](https://github.com/AymirAydinli/Flask-Todo-App/assets/22778361/3110f15d-a787-4796-9378-3809ab871e8d)
