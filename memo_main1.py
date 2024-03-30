from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget

from memo_app import app
from memo_data1 import *
from memo_main_layout1 import *
from memo_card_layout import *
from memo_edit_layout1 import txt_Question, txt_Answer, txt_Wrong1, txt_Wrong2, txt_Wrong3

main_width, main_height = 1000, 450 
card_width, card_height = 600, 500 
time_unit = 1000     
    
questions_listmodel = QuestionListModel() 
frm_edit = QuestionEdit(0, txt_Question, txt_Answer, txt_Wrong1, txt_Wrong2, txt_Wrong3) 
radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4] 
frm_card = 0 
timer = QTimer() 
win_card = QWidget() 
win_main = QWidget() 

def testlist():
    
    frm = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
    questions_listmodel.form_list.append(frm)
    frm = Question('Дім', 'house', 'horse', 'hurry', 'hour')
    questions_listmodel.form_list.append(frm)
    frm = Question('Мишка', 'mouse', 'mouth', 'muse', 'museum')
    questions_listmodel.form_list.append(frm)
    frm = Question('Число', 'number', 'digit', 'amount', 'summary')
    questions_listmodel.form_list.append(frm)

######################################     Функции для проведения теста:    #############################################

def set_card():
    win_card.resize(card_width, card_height)
    win_card.move(300, 300)
    win_card.setWindowTitle('Memory Card')
    win_card.setLayout(layout_card)

def sleep_card():
    win_card.hide()
    timer.setInterval(time_unit * box_Minutes.value() )
    timer.start()

def show_card():
    ''' вікно з таймером'''
    win_card.show()
    timer.stop()

def show_random():
    ''' показ випадковго запитання '''
    global frm_card 
    frm_card = random_AnswerCheck(questions_listmodel, lb_Question, radio_list, lb_Correct, lb_Result)
    
    frm_card.show()
    show_question()

def click_OK():
    ''' перевірка запитання або нове запитання '''
    if btn_OK.text() != 'Наступне запитання':
        frm_card.check()
        show_result()
    else:
        show_random()

def back_to_menu():
    ''' повернення до меню '''
    win_card.hide()
    win_main.showNormal()


def set_main():
    ''' вигляд головного вікна'''
    win_main.resize(main_width, main_height)
    win_main.move(100, 100)
    win_main.setWindowTitle('Список запитань')
    win_main.setLayout(layout_main)

def edit_question(index):
    ''' загрузка в форму запитання всіх об'єктів '''
    if index.isValid():
        i = index.row()
        frm = questions_listmodel.form_list[i]
        frm_edit.change(frm)
        frm_edit.show()

def add_form():
    ''' нове запитання '''
    questions_listmodel.insertRows() 
    last = questions_listmodel.rowCount(0) - 1   
                                                
    index = questions_listmodel.index(last) 
    list_questions.setCurrentIndex(index) 
    edit_question(index)    
    txt_Question.setFocus(Qt.TabFocusReason)

def del_form():
    ''' переключення фокуса + видалення запитання '''
    questions_listmodel.removeRows(list_questions.currentIndex().row())
    edit_question(list_questions.currentIndex())

def start_test():
    ''' показ випадкового запитання'''
    show_random()
    win_card.show()
    win_main.showMinimized()

def connects():
    list_questions.setModel(questions_listmodel) 
    list_questions.clicked.connect(edit_question) 
    btn_add.clicked.connect(add_form) 
    btn_delete.clicked.connect(del_form) 
    btn_start.clicked.connect(start_test) 
    btn_OK.clicked.connect(click_OK) 
    btn_Menu.clicked.connect(back_to_menu) 
    timer.timeout.connect(show_card) 
    btn_Sleep.clicked.connect(sleep_card) 

testlist()
set_card()
set_main()
connects()
app.setStyleSheet("""
    QWidget {
        background-color: plum ;
        color : #ffffff;
        font-size: 25px;
    }

    QPushButton {
        background-color: orchid;
        color : #aaaaff;
        border-radius: 7px ;
        border-color: #3232ff;
        border-style: hidden;
        border-width: 5px;
        min-height: 20px;
        font-size: 25px;
        font-family: none;

    }
                  
    QPushButton:hover{
        background-color: lavender;
    }

    QLabel {
        background-color: violet ;
        color : #ffffff;
        font-size: 25px;
    }
    
    QTextEdit {  
        background-color: orchid ;
        color : violet;
        font-size: 25px;
    }
    
    QListWidget {
        background-color: orchid ;
        color : #ffffff;
        font-size: 25px;
    }
    
    QLineEdit {
        background-color: orchid ;
        color : #ffffff;
        font-size: 25px;
    }
""")
win_main.show()
app.exec_()