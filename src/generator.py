import random
import string
import os

class PasswordGenerator:
    def __init__(self):
        self.common_passwords = [
            "attack12", "star22", "cool12", "doggy7", "tiger5", "lover1",
            "sunny8", "red123", "blue44", "catcat", "qwer12", "zxcv55",
            "pass12", "test11", "hello7", "mine3", "key123", "admin5"
        ]

    def _gen_weak(self):
        length = random.randint(4, 8)
        return "".join(random.choices(string.ascii_lowercase, k=length))

    def _gen_medium(self):
        chars = string.ascii_lowercase + string.digits
        length = random.randint(8, 12)
        return "".join(random.choices(chars, k=length))

    def _gen_strong(self):
        chars = string.ascii_letters + string.digits + "!@#$%^&*?"
        length = random.randint(12, 16)
        return "".join(random.choices(chars, k=length))

    def generate_dataset(self, count=100) -> list:
        dataset = []
        for _ in range(count):
            difficulty = random.choice(["weak", "medium", "strong"])
            if difficulty == "weak":
                dataset.append(self._gen_weak())
            elif difficulty == "medium":
                dataset.append(self._gen_medium())
            else:
                dataset.append(self._gen_strong())
        
        dataset.extend(self.common_passwords)
        return dataset

    def save_to_file(self, passwords, filepath="data/raw_passwords.txt"):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as f:
            for p in passwords:
                f.write(p + "\n")
        print(f"[Generator] Saved {len(passwords)} passwords to {filepath}")