from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append({'id': len(tasks) + 1, 'task': task})
    return jsonify(tasks=tasks)

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify(tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True, port=4321)
