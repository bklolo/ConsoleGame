import pygame

class Audio:
    def __init__(self, path):
        self.path = path
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)
        pygame.mixer.init()
        self.sound1 = pygame.mixer.Sound(path)

    def play_song(self):
        # TODO make intro music
        # Music
        pygame.mixer.music.load(self.path)
        pygame.mixer.music.play(-1)