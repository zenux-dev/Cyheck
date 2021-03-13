import requests

def check_token(token):
    response = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})
    check_token.result = response.status_code
