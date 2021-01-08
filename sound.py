door_sound = pygame.mixer.Sound('data\\door_05.wav')


def door():
    pygame.mixer.Sound.set_volume(door_sound, 0.2)
    pygame.mixer.Sound.play(door_sound)


