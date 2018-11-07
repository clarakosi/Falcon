# falcon
falcon is a simple key value data store mock up using the [Falcon](https://falconframework.org/) micro framework. 

### Start Virtual Environment
Assuming you have python 3:

Mac instructions: 
```$xslt
cd falcon
python3 -m venv venv
. venv/bin/activate
```
Windows instructions
```$xslt
cd falcon
py -3 -m venv venv
venv\Scripts\activate
```

### Install Dependencies
To install all of the dependencies found on `requirements.txt`
run the following in your terminal:
```$xslt
pip3 install -r requirements.txt 
```

### Start Development Server
To start the gunicorn server run the following in your terminal:
```$xslt
cd kVal
gunicorn --reload index:app
```
(Note the use of the `--reload` option is to tell Gunicorn to reload the app whenever its code changes.)



