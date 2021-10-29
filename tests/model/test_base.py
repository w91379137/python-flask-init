
# pytest -s tests/model/test_base.py

from flask import Flask
from asabulu.model.base import execute_raw_sql

def test_execute_raw_sql(app: Flask, db):

    with app.app_context():

        value = 'test_test'
        count = 9487

        result = execute_raw_sql(f"INSERT INTO text ('value', 'count')  VALUES ('{value}', {count});")
        # print(result)

        result = execute_raw_sql("select * from text").fetchall()
        # print(result)

        assert len(result) == 1
        first = result[0]
        # print(first)

        assert first[0] == 1
        assert first[1] == value
        assert first[2] == count
