import httpx
 r = httpx.get('https://www.example.org/')
 r.status_code
200
 r.headers['content-type']

 r.text