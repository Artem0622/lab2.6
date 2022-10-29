import sys

if __name__ == '__main__':
    # Список студентов.
    students = []
    count = 0
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о студентах.
            name = input("Фамилия и инициалы? ")
            number = input("Номер группы? ")
            marks = list(map(int,input("Успеваемость").split()))
            # Создать словарь.
            student = {
                'name': name,
                'number': number,
                'marks': marks,
            }
            # Добавить словарь в список.
            students.append(student)
            # Отсортировать список в алфавитном порядке.
            if len(student) > 1:
                students.sort(key=lambda item: item.get('name', ''))
        # Заголовок таблицы.
        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                    "№",
                    "Ф.И.О.",
                    "Номер группы",
                    "Успеваемость"
                )
            )
            print(line)
            # Вывести данные о всех студентах.
            for idx, worker in enumerate(students, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                        idx,
                        worker.get('name', ''),
                        worker.get('number', ''),
                        ' '.join([str(x) for x in worker.get('marks', 0)])

                    )
                )
            print(line)
        # Получить данные о студентах имеющих хотя бы одну оценку.
        elif command == 'select':
            # Инициализировать счётчик
            count = 0
            # Проверить студентов хотя бы на одну оценку.
            for student in students:
                if 2 in student.get('marks', []):
                    count -= 1
                    print(
                        '{:>4} {}'.format('*', student.get('name', '')),
                        '{:>1} {}'.format('группа №', student.get('number', ''))
                    )
                    # Если счётчик равен 0, то оценки не найдены.
            if count == 0:
                print('Таких студентов нет')
        # Вывести справку о работе с программой.
        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить студента;")
            print("list - вывести список студентов;")
            print("select - вывести список студентов, имеющих оценку 2;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)