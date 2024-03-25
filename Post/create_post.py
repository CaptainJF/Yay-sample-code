#投稿をする

import requests

access_token = 'TOKEN'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Authorization' : f'Bearer {access_token}'
}

post_text = str(input('[投稿文]>>'))
json = {
    'text' : post_text
}

post = requests.post('https://api.yay.space/v3/posts/new',headers=headers,json=json).json()
