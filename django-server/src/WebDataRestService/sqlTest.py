from sqlalchemy import *

#engine = create_engine('sqlite:///:memory:', echo=True)

￼#engine = create_engine(’mssql+pymssql://<username>:<password>@<freetds_name>?charset=utf8’, echo=True)
#engine = create_engine(’sqlite:////absolute/path/to/foo.db’)
engine = create_engine(’sqlite:////Users/apoka/JDrama1.sqlite’)
connection = engine.connect()
connection.execute(
    """

    CREATE TABLE users (

        username VARCHAR PRIMARY KEY,

        password VARCHAR NOT NULL

    );

    """
)

connection.execute(
    """

    INSERT INTO users (username, password) VALUES (?, ?);

    """,

    "foo", "bar"
)

result = connection.execute("SELECT username FROM users")

for row in result:
    print "username:", row['username']

connection.close()