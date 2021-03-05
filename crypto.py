import hashlib
import base64

def encrypt_md5(word):
  encrypt.md5 = hashlib.md5(word.encode())
  

def encode_base64(word):
  la = word.encode("ascii")
  la2 = base64.b64encode(la)
  la3 = la2.decode("ascii")
  encode_base64.result = la3
  
def decode_base64(word):
  la = word.encode("ascii")
  la2 = base64.b64decode(la)
  la3 = la2.decode("ascii")
  decode_base64.result = la3
