import os

from loguru_logging import stderror
from django.conf import settings
from dotenv import load_dotenv



def database_init() -> None:
	for cmd in settings.DATABASE_INIT:
		try:
			os.system(cmd)
		except Exception as exs:
			stderror(exs)


def objects_init() -> None:
	os.system(settings.LOCATIONS_OBJECTS_INIT)
	os.system(settings.MACHINES_OBJECTS_INIT)


def environment_init() -> None:
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Shipping.settings")
	dotenv_path = os.path.join(settings.BASE_DIR, '.env')
	if os.path.exists(dotenv_path):
		load_dotenv(dotenv_path)


def start() -> None:
	os.system(settings.START_COMMAND)

