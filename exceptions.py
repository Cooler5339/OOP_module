class GameOver(Exception):

    def __init__(self, name, score_player):
        self.name = name
        self.score_player = score_player
        self.write_score(self.name, score_player)

    @staticmethod
    def write_score(name, score_player):
        with open("scores.txt", "a+") as files:
            files.write(name + " score: " + str(score_player) + "\n")


class EnemyDown(Exception):
    pass

