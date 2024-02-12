import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSlot
from sqlitedict import SqliteDict
from datetime import date,time
import random

# IMPORT GAME FILES
# GAME DATA V0.1

#from Bot import Bot
#from Player import Player

game_saves = SqliteDict("game_saves.db",autocommit=True) # GAME SAVES
CURRENT_CLASS = "WARRIOR"
ENEMY_HP = 50
LAST_POS_X = 167
LAST_POS_Y = 210
LAST_IMG = "sprites/movement/down_1.png"
CURR_POS_X = 0
CURR_POS_Y = 0
CURRENT_HP = 100
ACCOUNT_STATUS = "OFFLINE"
CURRENT_ACCOUNT = "NONE"
CURRENT_SKILL1 = "NONE"
CURRENT_SKILL2 = "NONE"
CURRENT_SPRITE = ""
ENEMY_SPRITE = ""
BUTTON_CSS = "resources/css/button.css"
GLOBAL_CSS = "resources/css/global.css"
ACC_ABT_CSS = "resources/css/acc_abt.css"
    
    
class Homepage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.width = 636
        self.height = 400
        self.title = "project SAYAKA: BETA"
        self.initUI()
        
    def initUI(self):
        self.setFixedSize(self.width,self.height)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("resources/logo.ico"))
        
        self.frame = QFrame(self)
        self.frame.setGeometry(40,80,141,221)
        
        self.LOGIN_STATUS = QLabel(f"STATUS : {ACCOUNT_STATUS} as {CURRENT_ACCOUNT}",self)
        self.LOGIN_STATUS.setGeometry(0,0,200,20)
        self.LOGIN_STATUS.setStyleSheet("color: white;")

        self.homeicon = QToolButton(self)
        self.homeicon.setGeometry(70,60,81,51)
        self.homeicon.setIcon(QIcon("resources/home_icon.png"))
        self.homeicon.setIconSize(QSize(120,120))
        self.homeicon.clicked.connect(self.animate)

        self.startbtn = QPushButton("START",self)
        self.startbtn.setGeometry(50,120,121,31)
        self.startbtn.clicked.connect(self.start_game_window)
        self.startbtn.setStyleSheet("""
        *:hover{
        background: blue;
        color: white;}
                                    """)
        
        self.accountbtn = QPushButton("ACCOUNTS",self)
        self.accountbtn.setGeometry(50,180,121,31)
        self.accountbtn.clicked.connect(self.start_account_window)
        self.accountbtn.setStyleSheet("""
        *:hover{
        background: blue;
        color: white;}
                                    """)
        
        self.aboutbtn = QPushButton("ABOUT",self)
        self.aboutbtn.setGeometry(50,240,121,31)
        self.aboutbtn.clicked.connect(self.start_about_window)
        self.aboutbtn.setStyleSheet("""
        *:hover{
        background: blue;
        color: white;}
                                    """)
        
        self.lbltitle = QLabel("project SAYAKA",self)
        self.lbltitle.setGeometry(310,150,261,51)
        self.lbltitle.setStyleSheet("""                           
background: transparent;
color: black;
font-style: italic;
font-size:40px;
text-decoration: underline;
""")
        
        self.lbltitle2 = QLabel("marsel.ywy",self)
        self.lbltitle2.setGeometry(400,200,91,21)
        self.lbltitle2.setStyleSheet("""
background: transparent;
color: black;
                                  """)
        
        self.show()
    
    @pyqtSlot()
    
    def animate(self):
        pass
    def start_game_window(self):
        if ACCOUNT_STATUS == "ONLINE":
            self.new_window = Game_Engine()
            self.new_window.setStyleSheet("""
            *{
    font-family: pixelated;
    font-size:18px;
    background-image: url(resources/bg.jpeg);
    }                                      """)
            self.new_window.show()
            self.hide()
        else:
            QMessageBox.information(self,"LOG IN FIRST!","Please LOGIN First to START!",QMessageBox.Ok,QMessageBox.Ok)
            
            
    def start_account_window(self):
        self.new_window = Account()
        
        with open(ACC_ABT_CSS, 'r') as f:
            self.new_window.setStyleSheet(f.read())
        
        self.hide()
        self.new_window.show()
    
    def start_about_window(self):
        self.new_window = About()
        with open(ACC_ABT_CSS, 'r') as f:
            self.new_window.setStyleSheet(f.read())
        self.new_window.show()

