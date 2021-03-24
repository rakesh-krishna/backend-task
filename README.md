# backend-task

On the terminal execute the below command to create the projects' working directory and move into that directory.
```bash
$ mkdir backend-task
cd backend-task

```
In the projects' working directory execute the below command to create a virtual environment for our project. Virtual environments make it easier to manage packages for various projects separately.

```bash

$ virtualenv venv

```

To activate the virtual environment, execute the below command.

```bash

$ source venv/Script/activate

```
Clone this repository in the projects' working directory by executing the command below.
```bash
$ git clone https://github.com/rakesh-krishna/backend-task
$ cd backend-task
```

To install all the required dependencies execute the below command.
```bash
$ pip install -r requirements.txt
```
If any problem with installing requirements try refering [here](https://stackoverflow.com/questions/41457612/how-to-use-requirements-txt-to-install-all-dependencies-in-a-python-project)


Create an Environment Variable named ```youtube_api_key``` add your youtube API key to this variable

First start the API execute the below command.
```bash
$ python app.py
```

Then Run the Server execute the below command.
```bash
$ python server.py
```

