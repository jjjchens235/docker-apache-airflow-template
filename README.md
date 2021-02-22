## Purpose
The minimum code necessary to set-up Apache/Airflow Docker image. User can clone repo and then spin up apache/airflow Docker container quickly.

The puckel Docker image is great, but unfortunately it's no longer maintained, so I think it's better to switch over to the apache/airflow image.

This repo's code is based on this Medium [article](https://towardsdatascience.com/apache-airflow-and-postgresql-with-docker-and-docker-compose-5651766dfa96). Overall it was a very useful article, but the author left out a few lines of code that are necessary for the image to function.

It took me a while to figure out how to fill in the gaps, so I'm hoping this can help someone out :)


### Instructions
1. Install [Docker](https://docs.docker.com/get-docker/)
2. Install [docker-compose](https://docs.docker.com/compose/install/)
3. On the command line run `docker pull apache/airflow` to build the image
4. Clone this repo
5. Create an `.env` file in the root directory. Here is my .env file, customize it to your own needs:
	- Of note is the Fernet Key, if you don't have one already, this [link](https://airflow.apache.org/docs/apache-airflow/stable/security/secrets/fernet.html) explains how to create one.
``` sh
AIRFLOW__CORE__EXECUTOR=LocalExecutor
AIRFLOW__WEBSERVER__RBAC=False
AIRFLOW__SCHEDULER__SCHEDULER_HEARTBEAT_SEC=10
AIRFLOW__SCHEDULER__MIN_FILE_PROCESS_INTERVAL=60 # Prevent airflow from reloading the dags all the time and set. This is the main setting that reduces CPU load in the scheduler
AIRFLOW__SCHEDULER__SCHEDULER_MAX_THREADS=2 # This should be set to (CPU Cores - 1)
AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres:5432/airflow
AIRFLOW__CORE__FERNET_KEY=${FERNET_KEY}
```
5. To spin up the server, run `docker-compose up -d`
6. Go to http://localhost:8080/
7. Login using these credentials
	- UN: admin 
	- PW: password
8. To spin down, run `docker-compose down`
