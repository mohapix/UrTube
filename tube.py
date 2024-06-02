from auth import User
from time import sleep


class UrTube:
    """

    """
    total_video = 0

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        if self.current_user and self.current_user.nickname == login:
            # print(f'Вы уже вошли')
            return
        user_check = User(login, password, False)
        for i in range(len(self.users)):
            if user_check == self.users[i]:
                self.current_user = self.users[i]
                print(f'Привет, {self.current_user.nickname}')
                del user_check
                return
        del user_check
        print(f'Неверное имя пользователя или пароль')

    def register(self, nickname, password, age):
        if len(self.users) > 0:
            for i in range(len(self.users)):
                if nickname == self.users[i].nickname:
                    print(f'Пользователь {nickname} уже существует')
                    return
        self.current_user = User(nickname, password, age)
        User.total += 1
        self.users.append(self.current_user)
        # print(f'Пользователь {nickname} успешно зарегистрирован')
        # print(f'Все пользователи:\n{self.users}')

    def log_out(self):
        self.current_user = None
        print('До свидания!')

    def add(self, *args):
        videos_to_add = [*args]
        videos_failed_to_add = []
        n = len(videos_to_add) - 1
        videos_to_add.reverse()
        while n >= 0:
            if len(self.videos) == 0:
                self.videos.append(videos_to_add.pop(n))
                UrTube.total_video += 1
                n -= 1
                continue
            if videos_to_add[n] in self:
                videos_failed_to_add.append(videos_to_add.pop(n))
            n -= 1
        self.videos += videos_to_add
        UrTube.total_video += len(videos_to_add)

        # print(f'Текущий список видео:\n{self.videos}')
        # if len(videos_failed_to_add):
        #     print(f'Не добавлены видео (уже есть):\n{videos_failed_to_add}')
        # print()

    def get_videos(self, key_word):
        titles_list = []
        for i in range(len(self.videos)):
            if key_word.lower() in self.videos[i].title.lower():
                titles_list.append(self.videos[i].title)
        if len(titles_list) == 0:
            return f'Видео не найдено'
        return titles_list

    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for i in range(len(self.videos)):
            if title == self.videos[i].title and self.videos[i].adult_mode and self.current_user.age < 18:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
                return
            elif title == self.videos[i].title:
                watch_finished = False
                while self.videos[i].time_now < self.videos[i].duration:
                    sleep(1)
                    self.videos[i].time_now += 1
                    print(self.videos[i].time_now, end=" ")
                    if self.videos[i].time_now == self.videos[i].duration:
                        print('Конец видео')
                        watch_finished = True
                if watch_finished:
                    self.videos[i].time_now = 0
                return
        # print(f'Видео не найдено')

    def __contains__(self, item):
        for i in range(len(self.videos)):
            if item.title == self.videos[i].title:
                return True
        return False

    def __str__(self):
        return f'Загружено видео: {UrTube.total_video}, пользователей: {User.total}'
