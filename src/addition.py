# app.py
# This is a test commit
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert sub(10, 5) == 5
    assert sub(15, 5) == 10


test_add()

print("Hello World")
