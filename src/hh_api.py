from abc import ABC, abstractmethod
from src.vacancy import Vacancy

import requests


class Api(ABC):
    """
    Абстрактный класс для работы с API по поиску вакансий.
    """

    @abstractmethod
    def get_vacancies(self, search_query):
        """
        Получает данные о вакансиях на основе поискового запроса.
        """
        pass


class HeadHunterAPI(Api):
    """
    Класс для работы с API HeadHunter (HH.ru).
    """

    def __init__(self):
        self.base_url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, search_query):
        """
        Получает данные о вакансиях с сайта HH.ru на основе поискового запроса.
        """
        settings = {"text": search_query, "area": 1}  # 1 - код региона (Москва)
        response = requests.get(self.base_url, params=settings).json()['items']
        vacancy_list = []
        for vacancy_info in response:
            name = vacancy_info.get('name', 'Не указано')
            alternate_url = vacancy_info.get('alternate_url', 'Не указано')
            salary_info = vacancy_info.get('salary')
            description = vacancy_info.get('description', 'Описание отсутствует')
            vacancy_list.append(Vacancy(name, alternate_url, salary_info, description).to_json())
        return vacancy_list
