import requests
import json
import sys
import time
import logging

import addresses

cookie = {'PHPSESSID': 'mi1mj3ffkslq1qcmh435j4op81'}
logging.basicConfig(filename='log.txt', level=logging.INFO, format='[%(asctime)s] - %(levelname)s - %(message)s', datefmt='%H:%M:%S')

def session_get(session, url):
	ok = 1
	while ok == 1:
		try:
        		answer = requests.get(url, cookies = cookie, timeout = 5)
			ok = 0
		except:
			#print 'retry...'
			logging.info('retry...')
#	print answer.content
        if answer.status_code == 429:
            #print "Too many requests"
	    logging.error('Too many requests')
        else:
            return answer

headers = {
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/43.0.2357.130 Chrome/43.0.2357.130 Safari/537.36',
	'PHPSESSID': 'mi1mj3ffkslq1qcmh435j4op81',
	'__zlcmid': 'YWfEEEOgH04sYZ',
	'_ga': 'GA1.2.275653443.1451944407',
}

session = requests.Session()
#response = session_get(session, 'http://zalamo.com/resizer.php?size=5000x5000&nocrop=1&file=17150202&module=client&controller=session&action=show&single_session_id=10019218', cookies)

#print response

liczba = 1
for numer in addresses.lista:
	adres = 'http://zalamo.com/resizer.php?file=' + numer + '&size=5000x5000&nocrop=1&module=client&controller=session&action=edit&single_session_id=10019218'
	#print '[', liczba, ' z 125] ', adres
	logging.info('[%s z 125] %s' % (liczba, adres))
	response = session_get(session, adres)
	#print response.status_code
	logging.info(response.status_code)
	path = 'zdjecia/' + numer + '.jpg'
#	with open(path, 'w') as file_:
#		file_.write(response.content)
	liczba += 1
	time.sleep(1)

#print 'KONIEC'
logging.info('KONIEC')
