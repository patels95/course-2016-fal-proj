import dml
import matplotlib.pyplot as plt

class mapData():
	contributor = 'alaw_markbest_tyroneh'
	reads = ['alaw_markbest_tyroneh.PropertyGeoJSONs','alaw_markbest_tyroneh.StationsGeoJSONs']
	writes = []

	
	def data():
		'''Opens and retrieves data from Residental and Stations GeoJSONs'''

		client = dml.pymongo.MongoClient()
		repo = client.repo
		repo.authenticate('alaw_markbest_tyroneh', 'alaw_markbest_tyroneh')
		
		#pull Property and stations data
		data = (repo['alaw_markbest_tyroneh.PropertyGeoJSONs'].find(),repo['alaw_markbest_tyroneh.StationsGeoJSONs'].find())

		return data

	@staticmethod
	def visualize():
		'''Outputs matplotlib scatterplot'''

		prop_data,stat_data = mapData.data()

		rx = []
		ry = []

		cx = []
		cy = []

		for json in prop_data:
			y = json['value']['geometry']['coordinates'][0]
			x = json['value']['geometry']['coordinates'][1]

			if(json['value']['properties']['type'] == 'Residential'):
				rx.append(x)
				ry.append(y)
			else:
				cx.append(x)
				cy.append(y)

		sx = []
		sy = []

		# print(len(rx))
		# print(len(cx))

		for json in stat_data:
			y = json['value']['geometry']['coordinates'][0]
			x = json['value']['geometry']['coordinates'][1]
			sx.append(x)
			sy.append(y)

		# print(len(sx))
		plt.figure(figsize=(10,10))
		plt.scatter(rx, ry, color='blue')
		plt.scatter(cx, cy, color='blue')
		plt.scatter(sx, sy, color='red')
		#plt.ylim(42.23,42.41)
		#plt.xlim(-71.18,-70.993)
		plt.show()

		repo.logout()

# if __name__ == '__main__':
# 	mapData.visualize()
## eof
