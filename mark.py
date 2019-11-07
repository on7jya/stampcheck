# -*- coding: utf-8 -*-
import os
from threading import Thread

import paramiko
import urllib3
from bs4 import BeautifulSoup

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
        self.mark_line.setMaxLength(155)
        self.mark_line.setObjectName("mark")
        self.mark_line.setText(
            '1702002135294910180017Z7Z4NERQB4FWB4T5WMZTABH4E5DXSQIWJS6PAORZFTF2SKFEIG2YDWGLGAZK2U2XCFI7VT3WJXHCP227UAYM2L4TNYCWL67RBCRBMRJRAVKWJDEECXIZQCO4AOK47U4Y')

        self.text = QtWidgets.QTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(10, 475, 1280, 580))
        self.text.setObjectName("text")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)  # Запросить в GK и Бахусе
        self.pushButton.setGeometry(QtCore.QRect(1020, 10, 141, 21))
        self.pushButton.setObjectName("pushButton")

        main_window.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.table_plu_alccode = QtWidgets.QTableWidget(self.centralwidget)
        self.table_plu_alccode.setGeometry(10, 50, 1280, 160)
        self.table_plu_alccode.setColumnCount(12)
        self.table_plu_alccode.setRowCount(3)

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
        self.table_ttn_amc.setGeometry(10, 160, 1280, 110)
        self.table_ttn_amc.setColumnCount(14)
        self.table_ttn_amc.setRowCount(3)

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
        self.table_ttn_amc.setAlternatingRowColors(True)
        self.table_ttn_amc.horizontalHeader().setStretchLastSection(True)

        self.table_ttn_amc.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

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
        self.table_gk_cache.setGeometry(10, 270, 1280, 160)
        self.table_gk_cache.setColumnCount(7)
        self.table_gk_cache.setRowCount(2)

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

        self.table_gk_cache.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem('Завод'))
        self.table_gk_cache.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem('Агент'))
        self.table_gk_cache.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem('FSRAR_ID'))
        self.table_gk_cache.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem('IP UTM'))
        self.table_gk_cache.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem('Кеш'))
        self.table_gk_cache.setHorizontalHeaderItem(5, QtWidgets.QTableWidgetItem('Продажа'))
        self.table_gk_cache.setHorizontalHeaderItem(6, QtWidgets.QTableWidgetItem('Запросы в УТМ'))

        self.table_gk_cache = self.table_gk_cache

        ########################################################
        self.table_gk_transport_module = QtWidgets.QTableWidget(self.centralwidget)
        self.table_gk_transport_module.setGeometry(10, 350, 1280, 324)
        self.table_gk_transport_module.setColumnCount(15)
        self.table_gk_transport_module.setRowCount(10)

        self.table_gk_transport_module.setStyleSheet("QTableWidget {\n"
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
        # Сортировка по щелчку на заголовке столбца
        self.table_gk_transport_module.setSortingEnabled(True)
        self.table_gk_transport_module.verticalHeader().setVisible(True)
        self.table_gk_transport_module.verticalHeader().setDefaultSectionSize(90)
        self.table_gk_transport_module.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignTop)

        self.table_gk_transport_module.setAlternatingRowColors(True)
        self.table_gk_transport_module.horizontalHeader().setStretchLastSection(True)

        self.table_gk_transport_module.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem('SAP'))
        self.table_gk_transport_module.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem('Чек'))
        self.table_gk_transport_module.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem('Статус'))
        self.table_gk_transport_module.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem('POS'))
        self.table_gk_transport_module.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem('Сумма'))
        self.table_gk_transport_module.setHorizontalHeaderItem(5, QtWidgets.QTableWidgetItem('PLU'))
        self.table_gk_transport_module.setHorizontalHeaderItem(6, QtWidgets.QTableWidgetItem('Наимен-е PLU'))
        self.table_gk_transport_module.setHorizontalHeaderItem(7, QtWidgets.QTableWidgetItem('EAN'))
        self.table_gk_transport_module.setHorizontalHeaderItem(8, QtWidgets.QTableWidgetItem('Дата'))
        self.table_gk_transport_module.setHorizontalHeaderItem(9, QtWidgets.QTableWidgetItem('Смена'))
        self.table_gk_transport_module.setHorizontalHeaderItem(10, QtWidgets.QTableWidgetItem('Фискал'))
        self.table_gk_transport_module.setHorizontalHeaderItem(11, QtWidgets.QTableWidgetItem('Подпись'))
        self.table_gk_transport_module.setHorizontalHeaderItem(12, QtWidgets.QTableWidgetItem('URL'))
        self.table_gk_transport_module.setHorizontalHeaderItem(13, QtWidgets.QTableWidgetItem('Ошибки'))
        self.table_gk_transport_module.setHorizontalHeaderItem(14, QtWidgets.QTableWidgetItem('XML'))

        self.table_gk_transport_module = self.table_gk_transport_module

        # self.checker_fsrar_js = QtWidgets.QTextEdit(self.centralwidget)
        # self.checker_fsrar_js.setGeometry(QtCore.QRect(1090, 30, 205, 570))
        # self.checker_fsrar_js.setObjectName("checker_fsrar_js")
        # self.checker_fsrar_js.setFont(QtGui.QFont("Times", 7))

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        """
        Действия и подписи на форме
        """
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", 'Проверка марки'))

        self.pushButton.setText(_translate("main_window", "Запросить"))
        try:
            self.pushButton.clicked.connect(self.clear_text)

            self.pushButton.clicked.connect(lambda: self.table_plu_alccode.clearContents())
            self.pushButton.clicked.connect(lambda: self.table_ttn_amc.clearContents())
            self.pushButton.clicked.connect(lambda: self.table_gk_cache.clearContents())
            self.pushButton.clicked.connect(lambda: self.table_gk_transport_module.clearContents())
            # self.pushButton.clicked.connect(BacchusMark.get_mark_bacchus)
            self.pushButton.clicked.connect(GkMark.get_mark_gk)

            # self.pushButton.clicked.connect(EgaisMark.start_check_fsrar_js)

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
        _result = _result.replace('(', '')
        _result = _result.replace(')', '')
        _result = _result.replace('-', '')
        _result = _result.replace('.', '')
        _result = _result.replace(',', '')
        return _result

    def get_len_mark(self, _mark):
        """
        Получение длины марки
        """
        _result = len(_mark)
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
            mark_select_incoming_oracle = f"""
select /*+ PARALLEL(6) */ DISTINCT
    C_ORG_DIVISIONS.CODV_CODE
  , C_ORG_DIVISIONS.CODV_NAME
  , case when INC.BAMC_STATUS is null then B_AMC.BAMC_STATUS else INC.BAMC_STATUS end
  , to_char(B_AMC.BAMC_DATE, 'dd.mm.rrrr hh24:mi:ss') BAMC_DATE
  , INC.BINC_TRANSACTIONID
  , INC.BINC_TRANSACTIONDATE
  , INC.SDSS_CODE
  , INC.EWBH_WBNUMBER
  , INC.EWBH_WBREGID
  , INC.EWBH_CLIENTID
  , INC.EWBS_NAME
  , INC.EFB_F2REGID
  , INC.EFB_IS_MARK
  , INC.BBP_MARK
  , INC.BAMC_AMC
from B_AMC
INNER JOIN C_ORG_DIVISIONS ON B_AMC.CODV_ID = C_ORG_DIVISIONS.CODV_ID
LEFT JOIN
  (SELECT
  /*+ PARALLEL(6) */ DISTINCT
    CODV_CODE
  , CODV_NAME
  , BAMC.BAMC_LID
  , BAMC.BAMC_STATUS || ' - ' || B_AMC_STATUSES.BAMC_DESCR BAMC_STATUS
  , to_char(BAMC_DATE, 'dd.mm.rrrr hh24:mi:ss') BAMC_DATE
  , BINC_TRANSACTIONID
  , to_char(BINC_TRANSACTIONDATE, 'dd.mm.rrrr') BINC_TRANSACTIONDATE
  , SDSS_CODE
  , W.EWBH_WBNUMBER
  , W.EWBH_WBREGID
  , W.EWBH_CLIENTID
  , WS.EWBS_NAME
  , FE.EFB_F2REGID
  , case when FE.EFB_IS_MARK = '1' then 'помарка'
        when FE.EFB_IS_MARK = '0' or FE.EFB_IS_MARK is null then 'партионка'
        else null end EFB_IS_MARK
  , to_char(BBP_MARK) BBP_MARK
  , BAMC_AMC
FROM B_INCOMING I
  left JOIN B_INCOMING_DETAILS D ON D.BINC_ID = I.BINC_ID
  left JOIN B_INCOMING_DETAILS_FB F ON F.BIND_ID = D.BIND_ID
  left JOIN S_DOCSTATUSES ON I.DOC_STATUS = S_DOCSTATUSES.SDSS_ID
  left join E_WAYBILL W on I.EWBH_ID = W.EWBH_ID
  left join E_WAYBILL_STATUSES WS on W.EWBH_STATUS = WS.EWBS_CODE
  left JOIN B_BOXPOS B ON B.BIND_ID = D.BIND_ID
  left JOIN B_BOXPOS_BAMC_REL R ON R.BBP_ID = B.BBP_ID
  left JOIN B_AMC BAMC ON BAMC.BAMC_LID = R.BAMC_LID
  left JOIN B_AMC_STATUSES ON BAMC.BAMC_STATUS = B_AMC_STATUSES.BAMC_STATUS
  left JOIN E_FB FE ON FE.EFB_ID = F.EFB_ID
  INNER JOIN C_ORG_DIVISIONS ON BAMC.CODV_ID = C_ORG_DIVISIONS.CODV_ID
  where BAMC.BAMC_AMC = '{mark}' ORDER BY FE.EFB_F2REGID)
  INC ON B_AMC.BAMC_LID = INC.BAMC_LID AND C_ORG_DIVISIONS.CODV_CODE = INC.CODV_CODE
where B_AMC.BAMC_AMC = '{mark}'
ORDER BY 6, 12 """

            cursor_from_inc = db_mark.cursor()
            cursor_from_inc.execute(mark_select_incoming_oracle)
            result_mark_from_inc = cursor_from_inc.fetchall()
            cursor_from_inc.close()

            mark_select_amc_oracle = f"""
SELECT
  /*+ PARALLEL(10) */  DISTINCT
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
  INNER JOIN B_STOCKENTRY_AMC B ON BAMC.CODV_ID = B.CODV_ID AND BAMC.BAMC_LID = B.BAMC_LID
  INNER JOIN B_STOCKENTRY BS ON BS.BSTE_ID = B.BSTE_ID
  INNER JOIN E_FB FE ON FE.EFB_ID = BS.EFB_ID AND BS.ROW_STATUS = 'A'
  INNER JOIN C_ARTICLES CART ON BS.CART_ID = CART.CART_ID
  INNER JOIN E_ALCCODES EA ON EA.EACC_ALCCODE = FE.EFB_ALCCODE
  INNER JOIN C_ORG_DIVISIONS ON BS.CODV_ID = C_ORG_DIVISIONS.CODV_ID
            where BAMC_AMC = '{mark}' """

            cursor_from_amc = db_mark.cursor()
            cursor_from_amc.execute(mark_select_amc_oracle)
            result_mark_from_amc = cursor_from_amc.fetchall()
            cursor_from_amc.close()

            if len(mark) < 100 or result_mark_from_amc.__len__ == 0:
                mark_select_old_amc_oracle = f"""
SELECT   /*+ PARALLEL(4) */  DISTINCT
        'партионка'
      , CART.CART_CODE
      , CART.CART_NAME
      , to_char(CART.CART_ALCVOLUME)
      , to_char(CART.CART_INHAL)
      , to_char(CART.CART_CODERAR)
      , getalcode(BAMC.BAMC_AMC) "АЛКОКОД"
      , EA.EACC_FULLNAME
      , to_char(EA.EACC_ALCVOLUME)
      , to_char(EA.EACC_CAPACITY)
      , to_char(EA.EACC_PRODUCTVCODE)
      , BAMC.BAMC_AMC
    FROM B_AMC BAMC
      left JOIN C_ORG_DIVISIONS ON BAMC.CODV_ID = C_ORG_DIVISIONS.CODV_ID
      left JOIN E_ALCCODES EA ON EA.EACC_ALCCODE = getalcode(BAMC.BAMC_AMC)
      left join B_ALCCODES_TO_ARTICLES aa on EA.eacc_alccode = aa.BATA_ALC_CODE and aa.DOC_STATUS = '263'
      left JOIN C_ARTICLES CART ON aa.BATA_ARTICLE = CART.CART_ID
     where BAMC_AMC = '{mark}' """

                cursor_from_old_amc = db_mark.cursor()
                cursor_from_old_amc.execute(mark_select_old_amc_oracle)
                result_mark_from_old_amc = cursor_from_old_amc.fetchall()
                cursor_from_old_amc.close()
                result_mark_from_amc = result_mark_from_old_amc

            for i, tuple_item in enumerate(result_mark_from_amc):
                for j, item in enumerate(tuple_item):
                    ui.table_plu_alccode.setItem(i, j, QtWidgets.QTableWidgetItem(item))

            ui.table_plu_alccode.resizeColumnsToContents()

            ui.table_ttn_amc.setRowCount(len(result_mark_from_inc))
            for i, tuple_item in enumerate(result_mark_from_inc):
                for j, item in enumerate(tuple_item):
                    ui.table_ttn_amc.setItem(i, j, QtWidgets.QTableWidgetItem(item))

            ui.table_ttn_amc.resizeColumnsToContents()

            codv_code = dict()
            for item_sap in result_mark_from_inc:
                mark_select_agent_oracle = f"""
                     SELECT max(t.a_agent_id), max(FSRAR_ID),
  CASE WHEN max(CODV_IPUTMINDEX) = 1 THEN max(CODV_IPUTM)
    WHEN max(CODV_IPUTMINDEX) = 2 THEN max(CODV_IPUTM2)
    ELSE NULL END
                        FROM a_agents_org_divisions_rel t INNER JOIN c_org_divisions c ON t.codv_id = c.codv_id
                        WHERE c.CODV_CODE = upper('{item_sap[0]}') """
                cursor_agent = db_mark.cursor()
                cursor_agent.execute(mark_select_agent_oracle)
                result_agent = cursor_agent.fetchall()
                cursor_agent.close()

                for item_agent in result_agent:
                    codv_code.update({item_sap[0]: item_agent})

            db_mark.close()
        except Exception as e:
            logger.error(e)
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
            codes = BacchusMark.get_mark_bacchus(bacchus_mark)
            counter = 0
            for code in codes:
                ssh_client = GkMark.ssh_connection(code)
                if ssh_client == 1:
                    pass
                else:
                    agent = codes.get(code)
                    GkMark.step_xrg_transport_module(mark, ssh_client, counter, code, agent)
                    counter += 1
                    return ssh_client
        except Exception as e:
            logger.error(e)

    def step_xrg_transport_module(mark, client, row, code, agent):
        """
        Получение информации о документе приемки из GK
        """
        try:
            status_egais_stock = GkMark.result_egais_stock(mark, client)
            agent_numb = str(agent[0])
            fsrar = str(agent[1])
            ip_utm = str(agent[2])
            ui.table_gk_cache.setItem(row, 0, QtWidgets.QTableWidgetItem(code))
            ui.table_gk_cache.setItem(row, 1, QtWidgets.QTableWidgetItem(agent_numb))
            ui.table_gk_cache.setItem(row, 2, QtWidgets.QTableWidgetItem(fsrar))
            ui.table_gk_cache.setItem(row, 3, QtWidgets.QTableWidgetItem(ip_utm))
            if status_egais_stock:
                ui.table_gk_cache.setItem(row, 4, QtWidgets.QTableWidgetItem('Марка есть в кеше GK'))
            else:
                ui.table_gk_cache.setItem(row, 4, QtWidgets.QTableWidgetItem('Марки нет в кеше GK'))

            status_egais_stamps = GkMark.result_egais_stamps(mark, client)
            if status_egais_stamps:
                ui.table_gk_cache.setItem(row, 5, QtWidgets.QTableWidgetItem('Есть продажа марки в GK'))
            else:
                ui.table_gk_cache.setItem(row, 5, QtWidgets.QTableWidgetItem('Нет продажи марки в GK'))

            status_transport_module = GkMark.result_transport_module(mark, client)
            if status_transport_module:
                ui.table_gk_cache.setItem(row, 6, QtWidgets.QTableWidgetItem('Есть запросы в УТМ в GK'))
                ui.table_gk_cache.resizeColumnsToContents()
            else:
                ui.table_gk_cache.setItem(row, 6, QtWidgets.QTableWidgetItem('Нет запросов в УТМ в GK'))
                ui.table_gk_cache.resizeColumnsToContents()

            status_transaction_module = GkMark.result_transaction_module(mark, client)
            if status_transaction_module:
                status_transaction_module = status_transaction_module.split('\n')

                for i, tuple_item in enumerate(status_transaction_module):
                    for j, item in enumerate(tuple_item.split('|')):
                        ui.table_gk_transport_module.setItem(i, j, QtWidgets.QTableWidgetItem(item))
                        ui.table_gk_transport_module.setColumnCount(len(tuple_item.split('|')))

                max_row_count_first = len(status_transaction_module)

                # ui.table_gk_transport_module.sortByColumn(5, QtCore.Qt.AscendingOrder)
                ui.table_gk_transport_module.setRowCount(max_row_count_first)
                ui.table_gk_transport_module.resizeColumnToContents(0)
                ui.table_gk_transport_module.resizeColumnToContents(1)
                ui.table_gk_transport_module.resizeColumnToContents(2)
                ui.table_gk_transport_module.resizeColumnToContents(3)
                ui.table_gk_transport_module.resizeColumnToContents(4)
                ui.table_gk_transport_module.resizeColumnToContents(5)
                ui.table_gk_transport_module.resizeColumnToContents(6)
                ui.table_gk_transport_module.resizeColumnToContents(7)
                ui.table_gk_transport_module.resizeColumnToContents(8)
                ui.table_gk_transport_module.setColumnWidth(9, 20)
                ui.table_gk_transport_module.setColumnWidth(10, 20)
                ui.table_gk_transport_module.setColumnWidth(11, 20)

            # UiMainWindow.setup_text(ui, f"Статус марки в BO-{code} xrg_transport_module:")
            # # UiMainWindow.setup_text(ui, str(status_transaction_module))
            # status = status_transaction_module.split('\n')
            # for item in status:
            #     UiMainWindow.setup_text(ui, str(item))
            #     UiMainWindow.setup_text(ui,
            #                             "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        except Exception as e:
            ui.statusbar_message(e)
            logger.error(e)

    def bash_postgres_cmd(query):
        cmd = "PGPASSWORD=gkretail /usr/bin/psql -h 127.0.0.1 -U gkretail -d postgres -t -A -F\"|\" --pset pager=off -c \"" + query + ";\""
        return cmd

    def result_transaction_module(mark, ssh_client):
        cmd = GkMark.bash_postgres_cmd(f"""
        SELECT distinct (select RETAIL_STORE_NUMBER from GK_STORE_DATA)
            , BONNR
            , case when belegstatus = '0' then 'создан' when belegstatus = '1' then 'отменен' when belegstatus = '2' then 'сторнирован' when belegstatus = '5' then 'оплачен' when belegstatus = '6' then 'отсрочек' when belegstatus = '7' then 'отложен' when belegstatus = '8' then 'забран' when belegstatus = '9' then 'аннулирован' else null end belegstatus
            , WORKSTATION_ID
            , AMOUNT
            , gk_bonposition.artnr
            , gk_bonposition.bontext
            , substr(substring(elem FROM 'ean...............'), 6, 15) ean_UTM
            , to_char(FINISH_TIME, 'yyyy.mm.dd hh24:mi:ss')
            , coalesce(FISCAL_DAY_NUMBER, '-')
            , coalesce(FISCAL_PRINTER_ID, '-')
            , coalesce(SIGN, '-')
            , coalesce(URL, '-')
            , coalesce(error_description, '-')
            , coalesce(TRANSACTION, '-')
FROM xrg_transport_module
  LEFT JOIN LATERAL unnest(
      string_to_array(xrg_transport_module.transaction, E'<Bottle ')) WITH ORDINALITY AS a(elem, nr) ON TRUE
  LEFT JOIN gk_bonkopf on xrg_transport_module.bon_seq_id = gk_bonkopf.bon_seq_id
  LEFT JOIN gk_bonposition ON xrg_transport_module.bon_seq_id = gk_bonposition.bon_seq_id
        AND gk_bonposition.ean = substr(substring(elem FROM 'ean...............'), 6, 15) 
WHERE 
a.nr != 1 and TRANSACTION ilike '%{mark}%'
and (
	substr(substring(ELEM FROM 'barcode........................................................................'), 9, 88)
	ilike '%{mark}%' OR
	substr(substring(ELEM FROM 'barcode.................................................................................................................................................................'),
				 9, 152) ilike '%{mark}%'
)
order by to_char(FINISH_TIME, 'yyyy.mm.dd hh24:mi:ss')""")
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


