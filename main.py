#!/usr/bin/python
import os
# import pathlib
import time
from tqdm import tqdm
from multiprocessing import Process, Queue, Pool


import ieee_crawler
import html_interpreter




if __name__ == '__main__':
    print "start crawler"

    query_text = "motion%20planning"
    # number_of_pages = 658
    number_of_pages = 2

    download_folder = os.getcwd() + "/download/search/"
    paper_folder = os.getcwd() + "/download/paper/"

    # pathlib.Path(download_folder).mkdir(parents=True, exist_ok=True)
    # pathlib.Path(paper_folder).mkdir(parents=True, exist_ok=True)

    print "download " + query_text + " to " + download_folder
    print "number of pages " + str(number_of_pages)

    process_list = list()

    for number in tqdm(range(1, number_of_pages + 1)):
        queue = Queue()
        p = Process(target=ieee_crawler.render_search, args=(queue, number, query_text, download_folder))
        p.start()
        print "process " + str(number) + " - active processes " + str(len(process_list))
        process_list.append(p)
        time.sleep(1)
        while (len(process_list) > 20):
            time.sleep(1)
            process_list[:] = [p for p in process_list if not (p.is_alive() == False)]

    for p in process_list:
        p.join()

    papers = html_interpreter.interprete_html(download_folder)

    print "found " + str(len(papers)) + " paper"

    process_list = list()

    for paper in tqdm(papers):
        queue = Queue()
        p = Process(target=ieee_crawler.render_article, args=(queue, paper, paper_folder))
        p.start()
        print "number of processes " + str(len(process_list))
        process_list.append(p)
        time.sleep(1)
        while (len(process_list) > 20):
            time.sleep(1)
            process_list[:] = [p for p in process_list if not (p.is_alive() == False)]

    for p in process_list:
        p.join()

    print "done"
