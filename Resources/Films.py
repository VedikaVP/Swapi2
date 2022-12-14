from Service.MainService import Service
from Resources.ResourceBase import Base
from Model.FilmModel import FilmModel, FilmsModel

class Films(Base):
    # Variables
    __filmsModel = FilmsModel()
    __page: int = 1
    __serviceObj = Service()

    # Initializers
    def __init__(self, service=Service()):
        super().__init__()
        self.__serviceObj = service

    # URL related code block
    def __get_relative_url(self):
        return "films/"

    def __get_complete_url(self):
        return self.host_url + self.__get_relative_url()

    # Data fetch related part
    def fetch(self):
        params = {"page": self.__page}
        res = self.__serviceObj.get_response(self.__get_complete_url(), params)
        results_data = res.get("results", [])
        count = res.get("count", 0)
        self.__filmsModel.extend_films(results_data)
        if len(self.__filmsModel.films) < int(count):
            self.__page += 1
            self.fetch()

    def get_names(self):
        if len(self.__filmsModel.films) > 0:
            print(self.__filmsModel.get_titles())
        else:
            print("No film name data found")

    def get_count(self):
        if len(self.__filmsModel.films) > 0:
            print("{0} data found".format(len(self.__filmsModel.films)))
        else:
            print("No film {0} data found".format(len(self.__filmsModel.films)))
