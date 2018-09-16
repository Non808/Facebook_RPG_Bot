import fbchat

class CustomClient(fbchat.Client):
	def getAuthor(self,author_id):
		a = str(self.fetchUserInfo(author_id)[autor_id])
		nam = ""
		for c in a[5:]:
			if c == "(":
				break
			else:
				nam += c
		return nam[1:-1]
	
	def SEND(self,txt,thid,thg):
		self.send(fbchat.Message(text=txt),thread_id=thid,thread_type=thg)
    
	def onMessage(self,mid,author_id,message_object,thread_id,thread_type,ts,metadata,msg,**kwargs):
		pass


client = CustomClient("botymcbotface808@gmail.com","[Password]")

client.listen()