class EgaisMark:

    def __init__(self, bamc_amc):
        self.bamc_amc = bamc_amc
        self.clear_files()

    @staticmethod
    def clear_files():
        """
        Удаление старого файла с разгаданной капчей
        """
        if os.path.exists(os.getcwd() + '/check1_fsrar.html'):
            os.remove(os.getcwd() + '/check1_fsrar.html')
        logger.debug('delete successful')

    def run_js(path, mark, key):
        """
        Запуск javascriipt файла для подключения к check1.fsrar.ru
        """
        os.system('"' + path + '/phantomjs.exe" fsrar.js {} {}'.format(mark, key))

    def start_check_fsrar_js(self):
        """
        Получение, обработка и вывод результатов с check1.fsrar.ru
        """
        logger.debug('start_check_fsrar_js')
        path = os.getcwd()
        logger.debug(path)
        ui.checker_fsrar_js.setText('')
        mark = LogicForm.get_mark(ui)
        processing = True
        try:
            EgaisMark.clear_files()
        except Exception as e:
            print(str(e))
        tries = 1
        logger.debug(
            'Получаем данные из ЕГАИС. Марка: "' + mark + '"')
        while processing:
            try:
                EgaisMark.clear_files()
            except Exception as e:
                print(str(e))
            try:
                phantom = Thread(target=EgaisMark.run_js,
                                 args=(path, mark, client_key))
                phantom.start()
                phantom.join()
            except KeyboardInterrupt:
                logger.debug('Выполнение прервано пользователем')
                self.clear_files()
                return []
            except Exception as e:
                logger.error(e)
                print('Ошибка:', e)
                self.clear_files()
                return []

            try:
                logger.debug("6")
                try:
                    with open(os.getcwd() + '/check1_fsrar.html', encoding='utf-8') as f:
                        parsed = f.read()
                except Exception as e:
                    logger.error(e)
                logger.debug("7")

                try:
                    soup = BeautifulSoup(parsed, 'html.parser')
                    for ul in soup.find_all('ul'):
                        ul.name = 'qwerty'
                    for li in soup.find_all('li'):
                        li.name = 'qwerty'
                    for li in soup.find_all('h2'):
                        li.name = 'h3'
                    for li in soup.find_all('h1'):
                        li.name = 'h3'
                    soup.find('qwerty').clear()
                except Exception as e:
                    logger.error(e)
                logger.debug("8")

                ui.checker_fsrar_js.append('-------------------------')
                ui.checker_fsrar_js.append(soup.prettify())
                ui.checker_fsrar_js.append('-------------------------')
                logger.debug("9")
                processing = False
                logger.debug("Successfully checked")
            except Exception as e:
                logger.error(e)
                tries += 1
                if tries > 3:
                    print('3 неудачные попытки. Переходим к следующей задаче')
                    processing = False
                print('Ошибка капчи. Повтор задачи')
                continue


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
