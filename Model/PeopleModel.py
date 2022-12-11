from pydantic import BaseModel
from typing import List
from Model.Base import Base


class PeopleModel(Base):
    name: str
    birth_year: str
    eye_color: str
    films: List[str]
    gender: str
    hair_color: str
    height: str
    homeworld: str
    mass: str
    skin_color: str
    species: List[str]
    starships: List[str]
    vehicles: List[str]

class PeoplesModel(BaseModel):
    peoples: List[PeopleModel] = []


    def extend_films(self, results_data):
        people_dict = {"peoples": results_data}
        peoples_obj = PeoplesModel(**people_dict)
        self.peoples.extend(peoples_obj.peoples)

    def get_names(self):
        return list(map(lambda x: x.name, self.peoples))