class Account(QMainWindow):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.width = 380
        self.height = 445
        self.title = "Account"
        self.today = date.today()
        self.account_list = game_saves.get('accounts',[])
        self.game_data = game_saves.get('gamesaves',[])
        self.initAccount()
    
    def initAccount(self):
        self.setFixedSize(self.width,self.height)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("resources/logo.ico"))
        
        self.back = QPushButton("BACK",self)
        self.back.clicked.connect(self.start_back_window)
        self.back.setStyleSheet("""
                                    *{
                                        background:red;
                                        border-radius:60px                        
                                    }
                                    *:hover{
                                        background: blue;
                                        color: white;
                                    }
                                    """)
        
        self.lblaccount = QLabel("ACCOUNT",self)
        self.lblaccount.setGeometry(160,10,151,61)
        
        self.lblusername = QLabel("Username",self)
        self.lblusername.setGeometry(50,100,91,31)
        self.lblusername.setStyleSheet("""
                                     background: transparent;
                                     font-size: 20px;
                                     """)       
        
        self.lblpassword = QLabel("Password",self)
        self.lblpassword.setGeometry(50,160,91,31)
        self.lblpassword.setStyleSheet("""
                                     background: transparent;
                                     font-size: 20px;
                                     """)
        
        self.tbusername = QLineEdit(self)
        self.tbusername.setGeometry(190,100,171,31)
        
        self.tbpassword = QLineEdit(self)
        self.tbpassword.setGeometry(190,160,171,31) 
        self.tbpassword.setEchoMode(QLineEdit.Password)
        
        self.frame = QLabel(self)
        self.frame.setGeometry(60,230,270,41)
        self.frame.setStyleSheet("""
                                 background: #333;
                                 """)
        if ACCOUNT_STATUS == "OFFLINE":
            self.loginbtn = QPushButton("LOG IN",self)
            self.loginbtn.setGeometry(70,240,75,23)
            self.loginbtn.clicked.connect(self.start_login_process)
            self.loginbtn.setStyleSheet("""
                                        *{
                                            background:red;
                                            border-radius:60px                        
                                        }
                                        *:hover{
                                            background: blue;
                                            color: white;
                                        }
                                        """)
            
            self.registerbtn = QPushButton("REGISTER",self)
            self.registerbtn.setGeometry(234,240,81,23)
            self.registerbtn.clicked.connect(self.start_register_process)
            self.registerbtn.setStyleSheet("""
                                        *{
                                            background:red;
                                            border-radius:60px                        
                                        }
                                        *:hover{
                                            background: blue;
                                            color: white;
                                        }
                                        """)
        else:
            self.curruser = QLabel(CURRENT_ACCOUNT,self)
            self.curruser.setGeometry(190,100,171,31) 
            
            self.lblpassword.hide()
            self.tbusername.hide()
            self.tbpassword.hide()
            self.logoutbtn = QPushButton("LOGOUT",self)
            self.logoutbtn.setGeometry(150,240,81,23)
            self.logoutbtn.clicked.connect(self.start_logout_process)
            self.logoutbtn.setStyleSheet("""
                                        *{
                                            background:red;
                                            border-radius:60px                        
                                        }
                                        *:hover{
                                            background: blue;
                                            color: white;
                                        }
                                        """)
            
    @pyqtSlot()
    def start_logout_process(self):
        global ACCOUNT_STATUS,CURRENT_ACCOUNT
        CURRENT_ACCOUNT = "NONE"
        ACCOUNT_STATUS = "OFFLINE"
        self.hide()
        self.new_window = Homepage()
        with open(GLOBAL_CSS, 'r') as f:
            self.new_window.setStyleSheet(f.read())
        self.new_window.show()
    def start_back_window(self):
        self.new_window = Homepage()
        
        with open(GLOBAL_CSS, 'r') as f:
            self.new_window.setStyleSheet(f.read())
        
        self.hide()
        self.new_window.show()
    def start_login_process(self):
        LOGIN_KEY = 0
        if self.tbusername.text() != "" and self.tbpassword.text() != "":
            for temp_account in self.account_list:
                if self.tbusername.text() == temp_account["Username"]:
                    if self.tbpassword.text() == temp_account["Password"]:
                        QMessageBox.information(self,"LOGIN SUCCESSFULY","LOGIN OK",QMessageBox.Ok,QMessageBox.Ok)
                        LOGIN_KEY = 2
                else:
                    if LOGIN_KEY == 2:
                        pass
                    else:
                        LOGIN_KEY = 1 # 1 MEANS USERNAME NOT FOUND
            if LOGIN_KEY == 2:
                global ACCOUNT_STATUS,CURRENT_ACCOUNT
                print("LOGIN_KEY = 1 , LOGIN SUCCESS")
                CURRENT_ACCOUNT = self.tbusername.text()
                ACCOUNT_STATUS = "ONLINE"
                self.hide()
                self.new_window = Homepage()
                
                with open(GLOBAL_CSS, 'r') as f:
                    self.new_window.setStyleSheet(f.read())
                
                self.new_window.show()
            elif LOGIN_KEY == 1:
                print("LOGIN_KEY : 1 Error Username or Password")
                QMessageBox.information(self,"Accounts","Wrong Username or Password!",QMessageBox.Ok,QMessageBox.Ok)
        else:
            QMessageBox.warning(self,"Empty Fields!","Make sure Fields are Complete!",QMessageBox.Ok,QMessageBox.Ok)
    def start_register_process(self):
        REGISTER_KEY = 0
        if self.tbusername.text() != '' and self.tbpassword.text() != '':
            for temp_account in self.account_list:
                if self.tbusername.text() == temp_account["Username"]:
                    QMessageBox.warning(self,"Same Username Found!","Please Try using a unique name!",QMessageBox.Ok,QMessageBox.Ok)
                    REGISTER_KEY = 1
            if REGISTER_KEY == 0:
                self.account_list.append({"Username":self.tbusername.text(),"Password":self.tbpassword.text()})
                game_saves["accounts"] = self.account_list
                QMessageBox.information(self,"Registered Successfuly!","Account Saved!",QMessageBox.Ok,QMessageBox.Ok)
                print(f"""
                      Account Registered!: 
                      Username: {self.tbusername.text()}
                      Password: {self.tbpassword.text()}
                      Registered On: {self.today}
                      
                      on target dictionary:
                      {self.account_list}
                      """)
        else:
            QMessageBox.warning(self,"Empty Fields!","Make sure Fields are Complete!",QMessageBox.Ok,QMessageBox.Ok)

