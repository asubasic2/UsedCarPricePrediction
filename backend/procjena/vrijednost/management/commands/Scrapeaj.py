import json

from django.core.management.base import BaseCommand
import pandas as pd
from vrijednost.serializers import AutoSerializer


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        df = pd.read_csv(r'C:\Users\Admir\Django\procjena\vrijednost\Automobili.csv',
                         names=['Proizvodjac', 'Model', 'Godiste', 'Kilometara', 'Gorivo', 'Kubika',
                                'BrojVrata', 'Cijena', 'Kilovata', 'Tip', 'Pogon', 'Mjenjac', 'Emisija'],
                         encoding='utf-8')

        result = df.to_json(orient="records")
        parsed = json.loads(result)
        json_data = json.dumps(parsed)
        #serializer = AutoSerializer(data=json_data, many=True)

        #if serializer.is_valid():
        #    print("Tu")
        #    serializer.save()

        #print(serializer.data)
        for data in parsed:
            serializer = AutoSerializer(data=data)

            if serializer.is_valid():
                print("Tu")
                serializer.save()

            print(serializer.data)