
import webapp2
import json
import cgi
from Handlers import LimitHandler
from Handlers import Alertas
from Handlers import PhoneHandler

class MainHandler(webapp2.RequestHandler):
	def post(self):
		try:
			jdata = json.JSONDecoder().decode(cgi.escape(self.request.body))
			Alertas.compararLimites(jdata)
		except (ValueError, TypeError):
			self.error(415) #Using 415 UNSUPPORTED MEDIA TYPE
			self.response.write("Not a JSON object")
			
	def get(self):
		self.response.write('Running module!')
		LimitHandler.set_Max_Alert("temperatura",45)
		LimitHandler.set_Min_Alert("temperatura",-10)
		#dict = {"Tipo":"temperatura","Valor":24,"Ubicacion":1}
		#PhoneHandler.set_new_userPhone("1","fruit samurai punch g","6643569771")
		#Alertas.compararLimites(dict)
	

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
