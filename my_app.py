from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

def next():
    print("Módulo de Enrique en construcción")

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle("Diagnóstico de Estado de Salud - Test de Ruffier")
main_win.resize(600, 400)

titulo = QLabel("Bienvenidos al programa de diagnóstico de estado de salud")
titulo.setStyleSheet("font-size: 18px; font-weight: bold; color: #2E4053;")
titulo.setAlignment(Qt.AlignCenter)

descripcion = QLabel(
    "Esta aplicación te permite realizar una evaluación inicial de tu condición física\n"
    "a través de la prueba de Ruffier, un método sencillo para estimar cómo responde\n"
    "tu corazón ante el esfuerzo físico.\n\n"
    "Durante la prueba deberás registrar tu frecuencia cardíaca en tres momentos:\n"
    "antes del ejercicio, justo después y un minuto más tarde.\n"
    "Con esos datos, el sistema calcula un índice que orienta tu nivel de resistencia\n"
    "y recuperación cardiovascular.\n\n"
    "Este diagnóstico tiene fines educativos y orientativos.\n"
    "No reemplaza la valoración médica profesional ni los exámenes clínicos.\n"
    "Ante cualquier duda o resultado anormal, consulta a tu médico de confianza."
)
descripcion.setWordWrap(True)
descripcion.setAlignment(Qt.AlignJustify)
descripcion.setStyleSheet("font-size: 14px; color: #1B2631;")

boton = QPushButton("Comenzar evaluación")
boton.setStyleSheet("font-size: 14px; padding: 8px 16px; background-color: #2471A3; color: white; border-radius: 6px;")
boton.clicked.connect(next)

layout = QVBoxLayout()
layout.setSpacing(20)
layout.addWidget(titulo)
layout.addWidget(descripcion)
layout.addWidget(boton, alignment=Qt.AlignCenter)

main_win.setLayout(layout)
main_win.show()

app.exec_()