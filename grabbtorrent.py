from __future__ import print_function, unicode_literals

import requests
import re
from bs4 import BeautifulSoup
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt, Separator
from examples import custom_style_1


# def search_torrent(name, quality):
#     url = f"https://1337x.to/search/{search_name}+{search_quality}/1/"

# def qbittorren_torrent(magnetic_link):


def main():
    questions = [
        {
            'type': 'list',
            'message': 'Would you like to download a:',
            'name': 'content_type',
            'choices': [
                {'name': 'Movie'},
                {'name': 'Series'}
            ],
        },
        {
            'type': 'input',
            'message': 'Type the name:',
            'name': 'content_name',
        },
        {
            'type': 'list',
            'message': 'Choose the quality you desire:',
            'name': 'content_quality',
            'choices': [
                {'name': '2160 - (4k)'},
                {'name': '1080 - (FULL HD)'},
                {'name': '720 - (HD)'},
                {'name': '480 - (SD)'},
            ]
        },
    ]

    answers = prompt(questions, style=custom_style_1)
    pprint(answers)

    formatted_name = answers['content_name']
    formatted_name = re.sub(r'[\W]', ' ', formatted_name).split()
    formatted_name = '+'.join(formatted_name)

    quality = answers['content_quality'][:4].rstrip()

    formatted_url = f"https://1337x.to/search/{formatted_name}+{quality}/1/"

    print(formatted_url)


main()
