#!/usr/bin/python3
"""script that takes in a URL, sends a request to the
URL and displays the value of the X-Request-Id variable
found in the header of the response."""


if __name__ == "__main__":
    import urllib.request
    import sys
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        html = response.headers
        data = html.get('X-Request-Id')
        print(data)
