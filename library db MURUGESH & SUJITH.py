# Establishing the connection to the database
import pymysql
connection=pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='library_db'
)

cursor = connection.cursor()

# Function to add book information
def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")
    query = "INSERT INTO books (book_id, title, author) VALUES (%s, %s, %s)"
    cursor.execute(query, (book_id, title, author))
    connection.commit()
    print("Book added successfully!")

# Function to display book information
def display_books():
    query = "SELECT * FROM books"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(f"Book ID: {row[0]}, Title: {row[1]}, Author: {row[2]}")

# Function to list all books of a given author
def list_books_by_author():
    author = input("Enter Author Name: ")
    query = "SELECT * FROM books WHERE author = %s"
    cursor.execute(query, (author,))
    for row in cursor.fetchall():
        print(f"Book ID: {row[0]}, Title: {row[1]}, Author: {row[2]}")

# Function to count the number of books in the library
def count_books():
    query = "SELECT COUNT(*) FROM books"
    cursor.execute(query)
    count = cursor.fetchone()[0]
    print(f"Total number of books: {count}")

# Main menu
def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add book information")
        print("2. Display book information")
        print("3. List all books of a given author")
        print("4. Count the number of books in the library")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            display_books()
        elif choice == '3':
            list_books_by_author()
        elif choice == '4':
            count_books()
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

# Closing the connection
connection.close()
