import sqlite3


def search_products(conn: sqlite3.Connection, term: str) -> list[tuple[int, str]]:
    """Return products whose names contain term, ordered by id."""
    query = f"SELECT id, name FROM products WHERE name LIKE '%{term}%' ORDER BY id"
    return conn.execute(query).fetchall()
