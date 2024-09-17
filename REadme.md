# Project Nebula

In this project seeks to design a dashboard for student. On the dashboard, the user has the ability to select a name from the list of students in the database with the corresponding cohort. When the selected details is correct, the cooresponding details of the student, i.e attendance and scores shall appear on the tiles of the frontend.

This project makes use of djnago's restframework as an API in conjunction with react as a frontend to accept data from a user and save into the AWS Postgres database. 

The application shall be hosted on AWS using the AWS Elastic Container Registry to host the images whiles utilizing the Elastic Container Services to run the application's images in AWS Fargate instances.


## Instalation Process

### Frontend Setup
The frontend of the apllication runs on react and nodejs. The responsive frontend was designed to receive dynamic information and display results to the dashboard of the user.
To run the frontend of the application, you can simply run the docker file into a docker image and run it on your local computer.

Clone the frontend files fron this repository using this command 
```
git clone https://github.com/PabloJermin/Project_Nebula_Frontend.git
```
Change directory into the cloned folder with this command 
```
cd Project_Nebula_Frontend
```

#### Running As An Image
* Use this code to run the docker file;
    ```
        docker build -t <name_of_image> .
    ```

* This builds an image from the docker file with the name provided above. 

    > **NOTE:**
    >  Use `docker images` to check all images avalable on you docker.

* Run the image into a container using the following codes 
    ```
    docker run <inamge_name> -d -p 3000:3000
    ```
Now your application will be available on localhost:3000.

#### Ruuning On A Developer Mode
* In your clone repository, install the `npm` manager using this command
    ```
    npm install
    ```

    > **Note:** 
    > Make sure Node.js is installed on your local computer.    Follow this [link](https://nodejs.org/en/download/package-manager) to install the Node.js application. 
* After installing the Node.js application and  the `npm` packages, run this command in your terminal to start the application.
    ```
    npm start
    ```

### Backend Setup
To install the django backend system, navigate to your Project directory. `cd project-name` or create the directory using `mkdir project-name`in your favorite code editor or command prompt.

#### Running In Developer Mode
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
    All the required dependencies shall be installed in your virtual environment.
* Create your environment variable file at the root of the folder with your database credentials using the format and save as `.env`
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

**_Now your backend is running..._**

#### Running As A Container

* Clone the project from this repository into your directory using this command:
    ```
    git clone https://github.com/PabloJermin/Project_Nebula.git 
    ```
* Change directory into the folder using `cd Project_Nebula`

    > ***NOTE:***
    > Ensure that the environment variable file `.env` has been created.
* Now create the image from the dockerfile using this command
    ```
    docker-compose up --build
    ```
**_Now your backend is running..._**

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

Interact with the application on the localhost of your browser by copying this link into your favorite browser `localhost:8000/api`.

In your browser, navigate to "/students" to display all students in the database. Your browser should look like this
![Screeonshot of a web broswer showing all students in a databse](<../../../Pictures/Screenshots/Screenshot (69).png>)


## Credits

A sincere gratitude is extended to my team members who have masively contributed to the success of this project. And to @ErnAzubi for his contribution to the frontend version of the project.
