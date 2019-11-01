# -*- coding: utf-8 -*-

import paramiko
import urllib3
from oracle_connection import OracleConn

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from PyQt5 import QtCore, QtGui, QtWidgets
from loggers import Loggers
from properties import *


class UiMainWindow(object):
    def __init__(self):
        """
        Инициализация формы
        """
        super().__init__()
        self.centralwidget = QtWidgets.QWidget()
        self.mark_line = QtWidgets.QLineEdit(self.centralwidget)
        self.widget_bacchus_plu_alc = QtWidgets.QWidget()
        self.widget_bacchus_amc = QtWidgets.QWidget()
        self.widget_gk_cache = QtWidgets.QWidget()
        self.widget_gk_sale = QtWidgets.QWidget()

    def setup_ui(self, main_window):
        """
        Создание и отрисовка элементов формы
        """
        main_window.setObjectName("main_window")
        main_window.setWindowIcon(QtGui.QIcon('app.ico'))
        main_window.setMinimumSize(QtCore.QSize(1300, 700))
        main_window.setMaximumSize(QtCore.QSize(1400, 700))

        self.centralwidget.setObjectName("centralwidget")

        self.mark_line.setGeometry(QtCore.QRect(10, 10, 1000, 20))
        self.mark_line.setMaxLength(150)
        self.mark_line.setObjectName("mark")
        self.mark_line.setText(
            '1344019161587903190012VV2C6KSA23SXHXCPPRZVO5PC4DJJTSNZSZB7HEUBFWTSK6SMMDRQIYEF4TJB6MEWWST37UB4T47KMQ5LZSCMW2VSXFFHGGKRICQREPNG4Z53TAKG5LKOYJCDAH7QXK2I')

        self.text = QtWidgets.QTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(10, 275, 1280, 580))
        self.text.setObjectName("text")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)  # Запросить в GK и Бахусе
        self.pushButton.setGeometry(QtCore.QRect(1020, 10, 141, 21))
        self.pushButton.setObjectName("pushButton")

        main_window.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.table_plu_alccode = QtWidgets.QTableWidget(self.centralwidget)
        self.table_plu_alccode.setGeometry(10, 50, 1280, 140)
        self.table_plu_alccode.setColumnCount(12)
        self.table_plu_alccode.setRowCount(1)

        self.table_plu_alccode.setStyleSheet("QTableWidget {\n"
                                             "border: 1px solid gainsboro;\n"
                                             "font-family: arial;\n"
                                             "font-size:10px;\n"
                                             "}\n"
                                             "QHeaderView::section\n"
                                             "{\n"
                                             "spacing: 0px;\n"
                                             "background-color: rgb(206, 215, 223);\n"
                                             "color: rgb(89, 98, 106);\n"
                                             "border: 1px white;\n"
                                             "margin: 0.5px;\n"
                                             "text-align: right;\n"
                                             "font-family: arial;\n"
                                             "font-size:11px;\n"
                                             "};\n"
                                             "")
        self.table_plu_alccode.horizontalHeader().setStretchLastSection(True)

        self.table_plu_alccode.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem('Признак'))
        self.table_plu_alccode.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem('PLU'))
        self.table_plu_alccode.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem('Наименование PLU'))
        self.table_plu_alccode.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem('Крепость'))
        self.table_plu_alccode.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem('Объем'))
        self.table_plu_alccode.setHorizontalHeaderItem(5, QtWidgets.QTableWidgetItem('Код'))
        self.table_plu_alccode.setHorizontalHeaderItem(6, QtWidgets.QTableWidgetItem('Алкокод'))
        self.table_plu_alccode.setHorizontalHeaderItem(7, QtWidgets.QTableWidgetItem('Наименование алкокода'))
        self.table_plu_alccode.setHorizontalHeaderItem(8, QtWidgets.QTableWidgetItem('Крепость'))
        self.table_plu_alccode.setHorizontalHeaderItem(9, QtWidgets.QTableWidgetItem('Объем'))
        self.table_plu_alccode.setHorizontalHeaderItem(10, QtWidgets.QTableWidgetItem('Код'))
        self.table_plu_alccode.setHorizontalHeaderItem(11, QtWidgets.QTableWidgetItem('Марка'))

        self.table_plu_alccode = self.table_plu_alccode

        ########################################################
        self.table_ttn_amc = QtWidgets.QTableWidget(self.centralwidget)
        self.table_ttn_amc.setGeometry(10, 100, 1280, 180)
        self.table_ttn_amc.setColumnCount(14)
        self.table_ttn_amc.setRowCount(4)

        self.table_ttn_amc.setStyleSheet("QTableWidget {\n"
                                         "border: 1px solid gainsboro;\n"
                                         "font-family: arial;\n"
                                         "font-size:10px;\n"
                                         "}\n"
                                         "QHeaderView::section\n"
                                         "{\n"
                                         "spacing: 0px;\n"
                                         "background-color: rgb(206, 215, 223);\n"
                                         "color: rgb(89, 98, 106);\n"
                                         "border: 1px white;\n"
                                         "margin: 0.5px;\n"
                                         "text-align: right;\n"
                                         "font-family: arial;\n"
                                         "font-size:11px;\n"
                                         "};\n"
                                         "")
        self.table_ttn_amc.horizontalHeader().setStretchLastSection(True)

        self.table_ttn_amc.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem('№'))
        self.table_ttn_amc.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem('Завод'))
        self.table_ttn_amc.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem('Статус АМ'))
        self.table_ttn_amc.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem('Дата марки'))
        self.table_ttn_amc.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem('Буфер'))
        self.table_ttn_amc.setHorizontalHeaderItem(5, QtWidgets.QTableWidgetItem('Дата буфера'))
        self.table_ttn_amc.setHorizontalHeaderItem(6, QtWidgets.QTableWidgetItem('Статус буфера'))
        self.table_ttn_amc.setHorizontalHeaderItem(7, QtWidgets.QTableWidgetItem('Номер ТТН'))
        self.table_ttn_amc.setHorizontalHeaderItem(8, QtWidgets.QTableWidgetItem('Номер движения'))
        self.table_ttn_amc.setHorizontalHeaderItem(9, QtWidgets.QTableWidgetItem('FSRARID пол-я'))
        self.table_ttn_amc.setHorizontalHeaderItem(10, QtWidgets.QTableWidgetItem('Статус'))
        self.table_ttn_amc.setHorizontalHeaderItem(11, QtWidgets.QTableWidgetItem('Справка Б'))
        self.table_ttn_amc.setHorizontalHeaderItem(12, QtWidgets.QTableWidgetItem('Признак'))
        self.table_ttn_amc.setHorizontalHeaderItem(13, QtWidgets.QTableWidgetItem('Короб'))

        self.table_ttn_amc = self.table_ttn_amc

        ########################################################
        self.table_gk_cache = QtWidgets.QTableWidget(self.centralwidget)
        self.table_gk_cache.setGeometry(10, 210, 1280, 60)
        self.table_gk_cache.setColumnCount(3)
        self.table_gk_cache.setRowCount(1)

        self.table_gk_cache.setStyleSheet("QTableWidget {\n"
                                          "border: 1px solid gainsboro;\n"
                                          "font-family: arial;\n"
                                          "font-size:10px;\n"
                                          "}\n"
                                          "QHeaderView::section\n"
                                          "{\n"
                                          "spacing: 0px;\n"
                                          "background-color: rgb(206, 215, 223);\n"
                                          "color: rgb(89, 98, 106);\n"
                                          "border: 1px white;\n"
                                          "margin: 0.5px;\n"
                                          "text-align: right;\n"
                                          "font-family: arial;\n"
                                          "font-size:11px;\n"
                                          "};\n"
                                          "")
        self.table_gk_cache.horizontalHeader().setStretchLastSection(True)

        self.table_gk_cache.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem('Кеш'))
        self.table_gk_cache.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem('Продажа'))
        self.table_gk_cache.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem('Запросы в УТМ'))

        self.table_gk_cache = self.table_gk_cache

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        """
        Действия и подписи на форме
        """
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", 'Проверка марки'))

        try:
            self.pushButton.clicked.connect(self.clear_text)
            self.pushButton.clicked.connect(BacchusMark.get_mark_bacchus)
            self.pushButton.clicked.connect(GkMark.get_mark_gk)
        except Exception as e:
            logger.error(e)

    def statusbar_message(self, message):
        """
        Вывод сообщения в статусбар
        """
        try:
            self.statusbar.setStyleSheet(
                "color: rgb(255, 0, 0)")  # делаем цвет текста статусбара красным
            self.statusbar.showMessage(message,
                                       msecs=10000)  # в статусбар пишем сообщение об ошибке
        except Exception as e:
            logger.error(e)
        return

    def setup_text(self, string):
        self.text.append(string)

    def clear_text(self):
        self.text.clear()


