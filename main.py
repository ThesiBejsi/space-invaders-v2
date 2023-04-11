def on_button_pressed_a():
    player.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global shoot
    shoot = game.create_sprite(player.get(LedSpriteProperty.X),
        player.get(LedSpriteProperty.Y))
    for index in range(4):
        shoot.change(LedSpriteProperty.Y, -1)
        basic.pause(25)
        if Enemy.is_touching(shoot):
            Enemy.delete()
            game.add_score(1)
    shoot.delete()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    player.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

Enemy: game.LedSprite = None
shoot: game.LedSprite = None
player: game.LedSprite = None
player = game.create_sprite(2, 4)

def on_forever():
    global Enemy
    Enemy = game.create_sprite(randint(-1, 4), randint(0, 1))
    basic.pause(500)
    for index2 in range(4):
        Enemy.change(LedSpriteProperty.Y, 1)
        basic.pause(500)
    basic.pause(10)
    Enemy.delete()
basic.forever(on_forever)

def on_forever2():
    if Enemy.is_touching(player):
        player.delete()
        game.game_over()
basic.forever(on_forever2)
