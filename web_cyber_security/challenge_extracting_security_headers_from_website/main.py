import requests

def get_security_headers(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Get the headers from the response
        headers = response.headers

        # Extract Content-Security-Policy (CSP) header
        csp_header = headers.get('Content-Security-Policy', 'CSP header not found')

        # Extract Strict-Transport-Security (HSTS) header
        hsts_header = headers.get('Strict-Transport-Security', 'HSTS header not found')

        return {
            'CSP': csp_header, 'HSTS': hsts_header
        }

    except requests.exceptions.RequestException as e:
        return f'Error: {e}'

# Example usage:
url_to_check = 'https://www.kaggle.com'
security_headers = get_security_headers(url_to_check)

# Print the extracted headers
print(f'CSP Header: {security_headers["CSP"]}')
print(f'HSTS Header: {security_headers["HSTS"]}')