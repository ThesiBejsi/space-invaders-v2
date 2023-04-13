def on_button_pressed_a():
    player.move(-1)
    music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
            200,
            1,
            255,
            0,
            100,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        SoundExpressionPlayMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global shoot
    shoot = game.create_sprite(player.get(LedSpriteProperty.X),
        player.get(LedSpriteProperty.Y))
    music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
            1600,
            1,
            255,
            0,
            300,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        SoundExpressionPlayMode.UNTIL_DONE)
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
    music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
            200,
            1,
            255,
            0,
            100,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        SoundExpressionPlayMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)

# debug stuff

def on_logo_pressed():
    game.add_score(10)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

speed = 0
Enemy: game.LedSprite = None
shoot: game.LedSprite = None
player: game.LedSprite = None
music.play_tone(196, music.beat(BeatFraction.DOUBLE))
player = game.create_sprite(2, 4)

def on_forever():
    global Enemy, speed
    Enemy = game.create_sprite(randint(-1, 4), randint(0, 1))
    speed = 500 - 10 * game.score()
    music.play_sound_effect(music.create_sound_effect(WaveShape.TRIANGLE,
            4237,
            1621,
            255,
            103,
            500,
            SoundExpressionEffect.WARBLE,
            InterpolationCurve.CURVE),
        SoundExpressionPlayMode.UNTIL_DONE)
    basic.pause(speed)
    for index2 in range(4):
        Enemy.change(LedSpriteProperty.Y, 1)
        basic.pause(speed)
    basic.pause(10)
    Enemy.delete()
basic.forever(on_forever)

def on_forever2():
    if Enemy.is_touching(player):
        player.delete()
        game.game_over()
basic.forever(on_forever2)
