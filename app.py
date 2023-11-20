from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route("/")
def root():
    return "Bienvenido a la API de Adrian Fuentes Hernandez<br/>Esta API forma parte del proyecto DAM 2023/2024 🤠"

@app.route("/character")
def falta_dato():
    return "Tiene que terminar la ruta /character/'id_del_personaje' para accedar a los datos de un personaje."

@app.route("/ayuda")
def help():
    return render_template("ayuda.html")

@app.route("/delete/<character_id>")
def borrado(character_id):
    conn = mysql.connector.connect(host='bgxxvvo90ixy8eb7ixyj-mysql.services.clever-cloud.com', user='uys3wvexwsduwfxe', passwd='OTMzZjpFh7Xw3p0PYBSm', database="bgxxvvo90ixy8eb7ixyj")

    cursor = conn.cursor()

    query = ("SELECT * FROM personajes WHERE nombre = %s")

    cursor.execute(query, (character_id,))

    datos = {}

    try:
        for (nombre, descripcion, especie, dimension) in cursor:
            datos = {
                "nombre" : nombre,
                "descripcion" : descripcion,
                "especie" : especie,
                "dimension" : dimension
            }
    except:
        pass

    if datos:
        cursor = conn.cursor()

        query = ("DELETE FROM personajes WHERE nombre = %s")

        cursor.execute(query, (character_id,))

        conn.commit()

    conn.close()

    if datos:
        vuelta = "Personaje borrado correctamente"
    else:
        vuelta = "No existe el personaje"
    return vuelta

@app.route("/create/<character_id>+<descripcion>+<especie>+<dimension>")
def insercion(character_id, descripcion, especie, dimension):
    conn = mysql.connector.connect(host='bgxxvvo90ixy8eb7ixyj-mysql.services.clever-cloud.com', user='uys3wvexwsduwfxe', passwd='OTMzZjpFh7Xw3p0PYBSm', database="bgxxvvo90ixy8eb7ixyj")

    query = ("SELECT * FROM personajes WHERE nombre = %s")

    cursor = conn.cursor()

    cursor.execute(query, (character_id,))

    datos = {}

    try:
        for (nombre, descripcion, especie, dimension) in cursor:
            datos = {
                "nombre" : nombre,
                "descripcion" : descripcion,
                "especie" : especie,
                "dimension" : dimension
            }
    except:
        pass

    if not datos:
        cursor = conn.cursor()

        query = ("INSERT INTO personajes (nombre, descripcion, especie, dimension) VALUES (%s, %s, %s, %s)")

        cursor.execute(query, (character_id, descripcion, especie, dimension))

        conn.commit()

    conn.close()
    if not datos:
        vuelta = "Personaje creado correctamente"
    else:
        vuelta = "Ya existe el personaje"
    return vuelta

@app.route("/character/<character_id>")
def character(character_id):
    conn = mysql.connector.connect(host='bgxxvvo90ixy8eb7ixyj-mysql.services.clever-cloud.com', user='uys3wvexwsduwfxe', passwd='OTMzZjpFh7Xw3p0PYBSm', database="bgxxvvo90ixy8eb7ixyj")

    cursor = conn.cursor()

    query = ("SELECT * FROM personajes WHERE nombre = %s")

    cursor.execute(query, (character_id,))

    datos = {}

    try:
        for (nombre, descripcion, especie, dimension) in cursor:
            datos = {
                "nombre" : nombre,
                "descripcion" : descripcion,
                "especie" : especie,
                "dimension" : dimension
            }
    except:
        pass

    if not datos:
        print("pepe")

    conn.close()
    return datos

if __name__ == "__main__":
    app.run(debug=True)