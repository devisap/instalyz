# from asyncio.windows_events import NULL
import time
from flask import Flask, jsonify, json
from scrapper import get_data_hashtag, get_data_post
from datetime import datetime
import uuid

app = Flask(__name__)

@app.route("/")
def index():
    hashtag_scrapes = get_data_hashtag("timnasu19")
    hashtag_scrapes = hashtag_scrapes['graphql']['hashtag']['edge_hashtag_to_media']['edges']
    list_data = []

    hashtag = {}
    hashtag['ID_DATASET'] = uuid.uuid4()

    x = 1
    counter = 0
    total_hashtag_scrape = len(hashtag_scrapes)
    print("Expected Total Data  : " + str(total_hashtag_scrape))
    while counter < 3:
        # try:
            hashtag_scrape = hashtag_scrapes[counter]['node']

            post_scrape = get_data_post(hashtag_scrape['shortcode'])
            post_scrape = post_scrape['items'][0]

            curr_date    = datetime.now()

            # post = {}
            # post['ID_DATASET']      = hashtag['ID_DATASET']
            # post['SHORTCODE_DD']    = hashtag_scrape['shortcode']
            # post['USERNAME_DD']     = post_scrape['user']['username']
            # post['FULLNAME_DD']     = post_scrape['user']['full_name']
            # post['PROFILEPICT_DD']  = post_scrape['user']['profile_pic_url']
            # post['DISPLAYURL_DD']   = hashtag_scrape['display_url']
            # post['COUNTLIKE_DD']    = post_scrape['like_count']
            # post['COUNTCOMMENT_DD'] = post_scrape['comment_count']
            # post['CAPTION_DD']      = post_scrape['caption']['text']
            # post['created_at']      = curr_date.strftime("%Y-%m-%d %H:%M:%S")
            # post['updated_at']      = curr_date.strftime("%Y-%m-%d %H:%M:%S")

            post = []
            post.append(hashtag['ID_DATASET']) 
            post.append(hashtag_scrape['shortcode']) 
            post.append(post_scrape['user']['username']) 
            post.append(post_scrape['user']['full_name']) 
            post.append(post_scrape['user']['profile_pic_url']) 
            post.append(hashtag_scrape['display_url']) 
            post.append(post_scrape['like_count']) 
            post.append(post_scrape['comment_count']) 
            post.append(post_scrape['caption']['text']) 
            post.append(curr_date.strftime("%Y-%m-%d %H:%M:%S")) 
            post.append(curr_date.strftime("%Y-%m-%d %H:%M:%S")) 

            try:
                list_tags = post_scrape['usertags']['in']
                tag_users = []
                
                for tag in list_tags:
                    tag_users.append(tag['user']['username'])
                post.append(';'.join(tag_users))
            except:
                post.append(None)
            
            post = tuple(post)

            json.dumps(post)
            list_data.append(post)

            print(x," | ",hashtag_scrape['shortcode'])
            time.sleep(1)            
            x = x + 1
        # except: 
            # time.sleep(3)
        
            counter = counter + 1

    # return jsonify(hashtag_scrapes[0]['node']['shortcode'])
    return jsonify(list_data)

if __name__ == "__main__":
    app.run(debug=True)