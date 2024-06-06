from auth import User
from message import Message
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
        self.msg = Message(silent=True)

    def log_in(self, login: str, password: str):
        user_check = User(login, password, None)
        if self.current_user and user_check == self.current_user:
            return
        for user in self.users:
            if user_check == user:
                if self.current_user:
                    self.log_out()
                self.current_user = user
                self.current_user.msg.user(4, self.current_user.nickname)
                return
        self.msg.user(3, login)

    def register(self, nickname: str, password: str, age: int, silent: bool = False):
        for user in self.users:
            if nickname == user.nickname:
                self.msg.user(1, nickname)
                return
        new_user = User(nickname, password, age, silent)
        UrTube.total_users += 1
        self.users.append(new_user)
        self.msg.user(2, nickname)
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user.msg.user(5, self.current_user.nickname)
        self.current_user = None

    def user_access_check(self, video):
        return video.author == self.current_user

    def add(self, *args):
        videos_to_add = [*args]
        if not self.current_user:
            self.msg.video_adg(1, *videos_to_add)
            return
        self.current_user.msg.video_adg(2, *videos_to_add)
        videos_to_add.reverse()
        n = len(videos_to_add) - 1
        while n >= 0:                                       # метод обратного цикла №1
            if not self.contains(videos_to_add[n]):
                video = videos_to_add.pop(n)
                self.videos.append(video)
                video.author = self.current_user
                UrTube.total_video += 1
                self.msg.video_adg(9, video, self.current_user.nickname)
            n -= 1
        if videos_to_add:
            videos_to_add.reverse()
            self.current_user.msg.video_adg(4, *videos_to_add)
            return
        self.current_user.msg.video_adg(3)

    def del_videos(self, *args):
        videos_to_del = [*args]
        if not self.current_user:
            self.msg.video_adg(5, *videos_to_del)
            return
        self.current_user.msg.video_adg(6, *videos_to_del)
        videos_to_del.reverse()
        for i in range(len(videos_to_del)-1, -1, -1):       # метод обратного цикла №2
            if self.contains(videos_to_del[i]):
                video = videos_to_del[i]
                if not self.user_access_check(video):
                    continue
                self.videos.remove(videos_to_del.pop(i))
                video.author = None
                UrTube.total_video -= 1
                self.msg.video_adg(10, video, self.current_user.nickname)
        if videos_to_del:
            videos_to_del.reverse()
            self.current_user.msg.video_adg(8, *videos_to_del)
            return
        self.current_user.msg.video_adg(7)

    def get_videos(self, key_word: str or None = None):
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
            self.msg.watch_video(2, video.title)
            return False
        elif video.adult_mode and self.current_user.age < 18:
            self.msg.watch_video(3, video.title)
            return False
        return True

    def watch_video(self, title: str, time_now: int = 0, speed: int = 1):
        video = self.contains(title)
        if not video:
            self.msg.watch_video(1, title)
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
        self.current_user.msg.watch_video(5, video.title, time_now, speed)
        while video.time_now < video.duration:
            sleep(sec)
            video.time_now += 1
            print(video.time_now, end=" ")
            if video.time_now == video.duration:
                self.current_user.msg.watch_video(4, video.title)
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

    def __repr__(self):
        return f'Всего видео: {UrTube.total_video}, пользователей: {UrTube.total_users}'
