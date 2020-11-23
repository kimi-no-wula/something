import sys
from random import randint, choice

from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow


class YellowEllipse(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.setFixedSize(700, 800)
        self.setWindowTitle('main')
        self.do_paint = False
        self.btn_yellow_ellipse.clicked.connect(self.touched)

    def touched(self):
        self.paint()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            # Создаем объект QPainter для рисования
            self.qp = QPainter()
            # Начинаем процесс рисования
            self.qp.begin(self)
            self.draw_smth()
            # Завершаем рисование
            self.qp.end()
            self.do_paint = False

    def draw_smth(self):
        self.qp.setBrush(QColor(0, 0, 255))
        z, x, y = randint(5, 200), randint(5, 680), randint(5, 580)

        self.qp.setBrush(QColor('yellow'))
        self.qp.drawEllipse(x, y, z, z)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowEllipse()
    ex.show()
    sys.exit(app.exec())
