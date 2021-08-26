from models import Player, Enemy
from exceptions import GameOver, EnemyDown
from settings import ALLOWED_ATTACKS


def play():
    name_player = input('Enter your name: ')
    start = input('ENTER IN GAME? Press "YES": ')
    if start == 'YES':
        player = Player(name=name_player, allowed_attacks=ALLOWED_ATTACKS)
        level_game = 1
        enemy = Enemy(level_game)
        while True:
            try:
                player.attack(enemy)
                player.defence()

            except EnemyDown:
                player.score += 5
                print("You have " + str(player.score) + " score")
                level_game += 1
                print("Your level: " + str(level_game))
                enemy = Enemy(level_game)

    else:
        print('INCORRECT INPUT')
        play()


if __name__ == '__main__':
    try:
        play()

    except GameOver:
        print("-------------------G-A-M-E O-V-E-R-------------------")

    except KeyboardInterrupt:
        pass

    finally:
        print('SEE LATER, NOOB')
