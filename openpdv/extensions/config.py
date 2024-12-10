from dynaconf import Dynaconf
from dotenv import load_dotenv


def init_app(app):
   Dynaconf(app, settings_files=['settings.toml', '.secrets.toml'], load_dotenv=True)
