# surveyAPI


Инструкция по установке:
  1. Скачать .zip или клонировать в удобную дирректорию.
  2. Установить зависимости,указанные в requirements.txt
  3. Для миграции бд, применить комманду python manage.py migrate
  4. Для запуска сервера применить комманду python manage.py runserver
  
  
Инструкция по API:
  1. Создание и просмотр всех опросов - <site.com>/surveys
  2. Изменение, удаление опроса - <site.com>/surveys/<int:pk>, где <int:pk> - id опроса
  3. Создание вопросов - <site.com>/questions
  4. Изменение, удаление вопроса - <site.com>/questions/<int:pk>, где <int:pk> - id вопроса
  5. Нвчать прохождение опроса - <site.com>/answer/<name>, где <name> - название опроса
  6. Ответить на вопрос - <site.com>/answer-for-question. Необходимо ввести ответ на вопрос и id вопроса
  7. Просмотр пройденных опросов - <site.com>/finished
  
Примеры:
Создание опроса:

    {
        "name": "Survey 4",
        "start_date": "2020-11-19",
        "end_date": "2020-11-19",
        "description": "adffsd",
        "questions": []
    }
    
 Создание вопроса:
 
     {
        "name": "Your state?",
        "survey": 1,
        "answer_type": "text",
        "answer_for_question": []
    }
    
Ответ на вопрос:

    {
        "answer": "Answer"
        "qurstion": 1
    }
