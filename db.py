import sqlite3

DB_NAME = 'reddit_posts.db'

def connect_db():
    """Connect to the SQLite database."""
    return sqlite3.connect(DB_NAME)


def create_table():
    """Create the posts table if it doesn't exist."""
    create_table_sql = '''CREATE TABLE IF NOT EXISTS posts (
        id TEXT PRIMARY KEY,
        title TEXT,
        score INTEGER,
        created_at TEXT,
        saved_to TEXT);
        '''
    with connect_db() as conn:
        conn.execute(create_table_sql)
        conn.commit()
            
def insert_post(post_id, title, score, created_at, saved_to):
    '''Insert a post into the database.'''
    insert_sql = 'INSERT INTO posts (id, title, score, created_at, saved_to) VALUES (?, ?, ?, ?, ?);'
    with connect_db() as conn:
        conn.execute(insert_sql, (post_id, title, score, created_at, saved_to))
        conn.commit()
        
def duplicate_check(post_id):
    """Check if a post already exists in the database."""
    check_sql = 'SELECT COUNT(*) FROM posts WHERE id = ?;'
    with connect_db() as conn:
        cursor = conn.execute(check_sql, (post_id,))
        count = cursor.fetchone()[0]
    return count > 0

def get_all_posts():
    """Retrieve all posts from the database."""
    select_sql = 'SELECT * FROM posts;'
    with connect_db() as conn:
        cursor = conn.execute(select_sql)
        return cursor.fetchall()
    