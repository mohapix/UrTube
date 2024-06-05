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
        for user in self.users:
            if user_check == user:
                if self.current_user:
                    self.log_out()
                self.current_user = user
                print(f'Привет, {self.current_user.nickname}')
                return
        print(f'Неверное имя пользователя или пароль')

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname == user.nickname:
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

    def user_access_check(self, video):
        return video.author == self.current_user

    def add(self, *args):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы добавить видео')
            return
        videos_to_add = [*args]
        videos_to_add.reverse()
        n = len(videos_to_add) - 1
        while n >= 0:                                       # метод обратного цикла №1
            if not self.contains(videos_to_add[n]):
                video = videos_to_add.pop(n)
                self.videos.append(video)
                video.author = self.current_user
                UrTube.total_video += 1
            n -= 1
        if videos_to_add:
            videos_to_add.reverse()
            print(f'Не удалось добавить видео:\n{videos_to_add}\n')
            return
        print('Все видео успешно добавлены')

    def del_videos(self, *args):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы удалить видео')
            return
        videos_to_del = [*args]
        videos_to_del.reverse()
        for i in range(len(videos_to_del)-1, -1, -1):       # метод обратного цикла №2
            if self.contains(videos_to_del[i]):
                video = videos_to_del[i]
                if not self.user_access_check(video):
                    continue
                self.videos.remove(videos_to_del.pop(i))
                UrTube.total_video -= 1
        if videos_to_del:
            videos_to_del.reverse()
            print(f'Не удалось удалить видео:\n{videos_to_del}\n')
            return
        print('Все видео успешно удалены')

    def get_videos(self, key_word=None):
        titles_list = []
        if not key_word:
            # titles_list = list(map(lambda titles: getattr(titles, 'title'), self.videos)) # метод №1
            titles_list = [video.title for video in self.videos]                            # метод №2
            return titles_list
        for video in self.videos:
            if key_word.lower() in video.title.lower():
                titles_list.append(video.title)
        if not titles_list:
            return f'Видео не найдено'
        return titles_list

    def show_all_videos(self):
        if not self.videos:
            return f'Нет добавленных видео'
        return f'Список всех видео:\n{self.get_videos()}\n'

    def watch_access_check(self, video):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return False
        elif video.adult_mode and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста, покиньте страницу')
            return False
        return True

    def watch_video(self, title, time_now=0, speed=1):
        video = self.contains(title)
        if not video:
            print('Видео не найдено')
            return
        elif not self.watch_access_check(video):
            return
        elif time_now >= video.duration:
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
        video.time_now = time_now
        watch_finished = False
        print(f"Запуск видео: '{video.title}' с {time_now} секунды со скоростью х{speed}")
        while video.time_now < video.duration:
            sleep(sec)
            video.time_now += 1
            print(video.time_now, end=" ")
            if video.time_now == video.duration:
                print('Конец видео')
                watch_finished = True
        if watch_finished:
            video.time_now = 0

    def contains(self, item):
        if not isinstance(item, str):
            item = item.title
        for video in self.videos:
            if item == video.title:
                return video
        return None

    def __str__(self):
        return f'Всего видео: {UrTube.total_video}, пользователей: {UrTube.total_users}'
