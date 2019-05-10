from numpy import * #导入numpy的库函数
import numpy as np  #这个方式使用numpy的函数时，需要以np.开头。
import control
from PyQt5 import QtCore, QtGui, QtWidgets
from control.matlab import *
from graphDisplay_alpha import *

class Ui_Panel(object):
    def setupUi(self, Panel):
        Panel.setObjectName("Panel")
        Panel.resize(583, 572)
        imgModel = QtGui.QPixmap('res/model.png')                    # （自定义）取得图片
        imgAttack = QtGui.QPixmap('res/attack.png')                  # （自定义）取得图片
        self.input_A = QtWidgets.QLineEdit(Panel)
        self.input_A.setGeometry(QtCore.QRect(80, 200, 471, 21))
        self.input_A.setText("")
        self.input_A.setObjectName("input_A")
        self.label_model = QtWidgets.QLabel(Panel)
        self.label_model.setGeometry(QtCore.QRect(30, 10, 81, 18))
        self.label_model.setObjectName("label_model")
        self.label_params = QtWidgets.QLabel(Panel)
        self.label_params.setGeometry(QtCore.QRect(30, 130, 101, 21))
        self.label_params.setObjectName("label_params")
        self.label_x0 = QtWidgets.QLabel(Panel)
        self.label_x0.setGeometry(QtCore.QRect(0, 170, 81, 18))
        self.label_x0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_x0.setAutoFillBackground(False)
        self.label_x0.setTextFormat(QtCore.Qt.AutoText)
        self.label_x0.setScaledContents(False)
        self.label_x0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_x0.setWordWrap(False)
        self.label_x0.setObjectName("label_x0")
        self.input_x0 = QtWidgets.QLineEdit(Panel)
        self.input_x0.setGeometry(QtCore.QRect(80, 170, 471, 21))
        self.input_x0.setText("")
        self.input_x0.setObjectName("input_x0")
        self.label_A = QtWidgets.QLabel(Panel)
        self.label_A.setGeometry(QtCore.QRect(0, 200, 81, 18))
        self.label_A.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_A.setAutoFillBackground(False)
        self.label_A.setTextFormat(QtCore.Qt.AutoText)
        self.label_A.setScaledContents(False)
        self.label_A.setAlignment(QtCore.Qt.AlignCenter)
        self.label_A.setWordWrap(False)
        self.label_A.setObjectName("label_A")
        self.input_C = QtWidgets.QLineEdit(Panel)
        self.input_C.setGeometry(QtCore.QRect(80, 260, 471, 21))
        self.input_C.setObjectName("input_C")
        self.label_C = QtWidgets.QLabel(Panel)
        self.label_C.setGeometry(QtCore.QRect(0, 260, 81, 18))
        self.label_C.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_C.setAutoFillBackground(False)
        self.label_C.setTextFormat(QtCore.Qt.AutoText)
        self.label_C.setScaledContents(False)
        self.label_C.setAlignment(QtCore.Qt.AlignCenter)
        self.label_C.setWordWrap(False)
        self.label_C.setObjectName("label_C")
        self.input_B = QtWidgets.QLineEdit(Panel)
        self.input_B.setGeometry(QtCore.QRect(80, 230, 471, 21))
        self.input_B.setObjectName("input_B")
        self.label_B = QtWidgets.QLabel(Panel)
        self.label_B.setGeometry(QtCore.QRect(0, 230, 81, 18))
        self.label_B.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_B.setAutoFillBackground(False)
        self.label_B.setTextFormat(QtCore.Qt.AutoText)
        self.label_B.setScaledContents(False)
        self.label_B.setAlignment(QtCore.Qt.AlignCenter)
        self.label_B.setWordWrap(False)
        self.label_B.setObjectName("label_B")
        self.input_D = QtWidgets.QLineEdit(Panel)
        self.input_D.setGeometry(QtCore.QRect(80, 290, 471, 21))
        self.input_D.setObjectName("input_D")
        self.label_D = QtWidgets.QLabel(Panel)
        self.label_D.setGeometry(QtCore.QRect(0, 290, 81, 18))
        self.label_D.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_D.setAutoFillBackground(False)
        self.label_D.setTextFormat(QtCore.Qt.AutoText)
        self.label_D.setScaledContents(False)
        self.label_D.setAlignment(QtCore.Qt.AlignCenter)
        self.label_D.setWordWrap(False)
        self.label_D.setObjectName("label_D")
        self.label_attack = QtWidgets.QLabel(Panel)
        self.label_attack.setGeometry(QtCore.QRect(30, 320, 241, 21))
        self.label_attack.setObjectName("label_attack")
        self.start = QtWidgets.QPushButton(Panel)
        self.start.setGeometry(QtCore.QRect(450, 500, 101, 41))
        self.start.setObjectName("start")
        self.radioButton = QtWidgets.QRadioButton(Panel)
        self.radioButton.setGeometry(QtCore.QRect(10, 360, 132, 22))
        self.radioButton.setObjectName("radioButton")
        self.label_dimension = QtWidgets.QLabel(Panel)
        self.label_dimension.setGeometry(QtCore.QRect(370, 20, 101, 21))
        self.label_dimension.setObjectName("label_dimension")
        self.input_dimension = QtWidgets.QLineEdit(Panel)
        self.input_dimension.setGeometry(QtCore.QRect(480, 20, 81, 21))
        self.input_dimension.setObjectName("input_dimension")
        self.label_duration = QtWidgets.QLabel(Panel)
        self.label_duration.setGeometry(QtCore.QRect(370, 50, 101, 21))
        self.label_duration.setObjectName("label_duration")
        self.input_duration = QtWidgets.QLineEdit(Panel)
        self.input_duration.setGeometry(QtCore.QRect(480, 50, 81, 21))
        self.input_duration.setObjectName("input_duration")
        self.input_sinA = QtWidgets.QLineEdit(Panel)
        self.input_sinA.setGeometry(QtCore.QRect(80, 400, 81, 21))
        self.input_sinA.setObjectName("input_sinA")
        self.input_sinOmega = QtWidgets.QLineEdit(Panel)
        self.input_sinOmega.setGeometry(QtCore.QRect(80, 430, 81, 21))
        self.input_sinOmega.setObjectName("input_sinOmega")
        self.label_sinOmega = QtWidgets.QLabel(Panel)
        self.label_sinOmega.setGeometry(QtCore.QRect(30, 430, 61, 21))
        self.label_sinOmega.setObjectName("label_sinOmega")
        self.label_sinA = QtWidgets.QLabel(Panel)
        self.label_sinA.setGeometry(QtCore.QRect(30, 400, 51, 21))
        self.label_sinA.setObjectName("label_sinA")
        self.input_sinK = QtWidgets.QLineEdit(Panel)
        self.input_sinK.setGeometry(QtCore.QRect(220, 430, 81, 21))
        self.input_sinK.setObjectName("input_sinK")
        self.input_sinPhi = QtWidgets.QLineEdit(Panel)
        self.input_sinPhi.setGeometry(QtCore.QRect(220, 400, 81, 21))
        self.input_sinPhi.setObjectName("input_sinPhi")
        self.label_sinK = QtWidgets.QLabel(Panel)
        self.label_sinK.setGeometry(QtCore.QRect(170, 430, 61, 21))
        self.label_sinK.setObjectName("label_sinK")
        self.label_sinPhi = QtWidgets.QLabel(Panel)
        self.label_sinPhi.setGeometry(QtCore.QRect(170, 400, 51, 21))
        self.label_sinPhi.setObjectName("label_sinPhi")
        self.label_sinTime = QtWidgets.QLabel(Panel)
        self.label_sinTime.setGeometry(QtCore.QRect(320, 400, 71, 21))
        self.label_sinTime.setObjectName("label_sinTime")
        self.input_sinTime = QtWidgets.QLineEdit(Panel)
        self.input_sinTime.setGeometry(QtCore.QRect(390, 400, 81, 21))
        self.input_sinTime.setObjectName("input_sinTime")
        self.display_model = QtWidgets.QLabel(Panel)
        self.display_model.setGeometry(QtCore.QRect(30, 40, 320, 80))
        self.display_model.setText("")
        self.display_model.setObjectName("display_model")
        self.display_model.setPixmap(imgModel)          # （自定义）绘图
        self.display_attack = QtWidgets.QLabel(Panel)
        self.display_attack.setGeometry(QtCore.QRect(80, 350, 251, 41))
        self.display_attack.setText("")
        self.display_attack.setObjectName("display_attack")
        self.display_attack.setPixmap(imgAttack)        # （自定义）绘图
        self.verify = QtWidgets.QPushButton(Panel)
        self.verify.setGeometry(QtCore.QRect(450, 450, 101, 41))
        self.verify.setObjectName("verify")
        self.verify.clicked.connect(self.preCompute)    # （自定义）Verify按钮绑定
        self.information = QtWidgets.QTextBrowser(Panel)
        self.information.setGeometry(QtCore.QRect(30, 460, 381, 81))
        self.information.setObjectName("information")
        self.retranslateUi(Panel)
        QtCore.QMetaObject.connectSlotsByName(Panel)
        Ui_Panel.preSet(self)                           # （自定义）预置默认值
        self.label_p1 = QtWidgets.QLabel(Panel)
        self.label_p1.setGeometry(QtCore.QRect(370, 80, 101, 21))
        self.label_p1.setObjectName("label_p1")
        self.label_p2 = QtWidgets.QLabel(Panel)
        self.label_p2.setGeometry(QtCore.QRect(370, 110, 101, 21))
        self.label_p2.setObjectName("label_p2")
        self.input_p1 = QtWidgets.QLineEdit(Panel)
        self.input_p1.setGeometry(QtCore.QRect(480, 80, 81, 21))
        self.input_p1.setObjectName("input_p1")
        self.input_p2 = QtWidgets.QLineEdit(Panel)
        self.input_p2.setGeometry(QtCore.QRect(480, 110, 81, 21))
        self.input_p2.setObjectName("input_p2")

    def retranslateUi(self, Panel):
        _translate = QtCore.QCoreApplication.translate
        Panel.setWindowTitle(_translate("Panel", "Form"))
        self.label_model.setText(_translate("Panel", "Model"))
        self.label_params.setText(_translate("Panel", "Parameters"))
        self.label_A.setText(_translate("Panel", "A"))
        self.label_C.setText(_translate("Panel", "C"))
        self.label_B.setText(_translate("Panel", "B"))
        self.label_D.setText(_translate("Panel", "D"))
        self.label_attack.setText(_translate("Panel", "Unknown Input (Attack)"))
        self.start.setText(_translate("Panel", "Start"))
        self.radioButton.setText(_translate("Panel", "sin"))
        self.label_dimension.setText(_translate("Panel", "Dimension"))
        self.label_duration.setText(_translate("Panel", "Duration(s)"))
        self.label_sinOmega.setText(_translate("Panel", "Omega"))
        self.label_sinA.setText(_translate("Panel", "A"))
        self.label_sinK.setText(_translate("Panel", "k"))
        self.label_sinPhi.setText(_translate("Panel", "Phi"))
        self.label_sinTime.setText(_translate("Panel", "Time(s)"))
        self.verify.setText(_translate("Panel", "Verify"))
        self.label_x0.setText(_translate("Panel", "x0"))
        self.label_p1.setText(_translate("Panel", "Pole Point1"))
        self.label_p2.setText(_translate("Panel", "Pole Point2"))

    def preCompute(self):
        '''
        判断是否可观
        :return: 文字提示
        '''
        A = Ui_Panel.toMatrix(self.input_A.text())
        B = Ui_Panel.toMatrix(self.input_B.text())
        C = Ui_Panel.toMatrix(self.input_C.text())
        D = Ui_Panel.toMatrix(self.input_D.text())
        n = int(self.input_dimension.text())
        u = [0]
        sinA = float(self.input_sinA.text())
        sinOmega = float(self.input_sinOmega.text())
        sinK = float(self.input_sinK.text())
        sinPhi = float(self.input_sinPhi.text())
        duration = float(self.input_duration.text())
        sinTime = float(self.input_sinTime.text())
        m = np.linalg.matrix_rank(C)
        q = np.linalg.matrix_rank(D)
        if m < q:
            self.information.setText('矩阵C的秩必须不小于矩阵D的秩序！')
            return
        if n == 3:              #  预置N矩阵
            N = [[0,0],[0,1],[1,0]]
        T = np.hstack((N,D))    #   拼接N D矩阵得到T矩阵
        T_inv = mat(np.linalg.inv(T))
        A1 = T_inv * mat(A) * mat(T)
        B1 = T_inv * mat(B)
        D1 = T_inv * mat(D)
        C0 = np.hstack((mat(C)*mat(N),mat(C)*mat(D)))
        (ha, wa) = A1.shape
        # 注意：python矩阵分割所用下标与matlab定义不同，从matlab过来冒号前的要-1
        A11 = A1[0:ha-q,0:wa-q]
        A12 = A1[0:ha-q,wa-q:wa]
        A21 = A1[ha-q:ha,0:wa-q]
        A22 = A1[ha-q:ha,wa-q:wa]
        (hb, wb) = B1.shape
        B11 = B1[0:hb-q,0:wb]
        B12 = B1[hb-q:hb,0:wb]

        Q = [[0],[1]]   # Q值自定义
        U = np.hstack((mat(C)*mat(D),Q))
        Um = np.linalg.inv(U)
        (hum,wum) = Um.shape
        U1 = Um[0:q,:]
        if m==q:
            U2 = zeros(m-q,wum)
        else:
            U2 = Um[q:m,:]
        AH = mat(A11)-mat(A12)*mat(U1)*mat(C)*mat(N)
        E1 = mat(A12)*mat(U1)
        C1 = mat(U2)*mat(C)*mat(N)

        ## 判断Luenberger观测器是否存在
        tmp = mat(C)*mat(D)
        if np.linalg.matrix_rank(tmp) == np.linalg.matrix_rank(D):
            flag1 = 1
        else:
            flag1 = 0
        (hc1, wc1) = C1.shape
        flag2 = 0
        (flag2, rank) = Ui_Panel.isObservable(AH, C1)
        existedText = self.information.toPlainText()        # 获取已存在的文本
        if (flag1 == 1) & (flag2 == 1):
            print('Luenberger观测器存在，降维系统可观')
            self.information.setText(existedText + '\nLuenberger观测器存在，降维系统可观')
            p1 = [complex(-6,1),complex(-6,-1)]
            p2 = [complex(-3,1),complex(-3,-1)]
            AHt = np.transpose(AH)
            C1t = np.transpose(C1)
            L1 = place(mat(AHt),mat(C1t),p1)
            L2 = place(mat(AHt),mat(C1t),p2)
            L1 = np.transpose(L1)
            L2 = np.transpose(L2)
            F1 = mat(AH)-mat(L1)*mat(C1)
            F2 = mat(AH)-mat(L2)*mat(C1)
            L1s = mat(L1)*mat(U2)+mat(E1)
            L2s = mat(L2)*mat(U2)+mat(E1)
            print(F1)
            print(zeros((n-q,n-q)))     # 这里的写法和matlab不一样
            tmp1 = np.hstack((F1,zeros((n-q,n-q))))
            tmp2 = np.hstack((zeros((n-q,n-q)),F2))
            F = np.row_stack((tmp1,tmp2))
            print(F)
            H = np.row_stack((L1s,L2s))
            S = np.row_stack((eye(n-q),eye(n-q)))
            G = np.row_stack((B11,B11))
            print(S)

            t0 = float(self.input_sinTime.text())           # 开始攻击时间
            tm = int(self.input_duration.text())            # 观测结束时刻
            x = Ui_Panel.toMatrix(self.input_x0.text())     # x初始状态值
            fx = (zeros((n,int(100*tm))))
            fx0 = (zeros((n, int(100*tm))))  # 注意写法
            fy = (zeros((n-1,int(100*tm))))
            fx[:,0] = x[:,0]
            fq = (zeros((n-1,int(100*tm))))
            fxe = (zeros((n,int(100*tm))))
            fz = (zeros((n+1,int(100*tm))))
            fq0 = (zeros((n-q,int(100*tm))))
            fxe0 = (zeros((n,int(100*tm))))
            error = (zeros((n, int(100 * tm))))
            xl = x[0:n-q,:]
            x0 = x

            for t in np.arange(0, tm, 0.01):
                if t<t0:
                    fx[:, int(100*t+1)] = np.transpose(mat(mat(x)+(mat(A)*mat(x)+mat(B)*mat(u))*0.01))
                    fx0[:, int(100*t+1)] = np.transpose(mat(mat(x)+(mat(A)*mat(x)+mat(B)*mat(u))*0.01))
                    fxe[:, int(100*t+1)] = np.transpose(mat(mat(x)+(mat(A)*mat(x)+mat(B)*mat(u))*0.01))
                    fxe0[:, int(100*t+1)] = np.transpose(mat(mat(x)+(mat(A)*mat(x)+mat(B)*mat(u))*0.01))
                    x = np.transpose(mat(fx[:,int(100*t+1)]))
                    fy[:, int(100*t+1)] = np.transpose(mat(C)*mat(x))
                else:
                    fx[:, int(100*t+1)] = np.transpose(mat(x)+(mat(A)*mat(x)+mat(B)*mat(u)+(2*sin(20*pi*t)+2))*0.01)
                    fx0[:, int(100 * t + 1)] = np.transpose(mat(x) + (mat(A) * mat(x) + mat(B) * mat(u)) * 0.01)
                    x = np.transpose(mat(fx[:,int(100*t+1)]))
                    x0 = np.transpose(mat(fx0[:,int(100*t+1)]))
                    fy[:, int(100 * t + 1)] = np.transpose(mat(C) * mat(x))
                    print(abs(mat(x[0,:]-x0[0,:])[0,0]))
                    if (abs(mat(x[0,:]-x0[0,:])[0,0]) > 0):
                        print('pass')
                        t_att = t
                        break
            print(t_att)
            #z = mat(S)*mat(np.hstack((eye(n-q),zeros((n-q,q)))))*mat(np.linalg.inv(T))*mat(x)
            #print(z)

            #for i in np.arange(0, t0, 0.01):
            #    fz[:,int(100*i+1)] = mat(z) + (mat(F)*mat(z)+mat(H)*mat(y)+mat(G)+mat(u))*0.01
            #print(fz[:,int(t0*100+1)])
            for t in np.arange(t0, tm-0.01, 0.01):
                #print(t)
                fx[:, int(100 * t + 1)] = np.transpose(mat(mat(x) + (mat(A) * mat(x) + mat(B) * mat(u)) * 0.01))
                x = np.transpose(mat(fx[:, int(100 * t + 1)]))
                fy[:, int(100 * t + 1)] = np.transpose(mat(C) * mat(x))
                y = np.transpose(mat(fy[:, int(100 * t + 1)]))
                #fz[:, int(100 * t + 1)] = np.transpose(mat(mat(z) + (mat(F) * mat(z) + mat(H) * mat(y) + mat(G) * mat(u)) * 0.01))
                #z = np.transpose(mat(fz[:, int(100 * t + 1)]))
                fq0[:, int(100 * t + 1)] = np.transpose(mat(mat(xl) + ((mat(AH)-mat(L1)*mat(C1))*mat(xl) + mat(B11)*mat(u)+mat(L1s)*mat(y))))*0.01
                xl = np.transpose(mat(fq0[:, int(100 * t + 1)]))
                fxe0[:, int(100 * t + 1)] = np.transpose(mat(T)*mat(np.row_stack((mat(xl),mat(mat(U1)*mat(y)-mat(U1)*mat(C)*mat(N)*mat(xl))))))
                #print(fxe0[:,int(100*t+1)])
                error = mat(fx)-mat(fxe0)
            Ui_Display_alpha.plotData(fx, fxe0, error, tm, n)  # 传递计算完毕的数组
        else:
            print('该系统不可观测')
            existedText = self.information.toPlainText()
            self.information.setText(existedText+'\n该系统不可观测！')

    def toMatrix(text):
        '''
        将输入的数字转为矩阵
        :param text: 矩阵元素字符串
        :return: 矩阵array
        '''
        # 将中文逗号替换为英文逗号
        text = text.replace('，', ',')
        text = text.replace('；', ';')

        # 切除矩阵元素前后的逗号
        if text[-1] == ',':
            text = text[:-1]
        if text[0] == ',':
            text = text[1:]
        if text[-1] == ';':
            text = text[:-1]
        if text[0] == ';':
            text = text[1:]

        numlist = []
        rowlist = text.split(';')
        matrix_height = len(rowlist)            # 获得矩阵的高
        matrix_hw = []

        for i in range(len(rowlist)):
            elementlist = rowlist[i].split(',')
            matrix_width = len(elementlist)     # 获得矩阵的宽
            for j in range(len(elementlist)):
                numlist.append(float(elementlist[j]))
        matrix_hw.append(matrix_height)
        matrix_hw.append(matrix_width)
        matrix = np.array(numlist).reshape(matrix_hw)
        #print(matrix)
        return matrix

    def preSet(self):
        '''
        预置输入
        '''
        self.input_A.setText('-2,-2,0;0,0,1;0,-3,-4')
        self.input_B.setText('1;0;0')
        self.input_C.setText('1,0,1;0,1,0')
        self.input_D.setText('1;-1;5')
        self.input_dimension.setText('3')
        self.input_duration.setText('8')
        self.input_sinTime.setText('0.5')
        self.input_sinA.setText('2')
        self.input_sinOmega.setText('20')
        self.input_sinK.setText('2')
        self.input_sinPhi.setText('0')
        self.radioButton.setChecked(True)
        self.input_x0.setText('5;5;5')

    def isObservable(A, C):
        AC = {}
        AC[0] = C
        for i in range(1, A.shape[0]):
            AC[i] = AC[i - 1].dot(A)
        print(AC.values())
        q = np.row_stack((AC.values()))
        print("系数矩阵为:", q)
        # 保证非奇异性
        z = q.dot(q.T)
        print(z)
        if np.linalg.det(z) != 0:
            print("非奇异矩阵，行列式为：", np.linalg.det(z))
        else:
            print("奇异矩阵行列式为：", np.linalg.det(z))
        print("矩阵的秩为", np.linalg.matrix_rank(q))
        if np.linalg.matrix_rank(z) != A.shape[0]:
            print("矩阵不可观")
            return 0, 0
        else:
            print("矩阵可观")
            return 1, np.linalg.matrix_rank(z)
