class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname:
                if hash(password) == user.password:
                    self.current_user = user
                break

    def register(self, nickname, password, age):
        is_exist = False
        for user in self.users:
            if nickname == user.nickname:
                is_exist = True
                break
        if not is_exist:
            user = User(nickname, hash(password), age)
            self.users.append(user)
            self.log_in(user.nickname, user.password)
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None
        print('Осуществлен выход из учетной записи')

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, search_word):
        result = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, video_title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        is_exist = False
        cur_video = None
        for video in self.videos:
            if video_title == video.title:
                is_exist = True
                cur_video = video
                break
        if is_exist:
            if cur_video.adult_mode and self.current_user.age < 18:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
                return
            while cur_video.time_now < cur_video.duration:
                cur_video.time_now += 1
                print(cur_video.time_now, end = ' ')
            print('Конец видео')
            cur_video.time_now = 0


class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)

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
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
