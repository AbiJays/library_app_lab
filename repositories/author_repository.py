from db.run_sql import run_sql

from models.author import Author


def save(author):
    sql = """
    INSERT INTO authors (first_name, last_name)
    VALUES (%s, %s)
    RETURNING id
    """
    values = [
        author.first_name,
        author.last_name
        ]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

def select_all():
    authors = []
    sql = "SELECT * FROM authors"
    results = run_sql(sql)
    for row in results:
        author = Author(row['first_name'], row['last_name'], row['id'])
        authors.append(author)
    return authors

# def select(id):
#     sql = "SELECT * FROM authors WHERE id = %s"
#     values = [id]
#     row = run_sql(sql, values)[0]
#     if row is not None:
#         author = Author(
#             row['first_name'],
#             row['last_name'],
#             row['id']
#         )
#     return author

# def delete_all():
#     sql = "DELETE FROM authors"
#     run_sql(sql)
