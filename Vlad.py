from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from time import *
app = QApplication([])

window = QWidget()
window.setWindowTitle("Клікер")
window.resize(500,500)

t1=QLabel("Час")
t2=QLabel("0")
c1=QLabel("Лількість")
c1=QLabel("0")
b=QPushButton('Ok')
box_Minutes = QSpinBox()
box_Minutes.setValue(60)

laoyth_v = QVBoxLayout() 
laoyth_h1 = QVBoxLayout() 
laoyth_h2 = QVBoxLayout() 
laoyth_h1.addWidget(t1)
laoyth_h1.addWidget(c1)

laoyth_h2.addWidget(t2)
laoyth_h2.addWidget(c2)
laoyth_h1.addWidget(box_Minutea)

laoyth_v.addLayout(laoyth_h1)
laoyth_v.addLayout(laoyth_h2)
laoyth_v.addWidget(b)
window.setLayout(laoyth_v)
window.show()
time1=int(time())
start_c=0
def click():
    new_time=time()
    global start_c,time1
    start_c=start_c+1
    c2.setText(str(start_c))
    t=int(new_time-time1)
    t2.setText(str(t))
    if box_Minutes.value()==t:

        win=QMessageBox()
        win.setWindowTitle('Результат')
        win.setText('Дякуємо, ваш результат'+c2.text())
        win.show()
        win.exec_()

b.clicked.connect(clict)
app.exec_()