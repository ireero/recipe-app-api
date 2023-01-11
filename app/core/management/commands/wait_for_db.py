from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Aguardando o banco de dados...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except(Psycopg2Error, OperationalError):
                self.stdout.write('O banco de dados não está pronto, aguarde um pouco.')
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS('Banco de dados disponivel!'))