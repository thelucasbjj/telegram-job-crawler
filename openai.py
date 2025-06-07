import openai
import json
from api_secrets import API_KEY

openai.api_key = API_KEY

with open('text.txt', 'r') as file:
    messages = file.read()

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Вакансия дня — менеджер по внутренним коммуникациям ✍🏻\n\nЧто нужно делать: вести блог, разрабатывать план публикаций и мероприятий для сотрудников, поддерживать и развивать корпоративную культуру и связи внутри компании.\n\nЧто ждем от вас: опыт работы в корпоративных коммуникациях от года, опыт организации мероприятий. Будут полезны навыки работы с текстом, фото и видео и навыки работы с бюджетом.\n\nПочему стоит откликнуться: достойный доход и бонус в конце года, работа из дома и в московском офисе у м. «Дмитровская», 5/2 с 09:00 до 18:00, ДМС, крутые коллеги и наставники и много других бонусов."
        },
        {
            "role": "system",
            "content": "Задача проанализировать и извлечь полезные данные для соискателей, так чтобы можно было фильтровать и быстро находить нужные вакансии"
        }
    ],
    temperature=0.7,
    functions=[
        {
            "name": "extract_data",
            "description": "Извлечение данных из текста вакансии",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "Место расположения вакансии. Это может быть город, страна. Может быть пустым"
                    },
                    "position": {
                        "type": "string",
                        "description": "Это конкретная должность или роль, которую займет кандидат"
                    },
                    "tags": {
                        "type": "array",
                        "description": "Это ключевые слова или фразы, которые описывают общие характеристики вакансии. Они помогают категоризировать вакансию и упрощают поиск для соискателей",
                        "items": {
                            "type": "string",
                            "enum": [
                                "FULL_TIME",
                                "PART_TIME",
                                "INTERNSHIP",
                                "FREELANCE",
                                "ON_SITE",
                                "VOLUNTEER",
                                "REMOTE",
                                "TEMPORARY",
                                "CONTRACT",
                                "FLEXIBLE_HOURS",
                                "HYBRID",
                                "NO_EXPERIENCE",
                                "ENTRY_LEVEL",
                                "EXPERIENCED"
                            ]
                        }
                    },
                    "title": {
                        "type": "string",
                        "description": "Это уникальное и конкретное описание вакансии, которое сразу же дает представление о должности и требованиях. Оно должно быть ясным и отражать суть вакансии."
                    }
                },
                "required": [
                    "title",
                    "position",
                    "tags"
                ]
            }
        }
    ],
    function_call="auto"
)

function = response.choices[0].message.get('function_call')

if function is not None:
    data = function.arguments
    data_dict = json.loads(data)
    print(json.dumps(data_dict, indent=4, ensure_ascii=False))