class Game_Engine(QMainWindow):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.width = 632
        self.height = 371
        self.title = "Select Your Class"
        self.gameUI()

    def gameUI(self):
        enemy_level = "0"
        player_level = "0"
        self.setFixedSize(self.width,self.height)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("resources/logo.ico"))
        
        
        self.frame = QFrame(self)
        self.frame.setGeometry(129,189,371,101)
        self.frame.setStyleSheet("background: #333;")
        
        self.label = QLabel("               CLASS CHANGE!!!",self)
        self.label.setGeometry(100,100,451,80)
        self.label.setStyleSheet("""
                                 *{
                                 background: #333;
                                 font-size: 44px;
                                 text-align:center;
                                 color: blue;}
                                 """)
        
        self.warriorframe = QLabel(self)
        self.warriorframe.setPixmap(QPixmap("sprites/0.png"))
        self.warriorframe.setGeometry(150,190,71,91)
        self.warriorbtn = QPushButton("WARRIOR",self)
        self.warriorbtn.setGeometry(150,290,71,23)
        
        with open(BUTTON_CSS, 'r') as f:
            self.warriorbtn.setStyleSheet(f.read())
            
        self.warriorbtn.clicked.connect(self.warrior_class)
        
        self.thiefframe = QLabel(self)
        self.thiefframe.setPixmap(QPixmap("sprites/1.png"))
        self.thiefframe.setGeometry(240,190,71,91)
        self.thiefbtn = QPushButton("THIEF",self)
        self.thiefbtn.setGeometry(240,290,71,23)
        
        with open(BUTTON_CSS, 'r') as f:
            self.thiefbtn.setStyleSheet(f.read())
        
        self.thiefbtn.clicked.connect(self.thief_class)
        
        self.wmageframe = QLabel(self)
        self.wmageframe.setPixmap(QPixmap("sprites/4.png"))
        self.wmageframe.setGeometry(330,190,70,91)
        self.wmagebtn = QPushButton("W-MAGE",self)
        self.wmagebtn.setGeometry(330,290,71,23)
        
        with open(BUTTON_CSS, 'r') as f:
            self.wmagebtn.setStyleSheet(f.read())
        
        self.wmagebtn.clicked.connect(self.wmage_class)
        
        self.bmageframe = QLabel(self)
        self.bmageframe.setPixmap(QPixmap("sprites/5.png"))
        self.bmageframe.setGeometry(420,190,71,91)
        self.bmagebtn = QPushButton("B-MAGE",self)
        self.bmagebtn.setGeometry(420,290,71,23)
        
        with open(BUTTON_CSS, 'r') as f:
            self.bmagebtn.setStyleSheet(f.read())
        
        self.bmagebtn.clicked.connect(self.bmage_class)
        
        self.starticon = QToolButton(self)
        self.starticon.setGeometry(260,50,120,45)
        self.starticon.setIcon(QIcon("resources/play.jpg"))
        self.starticon.setIconSize(QSize(120,120))
        self.starticon.hide()
        self.starticon.clicked.connect(self.update)
        
        self.show()
    
    @pyqtSlot()
    def update(self):
        self.new_window = Overworld()
        self.new_window.show()
        self.hide()
        
    def warrior_class(self):
        global CURRENT_CLASS,CURRENT_SKILL1,CURRENT_SKILL2
        CURRENT_CLASS = "WARRIOR"
        CURRENT_SKILL1 = "SLASH"
        CURRENT_SKILL2 = "DEFEND"
        self.starticon.show()
        
    def thief_class(self):
        global CURRENT_CLASS,CURRENT_SKILL1,CURRENT_SKILL2
        CURRENT_CLASS = "THIEF"
        CURRENT_SKILL1 = "STEAL"
        CURRENT_SKILL2 = "DODGE"
        self.starticon.show()
    def wmage_class(self):
        global CURRENT_CLASS,CURRENT_SKILL1,CURRENT_SKILL2
        CURRENT_CLASS = "WHITE MAGE"
        CURRENT_SKILL1 = "WHITE"
        CURRENT_SKILL2 = "HEAL"
        self.starticon.show()
    def bmage_class(self):
        global CURRENT_CLASS,CURRENT_SKILL1,CURRENT_SKILL2
        CURRENT_CLASS = "BLACK MAGE"
        CURRENT_SKILL1 = "BLACK"
        CURRENT_SKILL2 = "FIRE"
        self.starticon.show()
        
