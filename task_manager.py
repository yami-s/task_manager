from task import Task
from datetime import datetime
import json

class TaskManager:
    def __init__(self, data_file='tasks.json'):
        self.tasks = []
        self.data_file = data_file
        self.load_tasks()
        
    # Загружаем задачи из файла
    def load_tasks(self):
        try:
            with open(self.data_file, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []
    # Сохраняем задачи в файл
    def save_tasks(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=4)
    #проверка даты
    def validate_date(self, date_str):
        try:
            datetime.strptime(date_str, "%d-%m-%Y")
            return True
        except ValueError:
            return False
    # Добавляем задачу
    def add_task(self, name, description, category, due_date, priority):
        if not name or not description or not category:
                return "Ошибка: Названия, описания и категории задачи не могут быть пустыми"
        if not self.validate_date(due_date):
                    return "Ошибка: Дата должна быть в формате 'DD-MM-YYYY' и быть корректной"
        
        if priority not in ["низкий", "средний", "высокий"]:
            return "Ошибка: Приоритет должен быть 'низкий', 'средний' или 'высокий'"
        new_task = Task(name, description, category, due_date, priority)
        self.tasks.append(new_task.__dict__)
        self.save_tasks()
        return "Задача добавлена"
    # Помечаем задачу как выполненную
    def mark_task_as_done(self, task_id):
            for task in self.tasks:
                if task['id'] == task_id:
                    task['status'] = "Выполнена"
                    self.save_tasks()
                    return "Задача отмечена как выполненная."
            return "Ошибка: Задача не найдена."
    #Редактируем задачу
    def edit_task(self, task_id, name=None, description=None, category=None, due_date=None, priority=None):
        for task in self.tasks:
            if task['id'] == task_id:
                if name is not None:
                    task['name'] = name
                if description is not None:
                    task['description'] = description
                if category is not None:
                    task['category'] = category
                if due_date is not None:
                    task['due_date'] = due_date
                if priority is not None:
                    task['priority'] = priority
                self.save_tasks()  # Сохранение изменений
                return "Задача успешно отредактирована."
        return "Ошибка: Задача не найдена."
    #Удаляем задачу
    def delete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print("Задача удалена")
                return
        print("Задача с таким ID не найдена")


    def view_all_tasks(self, category=None,):
        for task in self.tasks:
            if category is None or task['category'] == category:
                print(task)
    # поиск задач
    def search_tasks(self, keyword=None, category=None, status=None):
        results = []
        for task in self.tasks:
            if (keyword and (keyword.lower() in task['name'].lower() or keyword.lower() in task['description'].lower())) or \
                (category and category.lower() == task['category'].lower()) or \
                (status and status.lower() == task['status'].lower()):
                results.append(task)
                
        return results