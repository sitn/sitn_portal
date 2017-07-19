# SITN portal

This application regroups every non-spatial web app developped
internally at SITN.

## Building the application

### Requirements

#### Cygwin

sitn_portal is meant to be built and used on Windows servers.

To do so, we need to be able to use "Linux" bash commands in a Windows cmd.

This can be achieved by installing some Cygwin components:

- make from the devel folder
- gettext-devel from the devel folder
- wget from the web folder

#### Python

Python 2.7 (should work on 3.x as well) should be installed and virtualenv as well.
To install virtualenv

    C:\Python27\Scripts\pip install virtualenv

#### Git for Windows
#### NodeJS and Npm

Once NodeJS and npm installed, you will need angularCLI as well. AngularCLI
has to be installed globally:

    npm install -g @angular/cli

At last, almost all requirements have to be in the path environment variable
(NodeJS and npm should already be there)

We recommand to add the following elements to the path (in the same order
and at the beginning of the variable !)

1. Path to git (something like C:\Program Files (x86)\Git\cmd)
2. Path to Python (something like C:\Python27)
3. Path to Python scripts (something like C:\Python27\Scripts)
4. Path to Cygwin executables (something like C:\cygwin64\bin)

In the end, the following string should be added at the begin of the path:

    C:\Program Files\Git\cmd;C:\Python27;C:\Python27\Scripts;C:\cygwin64\bin;....

## Developping

### Serving the server part

The server part is served using Pyramid's pserve.

To run it:

    .build\venv\Scripts\pserve --reload development.ini

This will start a local server on some specific port (usually 6543)

### Serving the client part

Each Angular app must be run independently when developping. To do so, go
to the Angular app folder and:

    cd sitn_portal\sitn-portal-client
    ng serve --app app_name

`app_name` is the name of an Angular application as described in the CLI
configuration file which is located in the `sitn-portal-client` folder.

### Developping the client part using the server part

You should define full development URLs in the Angular applications.

Thus, if you want ton use a webservice for which you have defined a
`my_webservice` route, then you should use
`http://localhost:6543/my_webservice` as URL in Angular. Do not forget
to declare them as globals in Angular.

### Building

The application is autmatically built by make. Note that the HMTL files are
duplicated in order for the Mako templating to be used.

While developping, the HTML files inside the `sitn-portal-client\src` while
be used.

In production, the HTML files inside the template folder `sitn_portal\template`
will be used, thus changes made in the Angular HTML files must be **MANUALLY**
reported to the Mako HTML templates.

### Creating a new Angular application

Basically, to create a new Angular application, one will have to copy-paste
a bunch of stuff.

#### CONST_Makefile

In `CONST_Makefile` search for the Angular apps section and copy-paste
the lines defining with the following variables:

* `ANGULAR_APP_PORTAL`
* `ANGULAR_PORTAL_BUILD_JS_FILES`
* `ANGULAR_PORTAL_BUILD_CSS_FILES`
* `ANGULAR_PORTAL_FILES`

Replace `PORTAL` in each name of these variables with the name of your new
app (like `MYAPP`) and replace it also inside the variable attribution.

Search for `ANGULAR_APPS` and add `$(ANGULAR_APP_MYAPP)-build` at the
end of the line (substituing `MYAPP`).

Next, search for the `.build/ng-portal.timestamp: $(ANGULAR_PORTAL_FILES) $(ANGULAR_BASE_DIR)/src/styles.css`
make block and duplicate it. Once again subsitute `PORTAL` with whatever you
called `MYAPP`

Finally, add this new block to the `.PHONY: build-frontend` make block.

#### Python routes & templates

We need to create a new route and new template for each Angular application.

First:
* Create a new `myapp.py`file inside `sitn_portal\views` by copying-pasting
the content of `CONST_Templates\sitn_portal\views`

* Create a new `myapp.html` template inside `sitn_portal\templates` by copying-pasting
the content of `CONST_Templates\sitn_portal\templates`

* In the sitn_portal `routes.py` files, add a section like:

```python
# myapp.py
config.add_route('myapp_fake', 'myapp/fake')
config.add_route('myapp', '/myapp')

```

Do not forget to **REPLACE** all `myapp` by whatever you called your application.

#### Angular & Angular CLI

Finally you will need to create a new Angular application. The easiest way to do so is to
copy-paste the following file and folder into the same given locations in sitn_portal
project:
* `CONST_templates\sitn_portal\sitn-portal-client\src\myapp.html`
* `CONST_templates\sitn_portal\sitn-portal-client\src\app\myapp`

Again, do no forget to replace all `myapp` by whatever you called your application.

Finally, we have to tell Angular CLI that there is a new application available:
* Open `sitn_portal\sitn-portal-client\.angular-cli.json`
* Duplicate the section named `sitn-portal`inside the `apps` section
* Inside of the duplicated section, replace all `portal` terms with `myapp`

Now you should be good to go...

### Python & Flake8

TODO