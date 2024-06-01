#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        for x in data:
            print(x['title'])
    else:
        print(response.status_code)


def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        data = response.json()
        structured_data = [{'id': post['id'], 'title': post['title'],
                            'body': post['body']} for post in data]

        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(structured_data)
    else:
        print(response.status_code)
