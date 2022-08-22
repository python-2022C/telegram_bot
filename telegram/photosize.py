class PhotoSize:
    def __init__(self, photo: dict) -> None:
        self.file_id = photo['file_id']
        self.file_unique_id = photo['file_unique_id']
        self.width = photo['width']
        self.height = photo['height']
        self.file_size = photo.get('file_size')

    def fromDict(self) -> dict:
        '''This object represents one size of a photo or a file/sticker thumbnail.'''

        photo_dict = {
            'file_id': self.file_id,
            'file_unique_id': self.file_unique_id,
            'width': self.width,
            'height': self.height, 
        }
        if self.file_size:
            photo_dict['file_size'] = self.file_size
        
        return photo_dict