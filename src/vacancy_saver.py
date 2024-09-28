from abc import ABC, abstractmethod
import json

from src.vacancy import Vacancy


class VacancySaver(ABC):
    """
    Абстрактный класс для сохранения вакансий.
    """

    @abstractmethod
    def write_data(self, vacancy):
        pass


    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class JSONSaver(VacancySaver):
    """
    Класс для сохранения вакансий в формате JSON.
    """

    def __init__(self, filename="vacancies.json"):
        self.filename = f"data/{filename}"

    def write_data(self, vacancy):
        with open(self.filename, "w") as f:
            json.dump(vacancy, f, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancy):
        pass
    