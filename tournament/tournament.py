from collections import defaultdict


class Team:
    def __init__(self) -> None:
        self.wins = 0
        self.loses = 0
        self.draws = 0

    @property
    def points(self):
        return self.wins * 3 + self.draws

    @property
    def matches(self):
        return self.wins + self.loses + self.draws


class League:
    def __init__(self) -> None:
        self.teams = defaultdict(Team)

    def add_match(self, match: str):
        local_team, away_team, result = match.split(";")
        if result == "draw":
            self.teams[local_team].draws += 1
            self.teams[away_team].draws += 1
        elif result == "win":
            self.teams[local_team].wins += 1
            self.teams[away_team].loses += 1
        else:
            self.teams[local_team].loses += 1
            self.teams[away_team].wins += 1

    def print_classification(self) -> str:
        league_str = ["Team                           | MP |  W |  D |  L |  P"]
        for name, results in sorted(
            self.teams.items(), key=lambda x: (-x[1].points, x[0])
        ):
            league_str.append(
                "{:<31}|{:>3} |{:>3} |{:>3} |{:>3} |{:>3}".format(
                    name,
                    results.matches,
                    results.wins,
                    results.draws,
                    results.loses,
                    results.points,
                )
            )
        return league_str


def tally(rows):
    league = League()
    for match in rows:
        league.add_match(match)
    return league.print_classification()
