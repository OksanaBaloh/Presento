# Presento

Presento is a dynamic web application with its frontend built using React, TypeScript, and SCSS with the Bootstrap UI library.

This app helps people to find the perfect gift for their loved ones. It’s a small service that can be improved and many other features can be added to it. Moreover, it can be added as a part of a big marketplace service. 

## Demo

You can view a live demo of the app [HERE](http://mate-presento.in.net/)

## Technologies
 - React
 - TypeScript
 - REST API
 - Axios
 - JWT authentication
 - React Router
 - Formik with Yup
 - Bootstrap
 - SCSS

## Run local with docker

Docker should be installed

Open terminal and run:
  ```
  git clone https://github.com/Terrrya/Library-service.git
  cd Library-service
  ```

Create in root directory of project and fill .env file as shown in .env_sample file

  ```
  docker compose -f docker-compose-local.yml up
  ```
Open in browser: localhost/

## Filling .env file

Don't forget to fill .env file as shown in .env_sample.

## Getting access

You can use following:
- superuser:
  - Email: admin@admin.com
  - Password: test12345

Or create another one by yourself
