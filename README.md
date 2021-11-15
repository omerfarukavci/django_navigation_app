## Django Navigation Data Project

In summary, this project sends the location information of the vehicles in the database for the last 48 hours.

In summary, this project has a function that returns the list of last points per vehicle that have sent navigation data in the last 48 hours.
It was built with Django ORM Framework and PostgreSQL database was used. Models were created and a REST API was created by serializing the data.

----
**The models are:**


NavigationRecord

Name  | Type
------------- | -------------
id  | Primary Key
vehicle | Foreign Key
datetime  | DateTimeField
latitude  | FloatField
longitude  | FloatField

Vehicle

Name  | Type
------------- | -------------
id  | Primary Key
plate | Charfield

----
To run the application, PostgreSQL database name and password must be entered in settings.py.

Because there are many queries, each query is costly in terms of performance. Therefore, the query should be completed as soon as possible. 

`NavigationRecord.objects.filter(datetime__gte=thetime).order_by('vehicle','-datetime').distinct('vehicle')` 


For an example record (POST):
http://127.0.0.1:8000/record
``` 
  {
        "latitude": "99.23",
        "longitude": "99.12",
        "vehicle": 1,
        "datetime": "2021-10-15T12:38:26+03:00"
  }
  ```
	
  
For an example query (GET): 
http://127.0.0.1:8000/record
``` 
[
    {
        "latitude": "0.000",
        "longitude": "0.000",
        "vehicle": 1,
        "datetime": "2021-11-15T17:48:43+03:00"
    },
    {
        "latitude": "1.100",
        "longitude": "1111111.100",
        "vehicle": 2,
        "datetime": "2021-11-15T14:42:38+03:00"
    },
    {
        "latitude": "7.900",
        "longitude": "7.200",
        "vehicle": 3,
        "datetime": "2021-11-15T12:31:00+03:00"
    }
]
``` 
