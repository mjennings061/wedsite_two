## Installation
1. If using Ubuntu, run 
```commandline
sudo apt install libpq-dev
```

2. Setup your python 3.8 virtual environment and install 
the requirements:
```commandline
pip install -r requirements.txt
```

3. Install postgres and setup your database. Change `DATABASES` in `settings.py` to match your setup.
4. Populate the new DB table:
```commandline
python manage.py migrate
```

6. Run the server on 127.0.0.1, port 8000. You should see the server
on http://127.0.0.1:8000/:
```commandline
python manage.py runserver 8000
```