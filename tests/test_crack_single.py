from src.cracker import Cracker
from src.hasher import Hasher

def test_dictionary_crack_success():
    password = "admin5"
    algo = "sha256"
    target_hash = Hasher.hash_string(password, algo)
    
    cracker = Cracker()
    # Ensure password is in the dictionary for the test
    cracker.dictionary.add(password)
    
    result = cracker.dictionary_attack(target_hash, algo)
    assert result == password