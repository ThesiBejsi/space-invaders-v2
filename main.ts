input.onButtonPressed(Button.A, function () {
    player.move(-1)
    music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 200, 1, 255, 0, 100, SoundExpressionEffect.None, InterpolationCurve.Curve), SoundExpressionPlayMode.UntilDone)
})
input.onButtonPressed(Button.AB, function () {
    shoot = game.createSprite(player.get(LedSpriteProperty.X), player.get(LedSpriteProperty.Y))
    music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 1600, 1, 255, 0, 300, SoundExpressionEffect.None, InterpolationCurve.Curve), SoundExpressionPlayMode.UntilDone)
    for (let index = 0; index < 4; index++) {
        shoot.change(LedSpriteProperty.Y, -1)
        basic.pause(25)
        if (Enemy.isTouching(shoot)) {
            Enemy.delete()
            game.addScore(1)
        }
    }
    shoot.delete()
})
input.onButtonPressed(Button.B, function () {
    player.move(1)
    music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 200, 1, 255, 0, 100, SoundExpressionEffect.None, InterpolationCurve.Curve), SoundExpressionPlayMode.UntilDone)
})
// debug stuff
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    game.addScore(10)
})
let speed = 0
let Enemy: game.LedSprite = null
let shoot: game.LedSprite = null
let player: game.LedSprite = null
music.playTone(196, music.beat(BeatFraction.Double))
player = game.createSprite(2, 4)
basic.forever(function () {
    Enemy = game.createSprite(randint(-1, 4), randint(0, 1))
    speed = 500 - 10 * game.score()
    music.playSoundEffect(music.createSoundEffect(WaveShape.Triangle, 4237, 1621, 255, 103, 500, SoundExpressionEffect.Warble, InterpolationCurve.Curve), SoundExpressionPlayMode.UntilDone)
    basic.pause(speed)
    for (let index = 0; index < 4; index++) {
        Enemy.change(LedSpriteProperty.Y, 1)
        basic.pause(speed)
    }
    basic.pause(10)
    Enemy.delete()
})
basic.forever(function () {
    if (Enemy.isTouching(player)) {
        player.delete()
        game.gameOver()
    }
})
