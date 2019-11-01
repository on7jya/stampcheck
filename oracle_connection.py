import cx_Oracle
from properties import *

class OracleConn(object):
    """oracle db connection"""

    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connector = None

    def __enter__(self):
        self.connector = cx_Oracle.connect(self.connection_string)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            self.connector.commit()
        else:
            self.connector.rollback()
        self.connector.close()

    def oracle_connection(agent):
        """
        Соединение с базой данных Бахуса
        """
        global oracle_pass, oracle_user, oracle_host
        if agent == 'hub':
            oracle_host = orahost_hub
            oracle_user = orauser_hub
            oracle_pass = orapass_hub
        elif agent == '3':
            oracle_host = orahost_3
            oracle_user = orauser_3
            oracle_pass = orapass_3
        elif agent == '4':
            oracle_host = orahost_4
            oracle_user = orauser_4
            oracle_pass = orapass_4
        elif agent == '5':
            oracle_host = orahost_5
            oracle_user = orauser_5
            oracle_pass = orapass_5
        elif agent == '6':
            oracle_host = orahost_6
            oracle_user = orauser_6
            oracle_pass = orapass_6
        elif agent == '7':
            oracle_host = orahost_7
            oracle_user = orauser_7
            oracle_pass = orapass_7
        elif agent == '8':
            oracle_host = orahost_8
            oracle_user = orauser_8
            oracle_pass = orapass_8
        elif agent == '9':
            oracle_host = orahost_9
            oracle_user = orauser_9
            oracle_pass = orapass_9
        elif agent == '10':
            oracle_host = orahost_10
            oracle_user = orauser_10
            oracle_pass = orapass_10
        elif agent == '11':
            oracle_host = orahost_11
            oracle_user = orauser_11
            oracle_pass = orapass_11
        elif agent == '12':
            oracle_host = orahost_12
            oracle_user = orauser_12
            oracle_pass = orapass_12
        else:
            print('NOT FOUND AGENT!!!')
            pass

        oracle_service = ora_service
        oracle_port = ora_port
        try:
            myconnection = cx_Oracle.makedsn(oracle_host, oracle_port, oracle_service)
            oracle_client = cx_Oracle.connect(oracle_user, oracle_pass, myconnection, encoding='UTF-8')
            return oracle_client
        except Exception as e:
            return False
