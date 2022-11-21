import random
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Рисование')
        self.btn = QPushButton('Рисовать', self)
        self.btn.move(100, 250)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setPen(QColor(255, 255, 0))
        for _ in range(1):
            r = random.randint(20, 100)
            qp.drawEllipse(random.randint(50, 150), random.randint(50, 150), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())