from .user import User
from .chat import Chat
class Message:
    def __init__(self, message) -> None:
        self.message_id  = message['message_id']
        self.from_user   = User(message['from'])
        self.chat        = Chat(message['chat'])

    def fromDict(self)->dict:
        '''
        Convert User object to dictionary
        Returns:
            dict: dictionary of user data
        '''
        msg_dict = {
            'message_id': self.message_id,
            'from_user': self.from_user.fromDict(),
            'caht': self.chat.fromDict()
        }
        return msg_dict

    #Override the __str__ method to print the user data
    def __str__(self):
        '''
        Print the user data
        '''
        pass
    