from mcstatus import MinecraftServer
import time
import traceback
import vk_api
import datetime

vk = vk_api.VkApi(
    token="VKTOKEN"
)
ip = "135.181.208.40:25585"
server = MinecraftServer.lookup(ip)
friends = [
    "Evil_KoT",
    "Xrustalix",
]
online = []
peer_id = 2000000003
debug_mode = False
print_mode = True


def get_message():
    message = vk.method(
        "messages.getHistory", {"peer_id": peer_id, "count": 1}
    )
    return message


def send_message(text):
    vk.method(
        "messages.send", {"peer_id": peer_id, "message": text, "random_id": 0}
    )


def ping():
    try:
        now = datetime.datetime.now()
        ping_value = str(server.ping()).split(".")[0]
        if int(ping_value) > 250:
            if (debug_mode or print_mode) and online != []:
                message = get_message()
                message_id = message.get("items")[0].get("id")
                message_text = message.get("items")[0].get("text")
                if "Высокий пинг" in message_text:
                    vk.method(
                        "messages.edit",
                        {
                            "peer_id": peer_id,
                            "message": "Высокий пинг: "
                            + str(ping_value)
                            + "! В "
                            + str(now.hour)
                            + "ч. "
                            + str(now.minute)
                            + "м. "
                            + str(now.second)
                            + " с.",
                            "message_id": message_id,
                        },
                    )
                else:
                    send_message(
                        "Высокий пинг: "
                        + str(ping_value)
                        + "! В "
                        + str(now.hour)
                        + " ч. "
                        + str(now.minute)
                        + " м. "
                        + str(now.second)
                        + " с."
                    )
                print("Ping > 250! Await 5 sec...")
            time.sleep(5)
        else:
            if debug_mode or print_mode:
                print("[Ping]: " + str(ping_value))
    except Exception:
        if debug_mode:
            print(traceback.format_exc())


if debug_mode:
    print("Debug Mode activated! All prints are active.")
    send_message(
        "[Бот] Внимание! Включен Debug режим. Просьба не реагировать на посылаемые ботом сообщения. Как только Дебаг закончится, сообщение удалится."
    )
    message = get_message()
    message_id = message.get("items")[0].get("id")
try:
    while True:
        try:
            ping()
            try:
                players = server.query().players.names
            except Exception:
                if debug_mode:
                    print(traceback.format_exc())
            if debug_mode or print_mode:
                i = 0
                print("=====")
                for x in players:
                    i = i + 1
                    print(str(i) + ". " + x)
                print("=====")
            for x in friends:
                if x in players:
                    if x not in online:
                        if debug_mode:
                            print("[Бот] " + x + " сейчас на сервере!")
                        else:
                            send_message("[Бот] " + x + " зашёл на сервер")
                        online.append(x)
            for x in online:
                if x not in players:
                    num = online.index(x)
                    if debug_mode:
                        print("[Бот] " + x + " вышел с сервера")
                    else:
                        send_message("[Бот] " + x + " вышел с сервера!")
                    online.pop(num)
        except Exception:
            if debug_mode:
                print(traceback.format_exc())
        time.sleep(1)
except KeyboardInterrupt:
    if debug_mode:
        vk.method("messages.delete", {"message_ids": message_id})
    else:
        print("GoodBye")
