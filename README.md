# Presento

Presento is a dynamic web application built with React, TypeScript, and SCSS, utilizing the Bootstrap UI library.

It serves as a comprehensive solution to help people find the perfect gift for their loved ones. With a wide range of options available, Presento caters to all ages, genders, occasions, and budgets. It’s a small service that can be improved and many other features can be added to it.

The application uses secure authentication by utilizing JSON Web Tokens (JWT) to enhance user privacy and ensure data protection.

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
