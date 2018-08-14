#!/usr/bin/python
import os
from lxml import html

def interprete_html( download_folder ):
    files = os.listdir( download_folder )

    all_titels = set()

    for file_name in files:
        try:
            file = open(download_folder + file_name, "r")

            html_file = file.read()

            tree = html.fromstring(html_file)

            search_results = tree.xpath("//div[contains(@class, 'col-22-24')]")

            for result in search_results:
                for element in result.getchildren():
                    if element.tag == 'h2':
                        for text in element.getchildren():
                            if text.tag == 'a':
                                string = text.attrib.get("href")
                                # string = text.attrib.get("href") + " :  " + text.text_content()
                                all_titels.add(string)
        except:
            print "failed to open " + file_name

    return all_titels

if __name__ == '__main__':
    relative_folder = "/download/"
    download_folder = os.getcwd() + relative_folder

    print download_folder

    results = interprete_html(download_folder)
    print results
