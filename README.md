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