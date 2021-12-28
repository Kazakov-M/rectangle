import pygame

size_x, size_y = input(), input()
if size_x.isdigit() == False or size_y.isdigit() == False:
    print("Неправильный формат ввода")
size = size_x, size_y = int(size_x), int(size_y)
pygame.init()
scr = pygame.display.set_mode(size)
pygame.display.set_caption("Прямоугольник")
scr.fill((255, 0, 0))
pygame.draw.line(scr, (0, 0, 0), (0, 0), (0, size_y), width=1)
pygame.draw.line(scr, (0, 0, 0), (0, size_y), (size_x, size_y), width=1)
pygame.draw.line(scr, (0, 0, 0), (size_x, size_y), (size_x, 0), width=1)
pygame.draw.line(scr, (0, 0, 0), (size_x, 0), (0, 0), width=1)
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.update()
pygame.quit()