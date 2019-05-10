# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import pyqtgraph as pg
import numpy as np
import array
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Display(object):
    app = QtGui.QApplication([])

    def setupUi(self, Display):
        Display.setObjectName("Display")
        Display.resize(776, 557)
        self.tabWidget = QtWidgets.QTabWidget(Display)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 741, 481))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 721, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.stateGraph = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.stateGraph.setContentsMargins(0, 0, 0, 0)
        self.stateGraph.setObjectName("stateGraph")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 721, 431))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.errorGraph = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.errorGraph.setContentsMargins(0, 0, 0, 0)
        self.errorGraph.setObjectName("errorGraph")
        self.tabWidget.addTab(self.tab_2, "")
        self.information2 = QtWidgets.QTextBrowser(Display)
        self.information2.setGeometry(QtCore.QRect(20, 500, 741, 41))
        self.information2.setObjectName("information2")
        self.retranslateUi(Display)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Display)

    def retranslateUi(self, Display):
        _translate = QtCore.QCoreApplication.translate
        Display.setWindowTitle(_translate("Display", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Display", "state"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Display", "error"))


    def plotData(fx, fxe0, error, tm):
        '''
        app = pg.mkQApp()
        t = np.arange(0, tm-0.01, 0.01)
        x = np.linspace(0, 6(np.pi, 100))
        y = np.sin(t)
        pg.plot(x, y, title=u'sample', left=u'state / x', bottom = u'time t / s')
        app.exec_()
        '''
        data_list = []
        pg.setConfigOptions(antialias=True)
        chart = Ui_Display.stateGraph.addWidget('State Graph')
        chart.plot(np.random.normal(size=500),pen=(200,0,0), name="real state")
        chart.plot(np.random.normal(size=500)+5,pen=(0,200,0), name="estimate state")

        print(error)