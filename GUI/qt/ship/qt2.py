#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we create a simple
window in PyQt5.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QFont

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)

    b = QLabel(w)
    b.setText("Hello World!")

    f = QFont("Times New Roman")
    f.setUnderline(True)
    b.setFont(f)
    # w.setGeometry(100, 100, 200, 50)
    b.move(50, 20)

    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())
