test = {
  'name': 'Dictionaries WWPD',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> pokemon = {'pikachu': 25, 'dragonair': 148}
          >>> pokemon
          {'pikachu': 25, 'dragonair': 148}
          >>> 'mewtwo' in pokemon
          False
          >>> len(pokemon)  
          2
          >>> pokemon['mew'] = pokemon['pikachu']   #If this errors, just type Error
          >>> pokemon[25] = 'pikachu'
          >>> pokemon
          {'pikachu': 25, 'dragonair': 148, 'mew': 25, 25: 'pikachu'}
          >>> pokemon['mewtwo'] = pokemon['mew'] * 2  
          >>> pokemon
          {'pikachu': 25, 'dragonair': 148, 'mew': 25, 25: 'pikachu', 'mewtwo': 50}
          >>> pokemon[['firetype', 'flying']] = 146  # If this errors, just type Error. Note that dictionary keys must be hashable.
          Error
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
