input.onButtonPressed(Button.A, function () {
    player.move(-1)
})
input.onButtonPressed(Button.AB, function () {
    shoot = game.createSprite(player.get(LedSpriteProperty.X), player.get(LedSpriteProperty.Y))
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
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    game.addScore(10)
})
let speed = 0
let Enemy: game.LedSprite = null
let shoot: game.LedSprite = null
let player: game.LedSprite = null
player = game.createSprite(2, 4)
basic.forever(function () {
    Enemy = game.createSprite(randint(-1, 4), randint(0, 1))
    speed = 500 - 10 * game.score()
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
