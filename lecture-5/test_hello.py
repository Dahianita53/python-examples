# estos ejemplos se corren con python3 -m pytest test_hello.py

#1
from hello import hello

def test_hello():
    hello("Carol") == "hello, Carol"

#2 
from hello import hello

def test_hello():
    assert hello("Carol") == "hello, Carol"

#3
from hello import hello

def test_hello():
    assert hello("Carol") == "hello, Carol"
    assert hello() == "hello, world"

#4
from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("Carol") == "hello, Carol"
