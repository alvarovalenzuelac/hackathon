from flask import Flask, render_template
from carta import Unidad,Efecto

app = Flask(__name__)


ninja_cinturon_rojo = Unidad("Ninja Cinturón Rojo",3,"https://www.otakulegion.com/wp-content/uploads/2021/02/wp5243810-726x1024.png","jugadorA",4,3)
ninja_cinturon_negro = Unidad("Ninja Cinturón Negro",4,"https://www.nawpic.com/media/2020/giyu-tomioka-nawpic-12.jpg","jugadorB",4,5)

algoritmo_duro = Efecto("Algoritmo Duro",2,"https://www.ulyces.co/wp-content/uploads/2021/04/news-insta6-1.jpg","jugadorA","aumentar la resistencia del objetivo en 3","resistencia",3)
promesa_no_manejada = Efecto("Promesa no Manejada",1,"https://st.depositphotos.com/1007971/1962/i/600/depositphotos_19629067-stock-photo-broken-promises.jpg","jugadorB","reducir la resistencia del objetivo en 2","resistencia",-2)
programacion_en_pareja = Efecto("Programación en pareja",3,"https://blog.basetis.com/sites/default/files/media/imatge_header/spooning.png","jugadorA","aumentar el poder del objetivo en 2","poder",2)

cartas = [
    ninja_cinturon_rojo,
    algoritmo_duro,
    ninja_cinturon_negro,
    promesa_no_manejada,
    programacion_en_pareja
]

def jugada1():
    cartas_por_mostrar.append(ninja_cinturon_rojo)
def jugada2():
    cartas_por_mostrar.append(algoritmo_duro)
    algoritmo_duro.jugar(ninja_cinturon_rojo)
def jugada3():
    cartas_por_mostrar.append(ninja_cinturon_negro)
def jugada4():
    cartas_por_mostrar.append(promesa_no_manejada)
    promesa_no_manejada.jugar(ninja_cinturon_rojo)
def jugada5():
    cartas_por_mostrar.append(programacion_en_pareja)
    programacion_en_pareja.jugar(ninja_cinturon_rojo)
def jugada6():
    ninja_cinturon_rojo.atacar(ninja_cinturon_negro)

jugadas =[jugada1,jugada2,jugada3,jugada4,jugada5,jugada6]
app.siguiente_jugada = 0
app.cont = 0
cartas_por_mostrar = []

@app.route("/")
def hello_world():
    if app.siguiente_jugada <= len(jugadas)-1:
        jugadas[app.siguiente_jugada]()
        app.siguiente_jugada += 1
    #if app.cont <= (len(cartas)-1):
        #cartas_por_mostrar.append(cartas[app.cont])
        #app.cont += 1

    #print(app.cont)
    

    return render_template('index.html', cartas=cartas_por_mostrar)

app.run(debug=True)
