import json
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
        if len(self.base_message) > 0:
            data_messag = self.base_message[-1]['message']['from']
        data = {
            'id':data_messag.get('id'),
            'last_name':data_messag.get('last_name'),
            'first_name':data_messag.get('first_name'),
            'username':data_messag.get('username'),
            'is_bot':data_messag.get('is_bot'),
            "language_code":data_messag.get('language_code'),
            'is_premium':data_messag.get('is_premium'),
            'added_to_attachment_menu':data_messag.get('added_to_attachment_menu'),
            'can_join_groups':data_messag.get('can_join_groups'),
            'can_read_all_group_messages':data_messag.get('can_read_all_group_messages'),
            'supports_inline_queries':data_messag.get('supports_inline_queries'),
        }
        
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
        return json.dumps(self.fromDict())
