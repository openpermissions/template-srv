FORMAT: 1A
HOST: http://openpermissions.org

# Open Permissions Platform Template Service
The Template Service is a simple service used to demonstrate how a
service is created in the Open Permissions Platform.

## Standard error output
On endpoint failure there is a standard way to report errors.
The output should be of the form

| Property | Description               | Type   |
| :------- | :----------               | :---   |
| status   | The status of the request | number |
| errors   | An array of errors        | array  |

### Error
| Property | Description                                 | Type   |
| :------- | :----------                                 | :---   |
| source   | The name of the service producing the error | string |
| message  | A description of the error                  | string |

# Authorization

This API requires authentication. Where [TOKEN] is indicated in an endpoint header you should supply an OAuth 2.0 access token with the appropriate scope (read, write or delegate). 

See [How to Auth](https://github.com/openpermissions/auth-srv/blob/master/documents/markdown/how-to-auth.md) 
for details of how to authenticate the OPP services.

# Group Service Information
Information on the service

## Service information [/v1/template]

### Retrieve service information [GET]

#### Output
| Property | Description               | Type   |
| :------- | :----------               | :---   |
| status   | The status of the request | number |
| data     | The service information   | object |

##### Service information
| Property     | Description                    | Type   |
| :-------     | :----------                    | :---   |
| service_name | The name of the api service    | string |
| service_id   | The id of the api service      | string |
| version      | The version of the api service | string |


+ Request
    + Headers

            Accept: application/json

+ Response 200 (application/json; charset=UTF-8)
    + Body

            {
                "status": 200,
                "data": {
                    "service_name": "Open Permissions Platform Template Service",
                    "service_id": "c9936d2ae20f11e597309a79f06e9478",
                    "version": "0.1.0"
                }
            }

## Hello World [/v1/template/hello]

### Hello World [GET]

| OAuth Token Scope |
| :----------       |
| read              |

#### Output
| Property | Description               | Type   |
| :------- | :----------               | :---   |
| status   | The status of the request | number |
| data     | A message                 | object |

#### Message
| Property     | Description                    | Type   |
| :-------     | :----------                    | :---   |
| service_name | The name of the api service    | string |
| version      | The version of the api service | string |
| message      | Hello World                    | string |


+ Request
    + Headers

            Accept: application/json
            Authorization: Bearer [TOKEN]

+ Response 200 (application/json; charset=UTF-8)
    + Body

            {
                "status": 200,
                "data": {
                    "service_name": "Open Permissions Platform Template Service",
                    "version": "0.1.0",
                    "message": "Hello World"
                }
            }
