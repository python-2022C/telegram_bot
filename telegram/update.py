
class Update:
    def __init__(self, update) -> None:
        self.base_update = update

    def fromDict(self)->dict:
        '''
        Convert User object to dictionary
        Returns:
            dict: dictionary of user data
        '''
        data = self.base_update[-1]['message']['from']
        id = data['id']
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        dicData = {
            'id':id,
            'first_name':first_name,
            'last_name':last_name,
            'username':username
            }
        return dicData



    #Override the __str__ method to print the user data
    def __str__(self):
        '''
        Print the user data
        '''
        data = self.fromDict()
        first_name = data['first_name']
        username = data['username']
        return f'First_name:{first_name},\nUsername:{username.title()}'