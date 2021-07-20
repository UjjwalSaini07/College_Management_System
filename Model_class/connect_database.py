class ConnectDatabase:
    """this is the model class for ConnectDatabase class from module connect_database, it connects frontend and
    backend """
    def __init__(self, host, port, username, password):
        self.__host = "localhost"
        self.__port = 3306
        self.__username = "root"
        self.__password = "ujjwal2003"

    def get_host(self):
        return self.__host

    def get_port(self):
        return self.__port

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password


class CreateDatabase:
    def __init__(self, database):
        self.__database = database

    def get_database(self):
        return self.__database