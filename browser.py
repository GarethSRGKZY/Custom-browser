import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_bttn = QAction('Back',self)
        back_bttn.triggered.connect(self.browser.back)
        navbar.addAction(back_bttn)

        forward_bttn = QAction('Forward',self)
        forward_bttn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_bttn)

        reload_bttn = QAction('Reload',self)
        reload_bttn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_bttn)

        home_bttn = QAction('Home',self)
        home_bttn.triggered.connect(self.navigate_home)
        navbar.addAction(home_bttn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    
    def update_url(self, url):
        self.url_bar.setText(url.toString())
    

app = QApplication(sys.argv)
QApplication.setApplicationName("GBser")
window = MainWindow()
app.exec_()
