import pytest
from task_manager import TaskManager 

@pytest.fixture
def task_manager():
    return TaskManager()

def test_add_task(task_manager):
    initial_task_count = len(task_manager.tasks)
    task_manager.add_task("Изучить основы FastAPI", "Пройти документацию по FastAPI и создать простой проект", "Обучение", "01-01-2025", "высокий")
    
    # Проверяем, что задача была добавлена
    assert len(task_manager.tasks) == initial_task_count + 1
    assert task_manager.tasks[-1]['name'] == "Новая задача"

def test_mark_task_as_done(task_manager):
    task_manager.add_task("Задача для выполнения", "Описание задачи", "Работа", "01-01-2025", "низкий")
    task_id = task_manager.tasks[0]['id']  # Получаем ID 
    
    # Помечаем задачу как выполненную
    task_manager.mark_task_as_done(task_id)
    
    # Проверяем статус
    assert task_manager.tasks[0]['status'] == "Выполнена"

def test_search_tasks(task_manager):
    # Добавляем несколько задач для поиска
    task_manager.add_task("Тест задача 1", "Описание 1", "Работа", "01-01-2025", "средний")
    task_manager.add_task("Тест задача 2", "Описание 2", "Личное", "02-01-2025", "низкий")
    
    # Ищем задачи
    found_tasks = task_manager.search_tasks("Тест")
    assert len(found_tasks) == 2  

def test_delete_task(task_manager):
    task_manager.add_task("Удаляемая задача", "Описание", "Работа", "2025-01-01", "высокий")
    task_id = task_manager.tasks[0]['id']  # Получаем ID 
    
    # Удаляем задачу
    task_manager.delete_task(task_id)
    assert len(task_manager.tasks) == 0