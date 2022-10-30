import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for line in reader:
                phone = Phone(name=line['name'], price=line['price'], image=line['image'], release_date=line['release_date'], lte_exists=line['lte_exists'], slug=slugify(line['name']))
                phone.save()
