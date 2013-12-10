import urllib2
import json
import os
import time

class Cryptocurrency:
	def __init__(self,name):
		self.name = name
		self.file = self.name + '_overnight.csv'
		self.url = 'https://btc-e.com/api/2/' + self.name + '/ticker'
		
	def log_price(self):
		f = open(self.file, 'a')
		line = '\n'

		try:
			response = urllib2.urlopen(self.url)
			data = json.load (response)
			line = str(data['ticker'].values()).strip('[]') + '\n'
		except urllib2.HTTPError, err:
			line = str(err) + '\n'
		except:
			line = '--\n'
		
		f.write(line)
		f.close()

period = 60
i = 0
usd_rur = Cryptocurrency('usd_rur')
btc_ltc = Cryptocurrency('btc_ltc')

while True:
	if i > 24 * period:
		break

	usd_rur.log_price()
	btc_ltc.log_price()
	
	i = i + 1
	time.sleep(period)