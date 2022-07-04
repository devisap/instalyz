from asyncio.windows_events import NULL
import time
from flask import Flask, jsonify, json
from scrapper import get_data_hashtag, get_data_post
from datetime import datetime
import uuid

app = Flask(__name__)

@app.route("/")
def index():
    hashtag_scrapes = get_data_hashtag("liverpool")
    hashtag_scrapes = hashtag_scrapes['graphql']['hashtag']['edge_hashtag_to_media']['edges']
    list_data = []

    # post_scrape = get_data_post("Cflaa29tk48")
    # post_scrape = post_scrape['items'][0]

    # post = {}
    # post['SHORTCODE_DD']    = "sjfhrg"
    # post['USERAME_DD']      = post_scrape['user']['username']
    # post['DISPLAYURL_DD']   = post_scrape['image_versions2']['candidates'][0]['url']
    # post['COUNTLIKE_DD']    = post_scrape['like_count']
    # post['COUNTCOMMENT_DD'] = post_scrape['comment_count']
    # post['CAPTION_DD']      = post_scrape['']
    i = 0
    x = 1
    for hashtag_scrape in hashtag_scrapes:
        try:
            # if i == 4:
            #     i = 0
            #     time.sleep(3)
            #     if x == 20:
            #         x = 1
            #         time.sleep(5)

            hashtag_scrape = hashtag_scrape['node']

            post_scrape = get_data_post(hashtag_scrape['shortcode'])
            post_scrape = post_scrape['items'][0]

            post = {}
            post['SHORTCODE_DD']    = hashtag_scrape['shortcode']
            post['USERNAME_DD']     = post_scrape['user']['username']
            post['FULLNAME_DD']     = post_scrape['user']['full_name']
            post['PROFILPICT_DD']     = post_scrape['user']['profile_pic_url']
            # post['DISPLAYURL_DD']   = post_scrape['image_versions2']['candidates'][0]['url']
            post['DISPLAYURL_DD']   = hashtag_scrape['display_url']
            post['COUNTLIKE_DD']    = post_scrape['like_count']
            post['COUNTCOMMENT_DD'] = post_scrape['comment_count']
            post['CAPTION_DD']      = post_scrape['caption']['text']

            try:
                list_tags = post_scrape['usertags']['in']
                tag_users = []
                
                for tag in list_tags:
                    tag_users.append(tag['user']['username'])
                post['LISTTAG_DD'] = ';'.join(tag_users)
            except:
                post['LISTTAG_DD']      = None

            json.dumps(post)
            list_data.append(post)

            print(x," | ",hashtag_scrape['shortcode'])
            time.sleep(1)

            
            i = i + 1
            x = x + 1
        except: 
            return jsonify(list_data)

    # return jsonify(hashtag_scrapes[0]['node']['shortcode'])
    return jsonify(list_data)

if __name__ == "__main__":
    app.run(debug=True)