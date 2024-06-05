from video import Video
from tube import UrTube


def watch_video(title, time_start=0, speed=1):
    ur.watch_video(title, time_start, speed)


ur = UrTube()
v0 = Video('Как сделать лучший пирог?', 30, adult_mode=True)
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 5, adult_mode=True)
v3 = Video('Как сделать лучший пирог?', 100)
v4 = Video('Программирование на Python', 150)
v5 = Video('Python для чайников', 50)

# Добавление видео
print(ur.show_all_videos())
ur.add(v1, v2)
ur.register('PetyaPetrov', 'qwerty', 18)
ur.add(v1, v2)
ur.register('Alex Pushkin', 'wasd', 16)
ur.add(v0, v3, v1, v4, v5)
ur.log_out()

# Удаление видео
ur.del_videos(v1, v2)
ur.log_in('Alex Pushkin', 'wasd')
ur.del_videos(v1, v2)
ur.del_videos(v0, v4)
ur.del_videos(v3, v5, v0)
ur.log_out()

# Проверка поиска
print(ur.show_all_videos())
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

# Проверка логина и выхода
ur.log_in('vasya_pupkin', 'F8098FM8fjm9jmi')
ur.log_out()
ur.log_in('vasya_pupkin', 'lolkekcheburek')

# Попытка воспроизведения несуществующего видео
watch_video('Лучший язык программирования 2024 года!')

# Воспроизведение видео с заданных времени и скорости
watch_video('Лучший язык программирования 2024 года', 190, 4)
