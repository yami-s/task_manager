from task_manager import TaskManager

def main():
    task_manager = TaskManager()
    while True:
        print("1. Добавить задачу \n"
            "2. Изменить задачу \n"
            "3. Отметить задачу как выполненную \n"
            "4. Удалить задачу \n"
            "5. Поиск задач \n"
            "6. Просмотр всех задач \n"
            "0. Выход \n")
        choice = input("Выберите опцию: ")

        if choice == '1':
            name = input("Название: ")
            description = input("Описание: ")
            category = input("Категория: ")
            due_date = input("Срок выполнения (DD-MM-YYYY): ")
            priority = input("Приоритет (низкий, средний, высокий): ").lower()
            task_manager.add_task(name, description, category, due_date, priority)
        elif choice == '2':
            task_id = input("ID задачи для изменения: ")
            name = input("Новое название (оставьте пустым для пропуска): ") or None
            description = input("Новое описание (оставьте пустым для пропуска): ") or None
            category = input("Новая категория (оставьте пустым для пропуска): ") or None
            due_date = input("Новый срок выполнения (оставьте пустым для пропуска): ") or None
            priority = input("Новый приоритет (оставьте пустым для пропуска): ") or None
            task_manager.edit_task(task_id, name, description, category, due_date, priority)
        elif choice == '3':
            task_id = input("ID задачи для отметки как выполненной: ")
            task_manager.mark_task_as_done(task_id)
        elif choice == '4':
            task_id = input("ID задачи для удаления")
            task_manager.delete_task(task_id)
        elif choice == '5':
            keyword = input("Ключевое слово для поиска: ") or None
            results = task_manager.search_tasks(keyword)
            print(results)
        elif choice == '6':
            category = input("Категория (или оставьте пустым): ") or None
            task_manager.view_all_tasks(category)
        elif choice == '0':
            break

if __name__ == "__main__":
    main()