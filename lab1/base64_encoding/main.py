import base64_encoding
from sys import argv

try:
    base64_encoding.base64_encode(argv[1], argv[2])
except Exception as e:
    print(e)