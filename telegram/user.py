class User:
    def __init__(self,user):
        self.id = user['id']
        self.first_name=user['first_name']
        self.username = user['username']


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
    
        