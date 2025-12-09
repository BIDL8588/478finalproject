from src.generator import PasswordGenerator

def test_gen_weak_password_properties():
    gen = PasswordGenerator()
    # Accessing internal method for testing purposes
    password = gen._gen_weak()
    assert password.islower()
    assert 4 <= len(password) <= 8