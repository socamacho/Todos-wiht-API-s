from flask import Flask, jsonify, request
import json
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    tarea_nueva = json.loads(request_body)
    todos.append(tarea_nueva)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)
#SOLUCION Ex.7: En postman creamos un metodo POST, y en el body (row, text = json).Agregamos un objeto.

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos)
#SOLUCION Ex.8: En Postman, uso metodo delete y agrego /numero de la position al
#URL.



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

#SOLUCION.Ex4: En  la ruta desplegada por el browser, adiciono /todos y puedo ver mi mensaje HTML.
#SOLUCION. Ex5: Importar jsonify. En return DIRECTAMENTE jsonify(todos).
#SOLUCION.Ex 7.2: Ambos return devuelven el jsonify. En la linea 17,se adiciono tarea al todos.