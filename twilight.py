from mastodon import Mastodon
import os, random
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%m/%d/%Y %H:%M:%S")

mastodon = Mastodon(
    access_token = 'token.secret',
    api_base_url = 'https://botsin.space/'
)

def PostTwi():
    random_file = random.choice(os.listdir("img/twi"))
    media = mastodon.media_post('img/twi/' + random_file)
    mastodon.status_post("!!New Twilight Image!!", media_ids=media)
    print('posted a twi at ' + dt_string  + ' :3')
    
PostTwi()
