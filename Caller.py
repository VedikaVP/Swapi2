from Resources.People import People
from Resources.Vehicle import Vehicle

# Methods to fetch Data
def getPeopleData():
    obj = People()
    obj.fetch()
    obj.get_names()
    obj.get_count()

def getVehicleData():
    obj = Vehicle()
    obj.fetch()
    obj.get_names()
    obj.get_count()


# Fetch People Data
# getPeopleData()
# Fetch Vehicle Data
getVehicleData()