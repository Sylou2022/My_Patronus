
import my_patronus_model, my_patronus_view
from PyQt5.QtWidgets import QApplication

class MyPatronusController:
        def __init__(self):
                self.my_patronus_view_object = my_patronus_view.MyPatronusView()
                self.my_patronus_view_object.show()

if __name__ == "__main__":
        app = QApplication([])
        my_patronus_controller_object = MyPatronusController()
        app.exec_()