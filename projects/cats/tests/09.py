test = {
  'name': 'Problem 9',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> p = [[1, 4, 6, 7], [0, 4, 6, 9]]
          >>> words = ['This', 'is', 'fun']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['This', 'is', 'fun']
          >>> times
          [[3, 2, 1], [4, 2, 3]]
          >>> p = [[0, 2, 3], [2, 4, 7]]
          >>> words, times = time_per_word(['hello', 'world'], p)
          >>> words
          ['hello', 'world']
          >>> words[1]
          'world'
          >>> times
          [[2, 1], [2, 3]]
          >>> times[0][1]
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[49, 53, 57, 58, 61, 63], [57, 61, 65, 69, 74, 76], [58, 61, 62, 65, 69, 72]]
          >>> words = ['gonalgia', 'smopple', 'modernizer', 'posticum', 'undiscernible']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['gonalgia', 'smopple', 'modernizer', 'posticum', 'undiscernible']
          >>> times
          [[4, 4, 1, 3, 2], [4, 4, 4, 5, 2], [3, 1, 3, 4, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[47, 50, 54, 55, 58], [88, 90, 91, 96, 97], [91, 95, 99, 101, 103]]
          >>> words = ['equalizing', 'phrymaceous', 'fluidimeter', 'seeds']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['equalizing', 'phrymaceous', 'fluidimeter', 'seeds']
          >>> times
          [[3, 4, 1, 3], [2, 1, 5, 1], [4, 4, 2, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[91, 95, 99, 100, 103, 108, 113], [73, 75, 77, 80, 85, 89, 90]]
          >>> words = ['unsupposable', 'seeingly', 'essexite', 'policemanism', 'havenet', 'ammonionitrate']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['unsupposable', 'seeingly', 'essexite', 'policemanism', 'havenet', 'ammonionitrate']
          >>> times
          [[4, 4, 1, 3, 5, 5], [2, 2, 3, 5, 4, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[58, 62, 66, 67, 69, 72, 76]]
          >>> words = ['unsanitariness', 'probatively', 'unabatedly', 'reundergo', 'unweld', 'handgun']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['unsanitariness', 'probatively', 'unabatedly', 'reundergo', 'unweld', 'handgun']
          >>> times
          [[4, 4, 1, 2, 3, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[35, 36, 39, 43, 45, 50, 52]]
          >>> words = ['extort', 'elysia', 'cungeboi', 'cams', 'plagueproof', 'overdeeming']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['extort', 'elysia', 'cungeboi', 'cams', 'plagueproof', 'overdeeming']
          >>> times
          [[1, 3, 4, 2, 5, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[46]]
          >>> words = []
          >>> words, times = time_per_word(words, p)
          >>> words
          []
          >>> times
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[22, 27, 29], [54, 57, 61], [96, 101, 103]]
          >>> words = ['glassine', 'supplies']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['glassine', 'supplies']
          >>> times
          [[5, 2], [3, 4], [5, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[89, 90, 95], [83, 84, 89], [88, 92, 95]]
          >>> words = ['epinaos', 'unpresented']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['epinaos', 'unpresented']
          >>> times
          [[1, 5], [1, 5], [4, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[9], [24]]
          >>> words = []
          >>> words, times = time_per_word(words, p)
          >>> words
          []
          >>> times
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[0], [20]]
          >>> words = []
          >>> words, times = time_per_word(words, p)
          >>> words
          []
          >>> times
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[46, 49, 51], [48, 53, 57]]
          >>> words = ['hypsochrome', 'isoborneol']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['hypsochrome', 'isoborneol']
          >>> times
          [[3, 2], [5, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[18, 22]]
          >>> words = ['nailless']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['nailless']
          >>> times
          [[4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[62, 65], [93, 97]]
          >>> words = ['ringcraft']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['ringcraft']
          >>> times
          [[3], [4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[68, 69, 70, 71], [66, 71, 74, 78], [18, 19, 21, 24]]
          >>> words = ['rug', 'misinstruction', 'durian']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['rug', 'misinstruction', 'durian']
          >>> times
          [[1, 1, 1], [5, 3, 4], [1, 2, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 4, 6, 11, 13, 14]]
          >>> words = ['epitomization', 'orchestrion', 'snideness', 'universalization', 'accroach']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['epitomization', 'orchestrion', 'snideness', 'universalization', 'accroach']
          >>> times
          [[3, 2, 5, 2, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[29, 30, 33, 35]]
          >>> words = ['hecatontome', 'glioma', 'dispiteousness']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['hecatontome', 'glioma', 'dispiteousness']
          >>> times
          [[1, 3, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[92, 95, 96, 101], [30, 32, 34, 35]]
          >>> words = ['irenically', 'spaceful', 'cautery']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['irenically', 'spaceful', 'cautery']
          >>> times
          [[3, 1, 5], [2, 2, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[44, 46], [91, 95]]
          >>> words = ['hieromachy']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['hieromachy']
          >>> times
          [[2], [4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[27, 31, 32, 34, 39], [20, 21, 24, 28, 29], [10, 11, 16, 21, 23]]
          >>> words = ['onliest', 'tubuliporoid', 'malleability', 'scusation']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['onliest', 'tubuliporoid', 'malleability', 'scusation']
          >>> times
          [[4, 1, 2, 5], [1, 3, 4, 1], [1, 5, 5, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[33, 37, 41, 44, 48, 51, 54]]
          >>> words = ['caulicle', 'shilling', 'shrubbiness', 'demoded', 'commentary', 'housewright']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['caulicle', 'shilling', 'shrubbiness', 'demoded', 'commentary', 'housewright']
          >>> times
          [[4, 4, 3, 4, 3, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[73], [55]]
          >>> words = []
          >>> words, times = time_per_word(words, p)
          >>> words
          []
          >>> times
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[60, 61], [43, 47], [30, 33]]
          >>> words = ['lithosis']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['lithosis']
          >>> times
          [[1], [4], [3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[93, 97, 98, 101, 105, 109], [55, 56, 58, 59, 61, 65], [82, 85, 87, 88, 92, 96]]
          >>> words = ['pemmicanize', 'diplosphenal', 'cholecystogram', 'maximization', 'arenilitic']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['pemmicanize', 'diplosphenal', 'cholecystogram', 'maximization', 'arenilitic']
          >>> times
          [[4, 1, 3, 4, 4], [1, 2, 1, 2, 4], [3, 2, 1, 4, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[37], [3], [0]]
          >>> words = []
          >>> words, times = time_per_word(words, p)
          >>> words
          []
          >>> times
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[92, 96, 99, 102], [43, 45, 47, 51], [34, 36, 38, 39]]
          >>> words = ['distressedly', 'gibbet', 'cannily']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['distressedly', 'gibbet', 'cannily']
          >>> times
          [[4, 3, 3], [2, 2, 4], [2, 2, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 5, 8, 11], [0, 4, 6, 10], [62, 65, 66, 68]]
          >>> words = ['paramorphic', 'triplocaulescent', 'postprandially']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['paramorphic', 'triplocaulescent', 'postprandially']
          >>> times
          [[4, 3, 3], [4, 2, 4], [3, 1, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[63, 64, 69], [90, 93, 94]]
          >>> words = ['sheered', 'electrofused']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['sheered', 'electrofused']
          >>> times
          [[1, 5], [3, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[87, 91, 94, 96, 99, 102], [50, 54, 58, 60, 63, 66], [57, 61, 64, 66, 69, 73]]
          >>> words = ['crotonaldehyde', 'unhabitableness', 'nidification', 'lampless', 'fibrochondroma']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['crotonaldehyde', 'unhabitableness', 'nidification', 'lampless', 'fibrochondroma']
          >>> times
          [[4, 3, 2, 3, 3], [4, 4, 2, 3, 3], [4, 3, 2, 3, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[63]]
          >>> words = []
          >>> words, times = time_per_word(words, p)
          >>> words
          []
          >>> times
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[51, 54]]
          >>> words = ['prissy']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['prissy']
          >>> times
          [[3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[31, 34, 39, 42, 47, 50], [73, 75, 78, 81, 86, 89]]
          >>> words = ['sinfonietta', 'trigon', 'effluviate', 'unhuman', 'energeia']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['sinfonietta', 'trigon', 'effluviate', 'unhuman', 'energeia']
          >>> times
          [[3, 5, 3, 5, 3], [2, 3, 3, 5, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[93, 95, 97, 98, 101], [75, 80, 84, 89, 93]]
          >>> words = ['traitor', 'tablespoon', 'anytime', 'ungotten']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['traitor', 'tablespoon', 'anytime', 'ungotten']
          >>> times
          [[2, 2, 1, 3], [5, 4, 5, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[66, 69], [85, 86]]
          >>> words = ['boucherism']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['boucherism']
          >>> times
          [[3], [1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[74, 75], [74, 75], [41, 43]]
          >>> words = ['uncertainty']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['uncertainty']
          >>> times
          [[1], [1], [2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[15, 18, 19, 23]]
          >>> words = ['redominate', 'dugong', 'cryptodiran']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['redominate', 'dugong', 'cryptodiran']
          >>> times
          [[3, 1, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[57, 60, 62, 66]]
          >>> words = ['estivage', 'hypersensualism', 'aminoacetal']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['estivage', 'hypersensualism', 'aminoacetal']
          >>> times
          [[3, 2, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[48, 53, 54, 55, 58, 62], [85, 86, 90, 94, 95, 100], [23, 25, 27, 32, 33, 37]]
          >>> words = ['semipervious', 'cactoid', 'quadrialate', 'preflattery', 'emancipation']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['semipervious', 'cactoid', 'quadrialate', 'preflattery', 'emancipation']
          >>> times
          [[5, 1, 1, 3, 4], [1, 4, 4, 1, 5], [2, 2, 5, 1, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[35, 36, 40, 44, 46, 47, 50], [53, 58, 62, 67, 68, 70, 74]]
          >>> words = ['otoconial', 'puboprostatic', 'tumescent', 'keraunograph', 'telecaster', 'selenigenous']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['otoconial', 'puboprostatic', 'tumescent', 'keraunograph', 'telecaster', 'selenigenous']
          >>> times
          [[1, 4, 4, 2, 1, 3], [5, 4, 5, 1, 2, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 5, 9, 10]]
          >>> words = ['unsculptured', 'quagginess', 'indisputableness']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['unsculptured', 'quagginess', 'indisputableness']
          >>> times
          [[3, 4, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[55], [37], [18]]
          >>> words = []
          >>> words, times = time_per_word(words, p)
          >>> words
          []
          >>> times
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[12, 13, 15, 20, 24], [51, 55, 56, 59, 60], [82, 83, 85, 90, 94]]
          >>> words = ['extol', 'siscowet', 'nevo', 'driftweed']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['extol', 'siscowet', 'nevo', 'driftweed']
          >>> times
          [[1, 2, 5, 4], [4, 1, 3, 1], [1, 2, 5, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[57, 61, 65, 67, 72, 76], [28, 33, 35, 37, 42, 45]]
          >>> words = ['tomtate', 'holland', 'nursedom', 'epidictical', 'defortify']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['tomtate', 'holland', 'nursedom', 'epidictical', 'defortify']
          >>> times
          [[4, 4, 2, 5, 4], [5, 2, 2, 5, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[25], [24], [2]]
          >>> words = []
          >>> words, times = time_per_word(words, p)
          >>> words
          []
          >>> times
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[42]]
          >>> words = []
          >>> words, times = time_per_word(words, p)
          >>> words
          []
          >>> times
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[84, 87, 88, 89, 90], [39, 43, 45, 49, 51], [52, 53, 57, 59, 63]]
          >>> words = ['pharyngognathous', 'metamerically', 'toxone', 'nucleiform']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['pharyngognathous', 'metamerically', 'toxone', 'nucleiform']
          >>> times
          [[3, 1, 1, 1], [4, 2, 4, 2], [1, 4, 2, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[13, 16, 20, 22, 27, 29]]
          >>> words = ['missile', 'tillot', 'douser', 'twankingly', 'eccentrate']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['missile', 'tillot', 'douser', 'twankingly', 'eccentrate']
          >>> times
          [[3, 4, 2, 5, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[70]]
          >>> words = []
          >>> words, times = time_per_word(words, p)
          >>> words
          []
          >>> times
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[67, 68, 73, 74, 79], [12, 17, 20, 21, 25], [55, 58, 62, 66, 67]]
          >>> words = ['unambiguously', 'standing', 'cameroon', 'unpretendingly']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['unambiguously', 'standing', 'cameroon', 'unpretendingly']
          >>> times
          [[1, 5, 1, 5], [5, 3, 1, 4], [3, 4, 4, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[54, 57], [76, 80], [24, 25]]
          >>> words = ['megascleric']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['megascleric']
          >>> times
          [[3], [4], [1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[6, 11], [91, 95], [60, 63]]
          >>> words = ['designee']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['designee']
          >>> times
          [[5], [4], [3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[14, 15, 20, 24, 25]]
          >>> words = ['dextrousness', 'whirley', 'coldly', 'compendiary']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['dextrousness', 'whirley', 'coldly', 'compendiary']
          >>> times
          [[1, 5, 4, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[21, 23, 24]]
          >>> words = ['plowfoot', 'caducicorn']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['plowfoot', 'caducicorn']
          >>> times
          [[2, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[61, 66, 69, 74, 79, 80]]
          >>> words = ['signist', 'plash', 'unbraceleted', 'runner', 'nickeline']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['signist', 'plash', 'unbraceleted', 'runner', 'nickeline']
          >>> times
          [[5, 3, 5, 5, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[7, 9, 12, 15, 18], [53, 54, 58, 63, 64], [28, 30, 35, 36, 41]]
          >>> words = ['ergastoplasmic', 'sulphurage', 'audibility', 'deuteride']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['ergastoplasmic', 'sulphurage', 'audibility', 'deuteride']
          >>> times
          [[2, 3, 3, 3], [1, 4, 5, 1], [2, 5, 1, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[22, 26, 31, 32, 37, 39, 40]]
          >>> words = ['uncontestable', 'millage', 'unbudging', 'hydrostatic', 'enterospasm', 'ectypography']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['uncontestable', 'millage', 'unbudging', 'hydrostatic', 'enterospasm', 'ectypography']
          >>> times
          [[4, 5, 1, 5, 2, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[26, 31], [40, 44]]
          >>> words = ['remissful']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['remissful']
          >>> times
          [[5], [4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[89, 91, 93, 95, 98, 100, 101], [83, 88, 92, 93, 95, 96, 98], [48, 50, 54, 56, 60, 64, 67]]
          >>> words = ['sacculus', 'sarcodous', 'microbiological', 'ruddy', 'gobble', 'pozzuolana']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['sacculus', 'sarcodous', 'microbiological', 'ruddy', 'gobble', 'pozzuolana']
          >>> times
          [[2, 2, 2, 3, 2, 1], [5, 4, 1, 2, 1, 2], [2, 4, 2, 4, 4, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[86, 87], [90, 94]]
          >>> words = ['monothelious']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['monothelious']
          >>> times
          [[1], [4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[74, 76, 78, 83]]
          >>> words = ['boy', 'leaverwood', 'bounteousness']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['boy', 'leaverwood', 'bounteousness']
          >>> times
          [[2, 2, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[16, 17, 20, 21, 25, 26], [46, 49, 52, 57, 61, 63], [96, 97, 98, 100, 103, 108]]
          >>> words = ['impedient', 'allochiral', 'hear', 'snur', 'myosarcomatous']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['impedient', 'allochiral', 'hear', 'snur', 'myosarcomatous']
          >>> times
          [[1, 3, 1, 4, 1], [3, 3, 5, 4, 2], [1, 1, 2, 3, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[89, 91], [37, 39], [63, 67]]
          >>> words = ['sulphurproof']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['sulphurproof']
          >>> times
          [[2], [2], [4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[62], [50], [26]]
          >>> words = []
          >>> words, times = time_per_word(words, p)
          >>> words
          []
          >>> times
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[44, 47, 51, 56, 58, 60], [4, 7, 11, 16, 19, 22]]
          >>> words = ['neoza', 'detinet', 'repolymerization', 'alchemy', 'caphar']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['neoza', 'detinet', 'repolymerization', 'alchemy', 'caphar']
          >>> times
          [[3, 4, 5, 2, 2], [3, 4, 5, 3, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[56, 61]]
          >>> words = ['deediness']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['deediness']
          >>> times
          [[5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[60, 62, 65, 68], [55, 56, 59, 60], [89, 92, 97, 100]]
          >>> words = ['outstartle', 'varicosed', 'ventilator']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['outstartle', 'varicosed', 'ventilator']
          >>> times
          [[2, 3, 3], [1, 3, 1], [3, 5, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 4, 9, 14, 17, 22, 27]]
          >>> words = ['evaporability', 'ultradolichocephalic', 'kinetophone', 'supernaturalness', 'schout', 'woodlander']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['evaporability', 'ultradolichocephalic', 'kinetophone', 'supernaturalness', 'schout', 'woodlander']
          >>> times
          [[3, 5, 5, 3, 5, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5]]
          >>> words = []
          >>> words, times = time_per_word(words, p)
          >>> words
          []
          >>> times
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[11], [37], [36]]
          >>> words = []
          >>> words, times = time_per_word(words, p)
          >>> words
          []
          >>> times
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[54, 55, 58, 62], [74, 76, 81, 82], [41, 43, 46, 47]]
          >>> words = ['payable', 'jaunt', 'oleostearin']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['payable', 'jaunt', 'oleostearin']
          >>> times
          [[1, 3, 4], [2, 5, 1], [2, 3, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[33, 34], [39, 40]]
          >>> words = ['entropium']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['entropium']
          >>> times
          [[1], [1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[72, 77, 82, 85, 90, 91], [5, 9, 14, 17, 21, 22]]
          >>> words = ['stookie', 'withsave', 'subchoroid', 'briefing', 'upbelch']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['stookie', 'withsave', 'subchoroid', 'briefing', 'upbelch']
          >>> times
          [[5, 5, 3, 5, 1], [4, 5, 3, 4, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[29, 34], [69, 70], [71, 72]]
          >>> words = ['battlewise']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['battlewise']
          >>> times
          [[5], [1], [1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[8, 10, 15, 18, 23, 26], [3, 7, 12, 13, 16, 17], [86, 89, 90, 95, 98, 101]]
          >>> words = ['muscoid', 'reliquidation', 'broad', 'tugging', 'retardant']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['muscoid', 'reliquidation', 'broad', 'tugging', 'retardant']
          >>> times
          [[2, 5, 3, 5, 3], [4, 5, 1, 3, 1], [3, 1, 5, 3, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[71, 73, 75, 80, 84], [3, 8, 10, 14, 16]]
          >>> words = ['hexatomic', 'trophobiosis', 'parascenium', 'gibbet']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['hexatomic', 'trophobiosis', 'parascenium', 'gibbet']
          >>> times
          [[2, 2, 5, 4], [5, 2, 4, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2], [83], [56]]
          >>> words = []
          >>> words, times = time_per_word(words, p)
          >>> words
          []
          >>> times
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[9, 13, 18, 19, 23, 26, 29], [85, 89, 92, 94, 97, 102, 105], [5, 9, 12, 13, 14, 15, 18]]
          >>> words = ['unimpressed', 'unexcusableness', 'bismuthyl', 'adapt', 'refutable', 'fluoridize']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['unimpressed', 'unexcusableness', 'bismuthyl', 'adapt', 'refutable', 'fluoridize']
          >>> times
          [[4, 5, 1, 4, 3, 3], [4, 3, 2, 3, 5, 3], [4, 3, 1, 1, 1, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[82, 86], [16, 18]]
          >>> words = ['ab']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['ab']
          >>> times
          [[4], [2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[77, 82, 83, 88, 92]]
          >>> words = ['theophysical', 'penceless', 'bromothymol', 'reticuloramose']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['theophysical', 'penceless', 'bromothymol', 'reticuloramose']
          >>> times
          [[5, 1, 5, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[90, 91, 93, 97, 98], [64, 68, 70, 73, 78], [95, 100, 103, 108, 113]]
          >>> words = ['beshag', 'monument', 'appressor', 'tutu']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['beshag', 'monument', 'appressor', 'tutu']
          >>> times
          [[1, 2, 4, 1], [4, 2, 3, 5], [5, 3, 5, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[86], [26], [8]]
          >>> words = []
          >>> words, times = time_per_word(words, p)
          >>> words
          []
          >>> times
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[25, 26, 30], [50, 54, 59], [52, 55, 60]]
          >>> words = ['confidentiality', 'inclementness']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['confidentiality', 'inclementness']
          >>> times
          [[1, 4], [4, 5], [3, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[58, 63]]
          >>> words = ['sardius']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['sardius']
          >>> times
          [[5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[77, 81, 85, 89]]
          >>> words = ['bluehearts', 'repugnatorial', 'bescorch']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['bluehearts', 'repugnatorial', 'bescorch']
          >>> times
          [[4, 4, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[75, 78, 80]]
          >>> words = ['efflorescency', 'presay']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['efflorescency', 'presay']
          >>> times
          [[3, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[53, 54, 59, 61], [47, 50, 54, 56]]
          >>> words = ['myologist', 'dualistic', 'becense']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['myologist', 'dualistic', 'becense']
          >>> times
          [[1, 5, 2], [3, 4, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[85, 90, 93, 95, 98, 102, 105], [5, 10, 12, 13, 14, 18, 22], [91, 94, 97, 100, 102, 105, 108]]
          >>> words = ['tentacle', 'nonrestitution', 'interventional', 'demiditone', 'chrysophilite', 'idiosyncratically']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['tentacle', 'nonrestitution', 'interventional', 'demiditone', 'chrysophilite', 'idiosyncratically']
          >>> times
          [[5, 3, 2, 3, 4, 3], [5, 2, 1, 1, 4, 4], [3, 3, 3, 2, 3, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[95, 98, 100, 103], [1, 3, 8, 13]]
          >>> words = ['clique', 'spuriae', 'introspectable']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['clique', 'spuriae', 'introspectable']
          >>> times
          [[3, 2, 3], [2, 5, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[10, 15, 19, 24, 28, 31]]
          >>> words = ['epicotyledonary', 'hiro', 'tremolo', 'ringgiving', 'pignoratitious']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['epicotyledonary', 'hiro', 'tremolo', 'ringgiving', 'pignoratitious']
          >>> times
          [[5, 4, 5, 4, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[31, 36, 39, 42, 44, 47, 50]]
          >>> words = ['wickerworker', 'disdiaclastic', 'tutoyer', 'fibrilliferous', 'undiscernedly', 'gloomily']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['wickerworker', 'disdiaclastic', 'tutoyer', 'fibrilliferous', 'undiscernedly', 'gloomily']
          >>> times
          [[5, 3, 3, 2, 3, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[7]]
          >>> words = []
          >>> words, times = time_per_word(words, p)
          >>> words
          []
          >>> times
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[87]]
          >>> words = []
          >>> words, times = time_per_word(words, p)
          >>> words
          []
          >>> times
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[37, 40, 43, 44, 48, 53]]
          >>> words = ['quadratical', 'principiate', 'archinfamy', 'cacomixle', 'endonuclear']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['quadratical', 'principiate', 'archinfamy', 'cacomixle', 'endonuclear']
          >>> times
          [[3, 3, 1, 4, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[69]]
          >>> words = []
          >>> words, times = time_per_word(words, p)
          >>> words
          []
          >>> times
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 8]]
          >>> words = ['subframe']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['subframe']
          >>> times
          [[5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[40], [49]]
          >>> words = []
          >>> words, times = time_per_word(words, p)
          >>> words
          []
          >>> times
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[8, 12, 16, 21, 26, 30]]
          >>> words = ['waling', 'sycophantishly', 'mistresshood', 'lazzarone', 'define']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['waling', 'sycophantishly', 'mistresshood', 'lazzarone', 'define']
          >>> times
          [[4, 4, 5, 5, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[31, 35], [97, 102], [27, 29]]
          >>> words = ['donary']
          >>> words, times = time_per_word(words, p)
          >>> words
          ['donary']
          >>> times
          [[4], [5], [2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5], [86], [1]]
          >>> words = []
          >>> words, times = time_per_word(words, p)
          >>> words
          []
          >>> times
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[79]]
          >>> words = []
          >>> words, times = time_per_word(words, p)
          >>> words
          []
          >>> times
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[59], [68], [75]]
          >>> words = []
          >>> words, times = time_per_word(words, p)
          >>> words
          []
          >>> times
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
