from Resources.People import People
from Resources.Vehicle import Vehicle
from Resources.Films import Films


# Methods to fetch Data
def get_people_data():
    obj = People()
    obj.fetch()
    obj.get_names()
    obj.get_count()


def get_vehicle_data():
    obj = Vehicle()
    obj.fetch()
    obj.get_names()
    obj.get_count()


def get_film_data():
    obj = Films()
    obj.fetch()
    obj.get_names()
    obj.get_count()


# Fetch People Data
# getPeopleData()
# Fetch Vehicle Data
# getVehicleData()
# fetch films data
get_film_data()
