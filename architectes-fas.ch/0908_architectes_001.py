#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import lxml.html
import urllib
import csv
import xlrd, xlwt
import time

writer = csv.writer(open('results.csv', 'ab+'), delimiter=';', quotechar='"')

# wb = xlwt.Workbook()
# ws = wb.add_sheet('New Sheet', cell_overwrite_ok=True)
# ws.write(0, 0, '1')
# ws.write(0, 1, '2')
# ws.write(0, 2, '3')


url = 'page.htm'
c = urllib.urlopen(url)
doc = lxml.html.document_fromstring(c.read())
region = []  # Название региона
for txt in doc.cssselect('div.txt p'):
    txt = txt.text
    txt = txt.replace('\n\t\t\t\t\t', '').replace('\t\t\t\t', '').replace(u'ü', 'u').replace(u'è', 'e')
    region.append(txt)

c = urllib.urlopen(url)
doc = lxml.html.document_fromstring(c.read())
links = []
for link in doc.cssselect('div.block-mini a'):
    link = link.get('href')
    links.append(link)

first_page = zip(region, links)

for a, b in first_page:
#     ws.write(i, 1, a)
#     ws.write(1, i, b)
# i += i
#         # ws.write(0, 1, b)
# wb.save('results.xls')
    writer.writerow([a, b])

reader = csv.reader(open('results.csv', 'rb'), delimiter=';', quotechar='"')

int_url = 'intpage.htm'
for row in reader:
    int_url = row[1]
    # print int_url
    c = urllib.urlopen(int_url)
    match = re.findall('member-name\"[>](.*)[<]\/span', c.read())
    for m in match:
        m = m.replace('<span><br />', '\t')
        print m

    #  Internal pages parsing
    #
    # c = urllib.urlopen(int_url)
    # n = c.read()
    # wo_br = n.replace('<br>', '')
    # doc = lxml.html.document_fromstring(wo_br)
    # info = []  # Блок с адресом
    # for block in doc.cssselect('div.info-block p'):
    #     block = block.text
    #     block = block.replace('\n\t\t\t\t\t', '').replace('\t\t\t\t', '')\
    #         .replace(u'ü', 'u').replace(u'è', 'e').replace(u'\xe9', 'e')\
    #         .replace(u'\xef', 'i').replace(u'\xe7', 'c').replace(u'\xe4', 'a')
    #     block = block.encode('utf-8')
    #     info.append(block)
    # str_info = '\t '.join(info)
    # writer.writerow([' ', str_info])
    #
    # c = urllib.urlopen(int_url)
    # others = re.findall('mailto\:(.*)\"[>]|target\=\"_blank\"[>](.*)[<]\/a', c.read())
    #
    # try:
    #     email = ''.join(others[0])
    # except IndexError:
    #     email = ' '
    # writer.writerow([' ', ' ', email])
    # try:
    #     website = ''.join(others[1])
    # except IndexError:
    #     website = ''
    # writer.writerow([' ', ' ', ' ', website])
    # time.sleep(2)
