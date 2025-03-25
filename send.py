import requests
import hmac
import hashlib
import time
import struct

from requests.auth import HTTPBasicAuth

def HOTP(K, C, digits=10):
    """HTOP:
    K is the shared key
    C is the counter value
    digits control the response length
    """
    K_bytes = str.encode(K)
    C_bytes = struct.pack(">Q", C)
    hmac_sha512 = hmac.new(key = K_bytes, msg=C_bytes, digestmod=hashlib.sha512).hexdigest()
    return Truncate(hmac_sha512)[-digits:]

def Truncate(hmac_sha512):
    """truncate sha512 value"""
    offset = int(hmac_sha512[-1], 16)
    binary = int(hmac_sha512[(offset *2):((offset*2)+8)], 16) & 0x7FFFFFFF
    return str(binary)

def TOTP(K, digits=10, timeref = 0, timestep = 30):
    """TOTP, time-based variant of HOTP
    digits control the response length
    the C in HOTP is replaced by ( (currentTime - timeref) / timestep )
    """
    C = int ( time.time() - timeref ) // timestep
    return HOTP(K, C, digits = digits)


URL = "https://api.challenge.hennge.com/challenges/003"

body = {
  "github_url": "https://gist.github.com/MichaelPells/dc6a80a309a866999c259645cfec65ce",
  "contact_email": "themichaelpells@gmail.com",
  "solution_language": "python"
}

userid = "themichaelpells@gmail.com"

secret = f"{userid}HENNGECHALLENGE003"
T0 = 0
timestep = 30

password = TOTP(secret, 10, T0, timestep).zfill(10)
print(password)

# response = requests.post(URL,
#               json = body,
#               auth = HTTPBasicAuth(userid, password)
#               )

# print(response.status_code)
# print(response.json())
