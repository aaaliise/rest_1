from requests import get, post, delete

print(get('http://localhost:5000/api/v2/jobs/1').json())
print(get('http://localhost:5000/api/v2/jobs/100').json())  # несуществующий id
print(get('http://localhost:5000/api/v2/jobs/q').json())  # id не int
print(get('http://localhost:5000/api/v2/jobs').json())
print(delete('http://localhost:5000/api/v2/jobs/q').json())  # не int
print(delete('http://localhost:5000/api/v2/jobs/100').json())  # удаление не существующего
print(post("http://localhost:5000/api/v2/jobs",
           json={'team_leader': 1,
                 'job': 'Заголовок',
                 'work_size': 1,
                 'collaborators': '1, 2',
                 'is_finished': False}).json())
print(get('http://localhost:5000/api/v2/jobs').json())  # id добавился
print(post("http://localhost:5000/api/v2/jobs",
           json={"surname": "Фамилия"}).json())  # недостаточно данных
print(post("http://localhost:5000/api/v2/jobs",  # неправильный запрос(не те аргументы)
           json={"surname": "Фамилия", "name": "name", "age": 2}).json())
print(delete("http://localhost:5000/api/v2/jobs/2").json())  # удаление верно
