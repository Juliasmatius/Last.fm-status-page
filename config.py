import configparser
config = configparser.ConfigParser()
config.read("config.ini")

API_KEY = config["config"]["API_KEY"]
MAIN_PAGE_PATH = config["config"]["MAIN_PAGE_PATH"]
USER = config["config"]["LASTFM_USER"]
port = config["config"]["PORT"]
debug = bool(config["config"]["DEBUG"])
api_root = config["DEV"]["api_root"]
refresh_time = config["DEV"]["REFRESH_TIME"]
WEBSERVER_REFRESH = str(int(config["DEV"]["WEBSERVER_REFRESH"])*1000)
del config