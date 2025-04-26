#create a simpe whiteboard app where users can write 
from flask import Flask, render_template, request

app = Flask(__name__)

# Lista para almacenar las notas
notes = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Obtener la nota que el usuario envió
        note = request.form.get('note')
        if note:
            notes.append(note)  # Agregarla a la lista de notas
    return render_template('index.html', notes=notes)

if __name__ == "__main__":
    app.run(debug=True)
    
    
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hola desde Azure"

if __name__ == '__main__':
    app.run()