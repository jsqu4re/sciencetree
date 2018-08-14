#!/usr/bin/python
from lxml import html

file = open("test.html","r")

html_file = file.read()

tree = html.fromstring(html_file)

search_results = tree.xpath("//div[contains(@class, 'col-22-24')]")
# search_results = tree.xpath("//a[contains(@class, 'ng-binding ng-scope')]")

for result in search_results:
    print result.getChildren()
