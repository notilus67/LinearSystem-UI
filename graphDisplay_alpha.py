import pyqtgraph as pg
import numpy as np

app = pg.mkQApp()

win = pg.GraphicsWindow()
win.setWindowTitle('Graph - simulator')
win.resize(800, 800)
pg.setConfigOptions(antialias=True)
pg.setConfigOption('background', '#FFF0F5')
pg.setConfigOption('foreground', '#F8F8FF')

class Ui_Display_alpha(object):
    def plotData(fx, fxe0, error, tm, n):
        x = np.linspace(0, tm-0.01, tm*100+1)
        fx1 = fx[0,:]
        fx2 = fx[1,:]
        fx3 = fx[2,:]
        fxe1 = fxe0[0,:]
        fxe2 = fxe0[1,:]
        fxe3 = fxe0[2,:]
        error1 = error[0,:]
        error2 = error[1,:]
        error3 = error[2,:]

        pen2 = pg.mkPen(color='#0000FF', width=3)
        pen1 = pg.mkPen(color='#DC143C', width=3)

        p1 = win.addPlot(left='State Value', bottom='t', title='row 1')
        p1.plot(x, fx1, pen=pen1)
        p1.plot(x, fxe1, pen=pen2)
        p1.showGrid(x=True, y=True)
        p1.setRange(xRange=[0, tm], yRange=[-5,5],padding=0)

        win.nextRow()
        p2 = win.addPlot(left='State Value', bottom='t', title='row 2')
        p2.plot(x, fx2, pen=pen1)
        p2.plot(x, fxe2, pen=pen2)
        p2.showGrid(x=True, y=True)
        p2.setRange(xRange=[0, tm], yRange=[-10, 10], padding=0)

        win.nextRow()
        p3 = win.addPlot(left='State Value', bottom='t', title='row 3')
        p3.plot(x, fx3, pen=pen1)
        p3.plot(x, fxe3, pen=pen2)
        p3.showGrid(x=True, y=True)
        p3.setRange(xRange=[0, tm], yRange=[-10, 10], padding=0)

        app.exec_()
