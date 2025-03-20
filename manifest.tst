Task 1. Python introduction
Description

Условие задачи

С использованием базы MySQL (или другая реляционная БД, например, PostgreSQL) создать схему данных соответствующую файлам во вложении (связь многие к одному)

Написать скрипт, целью которого будет загрузка этих двух файлов и запись данных в базу

Необходимые запросы к БД

Список комнат и количество студентов в каждой из них

5 комнат, где самый маленький средний возраст студентов

5 комнат с самой большой разницей в возрасте студентов

Список комнат где живут разнополые студенты

Требования и замечания

Предложить варианты оптимизации запросов с использования индексов

В результате надо сгенерировать SQL запрос который добавить нужные индексы

Выгрузить результат в формате JSON или XML

Всю "математику" делать стоит на уровне БД.

Командный интерфейс должен поддерживать следующие входные параметры

students (путь к файлу студентов)

rooms (путь к файлу комнат)

format (выходной формат: xml или json)

использовать ООП и SOLID.

отсутствие использования ORM (использовать SQL)

Перед тем как приступать к задаче

Убедись, что ты правильно понял условие

Создал и настроил виртуальное окружение

Продумал архитектуру

Декомпозировал на подзадачи в Jira тикете