from __future__ import print_function, unicode_literals

import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from qbittorrent import Client
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt, Separator
from examples import custom_style_1


def search_torrent(name, quality, url):
    url_content = f'/search/{name}+{quality}/1/'

    search_url = url + url_content
    try:
        soup = parse_html(search_url)

        link = soup.find('tbody').find(
            'td', {'class': 'coll-1 name'}).find_all('a')[1]['href']

        torrent_url = url + link
        soup = parse_html(torrent_url)
        magnetic_link = soup.find(
            'div', {'class': 'col-9 page-content'}).find('li').find('a')['href']

        return magnetic_link

    except AttributeError:
        print('Torrent not found, please choose another quality or try another name.')


def parse_html(url):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--incognito')
    browser = webdriver.Chrome(options=options)

    browser.get(url)
    page_source = browser.page_source
    html_parsed = BeautifulSoup(page_source, 'html.parser')

    return html_parsed


def qbittorren_torrent(magnetic_link, name, quality):
    qb = Client('http://127.0.0.1:8080/')
    qb.login()
    qb.download_from_link(magnetic_link, label=f'{name}+{quality}')


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

    name = answers['content_name']

    formatted_name = name
    formatted_name = re.sub(r'[\W]', ' ', formatted_name).split()
    formatted_name = '+'.join(formatted_name)

    quality = answers['content_quality'][:4].rstrip()

    url = 'https://1337x.to'

    magnetic_link = search_torrent(name, quality, url)
    qbittorren_torrent(magnetic_link, name, quality)

    print('Your download started!')


main()
