# Welltory-Challenge
1. Для начала нужно скопировать репозиторий с github
    git clone https://github.com/Alikhan0707/Welltory-Challenge
2. Зайти в папку Welltory-Challenge и создать файл .env
    cd Welltory-Challenge
    vim .env
    
    и вставить данные переменного окружения:
    DATABASE_NAME = 'welltory_app_test'
    USERNAME = 'postgres'
    PASSWORD = '123456'
    HOST = 'db'
    PORT = 5432
3. Далее набрать в командной строке:
    docker-compose up
    
4. Создать хотябы одного юзера:
    http://0.0.0.0:8000/users
    метод: POST
    Json body: 
    { "username": "exampleUser", "email": "example@example.com", "password": "123" }
5. Отправить данные для расчета:
    http://0.0.0.0:8000/calculate
    метод: POST
    Json body:
{
  "user_id": 1,
  "data": {
    "x_data_type": "sleep_hours",
    "y_data_type": "morning_pulse",
    "x": [
      {
        "date": "2022-01-14",
        "value": 9.7
      },
      {
        "date": "2022-01-08",
        "value": 9.0
      },
      {
        "date": "2022-02-01",
        "value": 6.5
      },
      {
        "date": "2022-01-11",
        "value": 8.6
      },
      {
        "date": "2022-01-25",
        "value": 6.0
      },
      {
        "date": "2022-01-04",
        "value": 9.9
      },
      {
        "date": "2022-01-27",
        "value": 5.2
      },
      {
        "date": "2022-01-03",
        "value": 5.3
      },
      {
        "date": "2022-01-02",
        "value": 7.7
      },
      {
        "date": "2022-01-19",
        "value": 6.0
      },
      {
        "date": "2022-01-12",
        "value": 6.4
      },
      {
        "date": "2022-01-26",
        "value": 5.2
      },
      {
        "date": "2022-01-18",
        "value": 5.6
      },
      {
        "date": "2022-01-16",
        "value": 9.0
      },
      {
        "date": "2022-01-23",
        "value": 5.4
      },
      {
        "date": "2022-01-09",
        "value": 5.6
      },
      {
        "date": "2022-01-06",
        "value": 6.9
      },
      {
        "date": "2022-01-17",
        "value": 9.3
      },
      {
        "date": "2022-01-15",
        "value": 9.1
      },
      {
        "date": "2022-01-13",
        "value": 7.3
      }
    ],
    "y": [
      {
        "date": "2022-01-16",
        "value": 96
      },
      {
        "date": "2022-01-31",
        "value": 77
      },
      {
        "date": "2022-01-01",
        "value": 45
      },
      {
        "date": "2022-01-05",
        "value": 60
      },
      {
        "date": "2022-01-08",
        "value": 47
      },
      {
        "date": "2022-02-01",
        "value": 97
      },
      {
        "date": "2022-01-26",
        "value": 93
      },
      {
        "date": "2022-01-23",
        "value": 68
      },
      {
        "date": "2022-01-13",
        "value": 49
      },
      {
        "date": "2022-01-06",
        "value": 44
      },
      {
        "date": "2022-01-29",
        "value": 75
      },
      {
        "date": "2022-01-10",
        "value": 88
      },
      {
        "date": "2022-01-20",
        "value": 54
      },
      {
        "date": "2022-01-11",
        "value": 82
      },
      {
        "date": "2022-01-27",
        "value": 62
      },
      {
        "date": "2022-01-19",
        "value": 57
      },
      {
        "date": "2022-01-18",
        "value": 82
      },
      {
        "date": "2022-01-17",
        "value": 65
      },
      {
        "date": "2022-01-03",
        "value": 64
      },
      {
        "date": "2022-01-28",
        "value": 50
      }
    ]
  }
}