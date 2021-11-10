from .main import hello_world

def test_default_greeting():
    greeting = hello_world()
    assert greeting == "hello world"

def test_custom_greeting():
    greeting = hello_world("kbc")
    assert greeting == "hello kbc"
