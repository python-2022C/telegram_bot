class User:
    def __init__(self,user):
        self.id = user['id']
        self.first_name=user['first_name']
        self.username = user['username']