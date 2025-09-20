import requests

url = "http://example.com"  # Replace with your application URL

try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Application is UP! Status code: {response.status_code}")
    else:
        print(f"Application is DOWN! Status code: {response.status_code}")
except Exception as e:
    print(f"Application is DOWN! Error: {e}")

