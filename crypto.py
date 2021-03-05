import hashlib
import base64

def encrypt_md5(word):
  lol = hashlib.md5(word.encode())
  encrypt_md5.md5 = lol.hexdigest()
  

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
