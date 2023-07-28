from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

@app.route('/', methods=['GET'])
def hello():
    return "Hello, this is the To-Do list API!"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    tasks_list = [{"id": task.id, "title": task.title, "description": task.description} for task in tasks]
    return jsonify(tasks_list)

@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        abort(400)

    title = request.json['title']
    description = request.json.get('description', '')

    task = Task(title=title, description=description)
    db.session.add(task)
    db.session.commit()

    return jsonify({"id": task.id, "title": task.title, "description": task.description}), 201

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({"id": task.id, "title": task.title, "description": task.description})

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    if not request.json:
        abort(400)

    if 'title' in request.json:
        task.title = request.json['title']
    if 'description' in request.json:
        task.description = request.json['description']

    db.session.commit()

    return jsonify({"id": task.id, "title": task.title, "description": task.description})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Task deleted successfully"})




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
