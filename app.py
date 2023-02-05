from flask import Flask, render_template, url_for, request
from consultas_chatgpt import ChatGPT

conversacion=[]

app=Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():

	global conversacion

	if request.method=="GET":
		conversacion=[]
		return render_template("base.html")
	if request.method=="POST":
		pregunta=request.form.get("pregunta_chatgpt")
		pregunta_respuesta=ChatGPT().preguntar(pregunta)
		conversacion.append(pregunta_respuesta)
		return render_template("base.html", respuesta=conversacion)

if __name__=="__main__":

	app.run(debug=True)