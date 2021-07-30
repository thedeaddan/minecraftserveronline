from mcstatus import MinecraftServer
import time
import vk_api
vk = vk_api.VkApi(token="") # VK Token for notification in the conversation
ip = "135.181.208.40:25585" # MineServer IP:Port
server = MinecraftServer.lookup(ip) # Connect to Server
friends = [""] # list of ur friends
online = [] # Do not modify, temporary array
peer_id = 2000000197 # VK Dialog ID
try:
	while True:
		query = server.query() # Request for server information
		players = query.players.names # Get server players
		for x in friends: # Checking ur friend on server
			if x in players:
				if x not in online:
					#print("[Бот] "+x+" сейчас на сервере!")
					vk.method("messages.send",{"peer_id":peer_id,"message":"[Бот] "+x+" сейчас на сервере!","random_id":0})# Return in dialog // X - Ur friend nick
					online.append(x) # add ur friend in online array
		for x in online: # Checking for your friend's exit from the server
			if x not in players:
				num = online.index(x) # Get ID ur friend in array 
				#print("[Бот] "+x+" вышел с сервера")
				vk.method("messages.send",{"peer_id":peer_id,"message":"[Бот] "+x+" вышел с сервера","random_id":0})# Return in dialog // X - Ur friend nick
				online.pop(num) # Delete ur friend nick out of array
		time.sleep(1) # Waiting, so as not to create a load
except Exception:
	print(traceback.format_exc())
