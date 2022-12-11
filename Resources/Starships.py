from Service.MainService import Service
from Resources.ResourceBase import Base

class Starships(Base):
    # "variables"
    __response = []
    __page: int = 1
    __serviceobj = Service()

    def __init__(self, service = Service()):
        super().__init__()
        self.__serviceobj = service

    def __get_relative_url(self):
        return "starships/"

    def __get_complete_url(self):
        return self.host_url + self.__get_relative_url()

    def fetch(self):
        params = {"page": self.__page}
        res = self.__serviceobj.get_response(self.__get_complete_url(), params)
        result_data = res.get("results", [])
        count = res.get("count", "0")
        self.__response.extend(result_data)
        if len(self.__response) < int(count):
            self.__page +=1
            self.fetch()

    def get_name(self):
         if len(self.__response) > 0:
             names = list(map(lambda x: x.get("name"), self.__response))
             print(names)
         else:
            print("no people data found")


    def get_count(self):
        if len(self.__response) > 0:
            print("total count is {0}".format(len(self.__response)))
        else:
            print('count is zero for starships.')
