import hashlib

class Hasher:
    @staticmethod
    def hash_string(text: str, algo: str) -> str:
        text_bytes = text.encode('utf-8')
        if algo == 'md5':
            return hashlib.md5(text_bytes).hexdigest()
        elif algo == 'sha1':
            return hashlib.sha1(text_bytes).hexdigest()
        elif algo == 'sha256':
            return hashlib.sha256(text_bytes).hexdigest()
        else:
            raise ValueError(f"Unknown algorithm: {algo}")

    @staticmethod
    def process_file(input_path, output_path, algo="sha256"):
        results = []
        with open(input_path, 'r') as f:
            passwords = [line.strip() for line in f if line.strip()]

        with open(output_path, 'w') as f:
            for p in passwords:
                h = Hasher.hash_string(p, algo)
                f.write(f"{p},{h}\n")
                results.append((p, h))
        
        print(f"[Hasher] Processed {len(results)} passwords using {algo}")
        return results