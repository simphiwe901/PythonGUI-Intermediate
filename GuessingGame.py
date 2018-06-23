# Guessing game -OOP
# uses PyQt4 to dispay interface
# Simphiwe Mchunu
# 04 March 2016


import sys
from PyQt4 import QtGui
import random


class Guessgame(QtGui.QWidget):
    '''Constructor that initialises variables'''
    def __init__(self,parent= None):
        QtGui.QWidget.__init__(self,parent)
        self.random_integer = random.randint(1,10)
        self.setWindowTitle('Guessing Game')
        self.setGeometry(500,200,150,200)
        self.integerholder1 = QtGui.QLabel('',self) # place holder to hold the first attempt in line edit
        self.integerholder2 = QtGui.QLabel('',self) # place holder to hold the second attempt in line edit
        self.integerholder3 = QtGui.QLabel('',self) # place holder to hold the third attempt in line edit
        self.textholder1 = QtGui.QLabel('',self) # place holder to hold the first text in line edit
        self.textholder2 = QtGui.QLabel('',self) # place holder to hold the second text in line edit
        self.textholder3 = QtGui.QLabel('',self) # place holder to hold the third text in line edit
        self.controler = 1

        '''variables to store the guesses'''
        self.big_guess = 'Too big'
        self.small_guess = 'Too small'
        self.correct_guess = 'Correct!'

        '''Creates default picture and background colour'''
        self.pixmap1 = QtGui.QPixmap('mickey.gif')
        self.pic_label1 = QtGui.QLabel(self)
        self.pic_label1.setPixmap(self.pixmap1)
        self.red_colour()
        self.setAutoFillBackground(True)
        '''Creates widgets to be displayed on the main window'''
        self.guess = QtGui.QLabel('Guesses:',self)
        self.guess.setFont(QtGui.QFont('Arial Black',11,1))
        self.guess1 = QtGui.QLabel('Guess1:',self)
        self.guess2 = QtGui.QLabel('Guess2:',self)
        self.guess3 = QtGui.QLabel('Guess3:',self)
        self.line_edit = edit = QtGui.QLineEdit()
        self.guess_button =QtGui.QPushButton('Guess') # create push button for guess
        self.guess_button.clicked.connect(self.return_guess) # connect the guess button to return_guess slot method
        '''Creates widgets to be displayed on the main window'''
        self.interface = QtGui.QLabel('Interface:',self)
        self.interface.setFont(QtGui.QFont('Arial Black',11,1))
        self.picture = QtGui.QLabel('Picture:',self)
        self.colour = QtGui.QLabel('Colour:',self)
        self.change_button = QtGui.QPushButton('Change')
        self.change_button.clicked.connect(self.colour_change) # connect the change button to colour_change slot method
        self.change_button.clicked.connect(self.picture_change) # connect the change button to colour_change slot method
        self.close_button =QtGui.QPushButton('Close') # create push button for close
        self.close_button.clicked.connect(self.close_game) # connect the close_button to close_game slot method
        self.newgame_button = QtGui.QPushButton('New Game') # create push button for new game
        self.newgame_button.clicked.connect(self.new_game_button) # connect the newgame_button to new_game_button slot method

        '''Combo box for pictures'''
        self.combo_box_picture = QtGui.QComboBox()
        self.combo_box_picture.addItem('mickey')
        self.combo_box_picture.addItem('pluto')
        self.text = self.combo_box_picture.currentText()
        '''Combo box for colour'''
        self.combo_box_colour = QtGui.QComboBox()
        self.combo_box_colour.addItem('red')
        self.combo_box_colour.addItem('blue')
        self.text = self.combo_box_colour.currentText()


        self.grid1 = QtGui.QGridLayout() # create grid layout
        '''Add widgets to the main window'''
        self.grid1.addWidget( self.pic_label1,0,0,8,1)
        self.grid1.addWidget(self.guess,0,1)
        self.grid1.addWidget(self.guess1,1,1)
        self.grid1.addWidget(self.guess2,2,1)
        self.grid1.addWidget(self.guess3,3,1)
        self.grid1.addWidget(self.line_edit,4,2)
        self.grid1.addWidget(self.guess_button,4,3)
        self.grid1.addWidget(self.interface,5,1)
        self.grid1.addWidget(self.picture,6,1)
        self.grid1.addWidget(self.combo_box_picture,6,2)
        self.grid1.addWidget(self.colour,7,1)
        self.grid1.addWidget(self.combo_box_colour,7,2)
        self.grid1.addWidget(self.change_button,7,3)
        self.grid1.addWidget(self.close_button,8,1)
        self.grid1.addWidget(self.newgame_button,8,2)
        self.grid1.addWidget(self.integerholder1,1,2)
        self.grid1.addWidget(self.integerholder2,2,2)
        self.grid1.addWidget(self.integerholder3,3,2)
        self.grid1.addWidget(self.textholder1,1,3)
        self.grid1.addWidget(self.textholder2,2,3)
        self.grid1.addWidget(self.textholder3,3,3)
        self.setLayout(self.grid1) # set grid layout
    '''colour change slot method'''
    def colour_change(self):
        self.sm = self.combo_box_colour.currentText()
        if self.sm == 'blue':
            self.blue_colour()
        else:
            self.red_colour()
    '''red colour slot method'''
    def red_colour(self):
        self.setPalette(QtGui.QPalette(QtGui.QColor('red')))
        self.setAutoFillBackground(True)
    '''blue colour slot method'''
    def blue_colour(self):
        self.setPalette(QtGui.QPalette(QtGui.QColor('blue')))
        self.setAutoFillBackground(True)
    '''mickey picture slot method'''
    def mickey_pic(self):
        self.pixmap2 = QtGui.QPixmap('mickey.gif')
        self.pic_label1.setPixmap(self.pixmap2)
    '''pluto picture method'''
    def pluto_pic(self):
        self.pixmap2 = QtGui.QPixmap('pluto.gif')
        self.pic_label1.setPixmap(self.pixmap2)
    '''slot method to alternate pictures'''
    def picture_change(self):
        self.pm = self.combo_box_picture.currentText()
        if self.pm == 'pluto':
            self.pluto_pic()
        else:
            self.mickey_pic()
    '''slot method to get the user's input and displays the results'''
    def return_guess(self):
        self.guess1 = self.line_edit.displayText()
        if int(self.guess1)>self.random_integer and self.controler==1:
            self.integerholder1.setText(self.guess1)
            self.textholder1.setText(self.big_guess)
            self.line_edit.clear()
            self.controler+=1
        elif int(self.guess1)>self.random_integer and self.controler==2:
            self.integerholder2.setText(self.guess1)
            self.textholder2.setText(self.big_guess)
            self.line_edit.clear()
            self.controler+=1
        elif int(self.guess1)>self.random_integer and self.controler==3:
            self.integerholder3.setText(self.guess1)
            self.textholder3.setText(self.big_guess)
            self.line_edit.clear()
            self.controler+=1
        if int(self.guess1)==self.random_integer and self.controler==1:
            self.integerholder1.setText(self.guess1)
            self.textholder1.setText(self.correct_guess)
            self.line_edit.clear()
            self.controler=0
        elif int(self.guess1)==self.random_integer and self.controler==2:
            self.integerholder2.setText(self.guess1)
            self.textholder2.setText(self.correct_guess)
            self.line_edit.clear()
            self.controler=0
        elif int(self.guess1)==self.random_integer and self.controler==3:
            self.integerholder3.setText(self.guess1)
            self.textholder3.setText(self.correct_guess)
            self.line_edit.clear()
            self.controler=0
        elif int(self.guess1)<self.random_integer and self.controler==1:
            self.integerholder1.setText(self.guess1)
            self.textholder1.setText(self.small_guess)
            self.line_edit.clear()
            self.controler+=1
        elif int(self.guess1)<self.random_integer and self.controler==2:
            self.integerholder2.setText(self.guess1)
            self.textholder2.setText(self.small_guess)
            self.line_edit.clear()
            self.controler+=1
        elif int(self.guess1)<self.random_integer and self.controler==3:
            self.integerholder3.setText(self.guess1)
            self.textholder3.setText(self.small_guess)
            self.line_edit.clear()
            self.controler+=1
    '''method that runs when the new game button is clicked...resets all values
    previously displayed'''
    def new_game_button(self):
        self.controler = 1
        self.random_integer = random.randint(1,10)
        self.integerholder1.clear()
        self.integerholder2.clear()
        self.integerholder3.clear()
        self.textholder1.clear()
        self.textholder2.clear()
        self.textholder3.clear()
    '''method for close button'''
    def close_game(self):
        sys.exit()

'''Enables the class to be executed properly'''
def main():
    app= QtGui.QApplication(sys.argv)
    widget= Guessgame()
    widget.show()
    sys.exit(app.exec_())
main()
