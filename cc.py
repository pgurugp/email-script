import urllib2
import json
import os
import time



class pair:
	def __init__(self,name,fileLocation,url,period):
		self.name = name
		self.file = fileLocation
		self.url = url
		self.period = period
		f = open(self.file, 'a')
		i = 0

		while True:
			# print ("it is working")
			if i%10 ==0:
				f = open(self.file, 'a')
			try:
				response = urllib2.urlopen(self.url)
			except urllib2.HTTPError, err:
				f.write(str(err) + '\n')
				continue
			except:
				f.write("--")
				continue
			data = json.load (response)
			line = str(data['ticker'].values()).strip('[]') + '\n'
			f.write(line)
			i = i+1
			if i%10 ==0:
				f.close()
				# print ("closed it")
			time.sleep(period)

usd_rur = pair('usd_rur', 'usd_rur_overnite.csv','https://btc-e.com/api/2/usd_rur/ticker', 60)