# Django Newsletter

Django newsletter is a webapp to let users subscribe for emails powered by Django and react 
## Features

- Accepts users email and fullname
- Uses mailchimp to add subscribers to email list
- Emails can be easily sent from the mailchimp panel or any other email marketing platform
- Has built in api's with djangorestframework to get all users and post data of users


Django newsletter is a lightweight webapp allowing users to signup to newsltters easily


## Tech

Django newsletter uses a number of open source projects to work properly:

- [Django] - Python based web framework for easy and fast MVP creation !
- [React JS] - Javascript library for frontend
- [Python] - Python programming language.
- [SQlite3] - Sqllite3 used as a database for Django App


And of course Django Newsletter itself is open source on GitHub.

## Installation

Django Newsletter requires [Django](https://docs.djangoproject.com/en/) 3.2.5+ to run.

Install the dependencies and devDependencies and start the server.

```sh
cd src
cd backend
pip install -r requirements.txt
python manage.py runserver

cd frontend
npm install
npm start
```

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000 -> Backend
localhost:3000 -> Frontend
```
API Endpoints:
```sh
http://127.0.0.1:8000/api/v1/email-signup/ -> POST to add users to subscriber list
http://127.0.0.1:8000/api/v1/email-signup/ -> GET to fetch users form database, this returns a paginated response and page can be passed as a parameter to url
```


## License

MIT

**Free Software, Hell Yeah!**
