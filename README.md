# golingo
Learn english by quizzes 

* Requires Python3

### Clone the project

```shell
$ git clone git@github.com:jesuejunior/golingo.git
```

```shell
$ cd golingo
```
### Install virtualenv 

It's better and easy if you use _virtualenv_ 

 * On Unix-like

``` $ sudo apt-get install python-pip ```

 * On OSX

```sudo easy_install pip```

### Install virtualenvwrapper via PIP

```shell
$ sudo pip install virtualenvwrapper 
```

### Creating virtualenv on Unix0like with Python3

```shell
$ mkvirtualenv --python=/usr/bin/python3 golingo
```

### Creating virtualenv on OSX with Python3

```shell
$ mkvirtualenv --python=/usr/local/bin/python3 golingo
```

### Install dependencies for the project

```shell
$ pip install -r requirements.txt
```

### Create a container of PostgreSQL if you don't have docker installed you will need run PostgreSQL instance locally

```shell
docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=123456 -e POSTGRES_USER=postgres -e POSTGRES_DB=golingo -d postgres
```

### Run syncdb to create an admin user

```shell
$ python manager.py syncdb
```

### Run migrations

```shell
$ python manager.py migrate
```

### Run all tests

```shell
$ py.test
```

### Run server on development mode

```shell
$ python manager.py runserver
```


