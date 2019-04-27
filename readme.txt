Instructions for Local Setup:

1. Git clone this repo into your local machine. 
	$ git clone https://github.com/dhungana/ConsumerAffairs.git
2. Install Docker CE(version: 18.09.5) from https://docs.docker.com/install
3. Install Docker Compose(version: 1.24.0) from https://docs.docker.com/compose/install
   (if Docker Compose was not included in the installation for Docker CE)
4. Change directory to go within the project folder.
	$ cd ConsumerAffairs
5. Change credentials in mysql.env and django-apache2.env:
	a. MYSQL_DATABASE must be same in both files
	b. MYSQL_ROOT_PASSWORD in mysql.env and MYSQL_PASSWORD in django-apache2.env must be same
	c. SECRET_KEY should be long, unique and unpredictable.
6. If there are any services like Apache, MySQL or Tomcat in your local machine operating 
	at ports 80, 3306, or 8080, stop those services. This project needs those ports for
	Apache, MySQL, and PhpMyAdmin.
7. From the project folder (which contains docker-compose.yml), run the following commands
	with administrative priviledge:
	$ sudo docker-compose build
	$ sudo docker-compose up -d
8. To run migrations, run the following command with administrative priviledge:
	$ sudo docker exec -it django-apache2 python manage.py migrate
9. To create a super user, run the following command:
	$ sudo docker exec -it django-apache2 python manage.py createsuperuser
10. To make the admin panel view look better, run the following command:
	$ sudo docker exec -it django-apache2 python manage.py collectstatic
11. Login to admin panel at http://localhost/admin and create users and companies.
	You can also view submitted reviews here.
12. You can now connect to the REST API endpoints at http://localhost
13. You can also view the database tables using PhpMyAdmin at http://localhost:8080/ using
	the same credentials that are in mysql.env 
14. To reflect any code change you make on the django folder ConsumerAffairs/ConsumerAffairs,
	run the following command:
	$ sudo docker exec -it django-apache2 service apache2 restart
15. To add/remove any library from use in the django app, add/remove the library 
	in requirements.txt and run the following commands with administrative priviledge
	from the project folder:
	$ sudo docker-compose build
	$ sudo docker-compose up -d
16. To run tests, run the following command:
	$ sudo docker exec -it django-apache2 python manage.py test
17. To check coverage, run the following commands:
	$ sudo docker exec -it django-apache2 coverage run --source='.' manage.py test
	$ sudo docker exec -it django-apache2 coverage report
18. To stop the docker containers, go to the project folder and run this command with
	administrative priviledge:
	$ sudo docker-compose stop



API Documentation:

You can find API Documentation at https://documenter.getpostman.com/view/477052/S1LpaC6B