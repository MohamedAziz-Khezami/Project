import os
import pytest
from project import revenue, expenses, delete_row, delete_file


def test_revenue(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "100")
    assert revenue() == None


def test_expenses(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "50")
    assert expenses() == None


def test_delete_row(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    file_path = "tracker.csv"
    with open(file_path, "w") as file:
        file.write("Revenues,Expenses,Type\n")
        file.write("100,50,Test\n")
    delete_row()
    with open(file_path, "r") as file:
        lines = file.readlines()
    assert len(lines) == 1


def test_delete_file(monkeypatch):
    file_path = "tracker.csv"
    with open(file_path, "w") as file:
        file.write("Revenues,Expenses,Type\n")
        file.write("100,50,Test\n")

    delete_file()
    assert not os.path.isfile(file_path)


if __name__ == "__main__":
    pytest.main()
