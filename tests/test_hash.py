from src.hasher import Hasher
import hashlib

def test_pass_sha256():
    password = "hello"
    expected_val = hashlib.sha256(password.encode()).hexdigest()
    assert Hasher.hash_string(password, "sha256") == expected_val

def test_hash_pass_not_plaintext():
    assert Hasher.hash_string("hello", "sha256") != "hello"