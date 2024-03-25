#投稿をする

import uuid
import requests

access_token = 'Token'

headers = {
        'Authorization': f'Bearer {access_token}',
    }

post_text = str(input('[投稿文]>>'))
json = {
    "post_type": "text",
    "text": post_text,
    "color": "0",
    "font_size": "0",
    "message_tags": "[]",
    "uuid": str(uuid.uuid4())
}

post = requests.post('https://yay.space/api/posts',headers=headers,json=json).json()
print(post)