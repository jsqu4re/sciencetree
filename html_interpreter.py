#!/usr/bin/python
import os
from lxml import html

files = os.listdir( os.getcwd() )

all_titels = set()

for file_name in files:
    try:
        file = open(file_name, "r")

        html_file = file.read()

        tree = html.fromstring(html_file)

        search_results = tree.xpath("//div[contains(@class, 'col-22-24')]")

        titels = set()

        for result in search_results:
            for element in result.getchildren():
                if element.tag == 'h2':
                    for text in element.getchildren():
                        if text.tag == 'a':
                            titels.add(text.text_content())
                            all_titels.add(text.text_content())

        for titel in titels:
            print titel

        print "Results: " + str(len(titels))
    except:
        print "failed to open " + file_name

print "Results: " + str(len(all_titels))
