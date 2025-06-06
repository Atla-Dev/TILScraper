import sqlite3

database='reddit_posts.db'
create_table='CREATE_TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, title TEXT, score INTEGER, created_at TEXT);'


try:
    with sqlite3.connect(database) as conn:
        print(f"Connected to the database successfully with version {sqlite3.sqlite_version}.")
        try:
            cursor= conn.cursor()
        
            # You can execute queries here using cursor
            # Example: cursor.execute("SELECT sqlite_version();")
        
            cursor.execute(create_table)
            conn.commit()
            print("Table created successfully or already exists.")
        except sqlite3.Error as e:
            print(f"An error occurred while creating the table: {e}")
                
except sqlite3.Error as e:
    print(f"An error occurred while connecting to the database: {e}")
