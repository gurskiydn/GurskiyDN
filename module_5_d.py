import hashlib
import time
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()  # Хэшируем пароль
        self.age = age
class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration  # Продолжительность в секундах
        self.time_now = 0  # Текущая секунда просмотра
        self.adult_mode = adult_mode  # Ограничение по возрасту
class UrTube:
    def __init__(self):
        self.users = []  # Список пользователей
        self.videos = []  # Список видео
        self.current_user = None  # Текущий пользователь
    def log_in(self, nickname, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f"Пользователь {nickname} вошел в систему.")
                return
        print("Неверные имя пользователя или пароль.")
    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user  # Автоматически входим после регистрации
        print(f"Пользователь {nickname} зарегистрирован и вошел в систему.")
    def log_out(self):
        if self.current_user:
            print(f"Пользователь {self.current_user.nickname} вышел из системы.")
            self.current_user = None
        else:
            print("Никто не вошел в систему.")
    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)
                print(f"Видео '{video.title}' добавлено.")
            else:
                print(f"Видео '{video.title}' уже существует.")
    def get_videos(self, keyword):
        keyword_lower = keyword.lower()
        return [video.title for video in self.videos if keyword_lower in video.title.lower()]
    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео.")
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу.")
                    return
                print(f"Начало просмотра: {video.title}")
                while video.time_now < video.duration:
                    print(f"Смотрим {video.title}: {video.time_now} сек.")
                    time.sleep(1)  # Пауза в 1 секунду для имитации просмотра
                    video.time_now += 1
                print("Конец видео")
                video.time_now = 0  # Сброс времени просмотра
                return
        print("Видео не найдено.")

# Пример использования классов
ur = UrTube()
v1 = Video('Лучший язык программирования 2025 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.log_out()