#!/usr/bin/python
import os
import ieee_crawler
import html_interpreter

from multiprocessing import Process, Queue



if __name__ == '__main__':
    print "start crawler"

    query_text = "motion%20planning"
    number_of_pages = 658

    download_folder = os.getcwd() + "/download/search/"
    paper_folder = os.getcwd() + "/download/paper/"
    
    print "download " + query_text + " to " + download_folder
    print "number of pages " + str(number_of_pages)

    for number in range(1, number_of_pages):
        queue = Queue()
        p = Process(target=ieee_crawler.render_search, args=(queue, number, query_text, download_folder))
        p.start()
        p.join()
        result = queue.get()
        print result
    
    papers = html_interpreter.interprete_html(download_folder)
    
    print "found " + str(len(papers)) + " paper"

    for paper in papers:
        queue = Queue()
        p = Process(target=ieee_crawler.render_article, args=(queue, paper, paper_folder))
        p.start()
        p.join()
        result = queue.get()
        print result

    print "done"
