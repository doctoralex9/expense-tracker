import sqlite3

# Function to create a new SQLite database
def create_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('my_database.db')
    # Create a cursor object to execute SQLite commands
    cursor = conn.cursor()
    
    # Create a new table called 'users' with two columns: 'id' and 'name'
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, name TEXT)''')
    
    # Create a new table called 'categories' with two columns: 'id' and 'name'
    cursor.execute('''CREATE TABLE IF NOT EXISTS categories
                      (id INTEGER PRIMARY KEY, name TEXT)''')
    
    # Create a new table called 'expenses' with three columns: 'id', 'user_id' (foreign key), 'category_id' (foreign key), and 'amount'
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses
                      (id INTEGER PRIMARY KEY, user_id INTEGER, category_id INTEGER, amount REAL,
                      FOREIGN KEY(user_id) REFERENCES users(id),
                      FOREIGN KEY(category_id) REFERENCES categories(id))''')
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Function to add a new user to the database
def add_user(name):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    
    # Insert a new row into the 'users' table with the given name
    cursor.execute('''INSERT INTO users (name) VALUES (?)''', (name,))
    
    conn.commit()
    conn.close()

# Function to add a new category to the database
def add_category(name):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    
    # Insert a new row into the 'categories' table with the given name
    cursor.execute('''INSERT INTO categories (name) VALUES (?)''', (name,))
    
    conn.commit()
    conn.close()

# Function to add a new expense to the database
def add_expense(user_id, category_id, amount):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    
    # Insert a new row into the 'expenses' table with the given user_id, category_id, and amount
    cursor.execute('''INSERT INTO expenses (user_id, category_id, amount) VALUES (?, ?, ?)''', (user_id, category_id, amount))
    
    conn.commit()
    conn.close()

# Function to retrieve all expenses for all users
def get_all_expenses():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    
    # Select all expenses for all users
    cursor.execute('''SELECT users.name, categories.name, expenses.amount
                      FROM expenses
                      INNER JOIN users ON expenses.user_id = users.id
                      INNER JOIN categories ON expenses.category_id = categories.id''')
    expenses = cursor.fetchall()
    
    conn.close()
    
    return expenses

# Main function to demonstrate the usage of the database functions
def main():
    create_database()
    
    # Add some users to the database
    add_user('Alice')
    add_user('Bob')
    add_user('Charlie')
    add_user('Tom')
    add_user('Kate')
    add_user('Maria')
    add_user('Stefanos')
    
    # Add some categories to the database
    add_category('Food')
    add_category('Transportation')
    add_category('Entertainment')
    
    # Add some expenses to the database
    add_expense(1, 1, 20.50)  # Alice spends $20.50 on Food
    add_expense(1, 2, 15.75)  # Alice spends $15.75 on Transportation
    add_expense(2, 1, 30.00)  # Bob spends $30.00 on Food
    add_expense(3, 3, 50.25)  # Charlie spends $50.25 on Entertainment
    add_expense(4, 1, 40.00)  # Tom spends $40.00 on Food
    add_expense(5, 2, 25.50)  # Kate spends $25.50 on Transportation
    add_expense(6, 1, 35.75)  # Maria spends $35.75 on Food
    add_expense(7, 3, 60.00)  # Stefanos spends $60.00 on Entertainment
    
    # Retrieve and print all expenses for all users
    all_expenses = get_all_expenses()
    print("All Expenses:")
    for expense in all_expenses:
        print(expense)

if __name__ == "__main__":
    main()