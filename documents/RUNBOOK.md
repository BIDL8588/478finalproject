Runbook (with rebuild/run instructions):
First download the following files into your downloads:
- crack_hash.py
- dictionary.txt
- gen_pass.py
- hash_password.py
- results.py

RUN:
1. cd downloads

2. python gen_pass.py 
(EXPECTED OUTPUT): 
Saved 100 passwords to data/raw_passwords.txt
Added common weak passwords to the file

3. python hash_password.py
(EXPECTED OUTPUT):
Usage: python hash_password.py <mode> <algorithm>
Modes: raw, dict
Algorithms: md5, sha1, sha256

4. python hash_password.py raw sha256
(EXPECTED OUTPUT):
Hashed 140 passwords -> data/hashed_raw.txt
Algorithm used -> sha256

5. python hash_password.py dict sha256
(EXPECTED OUTPUT):
Hashed 97 passwords -> data/hashed_dictionary.txt
Algorithm used -> sha256

6. crack_hash.py
(EXPECTED OUTPUT):
Usage:
  python crack_hash.py dict
  python crack_hash.py brute
  python crack_hash.py both

7. python crack_hash.py both
(EXPECTED OUTPUT):
Cracked Results saved to: data/cracked_raw_results.txt
Cracked Results saved to: data/cracked_dictionary_results.txt

8. python results.py
(EXPECTED OUTPUT):
Usage:
  python results.py raw dict
  python results.py raw brute
  python results.py raw both
  python results.py dict dict
  python results.py dict brute
  python results.py dict both

9. python results.py raw dict
(EXPECTED OUTPUT):
[OK] Saved JSON analysis -> results_raw_dict.json

10. python results.py dict dict
(EXPECTED OUTPUT):
[OK] Saved JSON analysis -> results_dictionary_dict.json

11. python results.py raw brute
(EXPECTED OUTPUT):
[OK] Saved JSON analysis -> results_raw_brute.json

12. python results.py dict brute
(EXPECTED OUTPUT):
[OK] Saved JSON analysis -> results_dictionary_brute.json



