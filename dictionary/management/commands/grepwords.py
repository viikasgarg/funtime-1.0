'''
script for Portal -- >  QB Call function
Author : Vikas Kumar
'''
from dictionary.models import NewWord
from django.core.management.base import BaseCommand
from urllib2 import urlopen
import xml.etree.ElementTree as ET
import logging
logging.basicConfig(filename='error.log', level=logging.ERROR)


class Command(BaseCommand):
    """ How to Use:
        $ python manage.py grepwords
    """

    def handle(self, *args, **options):
        url_template = "http://services.aonaware.com/DictService/DictService.asmx/Define?word=%s"
        prefix = "{http://services.aonaware.com/webservices/}"
        with open("wordlist.txt") as f:
            errors = 0
            saved = 0
            for line in f:
                url = url_template % str(line)
                try:
                    xml_data = urlopen(url).read()
                    root = ET.fromstring(xml_data)

                    for definition in root.iter(prefix + 'Definition'):
                        word = Word()
                        word.name = definition.find(prefix + 'Word').text
                        dictionary = definition.find(prefix + 'Dictionary')
                        word.dic_name = dictionary.find(prefix + 'Name').text
                        word.definition = definition.find(
                            prefix + 'WordDefinition').text
                        word.save()
                        saved += 1
                        print saved
                except:
                    errors += 1
                    print errors
                    logging.error(line)
