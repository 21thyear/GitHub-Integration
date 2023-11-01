from github import Github

# Ввод данных для аутентификации
username = input("Введите имя пользователя: ")
password = input("Введите пароль: ")
repo_name = input("Введите имя нового репозитория: ")

# Аутентификация в Github
g = Github(username, password)

# Создание нового репозитория
user = g.get_user()
repo = user.create_repo(repo_name)

# Вывод сообщения о создании репозитория
print(f"Репозиторий {repo.name} успешно создан!")
