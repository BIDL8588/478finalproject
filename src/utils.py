import json
import time
import os

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return result, (end - start)
    return wrapper


def validate_hash(hash_value):
    hex_chars = "0123456789abcdefghABCDEFGH"
    if any(c not in hex_chars for c in hash_value):
        return False

    valid_lengths = {32, 40, 64}
    return len(hash_value) in valid_lengths


def log_event(message, logfile="artifacts/release/logs.txt"):
    os.makedirs(os.path.dirname(logfile), exist_ok=True)

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(logfile, "a") as f:
        f.write(f"[{timestamp}] {message}\n")


def export_json(data, json_file):
    os.makedirs(os.path.dirname(json_file), exist_ok=True)

    with open(json_file, "w") as f:
        json.dump(data, f, indent=4)
