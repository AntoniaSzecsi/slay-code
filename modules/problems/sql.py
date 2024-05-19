class SQLStatements:
    ADD_INITIAL_DATA = [
        "INSERT INTO categories (name, difficulty) VALUES ('Algorithms', 1)",
        "INSERT INTO categories (name, difficulty) VALUES ('Pointers', 2)",
        "INSERT INTO categories (name, difficulty) VALUES ('Databases', 3)",
        "INSERT INTO problems (title, description, category_name) VALUES ('Join tables', 'Description 1', 'Databases')",
        "INSERT INTO problems (title, description, category_name) VALUES ('Add Two Numbers', 'Description 2', 'Algorithms')",
        "INSERT INTO problems (title, description, category_name) VALUES ('Problem 3', 'Longest Substring Without Repeating Characters', 'Pointers')",
        "INSERT INTO solutions (problem_id, example_code) VALUES (1, 'print(1)')",
        "INSERT INTO solutions (problem_id, example_code) VALUES (2, 'print(2)')",
        "INSERT INTO solutions (problem_id, example_code) VALUES (3, 'print(3)')"
    ]
    ADD_CATEGORY = "INSERT INTO categories (name, difficulty) VALUES (?, ?)"
    ADD_PROBLEM = "INSERT INTO problems (title, description, category_name) VALUES (?, ?, ?)"
    ADD_SOLUTION = "INSERT INTO solutions (problem_id, example_code) VALUES (?, ?)"
    GET_ALL_PROBLEMS_WITH_CATEGORIES = "SELECT problems.id, problems.title, problems.description, categories.name FROM problems JOIN categories ON problems.category_name = categories.name"
    GET_PROBLEMS_WITH_CATEGORIES_AND_DIFFICULTY = "SELECT problems.id, problems.title, problems.description, categories.name, categories.difficulty FROM problems JOIN categories ON problems.category_name = categories.name"
