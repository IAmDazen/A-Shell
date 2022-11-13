import pygame

pygame.init()
while True:
    shell = input("SHELL>>>")
    if shell == "consoleWIN:":
             screen = pygame.display.set_mode((800, 400))
             pygame.display.set_caption('CONSOLE_WINDOW')
             clock = pygame.time.Clock()

             test_surface = pygame.Surface((100,200))

             while True:
                 for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                        if quit == 1:
                            pygame.quit()
                            exit()
                        if not quit == 1:
                             pygame.display.set_caption('SYNTAX: I Think You Might Want To Tell Me What "pygame.QUIT" means...')
                        
             pygame.display.update()
             clock.tick(60)
    
    if shell == "C# Open Source Managed Operating System":
        print("Welcome To Calculator OS, What Would You Like To Calculate? (MADE WITH COSMOS)")
    
    if shell == "COSMOS":
        print("Welcome To Calculator OS, What Would You Like To Calculate? (MADE WITH COSMOS)")
    if shell == "Def pygame.QUIT as windowQuit.event":
        quit = 1