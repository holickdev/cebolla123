from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class FinalWin (QWidget):
    
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        
    def initUI(self):
        self.v_line = QVBoxLayout()
        self.label1 = QLabel("Indice de Rufier:")
        self.label2 = QLabel("Rendimiento Cardiaco:")
        self.v_line.addWidget(self.label1)
        self.v_line.addWidget(self.label2)
        self.setLayout(self.v_line)
    
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        
        self.show()