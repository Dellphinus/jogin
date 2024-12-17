# EntityFactory.py
from code.Entity import Entity
from code.Enemy import Enemy, Enemy3
from code.Player import Player
from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
import random

class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str):
        """Retorna a entidade correspondente ao nome especificado."""
        
        entity_dict = {
            'Level1Bg': EntityFactory.create_background('Level1Bg', 7),
            'Level2Bg': EntityFactory.create_background('Level2Bg', 5),
            'Level3Bg': EntityFactory.create_background('Level3Bg', 5),
            'Player1': EntityFactory.create_player('Player1', (10, WIN_HEIGHT / 2 - 30)),
            'Player2': EntityFactory.create_player('Player2', (10, WIN_HEIGHT / 2 + 30)),
            'Enemy1': EntityFactory.create_enemy('Enemy1'),
            'Enemy2': EntityFactory.create_enemy('Enemy2'),
            'Enemy3': EntityFactory.create_enemy('Enemy3'),
        }

        # Verifica se a entidade está no dicionário e retorna o valor correspondente
        return entity_dict.get(entity_name, None)

    @staticmethod
    def create_background(name: str, count: int):
        """Cria um nível de fundo com base no nome e número de imagens."""
        list_bg = []
        for i in range(count):
            list_bg.append(Background(f'{name}{i}', (0, 0)))
            list_bg.append(Background(f'{name}{i}', (WIN_WIDTH, 0)))
        return list_bg

    @staticmethod
    def create_player(name: str, position: tuple):
        """Cria um jogador na posição especificada."""
        return Player(name, position)

    @staticmethod
    def create_enemy(name: str):
        """Cria um inimigo com base no nome."""
        return Enemy(name, (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
