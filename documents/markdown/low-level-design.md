# Service Low Level Design

## Contents
+ [About](#about)
+ [Tornado](#tornado)
  + [Authenticated decorator](#authenticated-decorator)
  + [Authorised decorator](#authorised-decorator)
  + [Service access authorisation](#service-access-authorisation)
  + [Repository access authorisation] (#repository-access-authorisation)
  + [Default headers] (#default-headers)
  + [Default OPTIONS response] (#default-options-reponse)
  + [Common error output format](#common-error-output-format)
  + [Reading JSON body with the required keys] (#reading-json-body-with-the-required-keys)
+ [Configuring a service](#configuring-a-service)
  + [Identifying the service within the Hub](#identifying-the-service-within-the-hub)
  + [Configuring the HTTPS server](#configuring-the-https-server)
  + [Configuring the location of other services](#configuring-the-location-of-other-services)
+ [Commands](#commands)
  + [Command register_service](#command-register_service)
  + [Command create_dev_cert](#command-create_dev_cert)
  + [Adding commands to a service](#adding-commands-to-a-service)
+ [Makefile targets](#makefile-targets)
  + [requirements](#requirements)
  + [test](#test)
  + [pylint](#pylint)
  + [docs](#docs)
  + [egg_locks](#egg_locks)
+ [Logging](#logging)

## About
This document describes the shared design elements of services in the Hub.

## Tornado
These services are based on [Tornado Web Framework](http://www.tornadoweb.org/).
Common functionality and helpers for Tornado have been extended in the library
[Koi](https://github.com/openpermissions/koi)

They include:
+ Authenticated decorator
+ Authorised decorator
+ Service access authorisation
+ Repository access authorisation
+ Setting default headers
+ Default OPTIONS response
+ Common error output format
+ Reading JSON body with required keys

### Authenticated decorator
The authenticated decorator authenticates a provided token. This token is
requested by a user when they log in to the accounts service, and has an expiry time limit.

### Authorised decorator
The authorised decorator ensures that a user (as identified by a token) has permission to run a given action. 
The decorator wraps an authorisation function, which takes the identifying token and any keyword arguments 
needed to verify the user's access.

### Service access authorisation
Service-to-service access is controlled using SSL certificates, which are validated in koi using a call to the Auth service.
In order to access another service, a valid SSL certificate must be provided, and the identified organisation
must have been granted sufficient Read/Write permissions.

### Repository access authorisation
Access to repositories is controlled using either an SSL certificate or a [JSON Web Token](https://jwt.io/introduction/).
Koi will validate the given certificate or token with a call to the Auth service, ensuring that the identified organisation has sufficient Read/Write 
permissions for the requested repository.

### Default headers
To enable Cross-Origin Resource Sharing ([CORS](https://www.w3.org/TR/cors)) the 'cors' option is set to true in the service config, then the 'Access-Control-Allow-Origin' header will be set to '*'.

### Default OPTIONS response
If the 'cors' option is True, the service will respond with an empty response, and set the 'Access-Control-Allow-Headers' and
'Access-Control-Allow-Methods' headers.

### Common error output format
Errors will be reported in the following JSON format:

```json
{
    "status": 400,
    "errors": [
        {
            "source": "accounts" ,
            "message": "errormsg1"
        },
        {
            "source": "accounts",
            "message": "errormsg2"
        }
    ]
}
```
The value of "status" will vary depending on the [HTTP Status Code](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) and in relation to the Hub [API Standards](https://github.com/openpermissions/support-docs/blob/master/documents/markdown/arch/API-Standards.md).

### Reading JSON body with the required keys
This will take the body of a request and parse it as json. A list of required fields can be optionally provided, 
which will be checked for and reported if missing.
## Configuring a service
Each service will have a directory named *config*. Within this directory there is a
file, *default.conf*. This file is used within the Tornado framework and
stored as default command line option values. More details on Tornado command
line options can be found [here](http://tornadokevinlee.readthedocs.org/en/latest/options.html)

As well as overriding these values from the command line, a file *local.conf*
can be placed in the *config* directory with these values.

## Identifying the service within the Hub

Within the file *default.conf* you should find a set of values that can be used
to identify the service.

```
service_type = "template"
service_id = "template"
```
The ***service_type** identifies the type of service running from a restricted list of valid service types.

The ***service_id*** is used to identify a service within the Hub. The value of ***service_id*** should match the id 
assigned to the service when it is registered with the accounts service.

## Configuring the HTTPS server.
```
# ssl, i.e. https
use_ssl = True
# ssl key, cert, ca_cert will use private certs from koi if left empty
ssl_key = ""
ssl_cert = ""
ssl_ca_cert = ""
# whether a certificate is required from the other side of the connection
# use the constants from the standard lib ssl module
# 0 => ssl.CERT_NONE, 1 => ssl.CERT_OPTIONAL, 2 => ssl.CERT_REQUIRED
ssl_cert_reqs = 2
```

The **ssl_key** and **ssl_cert** specify files which contain a certificate to
be used to identify the local side of the connection.

The  **ssl_ca_cert** file contains a set of concatenated
“certification authority” certificates, which are used to validate certificates
passed from the other end of the connection

The **ssl_cert_reqs** specifies whether a certificate is required from the
other side of the connection, and whether it will be validated if provided.

Further information on certificates can be found
[here](https://docs.python.org/2/library/ssl.html#ssl-certificates)

### Configuring the location of other services
Within the file *default.conf* you should find a set of values for the url of
other services.
e.g

```conf
url_registry_db = ""
url_accounts = "https://localhost:8006"
url_authentication = "https://localhost:8007"
url_identity = ""
url_index = ""
url_onboarding = ""
url_query = ""
url_repository = ""
url_transformation = ""
url_registration = ""
```

Here we can see that the **accounts** service can be found at
**https://localhost:8006** and the **authentication** can be found at
**https://localhost:8007**.

If we were to have these at another location then the file *local.conf*
could be added with the new values for the endpoint of the services that have
changed.

## Commands
Python **click** is used to implement a command line interface (CLI).

Details on **click** can be found [here](http://click.pocoo.org/).

Koi has a set of default commands

### Command register_service
Registers the service with the accounts service.

Usage
```
register_service [OPTIONS] EMAIL PASSWORD ORGANISATION_ID
```

| option             | description                                                  |
| :-----             | :----------                                                  |
| --name             | The service name                                             |
| --service_type     | The service type                                             |
| --accounts_url     | URL for the accounts service                                 |
| --certificate_path | Location of the service certificate                          |
| --location         | The url including protocol and port (if required) of service |
| --config           | The configuration directory                                  |

| parameter       | description                             |
| :--------       | :----------                             |
| EMAIL           | a user's email                          |
| PASSWORD        | a user's password                       |
| ORGANISATION_ID | ID of the service's parent organisation |

### Command create_dev_cert
Generate a self signed certificate for development purposes.

Usage
```
create_dev_cert [OPTIONS] NAME
```

| option | description                                     |
| :----- | :----------                                     |
| --dest | The directory to put the certificate and key in |

| parameter | description                                 |
| :-------- | :----------                                 |
| NAME      | name ro be given to the certificate and key |

### Adding commands to a service
Using this template service as an example, there is a directory
*template/commands*. Within this directory there is a file load_data.py.

This implements a command, **load_data**.

To create a new command, create a python file whose name is the name of the
command and follow the **click** documentation and the example, **load_data**.

## Makefile targets
Each service will have a Makefile with a set of common targets.

Details on make and makefiles can be found [here](https://www.gnu.org/software/make/)

### requirements
This installs the python requirements for the service. The service will have
common requirements, as well as requirements specific to production mode and development mode. In production mode
only pips needed to run the service are included. In development mode pips to

+ run tests
+ get test coverage
+ run lint over the code
+ produce documentation

To install requirements for production mode run one of these two commands

```bash
make requirements
```

or

```bash
make requirements REQUIREMENT=prod
```

To install requirements for development mode run the following command

```bash
make requirements REQUIREMENT=dev
```

### test
The **test** target is used to run the unit tests. Unit tests are written using
the **pytest* framework.

Details on **pytest** can be found [here](http://pytest.org/)

Unit tests can be found in the directory **tests/unit**. Test result output
can be found at **tests/unit/reports**. This location can set by the makefile
property TEST_REPORTS_DIR.

As an example this will run the unit tests and output the reports to
**build/reports**

```bash
make test TEST_REPORTS_DIR=build/reports
```

### pylint
The **pylint** target runs the lint tool pylint over the python code. As with
the **test** target the property TEST_REPORTS_DIR can be used to set an
alternative directory for the lint reports.

Details on **pylint** can be found [here](https://www.pylint.org/) 

```bash
make pylint
```

### docs
The **docs** target builds documents belonging to the service. Document types
built are

+ api ([apiary](#https://apiary.io/blueprint) markdown)
+ in source ([sphinx](http://www.sphinx-doc.org/))
+ service ([github](https://help.github.com/categories/writing-on-github/) markdown)

These document build output by default goes to the directories
 
+ _build/api/html
+ _build/in_source
+ _build/service/html

respectively.

The properties BUILDDIR, BUILD_API_DOC_DIR, BUILD_SOURCE_DOC_DIR and
BUILD_SERVICE_DOC_DIR can be set to change the output directory.
BUILDDIR represents the base output directory, by default **\_build**

The other three can be used to specify the exact location of the output

```bash
make docs
```

### egg_locks
The **egg_locks** target is used to lock down the pip versions used in the
service.

When updating pips the only files that should be edited are
*requirements/common.txt*, *requirements/dev_top_level.txt* or
*requirements/prod_top_level.txt*. Once they have been edited the **egg_locks**
target needs to be run, this will then update the requirements files used in
the **requirements** target, *requirements/dev.txt* and
*requirements/prod.txt*.

Running the **egg_locks** without changing these files will update update to
the latest released version of the pips.

## Logging
Logging os performed by the standard python logging module. It is configured to
use the standard [SysLogHandler](https://docs.python.org/2/library/logging.handlers.html#sysloghandler).

Configuration of the handler is down within the tornado configuration file
*config/default.conf*.

These values can be overridden in the same way as
[Configuring a service](#configuring-a-service)

Default values are set to

```conf
# `log_to_stderr` turns on logging to console
log_to_stderr = True

# `log_file_prefix` turns on logging to file
log_file_prefix = 'app.log'

# `syslog_host` IP Address - turns on logging to a syslog server
# can be also defined as the CLI parameter:
# python template/ --logging=debug --syslog_host=54.77.151.169
syslog_host = '54.77.151.169'
syslog_port = 514
env = 'dev'
```
