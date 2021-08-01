from mcstatus import MinecraftServer
import time
import traceback
import vk_api
vk = vk_api.VkApi(token="") # VK Token for notification in the conversation
ip = "135.181.208.40:25585" # MineServer IP:Port
server = MinecraftServer.lookup(ip) # Connect to Server
friends = ["Steve","notch"] # list of ur friends
online = [] # Do not modify, temporary array
peer_id = 2000000197 # VK Dialog ID
debug_mode = False # Debug mode for add code and dont send message in dialog
errors = 0 # Do not modify, temporary array
while True:
	try:
		try:
			latency = str(server.ping()).split(".")[0] # get server ping
			print("ping: "+latency) # Print ping
			if int(latency) > 150: #Waiting so as not to send a lot of errors
				time.sleep(5)
		except Exception:
			errors = errors + 1 # Add the number of errors for the general report
			print("Количество зависаний: "+str(errors)) # Output of the number of errors
			if errors % 10 == 0 and not debug_mode:
				vk.method("messages.send",{"peer_id":peer_id,"message":"За сегодня сервер зависал уже "+str(errors)+" раз!","random_id":0}) # Sending if the number of errors is a multiple of 10
			time.sleep(5)
		query = server.query() # Request for server information
		players = query.players.names # Get server players
		i = 0
		for x in players: #Print players
			i = i+1
			print(str(i)+". "+x)
		print("=====")
		for x in friends: # Checking ur friend on server
			if x in players:
				if x not in online and not debug_mode:
					print("[Бот] "+x+" сейчас на сервере!")#Print return
					vk.method("messages.send",{"peer_id":peer_id,"message":"[Бот] "+x+" сейчас на сервере!","random_id":0})# Return in dialog // X - Ur friend nick
					online.append(x) # add ur friend in online array
		for x in online: # Checking for your friend's exit from the server
			if x not in players and not debug_mode:
				num = online.index(x) # Get ID ur friend in array 
				print("[Бот] "+x+" вышел с сервера")
				vk.method("messages.send",{"peer_id":peer_id,"message":"[Бот] "+x+" вышел с сервера","random_id":0})# Return in dialog // X - Ur friend nick
				online.pop(num) # Delete ur friend nick out of array
	except Exception:
		errors = errors + 1
		print("Количество зависаний: "+errors)
		if errors % 10 == 0:
			vk.method("messages.send",{"peer_id":peer_id,"message":"За сегодня сервер зависал уже "+str(errors)+" раз!","random_id":0})
	time.sleep(1) # Waiting, so as not to create a load
input()
