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
app/api/api.py                        8      0   100%
app/api/deps.py                      30      6    80%
app/api/endpoints/fuel_quote.py      40      3    92%
app/api/endpoints/profile.py         19      1    95%
app/api/endpoints/users.py           39      0   100%
app/app.py                            6      0   100%
app/database.py                       9      1    89%
app/models.py                        26      0   100%
app/schemas.py                       46      0   100%
tests/__init__.py                     0      0   100%
tests/conftest.py                    30      0   100%
tests/test_fuelquote.py              62      0   100%
tests/test_profile.py                21      0   100%
tests/test_users.py                  80      0   100%
-----------------------------------------------------
TOTAL                               416     11    97%
```