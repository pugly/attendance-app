__author__ = 'denrico'

import time as t
import shelve

period_start_H = 9
period_start_M = 0
s = shelve.open('my_students', writeback=True)

while True:
    entry = input('Begin scanning or enter q to quit: ')

    if entry in ['q', 'Q']:
        s.close()
        break

    elif entry not in s.keys():
        print('ID not found; scan again.')

    else:
        if int(t.strftime('%H')) <= period_start_H:
            if int(t.strftime('%M')) <= period_start_H:
                print(s[entry]['name'] + ' scanned in at ' + t.strftime('%H:%M\n', t.localtime()))
                s[entry]['attendance'].append(t.time())
            else:
                print(s[entry]['name'] + ' scanned in at ' + t.strftime('%H:%M\n', t.localtime())+'LATE')
                s[entry]['attendance'].append(t.time())
                s[entry]['lates'].append(t.time())
        else:
            print(s[entry]['name'] + ' scanned in at ' + t.strftime('%H:%M\n', t.localtime())+'LATE')
            s[entry]['attendance'].append(t.time())
            s[entry]['lates'].append(t.time())



