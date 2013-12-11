import urllib2
import json
import os
import time

class Cryptocurrency:
	def __init__(self,name):
		self.name = name
		self.file = 'data/' + self.name + '_overnight.csv'
		self.url = 'https://btc-e.com/api/2/' + self.name + '/ticker'
		
	def get_latest_prices(self):
		try:
			data = json.load( urllib2.urlopen(self.url) )
			data['error'] = ''
		except urllib2.HTTPError as err:
			data = json.load( '{"error":"' + str(err) + '"}' )
			
		self.data = data
		return data
		
	def log_price(self,fetch_data=true):
		f = open(self.file, 'a')
		line = '\n'

		if fetch_data:
			self.get_latest_prices()

		if self.data['error'] == '':
			line = str(self.data['ticker'].values()).strip('[]') + '\n'
		else:
			line = self.data['error'] + '\n'
		
		f.write(line)
		f.close()

period = 60
i = 0
usd_rur = Cryptocurrency('usd_rur')
btc_ltc = Cryptocurrency('ltc_btc')

while True:
	if i > 24 * period:
		break

	usd_rur.log_price()
	btc_ltc.log_price()
	
	i = i + 1
	time.sleep(period)