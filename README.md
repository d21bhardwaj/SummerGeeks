# SummerGeeks2020

EnteryLog is a website made according to the problem statement [SummerGeeks2020](https://summergeeks.in/static/assignments/summergeeks%202020%20-%20SDE%20Assignment.pdf)

## Features of EnteryLog

* **Details** of the **Visitor via a form** which are:
  * Title
  * Name
  * Email
  * Phone Number
  * **Host** (Only host which are available can be selected)
  
* **Email** is sent to **Host** during **check in** and to **Guest** during **checkout**
* A 4-digit OTP is generated which, will be used during CheckOut
* **Guest cannot checkin again if his previous entry is not Checkout**
* Employees can change their availablitity status
* A list of all the guest still in the office
* View all the visits of Guest with details of :
  * Host visited
  * Check in Time
  * **Check out Time** (If the Guest has checked out)
* Employees can be uploaded using an EXCEL sheet [Employee.xlsx](Employee.xlsx) 
  * Use the above file only for uploading data.
  * **In case of email of 2 employees are same, the file will not be uploaded**

### Following information is stored in the backend at
  The models for them are made at main/models.py. Check [Models.py](entryLog/main/models.py) 
* Visitor:
  **Title, Name, CheckIn, Checkout, Phone number, Email,  Host **, Left office** (True/False)**,OTP**.
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

  


  


