# Introduction

Sample django based issue tracker app. Features:

 * Project membership
 * Assigning issues to users.
 * Status and priority mapping to issues.
 * Commenting system for issue.
 * Documented APIs available at `/docs` path.
 * Ability to run as docker container (`docker-compose`). Requires docker 18.02+.
 * Environment based email configuration.
 * This **README** ^_^.

## Usage

Simply do a docker compose setup:

    docker-compose build
    docker-compose up

After a successful `up` command, you should have a running application
at port `4000`. To configure EMAIL values, create a `.env` file at the root (next to `docker-compose.yml`) with the following lines (as needed):

    # The APP_SEND_EMAIL=true is needed
    APP_SEND_EMAIL=true
    # rest all use as needed.
    EMAIL_USE_TLS=True
    EMAIL_HOST='smtp.gmail.com'
    EMAIL_HOST_PASSWORD='sth'
    EMAIL_HOST_USER='thing@some.where'
    EMAIL_PORT=587
    # The `DEFAULT_FROM_EMAIL` can be skipped if same as `EMAIL_HOST_USER`
    DEFAULT_FROM_EMAIL='some@other.thing'

Once the `.env` is defined, rebuild the composed application (`docker
compose build`).

## Docs?

Access publicly available docs at `/docs` route. Generated with
the python module `rest_framework.documentation.include_docs_urls`.

## Admin

The default admin user is created everytime the docker image gets built. The credentials are as follows:

 * **username**: `test`
 * **password**: `nowordpass`

## cURL/httpie

### Register

Register a new user from cli as:

    ➜ http :4000/api/v1/auth/register/ \
        username=new email=valid@where.com \
        password1=nowordpass password2=nowordpass

or

    curl --header 'Content-Type: application/json' \
    --data '{"email":"valid@where.com", "password1":"nowordpass", \
        "password2":"nowordpass", "username":"new"}' \
        'http://localhost:4000/api/v1/auth/register/'

### Login

Login as:

    ➜ http :4000/api/v1/auth/login/ username=h password=1

After successful auth requests, a `key` is sent back. This is used as
authorization header for future requests. For eg. a response like

    {"key": "62281424da9393cc844a95c8e3eacd8571baf725"}

would follow up with a header like

    Authorization: Token 62281424da9393cc844a95c8e3eacd8571baf725

---

### Known limitations

 1. The emails received have a verification URL, but the view doesn't
    exist for the same.
 2. Issue creation does not have a mandatory status/priority
    values. However, for an issue, the user has to be a member of the
    project they want to create issues inside.
 3. No implementation for user roles inside project. This is trivially
    similar to how project membership is designed.
 4. The API tester available at `/docs` endpoint has some
    CSRF/validation issue where it does not accept user authentication
    for several endpoints.
