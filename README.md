Database:
    To get the database installed go to [the postgress website](https://www.postgresql.org/download/)

    Make sure to run this in the top level folder.
    `pg_ctl -D ./db_data -l db_logs start` to start
    `pg_ctl -D ./db_data stop` to stop

Backend:
    `cd backend`
    `pip install -r requirements.txt`
    `python main.py`

Frontend:
    `cd frontend`
    `npm install`
    `npm start`