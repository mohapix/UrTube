from auth import User
from time import sleep


class UrTube:
    """
    """
    total_video = 0
    total_users = 0

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        user_check = User(login, password, None)
        if self.current_user and user_check == self.current_user:
            return
        for i in range(len(self.users)):
            if user_check == self.users[i]:
                if self.current_user:
                    self.log_out()
                self.current_user = self.users[i]
                print(f'Привет, {self.current_user.nickname}')
                return
        print(f'Неверное имя пользователя или пароль')

    def register(self, nickname, password, age):
        if len(self.users) > 0:
            for i in range(len(self.users)):
                if nickname == self.users[i].nickname:
                    print(f'Пользователь {nickname} уже существует')
                    return
        new_user = User(nickname, password, age)
        UrTube.total_users += 1
        self.users.append(new_user)
        print(f'Пользователь {nickname} успешно зарегистрирован')
        self.log_in(nickname, password)

    def log_out(self, msg=True):
        nickname = self.current_user.nickname
        self.current_user = None
        if msg:
            print(f'До свидания, {nickname}')

    def add(self, *args):
        videos_to_add = [*args]
        videos_to_add.reverse()
        n = len(videos_to_add) - 1
        while n >= 0:
            index = self.contains(videos_to_add[n])
            if index or index == 0:
                pass
            else:
                self.videos.append(videos_to_add.pop(n))
                UrTube.total_video += 1
            n -= 1
        if len(videos_to_add):
            videos_to_add.reverse()
            print(f'Не удалось добавить видео:\n{videos_to_add}\n')

    def del_videos(self, *args):
        videos_to_del = [*args]
        videos_to_del.reverse()
        for i in range(len(videos_to_del)-1, -1, -1):
            index = self.contains(videos_to_del[i])
            if index or index == 0:
                self.videos.pop(index)
                UrTube.total_video -= 1
                videos_to_del.pop(i)
        if len(videos_to_del):
            videos_to_del.reverse()
            print(f'Не удалось удалить видео:\n{videos_to_del}\n')

    def get_videos(self, key_word=None):
        titles_list = []
        if not key_word:
            titles_list = list(map(lambda titles: getattr(titles, 'title'), self.videos))
            return titles_list
        for i in range(len(self.videos)):
            if key_word.lower() in self.videos[i].title.lower():
                titles_list.append(self.videos[i].title)
        if len(titles_list) == 0:
            return f'Видео не найдено'
        return titles_list

    def show_all_videos(self):
        if len(self.videos) == 0:
            return f'Нет загруженных видео'
        return f'Список всех видео:\n{self.get_videos()}\n'

    def user_access_check(self, i):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return False
        elif self.videos[i].adult_mode and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста, покиньте страницу')
            return False
        return True

    def watch_video(self, i, time_now=0, speed=1):
        if not self.user_access_check(i):
            return
        elif time_now >= self.videos[i].duration:
            return
        match speed:
            case 0.25:
                sec = 4
            case 0.5:
                sec = 2
            case 1:
                sec = 1
            case 2:
                sec = 0.5
            case 4:
                sec = 0.25
            case _:
                sec = 1
        self.videos[i].time_now = time_now
        watch_finished = False
        print(f"Запуск видео: '{self.videos[i].title}' с {time_now} секунды со скоростью х{speed}")
        while self.videos[i].time_now < self.videos[i].duration:
            sleep(sec)
            self.videos[i].time_now += 1
            print(self.videos[i].time_now, end=" ")
            if self.videos[i].time_now == self.videos[i].duration:
                print('Конец видео')
                watch_finished = True
        if watch_finished:
            self.videos[i].time_now = 0

    def contains(self, item):
        if not isinstance(item, str):
            item = item.title
        for i in range(len(self.videos)):
            if item == self.videos[i].title:
                return i
        return None

    def __str__(self):
        return f'Загружено видео: {UrTube.total_video}, пользователей: {UrTube.total_users}'
