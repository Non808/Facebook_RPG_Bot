import fbchat
from random import randint

def nameMake(n=3,m=4):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiouy'
    consts = 'bcdfghjklmnpqrstvwxz'
    name = ''
    a = randint(1,n)
    for i in range(0,a):
        name += choice(alpha)
        name += choice(vowels)
        name += choice(consts)
    name += ' '
    b = randint(1,m)
    for i in range(0,b):
        name += choice(alpha)
        name += choice(vowels)
        name += choice(consts)

    return name.title()


class Game(object):

	class stats(object):
		def __init__(self,s,d,c,i):
			self.str,self.dex,self.con,self.int = s,d,c,i
	
	class Player(object):
		def __init__(self):
			pass
	
	class Enemy(object):
		def __init__(self,lev,typ,boss=False,wep=None,arm=None):
			self.type = typ
			self.boss = boss
			self.name = nameMake()
			self.level = lev
			self.stats = stats(randint(-lev+3,lev)+3,randint(-lev+1,lev)+1,randint(1,lev)+2,randint(-lev,lev)-1)
			self.HP = self.level*self.stats.con+self.level
			self.weapon = wep
			self.armour = arm
			if self.boss:
				self.title = str(self.name)+", King of the "+str(self.type)+"s."
			else:
				self.title = str(self.name)+" a "+str(self.type)+"."
				
		#def attack_close(self,target,
			
			
	class Map(object):
		
		class vector(object):
			def __init__(self,i,j):
				self.i = i
				self.j = j

		class City(object):

			class Quest(object):
				def __init__(self,lev):
					self.level = lev
					self.enemies = [Game.Enemy(self.level-i) for i in range(self.level)][::-1]
					self.name = "Kill "+str(self.enemies[-1].title)
					self.desc = "Kill "+str(self.enemies[-1].title)+" and co; reward: "+str(self.level*10)+" G."




			def __init__(self):
				self.name = nameMake()
				self.position = vector(randint(1,50),randint(1,50))
				self.quests = list()



		def __init__(self):
			self.name = "The Fbchat RPG Game"
			self.places = list()


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
