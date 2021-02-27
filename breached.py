import requests


word = 'However, someone else could have signed up using your email address. Read the explanation below.'
word2 = 'Oh no! Your email address has been leaked'

def check(email):
        url = 'https://ashley.cynic.al/'
        payload = {'email': email}

        x = requests.post(url, data = payload)
        check.breached = word in x.text

        url2 = 'https://check.cybernews.com/chk/'
        payload2 = {'e': email, 'lang': 'en_US'}

        z = requests.post(url2, data = payload2)
        check.breached2 = word2 in z.text
