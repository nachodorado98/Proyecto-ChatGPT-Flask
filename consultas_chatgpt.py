import openai

key="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"

class ChatGPT():

	clave=openai.api_key=key

	def preguntar(self, pregunta_usuario):

		pregunta="Yo: "+pregunta_usuario
		respuesta=openai.Completion.create(
			engine="text-davinci-003", 
			prompt=pregunta, 
			temperature=0.5, 
			max_tokens=150,
			top_p=1,
			frequency_penalty=0,
			presence_penalty=0.6)

		resupuesta_chatgpt="AI: "+respuesta.choices[0].text.strip()

		return [pregunta, resupuesta_chatgpt]