# Django Blog Application

This is a simple blog application built using Django. It allows users to create, read, update, and delete blog posts.

## Features

- User authentication: Users can sign up, log in, and log out.
- CRUD operations: Users can create, read, update, and delete their blog posts.
- Admin panel: Administrators can manage users, blog posts, and other site content through the Django admin interface.

## Installation

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/Saudmukhair/django-blog.git
    ```

2. Navigate to the project directory:

    ```
    cd django-blog
    ```

3. Create a virtual environment:

    ```
    python -m venv env
    ```

4. Activate the virtual environment:

    - On Windows:

        ```
        .\env\Scripts\activate
        ```

    - On macOS and Linux:

        ```
        source env/bin/activate
        ```

5. Install the dependencies:

    ```
    pip install -r requirements.txt
    ```

6. Apply migrations:

    ```
    python manage.py migrate
    ```

7. Create a superuser (admin):

    ```
    python manage.py createsuperuser
    ```

8. Run the development server:

    ```
    python manage.py runserver
    ```

9. Open your web browser and navigate to `http://127.0.0.1:8000` to access the blog application.

## Usage

- To create a new blog post, log in and navigate to the "Create Post" page.
- To edit or delete an existing blog post, navigate to the post detail page and click on the corresponding options (available to the post owner and administrators).
- Administrators can access the admin panel at `http://127.0.0.1:8000/admin` to manage users, blog posts, and other site content.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature_branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push your changes to your forked repository (`git push origin feature_branch`).
5. Create a new pull request.


