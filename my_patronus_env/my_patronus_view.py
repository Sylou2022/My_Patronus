from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

import os


class MyPatronusView(QMainWindow):

        def __init__(self):
                super(MyPatronusView, self).__init__()
                uic.loadUi(os.path.join(os.path.split(__file__)[0], "my_patronus.ui"), self)