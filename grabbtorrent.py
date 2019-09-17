from __future__ import print_function, unicode_literals

import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt, Separator
from examples import custom_style_1


def search_torrent(url):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--incognito')

    browser = webdriver.Chrome(options=options)
    browser.get(url)

    print(page_table)

    # soup = BeautifulSoup(page.text, 'html.parser')

    # name = soup.find(
    #     'table', {'class': 'table-list table table-responsive table-striped'}
    # )
    # link = soup.find

    # print(page.content)


name = 'number+23'
quality = '1080'
formatted_url = f'https://1337x.to/search/{name}+{quality}/1/'

search_torrent(formatted_url)


# def qbittorren_torrent(magnetic_link):


# def main():
#     questions = [
#         {
#             'type': 'list',
#             'message': 'Would you like to download a:',
#             'name': 'content_type',
#             'choices': [
#                 {'name': 'Movie'},
#                 {'name': 'Series'}
#             ],
#         },
#         {
#             'type': 'input',
#             'message': 'Type the name:',
#             'name': 'content_name',
#         },
#         {
#             'type': 'list',
#             'message': 'Choose the quality you desire:',
#             'name': 'content_quality',
#             'choices': [
#                 {'name': '2160 - (4k)'},
#                 {'name': '1080 - (FULL HD)'},
#                 {'name': '720 - (HD)'},
#                 {'name': '480 - (SD)'},
#             ]
#         },
#     ]

#     answers = prompt(questions, style=custom_style_1)
#     pprint(answers)

#     formatted_name = answers['content_name']
#     formatted_name = re.sub(r'[\W]', ' ', formatted_name).split()
#     formatted_name = '+'.join(formatted_name)

#     quality = answers['content_quality'][:4].rstrip()

#     search_torrent(formatted_name, quality)

#     print(formatted_url)


# main()
