from qgis.core import QgsDistanceArea
padova = (45.4072378, 11.8933948)
lamon = (46.0415222, 11.7468249)

#https://qgis.org/pyqgis/master/core/QgsDistanceArea.html

d = QgsDistanceArea()
d.setEllipsoid('WGS84')


lat1, lon1 = padova
lat2, lon2 = lamon
# Remember the order is X,Y
point1 = QgsPointXY(lon1, lat1)
point2 = QgsPointXY(lon2, lat2)

distance = d.measureLine([point1, point2])
print(distance/1000)
