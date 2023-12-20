import requests
import json

class APIIntegration:

	def get_users(self,url):
		header = {
			'Content-Type': "application/json"

		}
		response = requests.get(url)
		res = response.text
		return res

	def post_users(self,url,body):
		header = {
			'content-type': "application/json"

		}

		response = requests.post(url,data=json.dumps(body),headers=header)
		res = response.text
		return res