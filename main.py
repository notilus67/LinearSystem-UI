from graphDisplay import *
from simulator_alpha import *
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
import sys

class parentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_Panel()
        self.main_ui.setupUi(self)

class childWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_Display()
        self.child.setupUi(self)


if __name__=='__main__':

    app=QApplication(sys.argv)
    window=parentWindow()
    child=childWindow()

    #通过toolButton将两个窗体关联
    btn=window.main_ui.start
    btn.clicked.connect(child.show)

    # 显示
    window.show()
    sys.exit(app.exec_())