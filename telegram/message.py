
class Message:
    def __init__(self, message) -> None:
        self.message_id = message.get('message_id')
        self.from = message.get('from')
        self.sender_chat = message.get('sender_chat')
        self.date = message.get('date')
        self.chat = message.get('chat')
        self.forward_from = message.get('forward_from')
        self.forward_from_chat = message.get('forward_from_chat')
        self.forward_from_message_id = message.get('forward_from_message_id')
        self.forward_signature = message.get('forward_signature')
        self.forward_sender_name = message.get('forward_sender_name')
        self.forward_date = message.get('forward_date')
        self.is_automatic_forward = message.get('is_automatic_forward')
        self.reply_to_message = message.get('reply_to_message')
        self.via_bot = message.get('via_bot')
        self.edit_date = message.get('edit_date')
        self.has_protected_content = message.get('has_protected_content')
        self.media_group_id = message.get('media_group_id')
        self.author_signature = message.get('author_signature')
        self.text = message.get('text')
        self.entities = message.get('entities')
        self.animation = message.get('animation')
        self.audio = message.get('audio')
        self.document = message.get('document')
        self.photo = message.get('photo')
        self.sticker = message.get('sticker')
        self.video = message.get('video')
        self.video_note = message.get('video_note')
        self.voice = message.get('voice')
        self.caption = message.get('caption')
        self.caption_entities = message.get('caption_entities')
        self.contact = message.get('contact')
        self.dice = message.get('dice')
        self.game = message.get('game')
        self.poll = message.get('poll')
        self.venue = message.get('venue')
        self.location = message.get('location')
        self.new_chat_members = message.get('new_chat_members')
        self.left_chat_member = message.get('left_chat_member')
        self.new_chat_title = message.get('new_chat_title')
        self.new_chat_photo = message.get('new_chat_photo')
        self.delete_chat_photo = message.get('delete_chat_photo')
        self.group_chat_created = message.get('group_chat_created')
        self.supergroup_chat_created = message.get('supergroup_chat_created')
        self.channel_chat_created = message.get('channel_chat_created')
        self.message_auto_delete_timer_changed = message.get('message_auto_delete_timer_changed')
        self.migrate_to_chat_id = message.get('migrate_to_chat_id')
        self.migrate_from_chat_id = message.get('migrate_from_chat_id')
        self.pinned_message = message.get('pinned_message')
        self.invoice = message.get('invoice')
        self.successful_payment = message.get('successful_payment')
        self.connected_website = message.get('connected_website')
        self.passport_data = message.get('passport_data')
        self.proximity_alert_triggered = message.get('proximity_alert_triggered')
        self.video_chat_scheduled = message.get('video_chat_scheduled')
        self.video_chat_started = message.get('video_chat_started')
        self.video_chat_ended = message.get('video_chat_ended')
        self.video_chat_participants_invited = message.get('video_chat_participants_invited')
        self.web_app_data = message.get('web_app_data')
        self.reply_markup = message.get('reply_markup')

    def fromDict(self)->dict:
        '''
        Convert User object to dictionary
        Returns:
            dict: dictionary of user data
        '''
        data = {
            'message_id':self.message_id,
            'from':self.from,
            'sender_chat':self.sender_chat,
            'date':self.date,
            'chat':self.chat,
            'forward_from':self.forward_from,
            'forward_from_chat':self.forward_from_chat,
            'forward_from_message_id':self.forward_from_message_id,
            'forward_signature':self.forward_signature,
            'forward_sender_name':self.forward_sender_name,
            'forward_date':self.forward_date,
            'is_automatic_forward':self.is_automatic_forward,
            'reply_to_message':self.reply_to_message,
            'via_bot':self.via_bot,
            'edit_date':self.edit_date,
            'has_protected_content':self.has_protected_content,
            'media_group_id':self.media_group_id,
            'author_signature':self.author_signature,
            'text':self.text,
            'entities':self.entities,
            'animation':self.animation, 
            'audio':self.audio,
            'document':self.document,
            'photo':self.photo,
            'sticker':self.sticker, 
            'video':self.video, 
            'video_note':self.video_note, 
            'voice':self.voice,
            'caption':self.caption, 
            'caption_entities':self.caption_entities, 
            'contact':self.contact, 
            'dice':self.dice, 
            'game':self.game, 
            'poll':self.poll, 
            'venue':self.venue, 
            'location':self.location, 
            'new_chat_members':self.new_chat_members, 
            'left_chat_member':self.left_chat_member, 
            'new_chat_title':self.new_chat_title, 
            'new_chat_photo':self.new_chat_photo, 
            'delete_chat_photo':self.delete_chat_photo, 
            'group_chat_created':self.group_chat_created, 
            'supergroup_chat_created':self.supergroup_chat_created, 
            'channel_chat_created':self.channel_chat_created, 
            'message_auto_delete_timer_changed':self.message_auto_delete_timer_changed, 
            'migrate_to_chat_id':self.migrate_to_chat_id, 
            'migrate_from_chat_id':self.migrate_from_chat_id, 
            'pinned_message':self.pinned_message, 
            'invoice':self.invoice, 
            'successful_payment':self.successful_payment, 
            'connected_website':self.connected_website, 
            'passport_data':self.passport_data, 
            'proximity_alert_triggered':self.proximity_alert_triggered, 
            'video_chat_scheduled':self.video_chat_scheduled,
            'video_chat_started':self.video_chat_started,
            'video_chat_ended':self.video_chat_ended, 
            'video_chat_participants_invited':self.video_chat_participants_invited, 
            'web_app_data':self.web_app_data, 
            'reply_markup':self.reply_markup 
        }
        Dict1 = {}
        for a,b in data.items():
            if b != None:
                Dict1[a] = b
        return Dict1

    #Override the __str__ method to print the user data
    def __str__(self):
        '''
        Print the user data
        '''
        pass'
    