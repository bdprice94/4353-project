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

Backend formatting:
    `python -m black ./`

Frontend:
    `cd frontend`
    `npm install`
    `npm start`

Frontend formatting:
    `npx prettier . --write`

Tests:
    `cd backend`
    `pytest`

Test Code Coverage:
    `cd backend`
    `coverage run -m pytest`
    `coverage report`

Current code coverage:
```
Name                              Stmts   Miss  Cover
-----------------------------------------------------
app/__init__.py                       0      0   100%
app/api/__init__.py                   0      0   100%
app/api/api.py                        8      0   100%
app/api/deps.py                      28      5    82%
app/api/endpoints/__init__.py         0      0   100%
app/api/endpoints/fuel_quote.py      17      0   100%
app/api/endpoints/profile.py         20      1    95%
app/api/endpoints/users.py           44     10    77%
app/app.py                            6      0   100%
app/database.py                       9      1    89%
app/models.py                        26      0   100%
app/schemas.py                       45      3    93%
tests/__init__.py                     0      0   100%
tests/conftest.py                    30      0   100%
tests/test_fuelquote.py              34      0   100%
tests/test_profile.py                21      0   100%
tests/test_users.py                  32      0   100%
-----------------------------------------------------
TOTAL                               320     20    94%
```