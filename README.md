# SummerGeeks2020

EnteryLog is a website made according to the problem statement [SummerGeeks2020](https://summergeeks.in/static/assignments/summergeeks%202020%20-%20SDE%20Assignment.pdf)

## Built using
Django==2.2.7
Python 3.6.8
pip 9.0.1
Built on [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
**Tried and tested on Ubuntu** 
To use

Create a virtual environmet 
```bash
   $ python3 -m venv env
   $ source env/bin/activate
   $ pip3 install openpyxl
   $ pip3 install Django
  ``` 

## Features of EnteryLog

**All the models, views, forms, and urls are made in Main App**
EnteryLog director looks like 

```bash
  ├── db.sqlite3
├── entryLog
│   ├── __init__.py
│   ├── __pycache__
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── manage.py
```

* **Details** of the **Visitor via a form** which are http://localhost:8000/guest/entry :
  * Title
  * Name
  * Email
  * Phone Number
  * **Host** (Only host which are available can be selected)
  
* **Email** is sent to **Host** during **check in** and to **Guest** during **checkout**
* A 4-digit OTP is generated which, will be used during CheckOut
* A list of all the guest still in the office which is also used to checkout http://localhost:8000/guest/

* **Guest cannot checkin again if his previous entry is not Checkout**
* Employees can change their availablitity status. http://localhost:8000/employee/
* View all the visits of Guest with details at http://localhost:8000/log/ which are:
  * Host visited
  * Check in Time
  * **Check out Time** (If the Guest has checked out)
* Employees can be uploaded using an EXCEL sheet  [Employee.xlsx](Employee.xlsx) at link http://localhost:8000/employee/upload 
  * Use the above file only for uploading data.
  * **In case of email of 2 employees are same, the file will not be uploaded**

## Following information is stored in the backend at
  The models for them are made at main/models.py. Check [Models.py](entryLog/main/models.py) 
* Visitor:
  **Title, Name, CheckIn, Checkout, Phone number, Email,  Host **, Left office** (True/False)**,OTP** 
* Employee: 
  **Title, Name, Designation, Department, Phone number, Email, Room-No, In Office** (True/False)
  
## To check data in Backend 
* Visit admin panel (http://localhost:8000/admin/)
* Enter Username as ```admin``` and Password as ```admin```
**To create a user yourself**
  * Go to the folder contaning manage.py and in console type
 ```sh
 python3 manage.py createsuperuser
 ```
* Add relevant details thereafter as displayed in console

## In settings.py 
**Following code has been commented**
```python 
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = "email@gmail.com"
# EMAIL_HOST_PASSWORD = 'Google App key'
# DEFAULT_FROM_EMAIL = 'Test <EMAIL_HOST_USER>'
   ```
Enter your gmail account and generate 16 digit app key to test the service. 
And uncomment the following code in enteryLog/settings.py



