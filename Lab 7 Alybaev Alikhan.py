                                                         # Lab 7 Alybaev Alikhan
# Task 1:
import pygame
import sys
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

background = pygame.image.load("base_micky.jpg").convert_alpha()
minute_hand = pygame.image.load("minute.png").convert_alpha()
second_hand = pygame.image.load("second.png").convert_alpha()

background = pygame.transform.scale(background, (WIDTH, HEIGHT))
center = (WIDTH // 2, HEIGHT // 2)
clock = pygame.time.Clock()

def blit_rotate(surface, image, center_pos, angle, offset_y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=(center_pos[0], center_pos[1] + offset_y))
    surface.blit(rotated_image, new_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    now = datetime.now()
    minutes = now.minute
    seconds = now.second + now.microsecond / 1_000_000

    minute_angle = -minutes * 6 - 55
    second_angle = -seconds * 6 - 90

    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    blit_rotate(screen, minute_hand, center, minute_angle, 520 - minute_hand.get_height() // 2)

    blit_rotate(screen, second_hand, center, second_angle, 520 - second_hand.get_height() // 2)

    pygame.display.flip()
    clock.tick(60)

# Task 2:
import pygame
import keyboard
import time
import os

pygame.init()
pygame.mixer.init()

playlist = [
    "Drake - God's Plan.mp3",
    "Future feat. Drake - Life Is Good.mp3",
    "Travis Scott feat. Drake - Sicko Mode.mp3"
]

current_index = 0  

def play_song():
    global current_index
    song = playlist[current_index]
    if os.path.exists(song):
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        print(f"▶ Играет: {os.path.basename(song)}")
    else:
        print(f"⚠ Файл не найден: {song}")

def stop_song():
    pygame.mixer.music.stop()
    print("⏹ Музыка остановлена")

def next_song():
    global current_index
    current_index = (current_index + 1) % len(playlist)
    play_song()

def previous_song():
    global current_index
    current_index = (current_index - 1) % len(playlist)
    play_song()

print("🎧 Музыкальный плеер запущен.")
print("Управление:")
print("  P - Play")
print("  S - Stop")
print("  N - Next")
print("  B - Previous")
print("  Q - Quit")

while True:
    if keyboard.is_pressed('p'):
        play_song()
        time.sleep(0.3) 
    elif keyboard.is_pressed('s'):
        stop_song()
        time.sleep(0.3)
    elif keyboard.is_pressed('n'):
        next_song()
        time.sleep(0.3)
    elif keyboard.is_pressed('b'):
        previous_song()
        time.sleep(0.3)
    elif keyboard.is_pressed('q'):
        print("👋 Выход из программы.")
        stop_song()
        break

    time.sleep(0.1)

# Task 3:
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Red Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

radius = 25
x = WIDTH // 2
y = HEIGHT // 2
speed = 20

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and y - radius - speed >= 0:
        y -= speed
    if keys[pygame.K_DOWN] and y + radius + speed <= HEIGHT:
        y += speed
    if keys[pygame.K_LEFT] and x - radius - speed >= 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x + radius + speed <= WIDTH:
        x += speed

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), radius)

    pygame.display.flip()

pygame.quit()
sys.exit()