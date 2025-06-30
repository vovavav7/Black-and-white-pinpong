import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

center_x, center_y = WIDTH // 2, HEIGHT // 2
radius = 100
speed = 5

background = pygame.Surface((WIDTH, HEIGHT))
for y in range(0, HEIGHT):
    for x in range(0, WIDTH):
        color = random.choice([WHITE, BLACK])
        pygame.draw.rect(background, color, (x, y, 1, 1))

map1 = []
for y in range(radius * 2):
    row = []
    for x in range(radius * 2):
        row.append(random.choice([WHITE, BLACK]))
    map1.append(row)

def draw_pixel_circle(center_x, center_y, radius, pixel_map):
    for y in range(radius * 2):
        for x in range(radius * 2):
            dx = x - radius
            dy = y - radius
            if dx*dx + dy*dy <= radius*radius:
                color = pixel_map[y][x]
                px = center_x + dx
                py = center_y + dy
                if 0 <= px < WIDTH and 0 <= py < HEIGHT:
                    screen.set_at((px, py), color)

font = pygame.font.Font(None, 36)

angel = [random.randint(-speed, speed), random.randint(-speed, speed)]

running = True
while running:
    screen.blit(background, (0, 0))  # Малюємо фон

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_pixel_circle(center_x, center_y, radius, map1)

    center_x += angel[0]
    center_y += angel[1]

    if center_x > WIDTH - radius or center_x < radius:
        angel[0] = -angel[0]

    if center_y > HEIGHT - radius or center_y < radius:
        angel[1] = -angel[1]


    fps = int(clock.get_fps())
    text_surface = font.render(f"FPS: {fps}", True, (20, 255, 20))
    screen.blit(text_surface, (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
