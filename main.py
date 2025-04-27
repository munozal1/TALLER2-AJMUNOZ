from flask import Flask, jsonify, render_template, request, redirect, url_for
from app.models.perro import Perro
from app.models.gato import Gato
from app.models.huron import Huron
from app.models.boa_constrictor import Boa_Constrictor as Boa
import os
import dotenv

dotenv.load_dotenv(override=True)

app= Flask(__name__,template_folder="app/views")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/animales', methods=['GET','POST'])
def animales():
    if request.method=='GET':
        return render_template('index.html')
    else:
        pass

@app.route('/sonido/perro', methods=['GET'])
def get_perro():
    perro= Perro('Firulais',4,25,'Bulldog Ingles')
    sonido=perro.emitir_sonido()
    return jsonify({'Nombre':perro.get_nombre(),'Sonido':sonido}),200

@app.route('/sonido/gato', methods=['GET'])
def get_gato():
    gato= Gato('Michi','Gris',5,20)
    sonido=gato.emitir_sonido()
    return jsonify({'Nombre':gato.get_nombre(),'Sonido':sonido}),200

@app.route('/sonido/huron', methods=['GET'])
def get_huron():
    huron= Huron('Rasputin',3,23.8,'Colombia',5000)
    sonido=huron.hacer_sonido()
    return jsonify({'Nombre':huron.get_nombre(),'Sonido':sonido}),200

@app.route('/sonido/boa', methods=['GET'])
def get_boa():
    boa= Boa('Sami',7,30,'Brasil',5000,10)
    sonido=boa.hacer_sonido()
    return jsonify({'Nombre':boa.get_nombre(),'Sonido':sonido}),200

if __name__=="__main__":
    app.run(debug=True)