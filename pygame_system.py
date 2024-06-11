import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はじめてのPygame")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    font = pg.font.Font(None, 80)

    enn = pg.Surface((20, 20))
    pg.draw.circle(enn, (255, 0, 0), (10, 10), 10)
    enn.set_colorkey((0, 0, 0))

    tmr = 0
    en_y = 400
    en_x = 100
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            if en_y >= 0:
                en_y -= 10 
        elif key_lst[pg.K_DOWN]:
            if en_y <= 600:
                en_y += 10
        if key_lst[pg.K_RIGHT]:
            if en_x <= 800:
                en_x += 10
        elif key_lst[pg.K_LEFT]:
            if en_x >= 0:
                en_x -= 10

        
        txt = font.render(f"{tmr}", True, (255, 255, 255))
        screen.fill((50, 50, 50))
        screen.blit(txt, [300, 200])
        screen.blit(enn, [en_x, en_y])
        pg.display.update()
        tmr += 1        
        clock.tick(60)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()