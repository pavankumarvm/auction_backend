# Auction System

_BE Project_

<!-- Website link: __ -->

## How to install

1. git clone https://pavankumarvm@bitbucket.org/virtual-auction-system/auction_system_backend.git
2. Change to Auction System directory
   ```bash
   cd auction_system_backend
   ```
3. create virtual environment using virtualenv
   Commands are as follows:
   ```bash
   pip install virtualenv
   virtualenv venv
   venv\Scripts\activate
   ```
4. Check in command line if virtualenv is activated or not.
   If activated it will be as follows:
   ```bash
   (venv) A:auction_system_backend>
   ```
5. Now install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## How to run project

1. Be sure you have completed above installation steps.
2. Now first connect the project to database.
   - Open auction_system_backend>settings.py>
   - In this file you have to edit local MySql server login configuration(username and password).
   - After this create database _auction_system_ on your localhost
   ```bash
   create database auction_system;
   use auction_system;
   ```
3. Now first migrate all models.
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Now collect a static files.
   ```bash
   python manage.py collectstatic
   ```
5. Now you can run project using command:
   ```bash
   python manage.py runserver
   ```

## Contribute to Repository

```
1. Fork this repository
2. create a branch for your changes
3. configure an upstream to this repository
4. create a pull request
```
