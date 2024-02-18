# smart-parking-management

## Introduction 

https://perseverancemu.wixsite.com/my-site-1

Smart parking management is a web-based system with the following functionalities.
1. Register new users.
2. Log in registered users.
3. Logged in users can book for a parking spot from different parking zones, get parking receipt with parking details and checkout from a parking spot.
4. Admins can create parking zones indicating the number of parking spots available.
5. Admin can view parking details of all users.

### Prerequisites
You will find hereafter what I use to develop and to run the project
* Python 3
* Django 3.1.6
* pipenv (not mandatory but highly recommended)

### Installation

Get a local copy of the project directory by cloning "smart-parking-management" from github.

```bash
git clone https://github.com/Persemutengera/smart-parking-management.git
```

cd into the folder

```bash
cd smart-parking-management
```

The Framework, Packages and Libraries used in this project are installed in a virtual environment(Recommended); i use pipenv. Instructions on how to get pipenv [here](https://pypi.org/project/pipenv/)

```bash
python3 -m pipenv shell
```

Install the requirements

```bash
python3 -m pip install -r requirements.txt
```

Then follow these steps:
1. Move to root folder 

```bash
cd parking_management
```
2. Create a `.env` file in the root folder, provide the required database information  to the `.env` file (.env.example file is provided to help set this information). You can choose to rename the .env.example to .env

3. Create the tables with the django command line

```bash
python3 manage.py makemigrations
```
then migrate the changes
 
```bash
python3 manage.py migrate
```

Create an admin using command below and enter your preferred username, email and password.(You will use this to login django admin and create parking lots etc)
 
```bash
python3 manage.py createsuperuser
```


4. Finally, run the django server

```bash
python manage.py runserver
```

5. Access the django admin by adding ' /admin' to the url and login to create parking lots

## Usage

To get started with Smart parking management system, the hosted version of the product can be used. You can get started immediately at (https://perseverancemu.wixsite.com/my-site-1). After the login page, you will be guided through creating your first service. The [website](https://perseverancemu.wixsite.com/my-site-1) provides an overview of the application, additional information on the product and guides can be found in the web app.

## Contributing

Smart parking management system is an open-source project. We are committed to a fully transparent development process and highly appreciate any contributions. Whether you are helping us fix bugs, proposing new features, improving our documentation or spreading the word - we would love to have you as a part of the Amplication community. Please refer to our [contribution guidelines](./CONTRIBUTING.md) and [code of conduct](./CODE_OF_CONDUCT.md).

## Licensing

This is an open source project not under any particular license.
However framework, packages and libraries used are on their own license.



   
