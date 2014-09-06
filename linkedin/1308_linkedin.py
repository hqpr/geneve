#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
sample code :
https://www.dropbox.com/sh/3mjiej677wjrsrd/AAC29M8RVPUHKuRN1zGX4a0ma/10.%20LinkedIn.py

sample url
https://www.linkedin.com/in/sonjaholverson

loop
https://classic.scraperwiki.com/docs/python/python_css_guide/

User-agents
https://github.com/cvandeplas/pystemon/blob/master/user-agents.txt


"""
__author__ = 'adubnyak@gmail.com'

import lxml.html
from openpyxl import Workbook
import urllib2
import re

wb = Workbook()
ws = wb.active
ws.title = "Data"


def write(col, row, sheet, data):
    while True:
        try:
            sheet['%s%s' %(col,row)] = data
            break
        except:
            try:
                sheet['%s%s' %(col,row)] = " ".join(data)
                break
            except:
                try:
                    d2 = []
                    for i in data:
                        d2.append(" ".join(i))
                    sheet['%s%s' %(col,row)]= " ".join(d2)
                    break
                except:
                    sheet['%s%s' %(col,row)]= " "
                    break

r = 1
write('A', r, ws, "First Name")
write('B', r, ws, "Last Name")
write('C', r, ws, "Position")
write('D', r, ws, "Location")
write('E', r, ws, "Current position")
write('F', r, ws, "Past position")
write('G', r, ws, "Eduacation")
write('H', r, ws, "Friends")
write('I', r, ws, "Position title")
write('J', r, ws, "Experience")
write('K', r, ws, "profile-experience")
write('L', r, ws, "publications")
write('M', r, ws, "Skills")
write('N', r, ws, "Education")
write('O', r, ws, "interests")
write('P', r, ws, "Groups")
write('Q', r, ws, "Email")

wb.save("Linkedin.xlsx")

fp = open('urls.txt', 'rb')

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5)'
headers = {'User-Agent': user_agent}

for url in fp.readlines():
    print url
    req = urllib2.Request(url, None, headers)

    try:
        c = urllib2.urlopen(req)
    except:
        continue

    r += 1

    doc = lxml.html.document_fromstring(c.read())

    for f_name in doc.cssselect('span.given-name'):
        write('A', r, ws, f_name.text)

    for l_name in doc.cssselect('span.family-name'):
        write('B', r, ws, l_name.text)

    for pos in doc.cssselect('p.headline-title'):
        position = pos.text.replace('\n', '').replace('\r', '')
        write('C', r, ws, position)

    for location in doc.cssselect('span.locality'):
        location = location.text.replace('\n', '').replace('\r', '')
        write('D', r, ws, location)

    current_lst = []
    for current in doc.cssselect('ul.current li'):
        current = current.text.replace('\n', '').replace('\r', '')
        current_lst.append(current)
        write('E', r, ws, current_lst)

    past_lst = []
    for past in doc.cssselect('ul.past li'):
        past = past.text.replace('\n', '').replace('\r', '')
        past_lst.append(past)
        write('F', r, ws, past_lst)

    edu_lst = []
    for edu in doc.cssselect('dd.summary-education li'):
        edu = edu.text.replace('\n', '').replace('\r', '')
        edu_lst.append(edu)
        write('G', r, ws, edu_lst)

    for friends in doc.cssselect('dd.overview-connections strong'):
        friends = friends.text.replace('\n', '').replace('\r', '')
        write('H', r, ws, friends)

    for exp_work1 in doc.cssselect('span.title'):
        exp_work1 = exp_work1.text.replace('\n', '').replace('\r', '')
        write('I', r, ws, exp_work1)

    for exp in doc.cssselect('p.description'):
        exp = exp.text.replace('\n', '').replace('\r', '')
        write('J', r, ws, exp)

    works = []
    for txt in doc.cssselect('div#profile-experience div p'):
        txt = txt.text
        txt = txt.replace('\r\n', '')
        works.append(txt)
    write('K', r, ws, works)

    publications = []
    for pub in doc.cssselect('div#profile-publications div p'):
        pub = pub.text
        pub = pub.replace('\r\n', '')
        publications.append(pub)
    write('L', r, ws, publications)

    skill = []
    for skills in doc.cssselect('ol.skills li span'):
        skills = skills.text
        skills = skills.replace('\r\n', '')
        skill.append(skills)
    write('M', r, ws, skill)

    educat = []
    for edu in doc.cssselect('div.education h3'):
        edu = edu.text
        edu = edu.replace('\r\n', '')
        educat.append(edu)

    education = []
    for e in educat:
        if e != '':
            education.append(e)
    for edu2 in doc.cssselect('div.education a'):
        education.append(edu2.text)
    write('N', r, ws, education)

    for interests in doc.cssselect('dd.interests p'):
        interests = interests.text
        interests = interests.replace('\r\n', '')
        write('O', r, ws, interests)

    for groups in doc.cssselect('p.null'):
        groups = groups.text
        groups = groups.replace('\r\n', '')
        write('P', r, ws, groups)

    match = re.findall("[a-zA-Z0-9_]+(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?!([a-zA-Z0-9]*\.[a-zA-Z0-9]*\.[a-zA-Z0-9]*\.))(?:[A-Za-z0-9](?:[a-zA-Z0-9-]*[A-Za-z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?", c.read())
    if match:
        for m in match:
            write('Q', r, ws, groups)

    wb.save("Linkedin.xlsx")
print 'All done'
