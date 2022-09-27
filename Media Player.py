from select import select
from PyQt5.QtWidgets import QApplication , QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFileDialog
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
import sys

class Window(QWidget):
    def __init__(self):    

        super().__init__()

        p = self.palette()
        
        p.setColor(QPalette.Window, Qt.red)

        self.setWindowTitle("User Media Player")
        self.setGeometry(350, 100,700,500) 
        self.setPalette(p)
        
        self.create_player()

    def create_player(self):

        self.mediapPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        
        self.openbtn = QPushButton()
        self.playbtn = QPushButton()
        self.slider = QSlider(Qt.Horizontal)
         
        # self.openbtn.setEnabled(False) 
        self.playbtn.setEnabled(False)
        
        self.slider.setRange(0,0)

        videowidget  = QVideoWidget()
        
        self.openbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
                
        self.openbtn.clicked.connect(self.open_file)
        self.playbtn.clicked.connect(self.play_video)

        self.mediapPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediapPlayer.positionChanged.connect(self.position_changed)
        self.mediapPlayer.durationChanged.connect(self.duration_changed)

        self.slider.sliderMoved.connect(self.set_position)
        
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        
        hbox.setContentsMargins(0,0,0,0)
        
        hbox.addWidget(self.openbtn)
        hbox.addWidget(self.playbtn)
        hbox.addWidget(self.slider)
 
        vbox.addLayout(hbox)
        vbox.addWidget(videowidget)

        self.mediapPlayer.setVideoOutput(videowidget)
        self.setLayout(vbox)
    def open_file(self):
        
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
        
        if filename != '':
        
            self.mediapPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playbtn.setEnabled(True)

    def play_video(self):

        if self.mediapPlayer.state() == QMediaPlayer.PlayingState:
        
            self.mediapPlayer.pause()
        
        else : 
        
            self.mediapPlayer.play()
    
    def mediastate_changed(self, state):
        
        if self.mediapPlayer.state() == QMediaPlayer.PlayingState:
            
            self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))

        else : 

            self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def position_changed(self, position):

        self.slider.setValue(position)

    def duration_changed(self, duration):

        self.slider.setRange(0, duration)

    def set_position(self, position) : 

        self.mediapPlayer.setPosition(position)

app  = QApplication(sys.argv)

window_0 = Window()

window_0.show()

sys.exit(app.exec_())