class LogicForm(UiMainWindow):

    def __init__(self):
        super().__init__()
        self.centralwidget = QtWidgets.QWidget(MainWindow)

    def get_mark(self):
        """
        Получение local_id
        """
        _result = str(self.mark_line.text().strip())
        return _result


class BacchusMark:

    def __init__(self, codv_code, bamc_amc, bamc_status, bamc_date):
        self.codv_code = codv_code
        self.bamc_amc = bamc_amc
        self.bamc_status = bamc_status
        self.bamc_date = bamc_date

    def get_mark_bacchus(self):
        """
        Находим историю буфера приемки в Бахусе
        """
        try:
            db_mark = OracleConn.oracle_connection('hub')
            mark = LogicForm.get_mark(ui)
            mark_select_incoming_oracle = f"""SELECT
  /*+ PARALLEL(10) */ DISTINCT
    CODV_CODE
  , CODV_NAME
  , BAMC.BAMC_STATUS || ' - ' || B_AMC_STATUSES.BAMC_DESCR
  , to_char(BAMC_DATE, 'dd.mm.rrrr hh24:mi:ss')
  , BINC_TRANSACTIONID
  , to_char(BINC_TRANSACTIONDATE, 'dd.mm.rrrr')
  , SDSS_CODE 
  , W.EWBH_WBNUMBER
  , W.EWBH_WBREGID  
  , W.EWBH_CLIENTID
  , WS.EWBS_NAME 
  , FE.EFB_F2REGID
  , case when FE.EFB_IS_MARK = '1' then 'помарка'
        when FE.EFB_IS_MARK = '0' or FE.EFB_IS_MARK  is null then 'партионка'
        else null end 
  , to_char(BBP_MARK) BBP_MARK
FROM B_INCOMING I
  JOIN B_INCOMING_DETAILS D ON D.BINC_ID = I.BINC_ID
  JOIN B_INCOMING_DETAILS_FB F ON F.BIND_ID = D.BIND_ID
  JOIN S_DOCSTATUSES ON I.DOC_STATUS = S_DOCSTATUSES.SDSS_ID
  left join E_WAYBILL W on I.EWBH_ID = W.EWBH_ID
  left join E_WAYBILL_STATUSES WS on W.EWBH_STATUS = WS.EWBS_CODE
  JOIN B_BOXPOS B ON B.BIND_ID = D.BIND_ID
  JOIN B_BOXPOS_BAMC_REL R ON R.BBP_ID = B.BBP_ID
  JOIN B_AMC BAMC ON BAMC.BAMC_LID = R.BAMC_LID
  left JOIN B_AMC_STATUSES ON BAMC.BAMC_STATUS = B_AMC_STATUSES.BAMC_STATUS
  JOIN E_FB FE ON FE.EFB_ID = F.EFB_ID
  INNER JOIN C_ORG_DIVISIONS ON BAMC.CODV_ID = C_ORG_DIVISIONS.CODV_ID
where BAMC_AMC = '{mark}' ORDER BY FE.EFB_F2REGID"""

            cursor_from_inc = db_mark.cursor()
            cursor_from_inc.execute(mark_select_incoming_oracle)
            result_mark_from_inc = cursor_from_inc.fetchall()
            cursor_from_inc.close()

            mark_select_amc_oracle = f"""SELECT
          /*+ PARALLEL(10) */    DISTINCT
CASE WHEN FE.EFB_IS_MARK = '1'
  THEN 'помарка'
    WHEN FE.EFB_IS_MARK = '0' OR FE.EFB_IS_MARK IS NULL
      THEN 'партионка'
    ELSE NULL END
  , CART.CART_CODE
  , CART.CART_NAME
  , to_char(CART.CART_ALCVOLUME)
  , to_char(CART.CART_INHAL)
  , to_char(CART.CART_CODERAR)
  , FE.EFB_ALCCODE
  , EA.EACC_FULLNAME
  , to_char(EA.EACC_ALCVOLUME)
  , to_char(EA.EACC_CAPACITY)
  , to_char(EA.EACC_PRODUCTVCODE)
  , BAMC.BAMC_AMC
        FROM B_AMC BAMC
          left join B_STOCKENTRY_AMC b on BAMC.CODV_ID = b.CODV_ID AND BAMC.BAMC_LID = b.BAMC_LID
          left JOIN B_STOCKENTRY bs ON bs.BSTE_ID = b.BSTE_ID
          left JOIN E_FB FE ON FE.EFB_ID = bs.EFB_ID and bs.ROW_STATUS = 'A'
          left JOIN C_ARTICLES CART on bs.CART_ID = CART.CART_ID
          left JOIN E_ALCCODES EA ON EA.EACC_ALCCODE = FE.EFB_ALCCODE
          left JOIN C_ORG_DIVISIONS ON bs.CODV_ID = C_ORG_DIVISIONS.CODV_ID
            where BAMC_AMC = '{mark}' """

            cursor_from_amc = db_mark.cursor()
            cursor_from_amc.execute(mark_select_amc_oracle)
            result_mark_from_amc = cursor_from_amc.fetchall()
            cursor_from_amc.close()
            db_mark.close()

            for i, tuple_item in enumerate(result_mark_from_amc):
                for j, item in enumerate(tuple_item):
                    ui.table_plu_alccode.setItem(i, j, QtWidgets.QTableWidgetItem(item))

            ui.table_plu_alccode.resizeColumnsToContents()

            ui.table_ttn_amc.setRowCount(len(result_mark_from_inc))
            for i, tuple_item in enumerate(result_mark_from_inc):
                for j, item in enumerate(tuple_item):
                    ui.table_ttn_amc.setItem(i, j, QtWidgets.QTableWidgetItem(item))

            ui.table_ttn_amc.resizeColumnsToContents()

        except Exception as e:
            logger.error(e)
        return result_mark_from_inc

    def get_code(self):
        # UiMainWindow.setup_text(ui, "Статус марки в Бахусе:")
        result_mark = self.get_mark_bacchus()
        codv_code = list()
        for item in result_mark:
            # UiMainWindow.setup_text(ui, str(item))
            codv_code.append(item[0])
        return codv_code


