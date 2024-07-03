# Dev Ops Test APP - ADBL

This is a Django-based web application for displaying a list of employees with their respective codes, names, and images.

## Requirements

- Python 3.11
- Django 5.0.6
- Mysql 8.0.26

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/ab817/devopstest.git
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Apply database migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to create a superuser account.

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

8. **Access the admin interface:**

    Open your web browser and go to `http://127.0.0.1:8000/admin` to log in with the superuser account you created. Use the admin interface to add employee data, including images.

9. **View the employee list:**

    Open your web browser and go to `http://127.0.0.1:8000/employees/` to see the list of employees.

## Project Structure

- `myapp/`: Contains the main application code.
  - `models.py`: Defines the `Employee` model.
  - `views.py`: Contains the view to display the list of employees.
  - `urls.py`: Defines the URL patterns for the application.
  - `templates/`: Contains the HTML templates.
    - `base.html`: The base template that displays the employee list.
- `media/`: The directory where uploaded images are stored.
- `static/`: Contains static files like CSS.
- `requirements.txt`: Lists the required Python packages.
- `manage.py`: The command-line utility for administrative tasks.

## Adding Employee Data

1. **Log in to the admin interface:** Go to `http://127.0.0.1:8000/admin`.
2. **Add employees:** Use the "Employees" section to add new employees, including their code, name, and image.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
