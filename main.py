from src.hh_api import HeadHunterAPI
from src.vacancy_saver import JSONSaver
from src.utils import print_vacancies, filter_vacancies, sort_vacancies, get_top_vacancies


def user_interaction():
    # Функция для взаимодействия с пользователем
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()
    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies(search_query)
    # Сохранение информации о вакансиях в файл
    saver = JSONSaver()
    saver.write_data(hh_vacancies)
    print("Ответ API:", hh_vacancies)

    if hh_vacancies:
        vacancies_list = []

        for vac in hh_vacancies:
            print(vac)
            vacancies_list.append(vac)
        # Фильтрация, сортировка и выбор топ N вакансий
        print(vacancies_list)
        filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
        sorted_vacancies = sort_vacancies(filtered_vacancies)
        top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
        print_vacancies(top_vacancies)
    else:
        print("Не удалось получить вакансии. Пожалуйста, проверьте запрос и попробуйте снова.")


if __name__ == "__main__":
    user_interaction()
