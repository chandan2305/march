from pytest_class import studentDB:
import pytest



def test_scott_data():
    db = studentDB()
    db.connect('data.json')
    scott_data=db.get_data