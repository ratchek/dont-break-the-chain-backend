# Intro
This project is a **very** basic API for a don't break the chain calendar app.
It supports different calendars for different users.
Check "TODO" to find a list of things it does not support (including but not limited to authentication!)

# Setup

This project is managed with poetry instead of pip + venv
To set up the environment, you should have poetry installed, then run `poetry install`.
Modify `example.env` to include your database variables and rename it to `.env` (on linux)
To run the project:
```
poetry shell
python app/app.py
```

# Endpoints
Here are the exposed endpoints along with what they do:
### /user/create
Required json:
{"email": "hello@world.com", "password":"test"}
Creates a new user with given email and password.
Will check if given email already exists, but will not handle that case very graciously
(It'll just return a string telling you what happened) 

### /cal 
Required json:
{"user":"62e421e7f3db7816a31e5898"}
Returns the calendar associated with that user

### /cal/flip_date
Required json:
{"user":"62e4351b604f2666e0e1401d", "date": {"year":"2022","month":"3","day":"1"}}
Flips the given date in the user's calendar (if it existed, then will delete it and vice-versa)

### /cal/save
Required json:
{"user": "62e4351b604f2666e0e1401d", "cal": {"1993":{"01":["04","05"]}, "1994":{"03":["04"]}}}
Will save (and overwrite!) the calendar for the given user.

