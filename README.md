# Gymnasium-Management-System

This is a Django-based web application to manage the day-to-day attendance of gym members, track payments,  and allocate trainers. The application is currently used by a local gymnasium as an ERP system.


## How to implement this web app
- Download the zip
- Extract the contents
- Install all dependencies by executing the following command:

    ```
    $pip install -r requirements.txt
    ```

- For running the application simply execute the following commands:

    ```
    $python3 manage.py migrate
    $python3 manage.py runserver
    ```

- For creating a user execute:

    ```
    $python3 manage.py createsuperuser
    # Follow the instructions
    ```

- You can now login to the system!