class Start_Game_Engine(QMainWindow):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.width = 632
        self.height = 371
        self.counter = 0
        self.title = "Sayaka v1.4 20200319"
        self.damage = 5
        
        with open(GLOBAL_CSS, 'r') as f:
            self.setStyleSheet(f.read())
        
        if CURRENT_CLASS == "WARRIOR":
            self.cast = "sprites/cast/0.png"
            self.sprite = "sprites/0.png"
        elif CURRENT_CLASS == "THIEF":
            self.cast = "sprites/cast/1.png"
            self.sprite = "sprites/1.png"
        elif CURRENT_CLASS == "WHITE MAGE":
            self.cast = "sprites/cast/2.png"
            self.sprite = "sprites/4.png"
        elif CURRENT_CLASS == "BLACK MAGE":
            self.cast = "sprites/cast/3.png"
            self.sprite = "sprites/5.png"
        self.random_question()
        self.gameUI()

    def gameUI(self):
        enemy_level = "0"
        player_level = "0"
        
        
        self.setFixedSize(self.width,self.height)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("resources/logo.ico"))
        
        self.frame = QFrame(self)
        self.frame.setGeometry(30,199,271,111)
        self.frame.setStyleSheet("background: #333")
        
        self.attack = QPushButton("ATTACK",self)
        self.attack.setGeometry(50,210,101,31)
        
        with open(BUTTON_CSS, 'r') as f:
            self.attack.setStyleSheet(f.read())
        
        self.attack.clicked.connect(self.attack_on_click)
        
        self.skill1 = QPushButton(CURRENT_SKILL1,self)
        self.skill1.setGeometry(180,210,101,31)
        
        with open(BUTTON_CSS, 'r') as f:
            self.skill1.setStyleSheet(f.read())
        
        self.skill1.clicked.connect(self.s1_on_click)
        
        self.skill2 = QPushButton(CURRENT_SKILL2,self)
        self.skill2.setGeometry(50,260,101,31)
        
        with open(BUTTON_CSS, 'r') as f:
            self.skill2.setStyleSheet(f.read())
        
        self.skill2.clicked.connect(self.s2_on_click)
        
        self.run = QPushButton("RUN",self)
        self.run.setGeometry(180,260,101,31)
        
        with open(BUTTON_CSS, 'r') as f:
            self.run.setStyleSheet(f.read())
        
        self.run.clicked.connect(self.run_on_click)
        
        self.ansbox = QLineEdit("",self)
        self.ansbox.setGeometry(370,240,241,71)
        self.ansbox.setStyleSheet("""
                                   background: transparent;
                                   color: white;
                                   """)
        
        self.qstnbox = QLabel(self.question,self)
        self.qstnbox.setGeometry(450,190,161,41)
        self.qstnbox.setStyleSheet("""
                                   background: transparent;
                                   color: white;
                                   border: 3px solid;
                                   """)
        
        self.refbtn = QPushButton("REFRESH",self)
        self.refbtn.setGeometry(370,200,75,23)
        
        with open(BUTTON_CSS, 'r') as f:
            self.refbtn.setStyleSheet(f.read())
        
        self.refbtn.clicked.connect(self.refresh)
        
        self.frame2 = QFrame(self)
        self.frame2.setGeometry(50,20,531,161)
        self.frame2.setStyleSheet("""
                                   background: url(resources/bg5.jpg);
                                   color: white;
                                   border: 2px solid;
                                   """)
        
        self.p1hp = QProgressBar(self)
        self.p1hp.setGeometry(80,20,200,20)
        self.hplbl = QLabel("HP",self)
        self.hplbl.setStyleSheet("""
                                 *{
                                 background: transparent;
                                 color: white;
                                 }""")
        self.hplbl.move(55,15)
        
        self.p1hp.setValue(CURRENT_HP)
        self.playerimg = QLabel(self)
        self.playerimg.setPixmap(QPixmap(self.sprite))
        self.playerimg.setGeometry(110,50,71,91)
        
        self.enemyhplbl = QLabel("HP",self)
        self.enemyhplbl.move(355,15)
        self.enemyhplbl.setStyleSheet("""
                                 *{
                                 background: transparent;
                                 color: white;
                                 }""")
        
        self.enemyhp = QProgressBar(self)
        self.enemyhp.setGeometry(380,20,200,20)
        self.enemyhp.setValue(ENEMY_HP)
        self.enemyimg = QLabel(self)
        self.enemyimg.setPixmap(QPixmap("sprites/enemy/"+ENEMY_SPRITE+".png"))
        self.enemyimg.setGeometry(426,50,71,91)
        
        
        self.show()
    
    def random_question(self):
        self.q1 = str(random.randint(0,100))
        self.q2 = str(random.randint(0,100))
        self.symbol = ["+","-","/","*"]
        self.symb_rand = random.randint(0,3)
        self.question = self.q1 + self.symbol[self.symb_rand] + self.q2
    
    @pyqtSlot()
    def cast_animate(self):
        import time
        self.playerimg.hide()
        self.playerimg.setPixmap(QPixmap(self.cast))
        self.playerimg.show()
        self.playerimg.hide()
        self.playerimg.setPixmap(QPixmap(self.sprite))
        self.playerimg.show()
    def update(self):
        if self.p1hp.value() >0 and self.enemyhp.value() > 0:
            self.q1 = str(random.randint(0,100))
            self.q2 = str(random.randint(0,100))
            self.symbol = ["+","-","/","*"]
            self.symb_rand = random.randint(0,3)
            if self.symbol[self.symb_rand] == "/":
                if self.q1 > self.q2:
                    temp = self.q1
                    self.q1 = self.q2
                    self.q2 = temp
                else:
                    print("A is Higher for division.")
            self.question = self.q1 + self.symbol[self.symb_rand] + self.q2
            self.qstnbox.setText(self.question)
            self.enemyattack()

        elif self.enemyhp.value() <= 0 or self.p1hp.value() <= 0:
            if self.enemyhp.value() <= 0: # WIN
                CURRENT_HP = self.p1hp.value()
                print("user-win")
                QMessageBox.information(self,"YOU WIN!","RETURNING TO WORLD",QMessageBox.Ok,QMessageBox.Ok)
                self.hide()
                self.new_window = Overworld()
                self.new_window.show()
            elif self.p1hp.value() <=0: #LOSE
                QMessageBox.information(self,"GAMEOVER","HP DROPS TO 0!",QMessageBox.Ok,QMessageBox.Ok)
                self.hide()
                self.new_window = Homepage()
                self.new_window.show()
                
                with open(GLOBAL_CSS, 'r') as f:
                    self.new_window.setStyleSheet(f.read())
             
    def attack_on_click(self):
        if self.ansbox.text() == '' or self.ansbox.text() != '':
            if self.ansbox.text() == '':
                self.damage = 0
            else:
                self.damage = int(self.ansbox.text())
        if self.ansbox.text() == float(eval(self.qstnbox.text())):
            self.do_damage(9)
            self.cast_animate()
        else:
            self.curr_p1hp = self.p1hp.value()
            self.p1hp.setValue(self.curr_p1hp)
            self.update()
            
    def s1_on_click(self):
        if CURRENT_SKILL1 == "SLASH":
            self.do_damage(9+random.randint(0,4))
        elif CURRENT_SKILL1 == "STEAL":
            self.do_damage(5+random.randint(0,3))
            self.do_damage(2.8+random.randint(0,5))
        elif CURRENT_SKILL1 == "WHITE":
            self.do_damage(7+random.randint(0,3))
            self.p1hp.setValue(self.p1hp.value()+3)
        elif CURRENT_SKILL1 == "BLACK":
            self.do_damage(14+random.randint(2,9))
            self.do_damage(3)
            self.p1hp.setValue(self.p1hp.value()-5)
        self.cast_animate()
    def s2_on_click(self):
        
        if CURRENT_SKILL2 == "DEFEND":
            
            self.barrier = self.p1hp.value()
            print("defend process start")
            if self.barrier > 39:
                if self.counter < 4:
                    self.counter += 1
                    print("print defend process > 39")
                    self.p1hp.setValue(self.barrier+(self.barrier*0.03))    
            elif self.barrier < 40:
                if self.counter < 4:
                    self.counter += 1
                    print("print defend process < 39")
                    self.p1hp.setValue(self.barrier+(self.barrier*0.30))
        elif CURRENT_SKILL2 == "DODGE":
            self.skill2.show()
            if self.counter < 4:
                self.counter +=1
                pass
            if self.counter >= 4:
                self.skill2.hide()
        elif CURRENT_SKILL2 == "HEAL":
            self.curr_p1hp = self.p1hp.value()
            if self.curr_p1hp > 49:
                self.p1hp.setValue(self.curr_p1hp+self.curr_p1hp*0.25)
            elif self.curr_p1hp < 50:
                self.p1hp.setValue(self.curr_p1hp+self.curr_p1hp*0.64)
            self.do_damage(2.5)
        elif CURRENT_SKILL2 =="FIRE":
            self.curr_p1hp = self.p1hp.value()
            if self.counter < 4:
                if self.counter >2:
                    self.do_damage(34)
                else:
                    self.do_damage(20)
                self.counter += 1
        self.cast_animate()
    def run_on_click(self):
        self.chance = random.randint(0,100)
        if self.chance < 36:
            global CURRENT_HP
            CURRENT_HP = self.p1hp.value()
            self.new_window = Overworld()
            self.new_window.show()
            self.hide()
        else:
            self.do_damage(0)
    def refresh(self):
        self.curr_p1hp = self.p1hp.value()
        self.p1hp.setValue(self.curr_p1hp-2)
        self.update()
    def do_damage(self,damage):
        if self.enemyhp.value() > 0:
            self.curr_enemyhp = self.enemyhp.value()
            if self.curr_enemyhp-damage <= 0:
                self.enemyhp.setValue(0)
            elif self.curr_enemyhp-damage >0:
                self.enemyhp.setValue(self.curr_enemyhp-damage)
            print(self.enemyhp.value())
            if self.enemyhp.value() < 0:
                QMessageBox.information(self,"YOU WIN!","Returning to World..",QMessageBox.Ok,QMessageBox.Ok)
                self.new_window = Overworld()
                self.hide()
                self.new_window.show()
            self.update()
        else:
            QMessageBox.information(self,"YOU WIN!","Returning to World..",QMessageBox.Ok,QMessageBox.Ok)
            self.new_window = Overworld()
            self.hide()
            self.new_window.show()
    def enemyattack(self):
        print("ENEMY TURN")  
        self.enemydamage = 3+ random.randint(2,6)
        self.currhp = self.p1hp.value()
        if self.currhp-self.enemydamage <= 0:
            self.p1hp.setValue(0)
        elif self.currhp-self.enemydamage > 0:
            self.p1hp.setValue(self.currhp-self.enemydamage)
         
            
