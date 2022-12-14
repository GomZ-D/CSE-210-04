import os
import random

from game.casting.actor import Actor
from game.casting.stone import Stone
from game.casting.cast import Cast
from game.casting.score import Score

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_STONES = 40


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
   
    
    # create the player
    x = int(MAX_X / 2)
    y = int(MAX_Y - (MAX_Y / 8))
    position = Point(x, y)

    player = Actor()
    player.set_text("#")
    player.set_font_size(20)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("players", player)
    

    # for n in range(DEFAULT_STONES): #may not need
    #     characters = [42, 79]
    #     text = chr(random.choice(characters))

    #     x = random.randint(1, COLS - 1)
    #     y = random.randint(1, ROWS - 1)
    #     position = Point(x, 5)
    #     position = position.scale(CELL_SIZE)

    #     # r = random.randint(0, 255)
    #     # g = random.randint(0, 255)
    #     # b = random.randint(0, 255)
    #     # color = Color(r, g, b)
    #     color = Color(255,0,0)
    #     # create the stones 
    #     stone = Stone()
    #     stone.set_text('*')
    #     stone.set_font_size(FONT_SIZE)
    #     stone.set_color(color)
    #     stone.set_position(position)
    #     cast.add_actor("stones", stone)

        
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service, COLS, ROWS, CELL_SIZE, FONT_SIZE)
    director.start_game(cast)


if __name__ == "__main__":
    main()