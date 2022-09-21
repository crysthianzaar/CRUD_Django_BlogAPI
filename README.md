# Django Challenge
## _prerequisites:_

- Python 3
- Git
- Docker
- Docker Compose

### STAR PROJECT IN DEVELOPMENT: 
- Clone this project
- Run Docker Compose: `docker-compose up`
- Make makemigrations: `docker-compose exec web python manage.py makemigrations`
- Make Migrate:  `docker-compose exec web python manage.py migrate`
- Create a superuser: `docker-compose exec web python manage.py createsuperuser`

### DEPLOY PROJECT IN PRODUCTION:
- Set `DEBUG = False` in `APIcore\settings.py`
- Add the server domain to the `ALLOWED_HOSTS` in `APIcore\settings.py`
- Docker Compose: `docker-compose -f docker-compose.yml -f production.yml up -d` [More Information](https://docs.docker.com/compose/production/)
- Createsuperuser in production
### _Features Delivered:_

- Login API: `/api/login/`
- Sign-up API: `/api/sign-up/`
- CRUD `/api/admin/authors/`
- CRUD `/api/admin/articles/`
- `/api/articles/?category=:slug`
- `/api/articles/:id/`
## API documentation
- Authentication Method in Postman: `Basic Auth: username and password` [Example](https://i.ibb.co/8bgycqH/imagem-2021-06-17-100118.png) 

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/eca4f5e62ae19caea527)

| EndPoint           | Authentication | Parameters   | Methods | Comments | 
|----------------|---------------|---------------|----------------|-----------|
| `/api/login/`  | All  | username , password | POST | - 
| `/api/sign-up/`| All  | username, email, password1, password1 | POST | -
| `/api/logout/`   | IsAuthenticated  |  | POST | -
| `/api/user/`   | IsAdmin  |  | GET | -
| `/api/admin/authors/`   | IsAdmin  | name, picture | GET, POST, PUT , DELETE |
| `/api/admin/articles/`   | IsAdmin  | category, author,title, summary, firstParagraph, body | GET, POST, PUT , DELETE |
| `/api/articles/?category=:slug`   | IsAdmin  | category | GET | partially reached the demand, authentication is for admins only
| `/api/articles/:id/`   | IsAdmin  | id | GET | Partially reached the demand, authentication is for admins only


### Final remarks:
- The authentication and CRUD Admin part has ended.
- The query part for authenticated and unauthenticated users was partially terminated as a change had to be made to the original requirements
- There are some differences from the initial requirements, such as endpoint change, author is not an object and there are no differences between an authenticated and unauthenticated user in the api `/api/all/articles/:id/` 
-----


## Description

**Challenge goal**: The purpose of this challenge is to give an overall understanding of a backend application. You’ll be implementing a simplified version of a news provider API. The concepts that you’re going to apply are:

- REST architecture;
- Authentication and permissions;
- Data modeling and migrations;
- PostgreSQL database;
- Query optimization;
- Serialization;
- Production builds (using Docker).

**Target level**: This is an all around challenge that cover both juniors and experience devs based on the depth of how the concepts were applied.

**Final accomplishment**: By the end of this challenge you’ll have a production ready API.

## Acceptance criteria

- Clear instructions on how to run the application in development mode
- Clear instructions on how to run the application in a Docker container for production
- A good API documentation or collection
- Login API: `/api/login/`
- Sign-up API: `/api/sign-up/`
- Administrator restricted APIs:
  - CRUD `/api/admin/authors/`
  - CRUD `/api/admin/articles/`
- List article endpoint `/api/articles/?category=:slug` with the following response:
```json
[
  {
    "id": "39df53da-542a-3518-9c19-3568e21644fe",
    "author": {
      "id": "2d460e48-a4fa-370b-a2d0-79f2f601988c",
      "name": "Author Name",
      "picture": "https://picture.url"
    },
    "category": "Category",
    "title": "Article title",
    "summary": "This is a summary of the article"
  },
  ...
]
```
- Article detail endpoint `/api/articles/:id/` with different responses for anonymous and logged users:

    **Anonymous**
    ```json
    {
      "id": "39df53da-542a-3518-9c19-3568e21644fe",
      "author": {
        "id": "2d460e48-a4fa-370b-a2d0-79f2f601988c",
        "name": "Author Name",
        "picture": "https://picture.url"
      },
      "category": "Category",
      "title": "Article title",
      "summary": "This is a summary of the article",
      "firstParagraph": "<p>This is the first paragraph of this article</p>"
    }
    ```

    **Logged user**
    ```json
    {
      "id": "39df53da-542a-3518-9c19-3568e21644fe",
      "author": {
        "id": "2d460e48-a4fa-370b-a2d0-79f2f601988c",
        "name": "Author Name",
        "picture": "https://picture.url"
      },
      "category": "Category",
      "title": "Article title",
      "summary": "This is a summary of the article",
      "firstParagraph": "<p>This is the first paragraph of this article</p>",
      "body": "<div><p>Second paragraph</p><p>Third paragraph</p></div>"
    }
    ```

