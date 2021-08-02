from mcstatus import MinecraftServer
import time
import traceback
import vk_api
vk = vk_api.VkApi(token="") 
ip = "135.181.208.40:25585" 
server = MinecraftServer.lookup(ip) 
friends = ["thedeaddan","MICROBOOM"] 
online = [] 
peer_id = 2000000197 
debug_mode = False # If u need print all info and errors in console
print_mode = True # If u need print all info in console
def get_message():
	message = vk.method("messages.getHistory",{"peer_id":peer_id,"count":1})
	return message
def send_message(text):
	vk.method("messages.send",{"peer_id":peer_id,"message":text,"random_id":0})
def ping():
	try:
		ping_value = str(server.ping()).split(".")[0] 
		if int(ping_value) > 150:
			if debug_mode or print_mode:
				print("Ping > 150! Await 5 sec...")
			time.sleep(5)
		else:
			if debug_mode or print_mode:
				print("[Ping]: "+str(ping_value))
	except Exception:
		if debug_mode:
			print(traceback.format_exc())
if debug_mode:
	print("Debug Mode activated! All prints are active.")
	send_message("[Бот] Внимание! Включен Debug режим. Просьба не реагировать на посылаемые ботом сообщения. Как только Дебаг закончится, сообщение удалится.")
	message = get_message()
	message_id = message.get("items")[0].get("id")
try:
	while True:
		try:
			ping()
			try:
				players = server.query().players.names  
			except Exception:
				print(traceback.format_exc())
			if debug_mode or print_mode:
				i = 0
				print("=====")
				for x in players: 
					i = i+1
					print(str(i)+". "+x)
				print("=====")
			for x in friends: 
				if x in players:
					if x not in online:
						if debug_mode:
							print("[Бот] "+x+" сейчас на сервере!")
						else:
							send_message("[Бот] "+x+" зашёл на сервер")
						online.append(x) 
			for x in online: 
				if x not in players:
					num = online.index(x) 
					if debug_mode: 
						print("[Бот] "+x+" вышел с сервера")
					else:
						send_message("[Бот] "+x+" сейчас на сервере!")
					online.pop(num) 
		except Exception:
			if debug_mode:
				print(traceback.format_exc())
		time.sleep(1) 
except KeyboardInterrupt:
	if debug_mode:
		vk.method("messages.delete",{"message_ids":message_id})
	else:
		print("GoodBye")
