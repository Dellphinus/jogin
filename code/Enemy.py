#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Const import WIN_HEIGHT
import pygame




class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay <= 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
        return None  # Retorna None se não atirar


class Enemy3(Enemy):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.health = 3
        self.speed = 2
        self.image = pygame.image.load('asset/Enemy3.png').convert_alpha()  # Carrega a imagem
        self.rect = self.image.get_rect(center=position)  # Atualiza o retângulo com a posição fornecida
        self.vertical_speed = 2  # Velocidade de movimento vertical
        self.direction = 1  # 1 para subir, -1 para descer
        self.normal_vertical_speed = 2  # Velocidade normal de subida/descida
        self.double_vertical_speed = 4  # Velocidade quando ele atinge a borda superior

    def move(self):
        # Movimento horizontal
        self.rect.x -= 5  # Movimento horizontal para a esquerda

        # Movimento vertical
        self.rect.y += self.vertical_speed * self.direction

        # Verifica colisão com as bordas
        if self.rect.top <= 0:  # Bate na borda superior
            self.direction = -1  # Começa a descer
            self.vertical_speed = self.double_vertical_speed  # Dobrar a velocidade de descida
        elif self.rect.bottom >= WIN_HEIGHT:  # Bate na borda inferior
            self.direction = 1  # Começa a subir
            self.vertical_speed = self.normal_vertical_speed  # Velocidade normal ao subir

        print(f"Enemy3 position: {self.rect.x}, {self.rect.y}")  # Debugging para verificar posição

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # Desenha a imagem do inimigo na tela


