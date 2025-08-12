from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from settings import CSV_PATH
from settings import JSON_PATH
from settings import XLSX_PATH
from src.csv_xlsx_utils import get_csv
from src.csv_xlsx_utils import get_excel
from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.processing import filter_by_state
from src.processing import get_searched_transactions
from src.processing import sort_by_date
from src.utils import get_transaction_data
from src.widget import get_date
from src.widget import mask_account_card


def main() -> Optional[List[Dict[str, Any]]]:
    """
    Функция отвечает за основную логику проекта
    и связывает функциональности между собой.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    result: List[Dict[str, Any]] = []

    # Получение данных из файла
    while True:
        print("Выберите необходимый пункт меню:")
        print(
            "1. Получить информацию о транзакциях из JSON-файла"
            "\n2. Получить информацию о транзакциях из CSV-файла"
            "\n3. Получить информацию о транзакциях из XLSX-файла"
        )

        user_choose_point = input("Введите номер пункта меню (1-3): ").strip()

        if user_choose_point == "1":
            print("Для обработки выбран JSON-файл.")
            transaction_data = get_transaction_data(str(JSON_PATH))
            # Предполагается, что get_transaction_data возвращает Dict[str, Any]
            transactions: List[Dict[str, Any]] = transaction_data
            break

        elif user_choose_point == "2":
            print("Для обработки выбран CSV-файл.")
            transactions = get_csv(str(CSV_PATH))
            break

        elif user_choose_point == "3":
            print("Для обработки выбран XLSX-файл.")
            transactions = get_excel(str(XLSX_PATH))
            break

        else:
            print("Введен неверный номер пункта меню.")

    # Фильтрация по статусу
    print(
        "Выберите статус, по которому необходимо выполнить фильтрацию. "
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )

    while True:
        user_choose_status = input("Введите статус: ").strip().upper()

        if user_choose_status in ["EXECUTED", "CANCELED", "PENDING"]:
            transactions_filtered = filter_by_state(transactions, user_choose_status)
            break
        else:
            print(f"Статус операции {user_choose_status} недоступен")

    # Сортировка по дате
    while True:
        user_choose_data_filter = input("Отсортировать операции по дате? Да/Нет: ").strip().title()

        if user_choose_data_filter == "Да":
            while True:
                user_choose_data_filter_reverse = (
                    input("Отсортировать по убыванию или по возрастанию? ").strip().lower()
                )
                if user_choose_data_filter_reverse.lower() == "по убыванию":
                    sorted_transactions = sort_by_date(transactions_filtered)
                    break
                elif user_choose_data_filter_reverse.lower() == "по возрастанию":
                    sorted_transactions = sort_by_date(transactions, reverse=False)
                    break
                else:
                    print("Введен неверный ответ. Введите 'по возрастанию' или 'по убыванию'")
            break

        elif user_choose_data_filter == "Нет":
            sorted_transactions = transactions_filtered
            break

        else:
            print("Введен неверный ответ. Введите 'Да' или 'Нет'")

    # Фильтр по валюте (Рубль)
    transactions_by_currency: List[Dict[str, Any]] = []

    while True:
        user_choose_rub = input("Выводить только рублевые транзакции? Да/Нет: ").strip().title()

        if user_choose_rub == "Да":
            transactions_by_currency = list(filter_by_currency(sorted_transactions, "RUB"))
            break

        elif user_choose_rub == "Нет":
            transactions_by_currency = sorted_transactions
            break

        else:
            print("Введен неверный ответ. Введите 'Да' или  'Нет'")
            continue

    # Фильтр по слову в описании
    print("Отфильтровать список транзакций по определенному слову в описании?")

    while True:
        user_choose_word_filter = input("Да/Нет ").strip().title()

        if user_choose_word_filter == "Да":
            user_search = input("Введите слово для поиска по описанию: ")
            result_transactions_iterable = get_searched_transactions(transactions_by_currency, user_search)
            result = list(result_transactions_iterable)
            break

        elif user_choose_word_filter == "Нет":
            result = list(transactions_by_currency)
            break

        else:
            print("Введен неверный ответ. Введите 'Да' или  'Нет'")
            continue

    # Вывод результатов
    if result:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(result)}")

        for transaction in result:
            if "date" in transaction:
                description = next(transaction_descriptions(result), "Описание отсутствует")
                print(f'{get_date(transaction["date"])} {description}')

                from_account = transaction.get("from")
                to_account = transaction.get("to")
                amount_info = transaction.get("operationAmount") or {}
                amount_value = amount_info.get("amount") or transaction.get("amount")
                currency_name = amount_info.get("currency", {}).get("name") or transaction.get("currency_name")

                if from_account and to_account:
                    print(f"{mask_account_card(from_account)} -> {mask_account_card(to_account)}")
                elif not from_account and to_account:
                    print(f"{mask_account_card(to_account)}")

                if user_choose_point == "1":
                    # Для JSON файла предполагается структура с operationAmount и currency
                    print(f"Сумма: {amount_value} {currency_name}\n")
                elif user_choose_point in ["2", "3"]:
                    # Для CSV/XLSX предполагается структура с 'amount' и 'currency_name'
                    amount_str = str(amount_value) if amount_value is not None else ""
                    currency_str = str(currency_name) if currency_name is not None else ""
                    print(f"Сумма: {amount_str} {currency_str}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    return result


if __name__ == "__main__":
    main()
