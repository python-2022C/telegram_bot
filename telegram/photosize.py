class PhotoSize:
    def __init__(self, photo: dict) -> None:
        self.file_id = photo['file_id']
        self.file_unique_id = photo['file_unique_id']
        self.width = photo['width']
        self.height = photo['height']
        self.file_size = photo.get('file_size')

    