class About(QMainWindow):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.width = 321
        self.height = 162
        self.title = "About"
        self.initAbout()
    
    def initAbout(self):
        self.setFixedSize(self.width,self.height)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("resources/logo.ico"))
        
        self.label = QLabel("project SAYAKA",self)
        self.label.setGeometry(100,20,181,21)
        self.label.setStyleSheet("background:transparent;")
        
        self.label2 = QLabel("""
                             A Requirement  for  OOP
                             Created by:  Jeric  Marcel  Gappi
                             """,self)
        self.label2.setGeometry(10,60,260,71)
        self.label2.setStyleSheet("font-size:16px;")

class Overworld(QMainWindow):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.width = 555
        self.height = 371
        self.title = "Sayaka v0.9 09231 BETA"
        
        with open(GLOBAL_CSS, 'r') as f:
            self.setStyleSheet(f.read())
        
        self.PLYR_IMG = LAST_IMG
        self.gameUI()

    def gameUI(self):
        enemy_level = "0"
        player_level = "0"
        
        
        
        
        self.mapAlloc = QLabel(self)
        self.mapAlloc.setPixmap(QPixmap("resources/map.jpeg"))
        self.mapAlloc.setGeometry(0,0,632,371)
        self.mapAlloc
        
        self.setFixedSize(self.width,self.height)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("resources/logo.ico"))
        
        self.warriorframe = QLabel(self)
        self.warriorframe.setPixmap(QPixmap(self.PLYR_IMG))
        self.warriorframe.setGeometry(LAST_POS_X,LAST_POS_Y,71,91)
        self.warriorframe.setStyleSheet("background: transparent;")
        
        self.frame = QFrame(self)
        self.frame.setGeometry(10,10,200,40)
        self.tb = QLabel(CURRENT_ACCOUNT,self)
        self.tb.setGeometry(10,30,200,40)
        self.tb.setStyleSheet("background: black;")
        self.frame.setStyleSheet("background: white;")
        self.hpbar = QProgressBar(self)
        self.hpbar.setValue(CURRENT_HP)
        self.hpbar.setGeometry(10,10,200,20)
        self.hpbar.setStyleSheet("color: black;")
        
        
        self.R_MOVE = QShortcut(QKeySequence("Right"),self)
        self.R_MOVE.activated.connect(self.MOVE_RIGHT)
        
        self.L_MOVE = QShortcut(QKeySequence("Left"),self)
        self.L_MOVE.activated.connect(self.MOVE_LEFT)
        
        self.U_MOVE = QShortcut(QKeySequence("Up"),self)
        self.U_MOVE.activated.connect(self.MOVE_UP)
        
        self.D_MOVE = QShortcut(QKeySequence("Down"),self)
        self.D_MOVE.activated.connect(self.MOVE_DOWN)
    
    @pyqtSlot()
    def GET_POS(self):
        global CURR_POS_X , CURR_POS_Y
        self.counter = 0
        self.warriorframe.setPixmap(QPixmap(self.PLYR_IMG).scaled(40,40))
        self.warriorframe.setStyleSheet("background: transparent;")
        CURR_POS_X = self.warriorframe.x()
        CURR_POS_Y = self.warriorframe.y()
        
        self.enemychance1 = random.randint(0,1000)
        print(self.enemychance1)
        if self.enemychance1%2==0:
            if self.enemychance1 > 900:
                global ENEMY_SPRITE
                ENEMY_SPRITE = str(random.randint(0,5))
                self.a=QMessageBox.warning(self,"ENEMY SPAWN","ENTER BATTLE SCENE",QMessageBox.Ok,QMessageBox.Ok)
                self.new_window = Start_Game_Engine()
                self.counter += 1
                print("current sprite: sprites/enemy/"+ENEMY_SPRITE+".png")
                global LAST_POS_X,LAST_POS_Y,LAST_IMG
                LAST_POS_X = self.warriorframe.x()
                LAST_POS_Y = self.warriorframe.y()
                LAST_IMG = self.PLYR_IMG
                self.new_window.show()
                self.hide()
            elif self.counter == 10:
                self.counter = 0
                pass
    def MOVE_UP(self):
        
        if self.PLYR_IMG == "sprites/movement/up_2.png":
            self.PLYR_IMG = "sprites/movement/up_1.png"
        elif self.PLYR_IMG == "sprites/movement/up_1.png":
            self.PLYR_IMG = "sprites/movement/up_2.png"
            
        if self.PLYR_IMG != "sprites/movement/up_1.png" and self.PLYR_IMG != "sprites/movement/up_2.png":
            self.PLYR_IMG = "sprites/movement/up_1.png"
        self.GET_POS()
        self.warriorframe.move(CURR_POS_X,CURR_POS_Y-5)
    def MOVE_DOWN(self):
        
        if self.PLYR_IMG == "sprites/movement/down_2.png":
            self.PLYR_IMG = "sprites/movement/down_1.png"
        elif self.PLYR_IMG == "sprites/movement/down_1.png":
            self.PLYR_IMG = "sprites/movement/down_2.png"
        if self.PLYR_IMG != "sprites/movement/down_1.png" and self.PLYR_IMG != "sprites/movement/down_2.png":
            self.PLYR_IMG = "sprites/movement/down_1.png"
        self.GET_POS()
        self.warriorframe.move(CURR_POS_X,CURR_POS_Y+5)
    def MOVE_LEFT(self):
        
        if self.PLYR_IMG == "sprites/movement/left_2.png":
            self.PLYR_IMG = "sprites/movement/left_1.png"
        elif self.PLYR_IMG == "sprites/movement/left_1.png":
            self.PLYR_IMG = "sprites/movement/left_2.png"           
        if self.PLYR_IMG != "sprites/movement/left_1.png" and self.PLYR_IMG != "sprites/movement/left_2.png":
            self.PLYR_IMG = "sprites/movement/left_1.png"
        self.GET_POS()
        self.warriorframe.move(CURR_POS_X-5,CURR_POS_Y)
    def MOVE_RIGHT(self):
        if self.PLYR_IMG == "sprites/movement/right_2.png":
            self.PLYR_IMG = "sprites/movement/right_1.png"
        elif self.PLYR_IMG == "sprites/movement/right_1.png":
            self.PLYR_IMG = "sprites/movement/right_2.png"
        if self.PLYR_IMG != "sprites/movement/right_1.png" and self.PLYR_IMG != "sprites/movement/right_2.png":
            self.PLYR_IMG = "sprites/movement/right_1.png"
        self.GET_POS()
        self.warriorframe.move(CURR_POS_X+5,CURR_POS_Y)
        
      
if __name__ == "__main__" or "__Accounts__":
    app = QApplication(sys.argv)
    ex = Homepage()
    with open(GLOBAL_CSS, 'r') as f:
        ex.setStyleSheet(f.read())
    sys.exit(app.exec_())
    