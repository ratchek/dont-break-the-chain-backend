# Intro
This project is a **very** basic API for a don't break the chain calendar app.  
It supports getting and saving different calendars for different users.  
Check "TODO" to find a list of things it does not support (including, but not limited to user authentication!)  

# Setup
## Environment
This project is managed with poetry instead of pip + venv  
The easiest way to set up the enviroment is to install poetry. Check out the documentation here:
https://python-poetry.org/docs/

Once you have poetry installed on your system, open a terminal in the project directory and run `poetry install`. 

## Database
This project uses mongodb as a database. You need to sign up for a (free) account. Once that is done, you should set up a project and get a connection string from the website.  
Modify `example.env` to include your database variables and connection string (make sure to switch out the password).Then rename the file to `.env` (on linux) 

## Running
To run the project:
```
poetry shell
python app/app.py
```

# Endpoints
Here are the exposed endpoints along with what they do:
### /user/create
Required json:
`{"email": "hello@world.com", "password":"test"}`  
Creates a new user with given email and password.  
Will check if given email already exists, but will not handle that case very graciously
(It'll just return a string telling you what happened) 

### /cal 
Required json:
`{"user":"62e421e7f3db7816a31e5898"}`  
Returns the calendar associated with that user

### /cal/flip_date
Required json:
`{"user":"62e4351b604f2666e0e1401d", "date": {"year":"2022","month":"3","day":"1"}}`  
Flips the given date in the user's calendar (if it existed, then will delete it and vice-versa)

### /cal/save
Required json:
`{"user": "62e4351b604f2666e0e1401d", "cal": {"1993":{"01":["04","05"]}, "1994":{"03":["04"]}}}`  
Will save (and overwrite!) the calendar for the given user.

