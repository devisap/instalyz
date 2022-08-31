import requests 
import browser_cookie3
import time, json

def get_data_hashtag (hashtag):
    cookiejar = browser_cookie3.firefox(domain_name='instagram.com')
    # scrape = requests.get(f'https://www.instagram.com/explore/tags/{hashtag}/?__a=1&__d=dis', cookies=cookiejar).json()
    scrape = requests.get(f'https://www.instagram.com/explore/tags/{hashtag}/?__a=1&__d=dis', cookies=cookiejar).json()
    return scrape

def get_data_post (shortcode):
    cookiejar = browser_cookie3.opera(domain_name='instagram.com')
    scrape = requests.get(f'https://www.instagram.com/p/{shortcode}/?__a=1&__d=dis', cookies=cookiejar).json()
    return scrape