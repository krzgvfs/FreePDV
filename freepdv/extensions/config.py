from dynaconf import Dynaconf


def init_app(app):
   Dynaconf(app, settings_files=['settings.toml', '.secrets.toml'])
