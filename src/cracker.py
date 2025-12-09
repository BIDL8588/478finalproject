import itertools
import string
import time
from src.hasher import Hasher

class Cracker:
    def __init__(self):
        # Internal dictionary for the demo
        self.dictionary = set([
            "attack12", "star22", "cool12", "doggy7", "tiger5", "lover1",
            "sunny8", "red123", "blue44", "catcat", "qwer12", "zxcv55",
            "pass12", "test11", "hello7", "mine3", "key123", "admin5"
        ])

    def dictionary_attack(self, target_hash, algo):
        for word in self.dictionary:
            if Hasher.hash_string(word, algo) == target_hash:
                return word
        return None

    def brute_force_attack(self, target_hash, algo, max_len=4, timeout=1.0):
        chars = string.ascii_lowercase + string.digits
        start_time = time.time()

        for length in range(1, max_len + 1):
            for attempt in itertools.product(chars, repeat=length):
                if time.time() - start_time > timeout:
                    return None  # Timeout
                
                word = "".join(attempt)
                if Hasher.hash_string(word, algo) == target_hash:
                    return word
        return None