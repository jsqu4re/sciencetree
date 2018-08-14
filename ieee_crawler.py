#!/usr/bin/python
import sys
import time

import PyQt5
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWebKitWidgets import QWebView , QWebPage
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtNetwork import *

from optparse import OptionParser


class Browser(QWebView):
    def __init__(self, url):
        self.app = QApplication(sys.argv) 
        # QWebView
        self.view = QWebView.__init__(self)
        self.setWindowTitle('IEEE')
        self.load(url)
        self.timer = QTimer(self)

        self.timer.timeout.connect(self.do_quit)
        self.timer.setInterval(10000)

        self.timer.start()
        self.app.exec_()
        self.timer.stop()

    def do_quit(self):
        self.app.quit()

    def load(self,url):
        self.setUrl(QUrl(url))

def render_search(q, page_number, query_text, absolute_path):
    file = open(absolute_path + "ieee_download_" + str(page_number) + ".html", "w")
    view = Browser("https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=(%22" + query_text + "%22)&matchBoolean=true&pageNumber=" + str(page_number) + "&rowsPerPage=10&searchField=Search_All")
    file.write(view.page().mainFrame().toHtml().encode('ascii','ignore'))
    q.put( "Created " + file.name )

def render_article(q, article_address, absolute_path):
    file = open(absolute_path + "ieee_paper_" + article_address.replace("/","_") + ".html", "w")
    view = Browser("https://ieeexplore.ieee.org/" + article_address)
    file.write(view.page().mainFrame().toHtml().encode('ascii','ignore'))
    q.put( "Created " + file.name )
