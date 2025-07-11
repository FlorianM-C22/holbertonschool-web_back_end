## Resources

****Read or watch:****

*   [Flask-Babel](/rltoken/O7S-gr-vGk6dOtLsp596dw "Flask-Babel")
*   [Flask i18n tutorial](/rltoken/5ZXAPeW50RkAGQAEjkToug "Flask i18n tutorial")
*   [pytz](/rltoken/EXJ3MBPdO7hOULxpS9a2jw "pytz")

## Learning Objectives

*   Learn how to parametrize Flask templates to display different languages
*   Learn how to infer the correct locale based on URL parameters, user settings or request headers
*   Learn how to localize timestamps

## Requirements

*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
*   All your files should end with a new line
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should use the pycodestyle style (version 2.5)
*   The first line of all your files should be exactly `#!/usr/bin/env python3`
*   All your `*.py` files should be executable
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
*   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
*   All your functions and methods should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
*   All your functions and coroutines must be type-annotated.

## Tasks

### 1.

First you will setup a basic Flask app in `0-app.py`. Create a single `/` route and an `index.html` template that simply outputs “Welcome to Holberton” as page title (`<title>`) and “Hello world” as header (`<h1>`).

  

### 2.

Install the Babel Flask extension:
```
$ pip3 install flask\_babel
```
Then instantiate the `Babel` object in your app. Store it in a module-level variable named `babel`.

In order to configure available languages in our app, you will create a `Config` class that has a `LANGUAGES` class attribute equal to `["en", "fr"]`.

Use `Config` to set Babel’s default locale (`"en"`) and timezone (`"UTC"`).

Use that class as config for your Flask app.

  

### 3.

Create a `get_locale` function and use `request.accept_languages` to determine the best match with our supported languages.

Use the `babel.init_app()` method to initialize Flask-Babel with your application. Pass the`locale_selector` parameter to specify your custom `get_locale` function.

  

### 4.

Use the `_` or `gettext` function to parametrize your templates. Use the message IDs `home_title` and `home_header`.

Create a `babel.cfg` file containing
```
\[python: \*\*.py\]
\[jinja2: \*\*/templates/\*\*.html\]
```
Then initialize your translations with
```
$ pybabel extract -F babel.cfg -o messages.pot .
```
and your two dictionaries with
```
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
```
Then edit files `translations/[en|fr]/LC_MESSAGES/messages.po` to provide the correct value for each message ID for each language. Use the following translations:

msgid

English

French

`home_title`

`"Welcome to Holberton"`

`"Bienvenue chez Holberton"`

`home_header`

`"Hello world!"`

`"Bonjour monde!"`

Then compile your dictionaries with
```
$ pybabel compile -d translations
```
Reload the home page of your app and make sure that the correct messages show up.

  

### 5.

In this task, you will implement a way to force a particular locale by passing the `locale=fr` parameter to your app’s URLs.

In your `get_locale` function, detect if the incoming request contains `locale` argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.

Now you should be able to test different translations by visiting `http://127.0.0.1:5000?locale=[fr|en]`.

**Visiting `http://127.0.0.1:5000/?locale=fr` should display this level 1 heading:** ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/3/f958f4a1529b535027ce.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20250711%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20250711T110125Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8b72d30b3bdfc5c0ca41d8bbec42dab0e7138b9e6c2ec4514283b2ba87c34c89)

  

### 6.

Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in `5-app.py`.
```
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
```
This will mock a database user table. Logging in will be mocked by passing `login_as` URL parameter containing the user ID to log in as.

Define a `get_user` function that returns a user dictionary or `None` if the ID cannot be found or if `login_as` was not passed.

Define a `before_request` function and use the `app.before_request` decorator to make it be executed before all other functions. `before_request` should use `get_user` to find a user if any, and set it as a global on `flask.g.user`.

In your HTML template, if a user is logged in, in a paragraph tag, display a welcome message otherwise display a default message as shown in the table below.

msgid

English

French

`logged_in_as`

`"You are logged in as %(username)s."`

`"Vous êtes connecté en tant que %(username)s."`

`not_logged_in`

`"You are not logged in."`

`"Vous n'êtes pas connecté."`

**Visiting `http://127.0.0.1:5000/` in your browser should display this:**

![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/3/2c5b2c8190f88c6b4668.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20250711%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20250711T110125Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=278c52664e935f110eafcec210f56a05f2183e8f41eec7e1f1a5f155816ea286)

**Visiting `http://127.0.0.1:5000/?login_as=2` in your browser should display this:** ![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/3/277f24308c856a09908c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20250711%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20250711T110125Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=334d8f46881a5974449d507c0d9ae119d23b24cba988922bff1a7becac7d4d30)

  

### 7.

Change your `get_locale` function to use a user’s preferred local if it is supported.

The order of priority should be

1.  Locale from URL parameters
2.  Locale from user settings
3.  Locale from request header
4.  Default locale

Test by logging in as different users

![](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/3/9941b480b0b9d87dc5de.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20250711%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20250711T110125Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f212e1f71aacb0277b83107b5cf1533df01eb2dd260285227691e1b0878425e8)

  

### 8.

Define a `get_timezone` function and in `babel.init_app()` Pass the`timezone_selector` parameter to specify your custom `get_timezone` function.

The logic should be the same as `get_locale`:

1.  Find `timezone` parameter in URL parameters
2.  Find time zone from user settings
3.  Default to UTC

Before returning a URL-provided or user time zone, you must validate that it is a valid time zone. To that, use `pytz.timezone` and catch the `pytz.exceptions.UnknownTimeZoneError` exception.