class GkMark:

    def __init__(self):
        self.get_mark_gk = None
        self.ssh_connection = None
        self.code = None
        self.mark = None

    def get_mark_gk(self):
        """
        Метод получения информации о марке из GK
        """
        try:
            mark = LogicForm.get_mark(ui)
            codes = BacchusMark.get_code(bacchus_mark)
            for code in codes:

                ssh_client = GkMark.ssh_connection(code)  # Получаем объект подключения из функции ssh_connection

                if ssh_client == 1:  # Если объект подключения равен 1,
                    pass
                else:
                    GkMark.step_xrg_transport_module(mark, ssh_client, code)
                    return ssh_client
        except Exception as e:
            logger.error(e)

    def step_xrg_transport_module(mark, client, code):
        """
        Получение информации о документе приемки из GK
        """
        try:
            status_egais_stock = GkMark.result_egais_stock(mark, client)
            if status_egais_stock:
                ui.table_gk_cache.setItem(0, 0, QtWidgets.QTableWidgetItem('Марка есть в кеше'))
            else:
                ui.table_gk_cache.setItem(0, 0, QtWidgets.QTableWidgetItem('Марки нет в кеше'))

            status_egais_stamps = GkMark.result_egais_stamps(mark, client)
            if status_egais_stamps:
                ui.table_gk_cache.setItem(0, 1, QtWidgets.QTableWidgetItem('Есть продажа марки в GK'))
            else:
                ui.table_gk_cache.setItem(0, 1, QtWidgets.QTableWidgetItem('Нет продажи марки в GK'))

            status_transport_module = GkMark.result_transport_module(mark, client)
            if status_transport_module:
                ui.table_gk_cache.setItem(0, 2, QtWidgets.QTableWidgetItem('Есть запросы в УТМ в GK'))
                ui.table_gk_cache.resizeColumnsToContents()
            else:
                ui.table_gk_cache.setItem(0, 2, QtWidgets.QTableWidgetItem('Нет запросов в УТМ в GK'))
                ui.table_gk_cache.resizeColumnsToContents()

            status_transaction_module = GkMark.result_transaction_module(mark, client)

            UiMainWindow.setup_text(ui, f"Статус марки в BO-{code} xrg_transport_module:")
            # UiMainWindow.setup_text(ui, str(status_transaction_module))
            status = status_transaction_module.split('\n')
            for item in status:
                UiMainWindow.setup_text(ui, str(item))
                UiMainWindow.setup_text(ui,
                                        "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        except Exception as e:
            ui.statusbar_message(e)
            logger.error(e)

    def bash_postgres_cmd(query):
        cmd = "PGPASSWORD=gkretail /usr/bin/psql -h 127.0.0.1 -U gkretail -d postgres -t -A -F\"|\" --pset pager=off -c \"" + query + ";\""
        return cmd

    def result_transaction_module(mark, ssh_client):
        cmd = GkMark.bash_postgres_cmd(f"""
        SELECT
            M.BON_SEQ_ID
            , case when BELEGSTATUS = '1' then 'отменен'
            when BELEGSTATUS = '5' then 'оплачен' else null end
            , 'POS=' || WORKSTATION_ID POS
            , AMOUNT
            , TIMESTAMP
            , B.BONNR
            , B.FISCAL_DAY_NUMBER
            , FISCAL_PRINTER_ID
            , SIGN
            , URL
          , error_description
            , TRANSACTION
            FROM XRG_TRANSPORT_MODULE M
            INNER JOIN GK_BONKOPF B ON M.BON_SEQ_ID = B.BON_SEQ_ID
             where TRANSACTION ilike '%{mark}%' order by M.BON_SEQ_ID, TIMESTAMP""")
        std_in, out, std_err = ssh_client.exec_command(cmd)
        out = out.read().decode().strip()
        return out

    def result_egais_stock(mark, ssh_client):
        cmd = GkMark.bash_postgres_cmd(f"""SELECT PLU, ALCCODE, CREATION_TIMESTAMP, AMCCODE
    from EGAIS_EXCISE_STAMPS_STOCK where AMCCODE = '{mark}'""")
        std_in, out, std_err = ssh_client.exec_command(cmd)
        out = out.read().decode().strip()
        return out

    def result_egais_stamps(mark, ssh_client):
        cmd = GkMark.bash_postgres_cmd(f"""SELECT 'Марка в XRG_EGAIS_EXCISE_STAMPS:', *
    from XRG_EGAIS_EXCISE_STAMPS where EXCISE_STAMP = '{mark}'""")
        std_in, out, std_err = ssh_client.exec_command(cmd)
        out = out.read().decode().strip()
        return out

    def result_transport_module(mark, ssh_client):
        cmd = GkMark.bash_postgres_cmd(f"""SELECT * 
    from XRG_TRANSPORT_MODULE where TRANSACTION ilike '%{mark}%'""")
        std_in, out, std_err = ssh_client.exec_command(cmd)
        out = out.read().decode().strip()
        return out

    def ssh_connection(bo):
        """
        Функция подключения по ssh к серверу магазина
        :return: client
        """
        client = paramiko.SSHClient()  # создаем экземпляр класса paramiko.SSHClient в переменной client
        client.set_missing_host_key_policy(
            paramiko.AutoAddPolicy())  # устанавливаем политику подключения к серверам без известного ключа хоста. Иначе получим исключение SSHException Server 'наш ВО сервер' not found in known_hosts, т.е. не найден ключ для хоста
        try:
            client.connect(hostname='BO-' + bo, username=login_server_gk, password=pass_server_gk, port=port_server_gk,
                           timeout=timeout_server_gk)  # подключаемся к серверу
        except:
            client = 1
        return client  # возвращаем client как результат выполнения функции. client может быть объектом подключения, либо 1, если подключение не удалось


if __name__ == "__main__":
    import sys

    QtWidgets.QApplication.setStyle('fusion')
    app = QtWidgets.QApplication(sys.argv)
    logger = Loggers.logging(app, "MainWindow", "DEBUG")
    logger.info("============================")
    logger.info("started")

    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    bacchus_mark = BacchusMark(None, None, None, None)
    gk_mark = GkMark()
    sys.exit(app.exec_())
