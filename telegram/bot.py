import requests

class Bot:
    def __init__(self,token:str)->None:
        self.base_url = f'https://api.telegram.org/bot{token}'

    def getMe(self):
        """A simple method for testing your bot's auth token.
         Returns:
          A telegram.User instance representing that bot if the
          credentials are valid, None otherwise.
        """
        url = f'{self.base_url}/getMe'
        r = requests.get(url)
        return r.json()