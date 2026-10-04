import sqlite3

PRODUCTS = [
    (1, "Rice"),
    (2, "Milk"),
    (3, "Coffee"),
    (4, "Bread"),
    (5, "Pasta"),
]


def create_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
    conn.executemany("INSERT INTO products (id, name) VALUES (?, ?)", PRODUCTS)
    conn.commit()
    return conn
