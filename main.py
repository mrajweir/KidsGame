import pygame
import os

XBOX_BUTTON_A = 0
XBOX_BUTTON_B = 1
XBOX_BUTTON_X = 2
XBOX_BUTTON_Y = 3

clock = object()


def log(message):
    print("[ {} ] {}".format(pygame.time.get_ticks(), message))


def main():
    pygame.init()
    log("Program started")

    # Setup screen
    pygame.display.set_caption("Kids Game")
    screen = pygame.display.set_mode((800, 600))

    # Basic asset load
    image_active_a = pygame.image.load(os.path.join("assets/images/controllers/xbox/XboxSeriesX_A.png"))
    screen.blit(image_active_a, (50, 50))
    pygame.display.flip()

    # Controller setup
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    joystick = pygame.joystick.Joystick(0)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.JOYBUTTONUP:
                if event.button == XBOX_BUTTON_A:
                    log("A button - up")
                elif event.button == XBOX_BUTTON_B:
                    log("B button - up")
                elif event.button == XBOX_BUTTON_X:
                    log("X button - up")
                elif event.button == XBOX_BUTTON_Y:
                    log("Y button - up")

            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == XBOX_BUTTON_A:
                    log("A button - down")
                elif event.button == XBOX_BUTTON_B:
                    log("B button - down")
                elif event.button == XBOX_BUTTON_X:
                    log("X button - down")
                elif event.button == XBOX_BUTTON_Y:
                    log("Y button - down")


if __name__ == "__main__":
    main()