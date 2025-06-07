import json
import datetime

def addgroup_meslast_6hours():
    ''' Добавление чтения групп из файла groups.json и сбора всех сообщений за последние 6 часов '''

    with open('group.json', 'r', encoding='utf-8') as file_json:
        groups = json.load(file_json)


    app = 'client'

    async def get_message():
        async with app:
            async for group in groups:
                group_id = group['id']
                six_hours_ago = datetime.datetime.now() - datetime.timedelta(hours=6)
                message = app.get(group_id, limit=None, offset_date = six_hours_ago)