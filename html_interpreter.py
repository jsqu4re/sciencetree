#!/usr/bin/python
from lxml import html

file = open("test.html","r")

html_file = file.read()

tree = html.fromstring(html_file)

search_results = tree.xpath("//div[contains(@class, 'col-22-24')]")
# search_results = tree.xpath("//a[contains(@class, 'ng-binding ng-scope')]")

titels = set()

for result in search_results:
    for element in result.getchildren():
        if element.tag == 'h2':
            for text in element.getchildren():
                if text.tag == 'a':
                    titels.add(text.text_content())

for titel in titels:
    print titel

print "Results: " + str(len(titels))