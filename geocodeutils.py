import urllib
import arcpy
from arcpy import env
import json
from time import sleep
import csv


class Geocodeutils:

     def __init__(self):

        # syncing the config options
        self.configpath = "assets/config.json"
        self.syncConfigData()
        env.workspace = self.ConfigData[u'environment']

        # setting variable array & arcpy objects.
        self.Address = []
        self.Points = []
        self.Elevation = []
        self.ptGeoms = []
        self.sr = arcpy.SpatialReference(4326)
        self.pt = arcpy.Point()
        
        # initializing the process
        self.fetchCSVData()
        self.getlatlngInfo()
        self.getElevationInfo()
        self.pushInfoToDB()


     def syncConfigData(self):
        with open(self.configpath , mode='r') as data:    
            self.ConfigData = json.load(data)

     def fetchCSVData(self):
         with open(self.ConfigData[u'places'], 'rb') as csvfile:
	         reader = csv.reader( csvfile, delimiter = str(self.ConfigData[u'delimiter']) )
	         for row in reader:
		         self.Address.append(row[0])

     def getlatlngInfo(self):
         for row in self.Address:
	         sleep(float(self.ConfigData[u'timeout']))
	         arg = row + ' ' + self.ConfigData[u'poi1'] + ' ' + self.ConfigData[u'poi2']
	         returnset = self.geocodeHandler(arg)
	         lat = returnset['lat']
	         lng = returnset['lng']
	         arr = []
	         arr.append(lat)
	         arr.append(lng)
	         self.Points.append(arr)

     def getElevationInfo(self):
         for row in self.Points:
	        sleep(float(self.ConfigData[u'timeout']))
	        z = self.elevationHander(row)
	        self.Elevation.append(z)


     def pushInfoToDB(self):
		 #pusing geom into a Point object.
		 for p in self.Points:               

				self.pt.X = p[1]
				self.pt.Y = p[0]
				self.pt.Z = self.Elevation[self.Points.index(p)]
				self.ptGeoms.append(arcpy.PointGeometry(self.pt,self.sr,True))

		 bool = arcpy.Exists(self.ConfigData[u'featureclass'])
		 if bool:
			arcpy.Delete_management(self.ConfigData[u'featureclass'])

		 arcpy.CopyFeatures_management(self.ptGeoms, self.ConfigData[u'featureclass'])
		 arcpy.AddField_management(self.ConfigData[u'featureclass'], "Place", "TEXT", "", "", "50")
		 itr = 0
		 with arcpy.da.UpdateCursor(self.ConfigData[u'featureclass'],'Place') as cursor:
			for row in cursor:
				 row[0] = self.Address[itr]    #Naming the Points Accordingly
				 itr += 1
				 cursor.updateRow(row)       

    
     def geocodeHandler(self,addr):
	    url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" % (urllib.quote(addr.replace(' ', '+')))
	    data = urllib.urlopen(url).read()
	    returnset = json.loads(data).get("results")[0].get("geometry").get("location")
	    return returnset

     def elevationHander(self,point):
           point_str = str(point[0])+','+str(point[1])
           url = "http://maps.googleapis.com/maps/api/elevation/json?locations=%s&sensor=false" %   (urllib.quote(point_str))
           data = urllib.urlopen(url).read()
           returnset = json.loads(data).get("results")[0].get("elevation")
           return returnset



if __name__ == '__main__':

    geocodeutils =  Geocodeutils()
