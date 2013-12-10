import urllib2
import json
import os
import time

class Cryptocurrency:
	def __init__(self,name,period):
		self.name = name
		self.file = self.name + '_overnight.csv'
		self.url = 'https://btc-e.com/api/2/' + self.name + '/ticker'
		self.period = period
		
	def log_price(self):
		f = open(self.file, 'a')

		try:
			response = urllib2.urlopen(self.url)
		except urllib2.HTTPError, err:
			f.write(str(err) + '\n')
		except:
			f.write("--")
		
		data = json.load (response)
		line = str(data['ticker'].values()).strip('[]') + '\n'
		f.write(line)
		
		f.close()
		return True

period = 60
i = 0
usd_rur = Cryptocurrency('usd_rur', period)

while True:
	if i > 24 * period:
		break
	res = usd_rur.log_price()
	if res:
		i = i + 1
		time.sleep(period)