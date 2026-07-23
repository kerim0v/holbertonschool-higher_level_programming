#!/usr/bin/python3
"""fetch posts frfom jsonplaceholder api and either print or save them"""

import csv
import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    """stated"""
    response = requests.get(API_URL)
    print("Status code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])

fetch_and_print_posts()