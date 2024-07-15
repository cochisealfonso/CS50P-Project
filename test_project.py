import project
import pygame

def test_collision():
    assert project.collision(10, 10, 20, 20) == True

def test_show_score():
    font = pygame.font.Font('RangerEastwood.ttf',64)
    assert project.show_score(font, 10, 10, 10) == None

def test_set_window():
    assert project.set_window(800,600) == pygame.display.set_mode((800, 600)), pygame.image.load("icons\cowboy_bg.jpg")