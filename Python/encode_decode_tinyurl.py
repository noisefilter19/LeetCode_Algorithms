import base64

# link: https://leetcode.com/problems/encode-and-decode-tinyurl/

class Codec:
    
    def __init__(self):
        self.urls = {}
        self.URL_BASE = "http://tinyurl.com/"
        
        
    def encode(self, longUrl):
        urlEnc = longUrl.encode('ascii')
        url64Enc = base64.b64encode(urlEnc)
        url64Dec = url64Enc.decode('ascii')
        self.urls[url64Dec] = longUrl
        return self.URL_BASE + url64Dec
        

    def decode(self, shortUrl: str) -> str:
        urlSplited = shortUrl.split('/', 3)
        urlDecoded = self.urls[urlSplited[-1]]
        return urlDecoded
