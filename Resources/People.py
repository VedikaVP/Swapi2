from Service.MainService import Service
from Resources.ResourceBase import Base
from Model.PeopleModel import PeopleModel, PeoplesModel

class People(Base):
    # Variables
    __peoplesModel = PeoplesModel()
    __page: int = 1
    __serviceObj = Service()

    # Initializers
    def __init__(self, service=Service()):
        super().__init__()
        self.__serviceObj = service

    # URL related code block
    def __get_relative_url(self):
        return "people/"

    def __get_complete_url(self):
        return self.host_url + self.__get_relative_url()

    # Data fetch related part
    def fetch(self):
        params = {"page": self.__page}
        res = self.__serviceObj.get_response(self.__get_complete_url(), params)
        results_data = res.get("results", [])
        self.__peoplesModel.extend_films(results_data)
        count = res.get("count", 0)
        if len(self.__peoplesModel.peoples) < int(count):
            self.__page += 1
            self.fetch()

    def get_names(self):
        if len(self.__peoplesModel.peoples) > 0:
            print(self.__peoplesModel.get_names())
        else:
            print("No people name data found")

    def get_count(self):
        if len(self.__peoplesModel.peoples) > 0:
            print("{0} data found".format(len(self.__peoplesModel.peoples)))
        else:
            print("No people {0} data found".format(len(self.__peoplesModel.peoples)))