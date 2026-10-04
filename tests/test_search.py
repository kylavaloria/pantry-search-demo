from app.db import create_connection
from app.search import search_products


def test_search_finds_matching_product():
    conn = create_connection()
    assert search_products(conn, "Coffee") == [(3, "Coffee")]


def test_search_is_case_insensitive_for_ascii():
    conn = create_connection()
    assert search_products(conn, "milk") == [(2, "Milk")]


def test_search_treats_sql_control_characters_as_data():
    conn = create_connection()
    assert search_products(conn, "' OR 1=1 --") == []
