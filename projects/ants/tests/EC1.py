test = {
  'name': 'Problem EC 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing status parameters
          >>> slow = SlowThrower()
          >>> SlowThrower.food_cost
          6
          >>> slow.health
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing Slow
          >>> slow = SlowThrower()
          >>> bee = Bee(3)
          >>> gamestate.places["tunnel_0_0"].add_insect(slow)
          >>> gamestate.places["tunnel_0_5"].add_insect(bee)
          >>> slow.action(gamestate) # slow throws syrup at bee
          >>> gamestate.time = 1
          >>> bee.action(gamestate) # slow causes slowness when gamestate.time is odd. bee should take no action (moving or stinging)
          >>> bee.place.name
          'tunnel_0_5'
          >>> gamestate.time += 1
          >>> bee.action(gamestate) # bee is not affected when gamestate.time is even. bee should take its regular action
          >>> bee.place.name
          'tunnel_0_4'
          >>> for _ in range(5):
          ...    gamestate.time += 1
          ...    bee.action(gamestate)
          >>> bee.place.name # hint: remember that the slow effect wears off after 5 turns. consider how many turns the bee was already affected before the for loop starts.
          'tunnel_0_1'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing Slow
          >>> slow = SlowThrower()
          >>> bee = Bee(3)
          >>> gamestate.places["tunnel_0_0"].add_insect(slow)
          >>> gamestate.places["tunnel_0_5"].add_insect(bee)
          >>> slow.action(gamestate) # slow throws syrup at bee
          >>> gamestate.time = 1
          >>> bee.action(gamestate) # slow causes slowness when gamestate.time is odd. bee should take no action (moving or stinging)
          >>> bee.place.name
          'tunnel_0_5'
          >>> gamestate.time += 1
          >>> bee.action(gamestate) # bee is not affected when gamestate.time is even. bee should take its regular action
          >>> bee.place.name
          'tunnel_0_4'
          >>> slow.action(gamestate) # slow throws syrup again. slow's effects will take place for 5 more turns
          >>> for _ in range(5):
          ...    gamestate.time += 1
          ...    bee.action(gamestate)
          >>> bee.place.name
          'tunnel_0_2'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing that Bee.action was not modified
          >>> slow = SlowThrower()
          >>> bee = Bee(3)
          >>> gamestate.places["tunnel_0_0"].add_insect(slow)
          >>> gamestate.places["tunnel_0_5"].add_insect(bee)
          >>> slow.action(gamestate)
          >>> gamestate.time = 1
          >>> Bee.action(bee, gamestate) # uses original Bee.action
          >>> bee.place.name
          'tunnel_0_4'
          >>> gamestate.time += 1
          >>> Bee.action(bee, gamestate) # uses original Bee.action
          >>> bee.place.name
          'tunnel_0_3'
          >>> for _ in range(3):
          ...    gamestate.time += 1
          ...    bee.action(gamestate) # uses original new slowed action
          >>> bee.place.name
          'tunnel_0_2'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing normal Bee movement after Slow effect
          >>> slow = SlowThrower()
          >>> bee = Bee(3)
          >>> gamestate.places["tunnel_0_0"].add_insect(slow)
          >>> gamestate.places["tunnel_0_8"].add_insect(bee)
          >>> slow.action(gamestate) # slow throws syrup at bee
          >>> gamestate.time = 0
          >>> bee.action(gamestate) # Even time, bee should move
          >>> bee.place.name
          'tunnel_0_7'
          >>> gamestate.time = 1
          >>> bee.action(gamestate) # Odd time, bee should not move
          >>> bee.place.name
          'tunnel_0_7'
          >>> gamestate.time = 2
          >>> bee.action(gamestate) # Even time, bee should move
          >>> bee.place.name
          'tunnel_0_6'
          >>> gamestate.time = 3
          >>> bee.action(gamestate) # Odd time, bee should not move
          >>> bee.place.name
          'tunnel_0_6'
          >>> gamestate.time = 4
          >>> bee.action(gamestate) # Even time, bee should move
          >>> bee.place.name
          'tunnel_0_5'
          >>> gamestate.time = 5
          >>> bee.action(gamestate) # Slow effect ends, bee should move normally
          >>> bee.place.name
          'tunnel_0_4'
          >>> gamestate.time = 6
          >>> bee.action(gamestate) # Slow effect ends, bee should move normally
          >>> bee.place.name
          'tunnel_0_3'
          >>> gamestate.time = 7
          >>> bee.action(gamestate) # Slow effect ends, bee should move normally
          >>> bee.place.name
          'tunnel_0_2'
          >>> gamestate.time = 8
          >>> bee.action(gamestate) # Slow effect ends, bee should move normally
          >>> bee.place.name
          'tunnel_0_1'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> beehive, layout = Hive(AssaultPlan()), dry_layout
      >>> dimensions = (1, 9)
      >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
