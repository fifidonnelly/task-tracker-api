from flask import Flask, jsonify, request, abort

app = Flask(__name__)
tasks = []
task_id_counter = 1

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    data = request.get_json()
    if not data or 'title' not in data or not data['title'].strip():
        return jsonify({'error': 'Title is required and cannot be empty'}), 400
    task = {'id': task_id_counter, 'title': data['title'].strip(), 'completed': False}
    tasks.append(task)
    task_id_counter += 1
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    for task in tasks:
        if task['id'] == task_id:
            title = data.get('title')
            completed = data.get('completed')
            
            if title is not None:
                if not isinstance(title, str) or not title.strip():
                    return jsonify({'error': 'Title must be a non-empty string'}), 400
                task['title'] = title.strip()
            
            if completed is not None:
                if not isinstance(completed, bool):
                    return jsonify({'error': 'Completed must be a boolean'}), 400
                task['completed'] = completed
            
            return jsonify(task), 200
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    updated_tasks = [t for t in tasks if t['id'] != task_id]
    if len(updated_tasks) == len(tasks):
        return jsonify({'error': 'Task not found'}), 404
    tasks = updated_tasks
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
