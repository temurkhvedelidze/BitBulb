import sys, random
from PyQt5.QtWidgets import QApplication, QMainWindow
from start_menu_design import Ui_StartMenu
from main_window_design import Ui_MainWindow
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtCore import QUrl

# მთავარი ფანჯრის (უშუალოდ gameplay-ის ფანჯრის) კლასი
class MainWindow(QMainWindow, Ui_MainWindow):
    clicked1, clicked2, clicked3, clicked4, clicked5  = False, False, False, False, False # ამ ცვლადებით აღვწერ კონკრეტული ნათურების მდგომარეობას (ჩართული ან გამორთული)
    total_sum = 0 # ჩართული ნათურებით შედგენილი რიცხვი ათობითში (თითოეული ჩართული ნათურის შესაბამისი ორობითი რიცხვთა ჯამი)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.number.setText(f"{random.randint(1,31)}")

        self.lightbulb1.clicked.connect(lambda: self.lightbulb_clicked(self.lightbulb1))
        self.lightbulb2.clicked.connect(lambda: self.lightbulb_clicked(self.lightbulb2))
        self.lightbulb3.clicked.connect(lambda: self.lightbulb_clicked(self.lightbulb3))
        self.lightbulb4.clicked.connect(lambda: self.lightbulb_clicked(self.lightbulb4))
        self.lightbulb5.clicked.connect(lambda: self.lightbulb_clicked(self.lightbulb5))

        self.switch_sound = QSoundEffect()
        self.switch_sound.setSource(QUrl.fromLocalFile("switch.wav"))
        self.switch_sound.setVolume(1)
        self.correct_sound = QSoundEffect()
        self.correct_sound.setSource(QUrl.fromLocalFile("Coin.wav"))
        self.correct_sound.setVolume(1)

    # ამოწმებს მოთამაშის მიერ შედგენილი რიცხვი ემთხვევა თუ არა მოცემულ რიცხვს
    def check_if_matched(self):
        if self.total_sum == int(self.number.text()):
            self.number.setText(f"{random.randint(1,31)}")
            self.correct_sound.play()

    # ფუნქცია, რომელიც გაეშვება როდესაც მოთამაშე დააჭერს რომელიმე ნათურას (ჩართვას ან გამორთავს)
    def lightbulb_clicked(self, lightbulb):
        self.switch_sound.play()

        if lightbulb.objectName() == "lightbulb1":
            if self.clicked1 == False:
                lightbulb.setStyleSheet("border-image: url(:/lightbulbs/lightbulb_on.png);")
                self.clicked1 = True
                self.total_sum += 16
            else:
                lightbulb.setStyleSheet("border-image: url(:/lightbulbs/lightbulb_off.png);")
                self.clicked1 = False
                self.total_sum -= 16
        elif lightbulb.objectName() == "lightbulb2":
            if self.clicked2 == False:
                lightbulb.setStyleSheet("border-image: url(:/lightbulbs/lightbulb_on.png);")
                self.clicked2 = True
                self.total_sum += 8
            else:
                lightbulb.setStyleSheet("border-image: url(:/lightbulbs/lightbulb_off.png);")
                self.clicked2 = False
                self.total_sum -= 8
        elif lightbulb.objectName() == "lightbulb3":
            if self.clicked3 == False:
                lightbulb.setStyleSheet("border-image: url(:/lightbulbs/lightbulb_on.png);")
                self.clicked3 = True
                self.total_sum += 4
            else:
                lightbulb.setStyleSheet("border-image: url(:/lightbulbs/lightbulb_off.png);")
                self.clicked3 = False
                self.total_sum -= 4
        elif lightbulb.objectName() == "lightbulb4":
            if self.clicked4 == False:
                lightbulb.setStyleSheet("border-image: url(:/lightbulbs/lightbulb_on.png);")
                self.clicked4 = True
                self.total_sum += 2
            else:
                lightbulb.setStyleSheet("border-image: url(:/lightbulbs/lightbulb_off.png);")
                self.clicked4 = False
                self.total_sum -= 2
        elif lightbulb.objectName() == "lightbulb5":
            if self.clicked5 == False:
                lightbulb.setStyleSheet("border-image: url(:/lightbulbs/lightbulb_on.png);")
                self.clicked5 = True
                self.total_sum += 1
            else:
                lightbulb.setStyleSheet("border-image: url(:/lightbulbs/lightbulb_off.png);")
                self.clicked5 = False
                self.total_sum -= 1

        self.check_if_matched()

# საწყისი ფანჯრის (მენიუს) კლასი
class StartMenu(QMainWindow, Ui_StartMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.background_music = QSoundEffect()
        self.background_music.setSource(QUrl.fromLocalFile("background music.wav"))
        self.background_music.setVolume(0.5)
        self.background_music.setLoopCount(QSoundEffect.Infinite)
        self.background_music.play()

        self.start_sound = QSoundEffect()
        self.start_sound.setSource(QUrl.fromLocalFile("start_sound.wav"))
        self.start_sound.setVolume(1)
        self.pushButton.clicked.connect(self.start_game)
        self.main_window = None

    # თამაშის დაწყების ფუნქცია
    def start_game(self):
        self.start_sound.play()
        self.main_window = MainWindow()
        self.main_window.show()
        self.hide()

app = QApplication(sys.argv)
start_menu = StartMenu()
start_menu.show()
sys.exit(app.exec())