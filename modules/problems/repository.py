import sqlite3
from .utils import get_difficulty_level
from .sql import SQLStatements

DATABASE_NAME = "database.db"

def add_initial_data():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        for statement in SQLStatements.ADD_INITIAL_DATA:
            cursor.execute(statement)
        conn.commit()

def add_category(name, difficulty):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(SQLStatements.ADD_CATEGORY, (name, difficulty))
        conn.commit()

def add_problem(title, description, category_name):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(SQLStatements.ADD_PROBLEM, (title, description, category_name))
        conn.commit()

def add_solution(problem_id, example_code):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(SQLStatements.ADD_SOLUTION, (problem_id, example_code))
        conn.commit()

def get_all_problems_with_categories():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(SQLStatements.GET_ALL_PROBLEMS_WITH_CATEGORIES)
        problems = [{
            'id': row[0],
            'name': row[1],
            'description': row[2],
            'category': row[3]
        } for row in cursor.fetchall()]
        return problems

def get_problems_with_categories_and_difficulty():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(SQLStatements.GET_PROBLEMS_WITH_CATEGORIES_AND_DIFFICULTY)
        problems = [{
            'id': row[0],
            'name': row[1],
            'description': row[2],
            'category': row[3],
            'difficulty': get_difficulty_level(row[4])
        } for row in cursor.fetchall()]
        return problems
