#!/usr/bin/python3
""" Python script that takes in a URL and an email,
sends a POST request to the passed URL with the
email as a parameter, and displays the response (decoded in utf-8)"""


if __name__ == "__main__":
    import urllib.request
    import sys
    import urllib.parse
    url = sys.argv[1]
    email = sys.argv[2]
    # Encode the email parameter
    email_param = urllib.parse.urlencode({'email': email})
    # Create the full URL with the email parameter
    full_url = url + '?' + email_param
    # Open the URL with the POST method
    with urllib.request.urlopen(full_url) as response:
        # Read the response data
        response_data = response.read()
        # Decode the response data in UTF-8
        decoded_response = response_data.decode('utf-8')
        # Print the decoded response
        print(decoded_response)
