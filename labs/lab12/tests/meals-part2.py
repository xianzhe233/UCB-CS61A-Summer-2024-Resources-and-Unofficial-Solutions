test = {
  'name': 'meals-part2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM calories;
          22
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
