from collections import Counter
from collections import OrderedDict


class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict(
            [(player, Counter()) for player in players])

    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score

    # The player with the highest score is ranked first (rank 1). The player with the lowest score is ranked last.
    # If two players are tied on score, then the player who has played the fewest games is ranked higher.
    # If two players are tied on score and number of games played, then the player who was first in the list of players is ranked higher.

    def player_rank(self, rank):
        #Get a decending list based on score, then sort the previous list again based on games played, then sort the list based on position in the selection.
        ranking = sorted(self.standings, key=lambda p: (
            -self.standings[p]['score'], self.standings[p]['games_played'],
            self.standings[p]['pos']))
        return ranking[rank - 1]


if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    # All players have the same score. However, Arnold and Chris have played fewer games than Mike, and as Chris is before Arnold in the list of players, he is ranked first. Therefore, the code above should display "Chris".

    print(table.player_rank(1))
