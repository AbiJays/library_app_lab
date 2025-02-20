from db.run_sql import run_sql

from models.book import Book
import repositories.author_repository as author_repository

def save(book):
    sql = """
    INSERT INTO books (title, author_id)
    VALUES (%s, %s)
    RETURNING id
    """
    values = [book.title, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row["author_id"])
        book = Book(row['title'], author, row['id'])
        books.append(book)
    return books

def select(id):
    book = None
    sql = """
    SELECT * FROM books
    WHERE id = %s
    """
    values = [id]
    row = run_sql(sql, values)[0]

    if row is not None:
        author = author_repository.select(row['author_id'])
        book = Book(
            row['title'],
            author,
            row['id']
            )
    return book

def delete(id):
    sql = """
    DELETE FROM books
    WHERE id = %s
    """
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = """DELETE FROM books"""
    run_sql(sql)

def update(book):
    book = None
    sql = """
    UPDATE books
    SET (title, author_id) = (%s, %s)
    WHERE id = %s
    """
    values = [book.title, book.author.id, book.id]
    run_sql(sql, values)
