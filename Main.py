import fbchat

class CustomClient(fbchat.Client):
  def SEND(self,txt,thid,thg):
    self.send(fbchat.Message(text=txt),thread_id=thid,thread_type=thg)
  
  def onMessage(self,mid,author_id,message_object,thread_id,thread_type,ts,metadata,msg,**kwargs):
    pass
  


client = CustomClient("botymcbotface808@gmail.com","[Password]")

client.listen()
