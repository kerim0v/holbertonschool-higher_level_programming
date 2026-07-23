#!/usr/bin/python3
"""fetch posts frfom jsonplaceholder api and either print or save them"""

import csv
import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    """stated"""
    response = requests.get(API_URL)
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])

def fetch_and_save_posts():
    """balright"""
    response = requests.get(API_URL)

    if response.status_code == 200:
        posts = response.json()
        posts_data = [
            {"id" : post["id"], "title" : post["title"], "body" : post["body"]}
            for post in posts]

        with open("posts.csv", "w", newline="") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts_data)

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
