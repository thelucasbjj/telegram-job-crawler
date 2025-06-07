from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetHistoryRequest
import csv
import configparser

#from loguru import logger

#logger.add("logs/debug.log", rotation="500 MB", level="DEBUG")


#@logger.catch

config = configparser.ConfigParser()
config.read("config.ini")

def main():
    api_id = config['Telegram']['api_id']
    api_hash = config['Telegram']['api_hash']
    phone = config['Telegram']['phone']

    client = TelegramClient(phone, api_id, api_hash)

    client.start()

    chats = []
    last_date = None
    chunk_size = 200
    groups = []
    result = client(GetDialogsRequest(
        offset_date=last_date,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash=0
    ))
    chats.extend(result.chats)
    for chat in chats:
        try:
            if chat.megagroup:
                groups.append(chat)
        except:
            continue
    print("Выберите группу для парсинга сообщений и членов группы:")
    i = 0
    for g in groups:
        print(str(i) + "- " + g.title)
        i += 1
    g_index = input("Введите нужную цифру: ")
    target_group = groups[int(g_index)]
    print("Узнаём пользователей...")
    all_participants = client.get_participants(target_group)
    print("Сохраняем данные в файл...")
    with open("members.csv", "w", encoding="UTF-8") as f:
        writer = csv.writer(f, delimiter=",", lineterminator="\n")
        writer.writerow(["username", "name", "group"])
        for user in all_participants:
            if user.username:
                username = user.username
            else:
                username = ""
            if user.first_name:
                first_name = user.first_name
            else:
                first_name = ""
            if user.last_name:
                last_name = user.last_name
            else:
                last_name = ""
            name = (first_name + ' ' + last_name).strip()
            writer.writerow([username, name, target_group.title])
    print("Парсинг участников группы успешно выполнен.")

    offset_id = 0
    limit = 10
    all_messages = []
    total_messages = 0
    total_count_limit = 0
    history = client(GetHistoryRequest(
        peer=target_group,
        offset_id=offset_id,
        offset_date=None,
        add_offset=0,
        limit=limit,
        max_id=0,
        min_id=0,
        hash=0
    ))
    for message in history.messages:
        all_messages.append(message.message)
    out_text = ''''''
    for i in all_messages:
        out_text += ('_' * 30)
        out_text += '\n'
        out_text += str(i)
        out_text += '\n'
    with open('text.txt', 'w', encoding='utf-8') as f:
        f.write(out_text)


if __name__ == "__main__":
    main()