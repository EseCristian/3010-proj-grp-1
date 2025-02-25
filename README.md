# 3010-proj-grp-1

## Overview
- This project aims to create an ECU CS Dashboard utilizing PostgreSQL and Apache. The dashboard will provide a comprehensive and interactive view of various data related to the ECU Computer Science department. The backend of the application will be powered by PostgreSQL, ensuring robust and efficient data management. The frontend will be served using Apache, providing a reliable and scalable web server. The entire development and deployment process will be carried out in a Linux virtual machine running Ubuntu, ensuring a consistent and controlled environment.

##Team Memebers 
- Cristian Contreras Alvarado
- Tarrence Vaughn
- Antonio Ervin

##Development Tools and Software
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

##Project file locations
- **Database dumpall and config file**: Located in `/assignment/dbsrv/Team1_phase2_db_exports`
- **Python faculty webpage**: Located in `/assignment/websrv/webpages/py-connect-pgdb.py`
- **Tar file**: Located in `/assignment/Team1_phase2.tar`

  
## Connecting to the `project_db` Database
To connect to the `project_db` database using the `webuser1` login, follow these steps:

1. Open your terminal.
2. Use the following command to connect to the `project_db` database:
   ```bash
   psql -h 192.168.56.30 -d project_db -U webuser1
3. when prompted, Enter the password `student`.
