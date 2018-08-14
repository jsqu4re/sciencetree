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

from multiprocessing import Process, Queue

class Browser(QWebView):
    def __init__(self, url):
        self.app = QApplication(sys.argv) 
        # QWebView
        self.view = QWebView.__init__(self)
        self.setWindowTitle('IEEE')
        self.load(url)
        self.timer = QTimer(self)
        # self.timer.singleShot(20000, self.do_quit)
        # self.timer = QTimer(self)
        self.timer.timeout.connect(self.do_quit)
        self.timer.setInterval(20000)
        # self.timer.setSingleShot(True)
        self.timer.start()
        self.app.exec_()
        self.timer.stop()
    
    def do_quit(self):
        self.app.quit()

    def load(self,url):
        self.setUrl(QUrl(url))

def render(q, page_number):
    file = open("ieee_download_" + str(page_number) + ".html", "w")
    view = Browser("https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=(%22motion%20planning%22)&matchBoolean=true&pageNumber=" + str(page_number) + "&rowsPerPage=10&searchField=Search_All")
    file.write(view.page().mainFrame().toHtml().encode('ascii','ignore'))
    q.put( "Created " + file.name )    



if __name__ == '__main__':
    print "start crawler"
    
    for number in range(1,658):
        queue = Queue()
        p = Process(target=render, args=(queue, number))
        p.start()
        p.join() # this blocks until the process terminates
        result = queue.get()
        print result

    print "done"

    # render(0)

    # for page_number in range (0,3):
    #     render(page_number)
