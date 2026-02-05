import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Read_config:
    @staticmethod
    def get_admin_page_url():
        url = config.get('admin_login_info','admin_page_url')
        return url
    @staticmethod
    def get_username():
        username = config.get('admin_login_info','username')
        return username
    @staticmethod
    def get_password():
        password = config.get('admin_login_info','password')
        return password
    @staticmethod
    def get_invalid_username():
        invalid_username = config.get('admin_login_info','invalid_username')
        return invalid_username

