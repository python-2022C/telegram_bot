class User:
    def __init__(self,user):
        self.id = user['id']
        self.is_bot = user['is_bot']
        self.first_name=user['first_name']
        if user['last_name']:
            self.last_name = user['last_name']
        self.username = user['username']
        if user['language_code']:
            self.language_code = user['language_code']
        if user['is_premium']:
            self.is_premium = user['is_premium']
        if user['added_to_attachment_menu']:
            self.added_to_attachment_menu = user['added_to_attachment_menu']
        if user['can_join_groups']:
            self.can_join_groups = user['can_join_groups']
        if user['can_read_all_group_messages']:
            self.can_read_all_group_messages = user['can_read_all_group_messages']
        if user['supports_inline_queries']:
            self.supports_inline_queries = user['supports_inline_queries']
        


    def fromDict(self)->dict:
        '''
        Convert User object to dictionary
        Returns:
            dict: dictionary of user data
        '''
        pass 

    #Override the __str__ method to print the user data
    def __str__(self):
        '''
        Print the user data
        '''
        pass
    
        