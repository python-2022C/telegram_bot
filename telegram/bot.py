from typing import Dict
import requests

class Bot:
    def __init__(self,token:str)->Dict:
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


    def sendMessage(self,chat_id,text):
        """Use this method to send text messages.
        Args:
          chat_id:
            Unique identifier for the message recipient — telegram.User or
            telegram.GroupChat id.
          text:
            Text of the message to be sent.
        Returns:
          A telegram.Message instance representing the message posted.
        """
        payload = {
            'chat_id': chat_id,
            'text': text
        }

        url = f'{self.base_url}/sendMessage'
        r = requests.post(url, payload)

        
    def getUpdates(self):
        """Use this method to receive incoming updates using long polling.
        Args:
            
        Returns:
          A  telegram.Update object is returned.
        """
        url = f'{self.base_url}/getUpdates'
        answer = requests.get(url)
        data = answer.json()
        # Get result form data
        result = data['result']    
    
        return result