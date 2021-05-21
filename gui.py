import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit
from functools import partial

from frier import showsauteimage

class MemeFrierGUI(QApplication):
    def __init__(self):
        super(MemeFrierGUI, self).__init__([])
        #Initialize App
        self.UI = self.makeUI()

        #Show UI
        self.UI.show()

    def makeUI(self):
        #Make UI Base
        ui = QWidget()
        layout = QVBoxLayout()

        #Make UI Interactables
        self.input_path = QLineEdit('Insert File Path')
        self.saute_button = QPushButton('Saute')
        self.fry_button = QPushButton("Deepfry")
        self.nuke_button = QPushButton("Nuke")
        #self.save_button = QPushButton("Save")

        #Add functionality
        self.saute_button.clicked.connect(self.saute)
        #self.save_button.clicked.connect(save)       
        
        #Add to UI
        layout.addWidget(self.input_path)
        layout.addWidget(self.saute_button)
        layout.addWidget(self.fry_button)
        layout.addWidget(self.nuke_button)
        #layout.addWidget(self.save_button)

        #Commit UI
        ui.setLayout(layout)
        return ui

    def saute(self):
        path = self.input_path.text()
        showsauteimage(path)
