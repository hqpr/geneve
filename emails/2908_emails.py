#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
email parser
"""
__author__ = 'adubnyak@gmail.com'

import re
import csv

fp = open('mails.txt', 'rb')
mails = fp.readlines()


def mailer(domain, lst, count_lst, d):
    count_lst = []
    d = {}
    for l in lst:
        if domain in l:
            if l not in count_lst:
                count_lst.append(l)
                d1.update({domain: len(count_lst)})
    return d1

emails = []
d1 = {}
for m in mails:
    match = re.findall('@(.*)', m)
    for i in match:
        i = i.replace('\r', '')
        res = mailer(i, mails, emails, d1)

writer = csv.writer(open('results.csv', 'wb+'), delimiter=';', quotechar='"')

for k, v in res.items():
    writer.writerow([k, v])
    # print '%s: %s' % (k, v)

# raw_input('')
print 'done'

