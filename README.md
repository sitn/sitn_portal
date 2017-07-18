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

### Python & Flake8

