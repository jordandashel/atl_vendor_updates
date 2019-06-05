# Atl Media Vendor Update Platform

## How to Run

The easiest way to run this program is with docker. There is an image,
hosted on Docker hub.

```
$ docker run -d -p 5000:5000 docker.io/jordandashel/atl_vendor_updates
```

If you want to run the program locally, you will need `python3`, `pip`, etc. I would
recommend using a virtual environment. The dependencies can be installed with 

```
$ pip install requirements.txt
```

You need to have the variable `FLASK_APP` set in your env so that flask can find
it

```
$ export FLASK_APP=vendor_update.py
```

The database can be initialized with 

```
$ python -m flask initdb
```

It can also be created using `sqlite3` or simply `flask initdb`.
You can then run the program.

```
$ python vendor_update.py
```

The program should then be running on localhost at port 5000. You can also run
with `flask run`.


## Todo Items

Given more time to spend working on this program, there are a number of things
I'd like to take care of.

 - Improved test coverage

 Test coverage is minimal. I'd especially like to get some tests around the
 database operations, mocking out the db to test the calls made to it. There
 also could be functional tests in the web interface.

 - Refactor database functionality

 I'd like to pull all of the database operations into their own module

 - Data verification

 The program takes the user at their word. There is no verification
 of anything, from the file to the data in it. It would be nice to validate and
 check what is being saved to a database.

 - Updates vs Create only

 The only interaction with the database is writes. I would like to have a single
 record per order, updating it if the order is cancelled or otherwise modified.
 I wouldn't want to lose data fidelity, such as original order time, so there
 would be maybe an "original order date" field. 

 - DB Primary Key

 It should key on order number, not arbitrary integer.

 - Fail well

 The program has no tolerance for failure.

 - One source of truth for db columns

 Name, address, product info, etc., are manually represented several times.
 There should be one source of truth for that information.

etc.
