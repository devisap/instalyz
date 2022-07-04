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
    for hashtag_scrape in hashtag_scrapes:
        hashtag_scrape = hashtag_scrape['node']

        post_scrape = get_data_post(hashtag_scrape['shortcode'])
        post_scrape = post_scrape['items'][0]

        post = {}
        post['SHORTCODE_DD']    = hashtag_scrape['shortcode']
        post['USERNAME_DD']     = post_scrape['user']['username']
        post['DISPLAYURL_DD']   = post_scrape['image_versions2']['candidates'][0]['url']
        post['COUNTLIKE_DD']    = post_scrape['like_count']
        post['COUNTCOMMENT_DD'] = post_scrape['comment_count']
        post['CAPTION_DD']      = post_scrape['caption']['text']
        json.dumps(post)

        list_data.append(post)

    # return jsonify(hashtag_scrapes[0]['node']['shortcode'])
    return jsonify(list_data)

if __name__ == "__main__":
    app.run(debug=True)