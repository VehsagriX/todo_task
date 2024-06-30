from flask import Flask, jsonify, request, json
from orm import my_core
from models import Task
from schemas import TasksPostDto, TasksDTO
from pydantic import ValidationError


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
json.provider.DefaultJSONProvider.ensure_ascii = False



@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = my_core.select_all()
    tasks_dto = [task.model_dump_json(indent=1) for task in tasks]
    return jsonify({'result': tasks_dto}), 200


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_one_task(task_id):
    task = my_core.select_one(task_id)
    if isinstance(task, dict):
        return jsonify(task), 404
    res = TasksDTO.model_validate(task, from_attributes=True)
    return res.model_dump_json(indent=1), 201


@app.route('/tasks')
@app.route('/tasks', methods=['POST'])
def add_task():
    try:
        task = TasksPostDto.parse_raw(request.data)
    except ValidationError as e:
        return jsonify({'message': str(e)}), 400
    else:
        value = Task(title=task.title, description=task.description)
        res = my_core.insert_values(value)
        result = TasksDTO.model_validate(res, from_attributes=True)
        return result.model_dump_json(indent=1), 201


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id: int):
    try:
        task = TasksPostDto.parse_raw(request.data)
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400
    else:
        res = my_core.update_some(task_id, task)
        if isinstance(res, dict):
            return jsonify(res)
        return res.model_dump_json(indent=1), 201


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id: int):
    res = my_core.get_delete(task_id)
    if res is None:
        return jsonify({'Error': 'Task not found'}), 404
    return jsonify({'message': 'Successfully deleted'}), 200


if __name__ == '__main__':
    app.run(debug=True)
