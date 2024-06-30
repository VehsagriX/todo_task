from database import session_f
from sqlalchemy import select
from models import Task
from schemas import  TasksDTO, TasksPostDto


class OrmCore:

    def insert_values(self, value):
        with session_f() as session:
            session.add(value)
            session.flush()
            session.refresh(value)
            task_id = value.id
            session.commit()
            return self.select_one(task_id)

    def select_all(self):
        with session_f() as session:
            query = select(Task)
            res = session.execute(query)
            tasks = res.scalars().all()
            result_dto = [TasksDTO.model_validate(task, from_attributes=True) for task in tasks]
            return result_dto

    def select_one(self, task_id: int):
        with session_f() as session:
            task = session.get(Task, task_id)
            if task is None:
                return {'Error': 'Task not found'}
            return task

    def update_some(self, task_id: int, value: TasksPostDto):
        with session_f() as session:
            task = session.get(Task, task_id)
            if task is None:
                return {'Error': 'Task not found'}
            task.title = value.title
            task.description = value.description
            session.commit()
            result = TasksDTO.model_validate(task, from_attributes=True)
            return result

    def get_delete(self, task_id: int):
        with session_f() as session:
            task = session.get(Task, task_id)
            if task:
                session.delete(task)
                session.commit()
                return task
            return


my_core = OrmCore()
