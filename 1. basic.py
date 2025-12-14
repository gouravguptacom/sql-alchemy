from sqlalchemy import create_engine, text

# helps us to connect to db
engine = create_engine('sqlite:///mydatabase.db', echo=True)

conn = engine.connect()

conn.execute(text("CREATE TABLE IF NOT EXISTS people (name str, age int)"))

conn.commit()

from sqlalchemy.orm import Session

session = Session(engine)

session.execute(text('INSERT INTO people (name, age) VALUES ("Gaurav", 28);'))

session.commit()

# [Shell]
# sqlite3 ./mydatabase.db
# sqlite> .tables
# sqlite> PRAGMA table_info(people);
# sqlite> SELECT * FROM people