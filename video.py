class Video:

    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode
        self.author = None

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title
