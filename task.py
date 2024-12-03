import uuid

class Task:
    def __init__(self, name, description, category, due_date, priority):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority 
        self.status = "Не выполнена"
    


