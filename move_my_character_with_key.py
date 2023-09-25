from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('Skeleton_Sprite_Sheet.png')


def handle_events():
    global running, dir, Dir
    global bottom

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                bottom = 0
            elif event.key == SDLK_LEFT:
                dir -= 1
                bottom = 200
            elif event.key == SDLK_UP:
                Dir += 1
                bottom = 300
            elif event.key == SDLK_DOWN:
                Dir -= 1
                bottom = 100
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            bottom = 100
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                Dir -= 1
            elif event.key == SDLK_DOWN:
                Dir += 1

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dir = 0
Dir = 0
bottom = 100

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame*100,bottom,100,100,x,y)
    update_canvas()
    handle_events()
    frame = (frame + 1)%9
    if dir != 0:
        x += dir*5
    if Dir != 0:
        y += Dir*5
    delay(0.05)

close_canvas()

