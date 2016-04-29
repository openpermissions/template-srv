#Adding a new service

## Acronyms
|Acronym|Meaning|
|:------|:------|
|TCP|Transmission Control Protocol|

## Table Of Contents
* [Select service TCP port](#select-service-tcp-port)
* [Create Apiary documentation](#create-apiary-documentation)
* [Creating the Github repository](#creating-the-github-repository)
* [Populating the repository](#populating-the-repository)

## Select service TCP port
For the sake of running multiple Open Permissions Platform Coalition micro-services locally, which is
required when implementing integration/functional tests, it's been agreed that
each of the micro-services should be run on a different default port.

Rules:
* Please do not change the default port of any of the existing services
* When adding a new service to the list, simply follow the
"last_default_port_on_the_list + 1" rule

|Service|Default port|
|:------|-----------:|
|Identity|8001|
|Index (formerly named: Routing service)|8002|
|Onboarding|8003|
|Repository|8004|
|Transformation|8005|
|Accounts|8006|
|Authentication|8007|

## Create Apiary documentation
* Go to the documents/apiary directory, and rename to your new service
* Remove the Hello World endpoint from documents/apiary/api.md file
* Replace all occurrences of the word Template, with the new service name
* Log into Apiary as catapult bamboo Github account. Account details can be
found here
* Create a new API (for example Open Permissions Platform Coalition Authentication Service)
* Keep the tick-box (private API) unticked
* Copy (and paste) new service api.md into the Apiary editor
* Click save and publish
* A service endpoint will be created (in Apiary). To be used in service
documentation (for example http://docs.copyrighthubauthenticationservice.apiary.io/)
* Add the new service port number to this document

## Creating the Github repository
* From the dashboard click **+New repository** and follow the instructions
* For the settings of the service select **Collaborators**
* From the drop down list select **CDECatapult/catapult-bamboo** and then click
**Add Team**
* From the drop down list select **openpermissions/rusers** and then
click **Add Team**
* From the drop down list select **openpermissions/rwusers** and then
click **Add Team**
* [Log in to hipchat](https://www.hipchat.com/sign_in?d=%2Fhome)
* Select **Group admin**
* Select **Integrations**
* Scroll down to **GitHub for HipChat**
* Select **Manage -> Details**
* Select the **openpermissions** room
* Insert the repository name e.g **openpermissions/auth-srv** and press the **+** button
* **Close** the dialog

## Populating the repository
* Copy the contents of the template service into the new service
* Rename the folder **template** to the name of the new service in lower case
* If there the **template** contains the folder tests/behave delete it from the
new service
* In the root folder
  * Edit the following files, replacing **template** with the new service name
  preserving the case
    * .coveragerc
    * license.md
    * Makefile
    * README.md
    * setup.py
  * Remove the following files
    * USAGE.md
* In the folder **config**
  * Edit the following files, replacing **template** with the new service name
  preserving the case and set the port to the value assigned above
    * default.conf
* In the folder **documents/markdown**
  * The document low-level-desing.md should be replaced by

    ```md
    # Template Service Low Level Design
    
    ## Contents
    + [Classes](#classes)
    + [Class Relationship](#class-relationship)
      + [Class1](#class1)
      + [Class2](#class2)
    
    ## Classes
    + class1
    + class2
    
    ## Class Relationship
    TODO Add diagram
    
    ### Class1
    
    ### Class2
    ```

    Replacing **template** with the new service name preserving the case
* In the folder **tests/unit**
  * Edit the following files, replacing **template** with the new service name
  preserving the case
    * test_app.py
* In the folder **tests/unit/controllers**
  * Edit the following files, replacing **template** with the new service name
  preserving the case
    * test_root_handler.py
  * Remove the following files
    * test_hello_handler.py
* In the service name folder
  * Edit the following files, replacing **template** with the new service name
  preserving the case and remove any use of hello_handler
    * app.py
    * main.py
* In the sub folder **controllers** of the service name folder
  * Edit the following files, replacing **template** with the new service name
  preserving the case
    * root_handler.py
  * Remove the following files
    * hello_handler.py
