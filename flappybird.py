import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((1000,500))
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird")

bird_img = pygame.image.load("bird.png").convert_alpha()
bird_img = pygame.transform.scale(bird_img,(50,40))
bird_rect = bird_img.get_rect()
birdx = 333 # keep the bird at 1/3rd position
bird_rect.center = birdx,screen.get_height()//2

gravity = 0.46 # downword retarding force
flap_strength = -8 # how much to go up

pipew = 80 # width of the pipe
pipeg = 150 # gap between the pipes

font = pygame.font.SysFont(None,48)

def reset_game(): # game reset
    return {
        "birdy": screen.get_height()//2,
        "birdvel": 0,
        "pipes": [{"x":1000,"height":random.randint(100,400),"scored":False}],
        "pipesp": 4,
        "diff": 1, # difficulty score
        "score": 0,
        "start_time": time.time(),
        "running": True
    }

state = reset_game()
game_over = False

while True:
    if not game_over:
        screen.fill((135,206,235)) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() # quit
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                state["birdvel"] = flap_strength 

        state["birdvel"] += gravity # bird is affected by gravity
        state["birdy"] += state["birdvel"]

        angle = -state["birdvel"]*2 # tilt the bird to have better user experience
        rotated_bird = pygame.transform.rotate(bird_img,angle)
        bird_rect = rotated_bird.get_rect(center=(birdx,int(state["birdy"])))

        screen.blit(rotated_bird,bird_rect)
        
        for pipe in state["pipes"]:
            pipe["x"] -= state["pipesp"] # move left
            if pipe["x"] < -pipew: # remove when it is not on screen
                pipe["x"] = screen.get_width()
                pipe["height"] = random.randint(100,400)
                pipe["scored"] = False

            top_rect = pygame.Rect(pipe["x"],0,pipew,pipe["height"])
            bottom_rect = pygame.Rect(pipe["x"],pipe["height"]+pipeg,pipew,screen.get_height()-(pipe["height"]+pipeg))

            pygame.draw.rect(screen,(0,255,0),top_rect) # draw the rectangles 
            pygame.draw.rect(screen,(0,255,0),bottom_rect)

            if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect): # used built in function in pygame to check if the two rectangles overlap
                game_over = True

            if not pipe["scored"] and pipe["x"]+pipew < birdx:
                state["score"] += state["diff"]*10 # update score
                pipe["scored"] = True

        if state["birdy"]<=0 or state["birdy"]>=screen.get_height():
            game_over = True # game completed

        score_text = font.render(f"Score: {state['score']}",True,(255,255,255))
        level_text = font.render(f"Speed x{state['diff']}",True,(255,255,255))
        screen.blit(score_text,(10,10))
        screen.blit(level_text,(10,60)) # update score and speed

        elapsed_time = time.time()-state["start_time"]
        if elapsed_time >= 120:
            state["pipesp"] *= 1.2 # increase the speed if time elapsed >= 120
            state["diff"] += 1
            state["start_time"] = time.time()

    else: # end screen
        screen.fill((178,34,34))  
        game_over_text = font.render("GAME OVER",True,(255,255,255))
        score_text = font.render(f"Final Score:{state['score']}",True,(255,255,0))
        restart_text = font.render("Press SPACE to Restart or ESC to Quit",True,(255,255,255))

        screen.blit(game_over_text,(screen.get_width()//2-120,screen.get_height()//2-100))
        screen.blit(score_text,(screen.get_width()//2-130,screen.get_height()//2-40))
        screen.blit(restart_text,(screen.get_width()//2-280,screen.get_height()//2+40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = reset_game()
                    game_over = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

    pygame.display.flip()
    clock.tick(60)
