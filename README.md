Database:
    To get the database installed go to [the postgress website](https://www.postgresql.org/download/).
    Then, to initialize you need to run the following in the top level folder.
    
    pg_ctl -D db_data -l db_logs init
    
    You only need to do the above once.

    Finally, make sure to run this in the top level folder.
    `pg_ctl -D ./db_data -l db_logs start` to start
    `pg_ctl -D ./db_data stop` to stop

    Now, to run migrations once the database has started:
    `cd backend`
    `alembic upgrade head`

Backend:
    `cd backend`
    `pip install -r requirements.txt`
    `python main.py`

Frontend:
    `cd frontend`
    `npm install`
    `npm start`

Tests:
    `cd backend`
    `pytest`

Test Code Coverage:
    `cd backend`
    `coverage run -m pytest`
    `coverage report`

Current code coverage:
```
Name                                     Stmts   Miss  Cover
------------------------------------------------------------
backend/app/__init__.py                      0      0   100%
backend/app/api/__init__.py                  0      0   100%
backend/app/api/api.py                       8      0   100%
backend/app/api/deps.py                      7      4    43%
backend/app/api/endpoints/__init__.py        0      0   100%
backend/app/api/endpoints/fuelquote.py      21      9    57%
backend/app/api/endpoints/profile.py        30     18    40%
backend/app/api/endpoints/users.py          42     10    76%
backend/app/app.py                           6      0   100%
backend/app/database.py                      9      1    89%
backend/app/models.py                       25      0   100%
backend/app/schemas.py                      47      3    94%
backend/tests/__init__.py                    0      0   100%
backend/tests/conftest.py                   30      0   100%
backend/tests/test_profile.py                0      0   100%
backend/tests/test_users.py                 32      0   100%
------------------------------------------------------------
TOTAL                                      257     45    82%
```