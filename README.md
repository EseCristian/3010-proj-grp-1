# 3010-proj-grp-1

## Overview
- This project aims to create an ECU CS Dashboard utilizing PostgreSQL and Apache. The dashboard will provide a comprehensive and interactive view of various data related to the ECU Computer Science department. The backend of the application will be powered by PostgreSQL, ensuring robust and efficient data management. The frontend will be served using Apache, providing a reliable and scalable web server. The entire development and deployment process will be carried out in a Linux virtual machine running Ubuntu, ensuring a consistent and controlled environment.

## Team Memebers 
- Cristian Contreras Alvarado
- Tarrence Vaughn
- Antonio Ervin

## Development Tools and Software
The following tools and software were discussed and agreed upon by the team
- **Git**: Version control.
- **pgAdmin**: PostgreSQL database management.
- **Python**: Programming language.
- **SQL**: Structured Query Language for database interaction.
- **pgloader**: Tool for loading data into PostgreSQL.
- **psql**: Command-line tool for interacting with PostgreSQL.
- **curl**: Command-line tool for transfering data with URLs.
- **Requests**: HTTP library for python.
- **Apache**: Web server.
- **CGI bin**: Common Gateway Interface for running scripts.
- **OpenSSH**: Secure Shell for remote login.
- **Docker**

## Project file locations in main vm
- **Database dumpall and config file**: Located in `/3010-proj-grp-1/Phase4/`
- **Python faculty webpage**: Located in `/3010-proj-grp-1/Phase4/py-connect-pgdb.py`
- **Tar file**: Located in `/3010-proj-grp-1/Phase4/phase4.tar`
- **Dockerfile**: Located in `/3010-proj-grp-1/Phase4/dockerfile`

  
## Connecting to the `my_custom_postgres` Container 
The PostgreSQL container is set to **automatically start** when the Web VM is powered on.

1. Check if the container is `running sudo docker ps`
2. Get inside the running container `sudo docker exec -it my_custom_postgres bash` When prompted, enter the password: `student` (if required)
3. To open the project_db database using psql: `psql -d project_db` 

## Accessing Web Page
To connect to the web page, follow these steps:

1. login to web vm
2. open firefox browser
3. search for `192.168.56.10/cgi-bin/py-connect-pgdb.py`

## Rebuilding and Running the Container

If the container is not working or you need to rebuild it after changes:

1. stop and remove the old container `sudo docker stop my_custom_postgres` `sudo docker rm my_custom_postgres`
2. Rebuild the Docker image while being in the Phase4/ folder directory: `sudo docker build -t custom-postgres .`
3. run the container `sudo docker run -d --name my_custom_postgres -p 5433:5432 custom-postgres`
4. If you need to set (or reset) the PostgreSQL postgres user password: `sudo docker exec -it my_custom_postgres bash` ➡️ `psql` ➡️ `ALTER USER postgres WITH PASSWORD 'student';` ➡️ `\q`
5. Create the new database: `createdb project_db`
6. Restore the database: `psql -d project_db < /tmp/temp_dumpall.sql`

## conf files
The postgresql.conf file is coped into the container from an existing one in the Phase4 folder 
the pg_hba.conf file is altered through the dockerfile to make sure the connects are correct. 
  
