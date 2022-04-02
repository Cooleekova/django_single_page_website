from django.core.management.base import BaseCommand
from records.models import Film


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str, help='The csv file that contains data')

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        with open(f'{file_name}.csv', 'r', encoding="UTF-8") as file:
            content = file.readlines()
            rows = content[2:]
            for row in rows:
                values = list(row.split(";"))
                year = int(values[0])
                if values[1] == '':
                    continue
                else:
                    length = int(values[1])
                title = values[2]
                if values[3] == '':
                    subject = "No info provided"
                else:
                    subject = values[3]
                if values[4] == '':
                    actor = "No info provided"
                else:
                    actor = values[4]
                if values[5] == '':
                    actress = "No info provided"
                else:
                    actress = values[5]
                if values[6] == '':
                    director = "No info provided"
                else:
                    director = values[6]
                if values[7] == '':
                    popularity = 0
                else:
                    popularity = int(values[7])
                film = Film(
                    year=year,
                    length=length,
                    title=title,
                    subject=subject,
                    actor=actor,
                    actress=actress,
                    director=director,
                    popularity=popularity
                )
                film.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))

