import requests
import os
from dotenv import load_dotenv

import base64
load_dotenv()  # take environment variables from .env.

def login_to_get_athu_key():

    url = os.environ["url"]

    # Create a session with the required authentication credentials
    session = requests.Session()

    username = os.environ["username"]
    password = os.environ.get("password")
    tenant_id = os.environ.get("tenantid")

    combined_string = username + ':' + password + ':' + tenant_id
    encoded = base64.b64encode(combined_string.encode()).decode()

    authorization_header = 'Basic ' + encoded
    try:
        headers_val = {
            'Authorization': authorization_header
        }

        print('headersVal', headers_val)
        # Make an HTTP POST request
        response = session.post(url, headers=headers_val)  # Use headers=headers as named argument

        # Check if the request was successful (status code 200)
        if response.status_code == 201:
            data = response.json()
            automated_report(data[0]['access_token'])
        else:
            print("HTTP request failed json:", response.json())
            print("HTTP request failed with status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)


def automated_report(access_token):

    automated_mail_url = os.environ.get("automated_mail_url")
    session = requests.Session()

    try:
        headersVal = {
            'authorization': 'Bearer ' + access_token
        }

        print('headersVal', headersVal)
        print('automatedMailUrl', automated_mail_url)

        # Make an HTTP GET request
        response = session.get(automated_mail_url, headers=headersVal)  # Use headers=headers as named argument

        print('Automated_Mail_Response_json', response.json())
        # Check if the request was successful (status code 200)
        if response.status_code == 201:
            print("Success on Triggered automated mail for : - ",  os.environ.get("tenantid"))
        else:
            print("automated_report request failed with status code:", response.json())
            print("automated_report request failed with status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("An error occurred in automated_report:", e)


if __name__ == "__main__":
    login_to_get_athu_key()

