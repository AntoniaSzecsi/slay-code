import sqlite3

DATABASE_NAME = "database.db"

def init_db():
    with sqlite3.connect(DATABASE_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                name TEXT PRIMARY KEY,
                difficulty INTEGER NOT NULL
            );
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS problems (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                category_name TEXT,
                FOREIGN KEY (category_name) REFERENCES categories(name)
            );
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS solutions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                problem_id INTEGER NOT NULL,
                example_code TEXT NOT NULL,
                FOREIGN KEY (problem_id) REFERENCES problems(id)
            );
        ''')

def add_category(name, difficulty):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO categories (name, difficulty) VALUES (?, ?)", (name, difficulty))
        conn.commit()

def add_problem(title, description, category_name):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO problems (title, description, category_name) VALUES (?, ?, ?)",
                       (title, description, category_name))
        conn.commit()

def add_solution(problem_id, example_code):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO solutions (problem_id, example_code) VALUES (?, ?)", (problem_id, example_code))
        conn.commit()
