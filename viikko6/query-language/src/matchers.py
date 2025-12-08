class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True

        return False


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value


class All:
    @staticmethod
    def test(player):
        return True


# Not (parametrina olevan ehdon negaatio)
class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def test(self, player):
        return not self._matcher.test(player)


# HasFewerThan (HasAtLeast-komennon negaatio eli esim. on vähemmän kuin 10 maalia)
class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value


class QueryBuilder:
    def __init__(self, query_entity=All()):
        self.query_entity = query_entity

    def plays_in(self, team):
        return QueryBuilder(And(self.query_entity, PlaysIn(team)))

    def has_at_least(self, value, attr):
        return QueryBuilder(And(self.query_entity, HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self.query_entity, HasFewerThan(value, attr)))

    def build(self):
        return self.query_entity
    
    def one_of(self, *query_builders):
        query_entities = [qb.build() for qb in query_builders]
        return QueryBuilder(Or(*query_entities))