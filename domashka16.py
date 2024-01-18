import requests

try:
    resp = requests.request('GET', 'https://www.python.org')
    print(resp.status_code)
except Exception as e:
    print(f"Error {e}")
else:
    print(f' Response - {resp.headers}')
    data = resp.content
    con_t = resp.headers['Content-Type']
    print(con_t)

    if resp.status_code == 200 and 'text/html; charset=utf-8' in con_t:
        print('Content-Type is text/html and charset=utf-8')
        with open('index.html', 'wb') as f:
            f.write(data)
        print('Data was saved to index.html')
    else: print('Unecspected Content-Type or Status code')

