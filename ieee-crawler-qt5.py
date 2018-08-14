#!/usr/bin/python

import PyQt5
import time
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWebKitWidgets import QWebView , QWebPage
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtNetwork import *
import sys
from optparse import OptionParser

from time import sleep

class MyBrowser(QWebPage):
    ''' Settings for the browser.'''
 
    def userAgentForUrl(self, url):
        ''' Returns a User Agent that will be seen by the website. '''
        return "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
 
class Browser(QWebView):
    def __init__(self, url):
        self.app = QApplication(sys.argv) 
        # QWebView
        self.view = QWebView.__init__(self)
        #self.view.setPage(MyBrowser())
        self.setWindowTitle('Loading...')
        self.titleChanged.connect(self.adjustTitle)
        self.loadFinished.connect(self._loadFinished)
        #super(Browser).connect(self.ui.webView,QtCore.SIGNAL("titleChanged (const QString&)"), self.adjustTitle)
        self.load(url)
        timer = QTimer(self)
        timer.timeout.connect(self.do_quit)
        timer.setInterval(20000)
        timer.start()
        self.app.exec_()
    
    def do_quit(self):
        self.app.quit()

    def load(self,url):
        self.setUrl(QUrl(url))
 
    def adjustTitle(self):
        self.setWindowTitle(self.title())
    
    def _loadFinished(self, result):
        # self.frame = self.mainFrame()
        # time.sleep(30)
        print self.page().mainFrame().toHtml().encode('ascii','ignore')
        # self.app.quit()

    def disableJS(self):
        settings = QWebSettings.globalSettings()
        settings.setAttribute(QWebSettings.JavascriptEnabled, False)

view = Browser("https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=(%22motion%20planning%22)&matchBoolean=true&pageNumber=2&rowsPerPage=10&searchField=Search_All")
# print view.page().mainFrame().toHtml().encode('ascii','ignore')

# view.showMaximized()
# view.load("https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=(%22motion%20planning%22)&matchBoolean=true&pageNumber=2&rowsPerPage=10&searchField=Search_All")
# view.load("https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=(%22motion%20planning%22)&matchBoolean=true&pageNumber=3&rowsPerPage=10&searchField=Search_All")
# view.app.exec_()
# print view.page().mainFrame().toHtml().encode('ascii','ignore')