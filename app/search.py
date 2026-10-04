import sqlite3


def search_products(conn: sqlite3.Connection, term: str) -> list[tuple[int, str]]:
    """Return products whose names contain term, ordered by id."""
    query = "SELECT id, name FROM products WHERE name LIKE ? ORDER BY id"
    return conn.execute(query, (f"%{term}%",)).fetchall()
