import pygame
import random
import math
import pygame.font
import sys
from pygame.math import Vector2 as vector
from pygame import locals



class Particle:
    def __init__(self, position, velocity, color):
        self.position = vector(position)
        self.velocity = vector(velocity)
        self.acceleration = vector(0, 0.05)  # 模拟重力
        self.lifetime = 255  # 粒子的生命周期，用于透明度
        self.color = color


    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.lifetime -= 3
        if self.lifetime < 0:
            self.lifetime = 0


    def draw_1(self, screen):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), self.lifetime)  # 使用透明度
        num_points = 100
        heart_points = []
        for i in range(num_points):
            t = i / num_points * 2 * math.pi
            x = 10 * math.sin(t) ** 3
            y = 8 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
            heart_points.append((int(self.position.x + x), int(self.position.y - y)))
        pygame.draw.polygon(screen, color, heart_points)


    def draw_2(self, screen):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), self.lifetime)
        pygame.draw.ellipse(screen, color, pygame.Rect(int(self.position.x), int(self.position.y), 6, 20))


    def draw_3(self, screen):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), self.lifetime)
        pygame.draw.ellipse(screen, color, pygame.Rect(int(self.position.x), int(self.position.y), 2, 20))


class Firework:
    def __init__(self, position):
        self.position = vector(position)
        self.exploded = False
        self.velocity = vector(0, random.uniform(5, 15))  # 初始向上的速度
        self.particles = []
        self.a_1 = False
        self.a_2 = False
        self.a_3 = False


    def update(self):
        if not self.exploded:
            self.position -= self.velocity
            if 0 <= self.position.x <= 240 or 600 <= self.position.x <= 840 or 1680 <= self.position.x <= 1920 or 1200 <= self.position.x <= 1440:
                if self.position.y < random.uniform(0, 250):
                    self.a_1 = True  # 当速度变为向下时，烟花爆炸
                    self.explode_1()
            if 240 <= self.position.x <= 480 or 960 <= self.position.x <= 1200:
                if self.position.y < random.uniform(0, 250):
                    self.a_2 = True
                    self.explode_2()
            if 480 <= self.position.x <= 600 or 700 <= self.position.x <= 750 or 840 <= self.position.x <= 960 or 1440 <= self.position.x <= 1680:
                if self.position.y < random.uniform(0, 250):
                    self.a_3 = True
                    self.explode_3()
        else:
            for particle in self.particles:
                particle.update()


    def explode_1(self):
        self.exploded = True
        for i in range(30):
            particle_velocity = vector(random.uniform(-3, 3), random.uniform(-3, 3))
            particle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.particles.append(Particle(self.position, particle_velocity, particle_color))


    def explode_2(self):
        self.exploded = True
        for i in range(70):
            particle_velocity = vector(random.uniform(-3, 3), random.uniform(-3, 3))
            particle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.particles.append(Particle(self.position, particle_velocity, particle_color))


    def explode_3(self):
        self.exploded = True
        for i in range(70):
            particle_velocity = vector(random.uniform(-3, 3), random.uniform(-3, 3))
            particle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.particles.append(Particle(self.position, particle_velocity, particle_color))


    def draw(self, screen):
        if not self.exploded:
            pygame.draw.ellipse(screen, (255, 255, 255), pygame.Rect(int(self.position.x), int(self.position.y), 2, 800))  # 绘制未爆炸的烟花
        else:
            if self.a_1:
                for particle in self.particles:
                    particle.draw_1(screen)
            elif self.a_2:
                for particle in self.particles:
                    particle.draw_2(screen)
            elif self.a_3:
                for particle in self.particles:
                    particle.draw_3(screen)


def main():
    pygame.init()
    screen_width = 1920
    screen_height = 1080
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("新年烟花")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("SimHei", 100, bold=True, italic=True)
    fireworks = []
    firework_timer = 0  # 用于定时创建烟花

    pygame.mixer.music.load(r"D:\海贼王1.mp3")
    pygame.mixer.music.play(1)

    # 加载视频文件
    for i in range(254):

        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == 32:
                    pygame.quit()
                    sys.exit()

        background=pygame.image.load(r'D:\图片1\海贼王2.mp4_%d.jpg'%i)
        screen.blit(background, (0, 0))

        pygame.display.update()
        clock.tick(9.8)

    pygame.mixer.music.load(r"D:\海贼王1.1.mp3")
    pygame.mixer.music.play(-1)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == 32:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:  # 检测鼠标点击事件
                if event.button == 1:  # 检查是否是鼠标左键点击
                    # 在这里添加鼠标点击后的操作，例如创建烟花
                    fireworks.append(Firework(event.pos))


        screen.fill((0, 0, 0))

        # 更新视频帧


        text_1 = font.render('王士豪', True, (255, 255, 255))
        screen.blit(text_1, (screen_width // 2 - text_1.get_width() // 2, screen_height // 2-120))
        text_2 = font.render("新年快乐!", True, (255, 255, 255))
        screen.blit(text_2, (screen_width // 2 - text_2.get_width() // 2, screen_height // 2 ))

        # 定时创建烟花
        firework_timer += 1
        if firework_timer >= 10:  # 每 30 帧创建一个烟花
            fireworks.append(Firework((random.randint(0, screen_width), screen_height)))
            firework_timer = 0

        fireworks = [i for i in fireworks if not i.exploded or any(particle.lifetime > 0 for particle in i.particles)]

        # 移除已经消失的烟花

        for firework in fireworks:
            firework.update()
            firework.draw(screen)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
    pygame.quit()





