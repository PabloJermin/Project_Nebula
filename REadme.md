# Project Nebula

In this project seeks to design a dashboard for student. On the dashboard, the user has the ability to select a name from the list of students in the database with the corresponding cohort. When the selected details is correct, the cooresponding details of the student, i.e attendance and scores shall appear on the tiles of the frontend.

This project makes use of djnago restframework as an API in conjunction with html/css or react as a frontend to accept data from a user and save into the AWS Postgres database. The original intention for this project was to utilize the AWS Dynamo DB with the djnago backend, however, due to the short period given for the execution of the project, much time wasn't avalable to explore ways to integrate the django with dynamo db. Also, Django's limitaion on using only relational databases made it easier for me to resort to using the Postgres.

## Instalation Process

To install the django system, navigate to your Project directory. `cd project-name` or create the directory using `mkdir project-name`in your favorite code editor or command prompt.

* In the project directory, create your environment using this command:
    ```
    python virtualenv venv
    ```
    this creates a virtual envrinment in your directory called `venv`.
* Activate your virtual environment using this command:
    
    For windows
    ```
    venv\Scripts\activate
    ```

    For Mac
    ```
    source venv/bin/activate
    ```

* Clone the project from this repository into your directory using this command:
    ```
    git clone https://github.com/PabloJermin/Project_Nebula.git 
    ```
* Now, install the dependencies and django application from the requirements.txt file like this:
    ```
    pip install -r requirements.txt
    ```
    all the required dependencies shall be installed in your virtual environment.
* Create your environment variable at the root of the folder with your database credentials using the format as `.env`
    ```
    DB_HOST='your_host_name'
    DB_PASSWORD='your_pasword'
    DB_USER='your_username'
    DB_NAME='your_name'
    DB_ENGINE='django.db.backends.postgresql'
    DB_PORT=5432
    ```

* Finally, run the backend server
    ```
    python manage.py runserver
    ```
    this runs the server on your `localhost:8000`. However, ensure your database application is already running before starting the backend application to avoid errors.

**Now your backend is running...**

## How To Use The Application

Before running the application, ensure that the database has been properly setup and running on the AWS platform. 

To setup the django backend to interacts with your personal database,

* navigate to the **Nebula** folder and open the **Settings.py** file. 
* Scroll to the **DATABASE** section and replace the variables with your credentials and save the file with `ctrl + s`.
* Run 
    ```
     python manage.py makemigrations
    ``` 
    to effect your changes and make django intigrate with your databse.
* Finally, run 
    ```
    python manage.py migrate
    ```
    to effect all your data into your database.

**Now the application is running on your personal database..**

Interact with the application on the localhost of your browser by copying this link into your favorite browser `localhost:8000`.

In your browser, select a student whose data already exist in your database. The information of the selected student should populate in all the tiles or fields designed on your screen.


## Credits

A sincere gratitude is extended to my team members who have masively contributed to the success of this project. And to @ErnAzubi for his contribution to the frontend version of the project.
