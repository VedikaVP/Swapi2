from typing import Optional, List
from pydantic import BaseModel
from Model.Base import Base

class FilmModel(Base):
    title: str
    episodeid: Optional[int]
    openingcrawl: Optional[str]
    director: str
    producer: str
    characters: List[str]
    planets: List[str]
    starships: List[str]
    vehicles: List[str]
    species: List[str]

class FilmsModel(BaseModel):
    films: List[FilmModel] = []

    def extend_films(self, results_data):
        film_dict = {"films": results_data}
        films_obj = FilmsModel(**film_dict)
        self.films.extend(films_obj.films)

    def get_titles(self):
        return list(map(lambda x: x.title, self.films))