
class Update:
    def __init__(self, update) -> None:
        self.update_id = update.get('update_id')
        self.message = update.get('message')
        self.edited_message = update.get('edited_message')
        self.channel_post = update.get('channel_post')
        self.edited_channel_post = update.get('edited_channel_post')
        self.inline_query = update.get('inline_query')
        self.chosen_inline_result = update.get('chosen_inline_result')
        self.callback_query = update.get('callback_query')
        self.shipping_query = update.get('shipping_query')
        self.pre_checkout_query = update.get('pre_checkout_query')
        self.poll = update.get('poll')
        self.poll_answer = update.get('poll_answer')
        self.my_chat_member = update.get('my_chat_member')
        self.chat_member = update.get('chat_member')
        self.chat_join_request = update.get('chat_join_request')

    
    def fromDict(self)->dict:
        '''
        Convert User object to dictionary
        Returns:
            dict: dictionary of user data
        '''
        data = {
            'update_id':self.update_id, 
            'message':self.message,
            'edited_message':self.edited_message, 
            'channel_post':self.channel_post, 
            'edited_channel_post':self.edited_channel_post, 
            'inline_query':self.inline_query, 
            'chosen_inline_result':self.chosen_inline_result, 
            'callback_query':self.callback_query, 
            'shipping_query':self.shipping_query, 
            'pre_checkout_query':self.pre_checkout_query, 
            'poll':self.poll, 
            'poll_answer':self.poll_answer, 
            'my_chat_member':self.my_chat_member, 
            'chat_member':self.chat_member, 
            'chat_join_request':self.chat_join_request
        }
        Dict2 = {}
        for a,b in data.items():
            if b != None:
                Dict2[a] = b
        return Dict2

    #Override the __str__ method to print the user data
    def __str__(self):
        '''
        Print the user data
        '''
        pass
    