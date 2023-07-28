from os import environ
from typing import Any, Optional
from urllib.parse import urlparse
from datetime import date

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from dotenv import load_dotenv

from ...models import AdvetisementUrl, AdvetisementUrlCount


BASE_URL = 'https://api-ssl.bitly.com/v4/'


class Command(BaseCommand):
    help = 'Получение статистики переходов по ссылке'

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            'period', type=str, help='период')

    def handle(self, *args: Any, **options: Any) -> str:

        period = options['period']
        advetisementurls = AdvetisementUrl.objects.all()
        load_dotenv()
        bitly_token = environ['BITLY_TOKEN']
        headers = {
            'Authorization': f'Bearer {bitly_token}'
        }
        for url in advetisementurls:
            if is_bitlink(url.link, headers):
                try:
                    total_clicks = count_clicks(url.link, headers, period)
                    AdvetisementUrlCount.objects.create(
                        link=url,
                        date=date.today(),                        
                        total_clicks=total_clicks,
                    )
                    print(f'Количество кликов по ссылке: {total_clicks}')
                except requests.exceptions.HTTPError:
                    print('Введена неправильная сокращённая ссылка или неверный токен')
            else:
                print('Введена неправильная ссылка или неверный токен')


def count_clicks(bitlink, headers, period):

    parsed_link = urlparse(bitlink)
    link = f'{parsed_link.netloc}{parsed_link.path}'
    url = f'{BASE_URL}bitlinks/{link}/clicks/summary'
    url_params = {
        'unit': period,
        'units': '1'
    }
    response = requests.get(url, headers=headers, params=url_params)
    response.raise_for_status()

    return response.json()['total_clicks']


def is_bitlink(url, headers):

    parsed_link = urlparse(url)
    link = f'{parsed_link.netloc}{parsed_link.path}'
    url_link = f'{BASE_URL}bitlinks/{link}'
    response = requests.get(url_link, headers=headers)

    return response.ok
