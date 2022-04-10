#! /usr/bin/python
# coding: utf-8

import time
import calendar

calendar.setfirstweekday(6)

year, = time.localtime()[:1]

print "Content-type: text/html"
print """
    <html>
    <head>
    <title>%d年カレンダー</title>
    </head>
    <body>
    <table align="center" cellpadding="5">
    <th colspan="3"><big>%d</big><small>年</small></th>
""" % (year, year)
for mon in range(1, 13):
    if mon % 3 == 1:
        print "<tr>"
    print """
        <td valign="top">
        <table border="1" bordercolor="#3399ff" cellspacing="0" cellpadding="5">
        <tr><td colspan="7" align="center"><b>%d</b><small>月</small></td></tr>
    """ % (mon)
    print "<tr>"
    for s in ['日', '月', '火', '水', '木', '金', '土']:
        print "<td align=\"center\"><small>%s</small></td>" % s
    print "</tr>"
    for week in calendar.monthcalendar(year, mon):
        print "<tr>"
        for day in week:
            print "<td align=\"right\">"
            if day:    print day
            else:    print "　"
            print "</td>"
        print "</tr>"
    print """
        </table>
        </td>
    """
    if mon % 3 == 0:
        print "</tr>"
print """
    </table>
    </body>
    </html>
"""