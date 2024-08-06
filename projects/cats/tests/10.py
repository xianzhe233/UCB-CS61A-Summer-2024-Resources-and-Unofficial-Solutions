test = {
  'name': 'Problem 10',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> p = [[1, 4, 6, 7], [0, 4, 6, 9]]
          >>> words = ['This', 'is', 'fun']
          >>> match_object = time_per_word_match(words, p)
          >>> get_all_words(match_object)    # what does this selector do?
          ['This', 'is', 'fun']
          >>> get_all_times(match_object)    # what does this selector do?
          [[3, 2, 1], [4, 2, 3]]
          >>> p = [[0, 2, 3], [2, 4, 7]]
          >>> match_object = time_per_word_match(['hello', 'world'], p)
          >>> get_word(match_object, word_index=1)
          'world'
          >>> get_all_times(match_object)
          [[2, 1], [2, 3]]
          >>> get_time(match_object, player_num=0, word_index=1)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[49, 53, 57, 58, 61, 63], [57, 61, 65, 69, 74, 76], [58, 61, 62, 65, 69, 72]]
          >>> match_object = time_per_word_match(['gonalgia', 'smopple', 'modernizer', 'posticum', 'undiscernible'], p)
          >>> get_all_words(match_object)
          ['gonalgia', 'smopple', 'modernizer', 'posticum', 'undiscernible']
          >>> match_object['times']
          [[4, 4, 1, 3, 2], [4, 4, 4, 5, 2], [3, 1, 3, 4, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[47, 50, 54, 55, 58], [88, 90, 91, 96, 97], [91, 95, 99, 101, 103]]
          >>> match_object = time_per_word_match(['equalizing', 'phrymaceous', 'fluidimeter', 'seeds'], p)
          >>> get_all_words(match_object)
          ['equalizing', 'phrymaceous', 'fluidimeter', 'seeds']
          >>> match_object['times']
          [[3, 4, 1, 3], [2, 1, 5, 1], [4, 4, 2, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[91, 95, 99, 100, 103, 108, 113], [73, 75, 77, 80, 85, 89, 90]]
          >>> match_object = time_per_word_match(['unsupposable', 'seeingly', 'essexite', 'policemanism', 'havenet', 'ammonionitrate'], p)
          >>> get_all_words(match_object)
          ['unsupposable', 'seeingly', 'essexite', 'policemanism', 'havenet', 'ammonionitrate']
          >>> match_object['times']
          [[4, 4, 1, 3, 5, 5], [2, 2, 3, 5, 4, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[58, 62, 66, 67, 69, 72, 76]]
          >>> match_object = time_per_word_match(['unsanitariness', 'probatively', 'unabatedly', 'reundergo', 'unweld', 'handgun'], p)
          >>> get_all_words(match_object)
          ['unsanitariness', 'probatively', 'unabatedly', 'reundergo', 'unweld', 'handgun']
          >>> match_object['times']
          [[4, 4, 1, 2, 3, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[35, 36, 39, 43, 45, 50, 52]]
          >>> match_object = time_per_word_match(['extort', 'elysia', 'cungeboi', 'cams', 'plagueproof', 'overdeeming'], p)
          >>> get_all_words(match_object)
          ['extort', 'elysia', 'cungeboi', 'cams', 'plagueproof', 'overdeeming']
          >>> match_object['times']
          [[1, 3, 4, 2, 5, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[46]]
          >>> match_object = time_per_word_match([], p)
          >>> get_all_words(match_object)
          []
          >>> match_object['times']
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[22, 27, 29], [54, 57, 61], [96, 101, 103]]
          >>> match_object = time_per_word_match(['glassine', 'supplies'], p)
          >>> get_all_words(match_object)
          ['glassine', 'supplies']
          >>> match_object['times']
          [[5, 2], [3, 4], [5, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[89, 90, 95], [83, 84, 89], [88, 92, 95]]
          >>> match_object = time_per_word_match(['epinaos', 'unpresented'], p)
          >>> get_all_words(match_object)
          ['epinaos', 'unpresented']
          >>> match_object['times']
          [[1, 5], [1, 5], [4, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[9], [24]]
          >>> match_object = time_per_word_match([], p)
          >>> get_all_words(match_object)
          []
          >>> match_object['times']
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[0], [20]]
          >>> match_object = time_per_word_match([], p)
          >>> get_all_words(match_object)
          []
          >>> match_object['times']
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[46, 49, 51], [48, 53, 57]]
          >>> match_object = time_per_word_match(['hypsochrome', 'isoborneol'], p)
          >>> get_all_words(match_object)
          ['hypsochrome', 'isoborneol']
          >>> match_object['times']
          [[3, 2], [5, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[18, 22]]
          >>> match_object = time_per_word_match(['nailless'], p)
          >>> get_all_words(match_object)
          ['nailless']
          >>> match_object['times']
          [[4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[62, 65], [93, 97]]
          >>> match_object = time_per_word_match(['ringcraft'], p)
          >>> get_all_words(match_object)
          ['ringcraft']
          >>> match_object['times']
          [[3], [4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[68, 69, 70, 71], [66, 71, 74, 78], [18, 19, 21, 24]]
          >>> match_object = time_per_word_match(['rug', 'misinstruction', 'durian'], p)
          >>> get_all_words(match_object)
          ['rug', 'misinstruction', 'durian']
          >>> match_object['times']
          [[1, 1, 1], [5, 3, 4], [1, 2, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 4, 6, 11, 13, 14]]
          >>> match_object = time_per_word_match(['epitomization', 'orchestrion', 'snideness', 'universalization', 'accroach'], p)
          >>> get_all_words(match_object)
          ['epitomization', 'orchestrion', 'snideness', 'universalization', 'accroach']
          >>> match_object['times']
          [[3, 2, 5, 2, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[29, 30, 33, 35]]
          >>> match_object = time_per_word_match(['hecatontome', 'glioma', 'dispiteousness'], p)
          >>> get_all_words(match_object)
          ['hecatontome', 'glioma', 'dispiteousness']
          >>> match_object['times']
          [[1, 3, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[92, 95, 96, 101], [30, 32, 34, 35]]
          >>> match_object = time_per_word_match(['irenically', 'spaceful', 'cautery'], p)
          >>> get_all_words(match_object)
          ['irenically', 'spaceful', 'cautery']
          >>> match_object['times']
          [[3, 1, 5], [2, 2, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[44, 46], [91, 95]]
          >>> match_object = time_per_word_match(['hieromachy'], p)
          >>> get_all_words(match_object)
          ['hieromachy']
          >>> match_object['times']
          [[2], [4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[27, 31, 32, 34, 39], [20, 21, 24, 28, 29], [10, 11, 16, 21, 23]]
          >>> match_object = time_per_word_match(['onliest', 'tubuliporoid', 'malleability', 'scusation'], p)
          >>> get_all_words(match_object)
          ['onliest', 'tubuliporoid', 'malleability', 'scusation']
          >>> match_object['times']
          [[4, 1, 2, 5], [1, 3, 4, 1], [1, 5, 5, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[33, 37, 41, 44, 48, 51, 54]]
          >>> match_object = time_per_word_match(['caulicle', 'shilling', 'shrubbiness', 'demoded', 'commentary', 'housewright'], p)
          >>> get_all_words(match_object)
          ['caulicle', 'shilling', 'shrubbiness', 'demoded', 'commentary', 'housewright']
          >>> match_object['times']
          [[4, 4, 3, 4, 3, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[73], [55]]
          >>> match_object = time_per_word_match([], p)
          >>> get_all_words(match_object)
          []
          >>> match_object['times']
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[60, 61], [43, 47], [30, 33]]
          >>> match_object = time_per_word_match(['lithosis'], p)
          >>> get_all_words(match_object)
          ['lithosis']
          >>> match_object['times']
          [[1], [4], [3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[93, 97, 98, 101, 105, 109], [55, 56, 58, 59, 61, 65], [82, 85, 87, 88, 92, 96]]
          >>> match_object = time_per_word_match(['pemmicanize', 'diplosphenal', 'cholecystogram', 'maximization', 'arenilitic'], p)
          >>> get_all_words(match_object)
          ['pemmicanize', 'diplosphenal', 'cholecystogram', 'maximization', 'arenilitic']
          >>> match_object['times']
          [[4, 1, 3, 4, 4], [1, 2, 1, 2, 4], [3, 2, 1, 4, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[37], [3], [0]]
          >>> match_object = time_per_word_match([], p)
          >>> get_all_words(match_object)
          []
          >>> match_object['times']
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[92, 96, 99, 102], [43, 45, 47, 51], [34, 36, 38, 39]]
          >>> match_object = time_per_word_match(['distressedly', 'gibbet', 'cannily'], p)
          >>> get_all_words(match_object)
          ['distressedly', 'gibbet', 'cannily']
          >>> match_object['times']
          [[4, 3, 3], [2, 2, 4], [2, 2, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 5, 8, 11], [0, 4, 6, 10], [62, 65, 66, 68]]
          >>> match_object = time_per_word_match(['paramorphic', 'triplocaulescent', 'postprandially'], p)
          >>> get_all_words(match_object)
          ['paramorphic', 'triplocaulescent', 'postprandially']
          >>> match_object['times']
          [[4, 3, 3], [4, 2, 4], [3, 1, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[63, 64, 69], [90, 93, 94]]
          >>> match_object = time_per_word_match(['sheered', 'electrofused'], p)
          >>> get_all_words(match_object)
          ['sheered', 'electrofused']
          >>> match_object['times']
          [[1, 5], [3, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[87, 91, 94, 96, 99, 102], [50, 54, 58, 60, 63, 66], [57, 61, 64, 66, 69, 73]]
          >>> match_object = time_per_word_match(['crotonaldehyde', 'unhabitableness', 'nidification', 'lampless', 'fibrochondroma'], p)
          >>> get_all_words(match_object)
          ['crotonaldehyde', 'unhabitableness', 'nidification', 'lampless', 'fibrochondroma']
          >>> match_object['times']
          [[4, 3, 2, 3, 3], [4, 4, 2, 3, 3], [4, 3, 2, 3, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[63]]
          >>> match_object = time_per_word_match([], p)
          >>> get_all_words(match_object)
          []
          >>> match_object['times']
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[51, 54]]
          >>> match_object = time_per_word_match(['prissy'], p)
          >>> get_all_words(match_object)
          ['prissy']
          >>> match_object['times']
          [[3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[31, 34, 39, 42, 47, 50], [73, 75, 78, 81, 86, 89]]
          >>> match_object = time_per_word_match(['sinfonietta', 'trigon', 'effluviate', 'unhuman', 'energeia'], p)
          >>> get_all_words(match_object)
          ['sinfonietta', 'trigon', 'effluviate', 'unhuman', 'energeia']
          >>> match_object['times']
          [[3, 5, 3, 5, 3], [2, 3, 3, 5, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[93, 95, 97, 98, 101], [75, 80, 84, 89, 93]]
          >>> match_object = time_per_word_match(['traitor', 'tablespoon', 'anytime', 'ungotten'], p)
          >>> get_all_words(match_object)
          ['traitor', 'tablespoon', 'anytime', 'ungotten']
          >>> match_object['times']
          [[2, 2, 1, 3], [5, 4, 5, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[66, 69], [85, 86]]
          >>> match_object = time_per_word_match(['boucherism'], p)
          >>> get_all_words(match_object)
          ['boucherism']
          >>> match_object['times']
          [[3], [1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[74, 75], [74, 75], [41, 43]]
          >>> match_object = time_per_word_match(['uncertainty'], p)
          >>> get_all_words(match_object)
          ['uncertainty']
          >>> match_object['times']
          [[1], [1], [2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[15, 18, 19, 23]]
          >>> match_object = time_per_word_match(['redominate', 'dugong', 'cryptodiran'], p)
          >>> get_all_words(match_object)
          ['redominate', 'dugong', 'cryptodiran']
          >>> match_object['times']
          [[3, 1, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[57, 60, 62, 66]]
          >>> match_object = time_per_word_match(['estivage', 'hypersensualism', 'aminoacetal'], p)
          >>> get_all_words(match_object)
          ['estivage', 'hypersensualism', 'aminoacetal']
          >>> match_object['times']
          [[3, 2, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[48, 53, 54, 55, 58, 62], [85, 86, 90, 94, 95, 100], [23, 25, 27, 32, 33, 37]]
          >>> match_object = time_per_word_match(['semipervious', 'cactoid', 'quadrialate', 'preflattery', 'emancipation'], p)
          >>> get_all_words(match_object)
          ['semipervious', 'cactoid', 'quadrialate', 'preflattery', 'emancipation']
          >>> match_object['times']
          [[5, 1, 1, 3, 4], [1, 4, 4, 1, 5], [2, 2, 5, 1, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[35, 36, 40, 44, 46, 47, 50], [53, 58, 62, 67, 68, 70, 74]]
          >>> match_object = time_per_word_match(['otoconial', 'puboprostatic', 'tumescent', 'keraunograph', 'telecaster', 'selenigenous'], p)
          >>> get_all_words(match_object)
          ['otoconial', 'puboprostatic', 'tumescent', 'keraunograph', 'telecaster', 'selenigenous']
          >>> match_object['times']
          [[1, 4, 4, 2, 1, 3], [5, 4, 5, 1, 2, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 5, 9, 10]]
          >>> match_object = time_per_word_match(['unsculptured', 'quagginess', 'indisputableness'], p)
          >>> get_all_words(match_object)
          ['unsculptured', 'quagginess', 'indisputableness']
          >>> match_object['times']
          [[3, 4, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[55], [37], [18]]
          >>> match_object = time_per_word_match([], p)
          >>> get_all_words(match_object)
          []
          >>> match_object['times']
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[12, 13, 15, 20, 24], [51, 55, 56, 59, 60], [82, 83, 85, 90, 94]]
          >>> match_object = time_per_word_match(['extol', 'siscowet', 'nevo', 'driftweed'], p)
          >>> get_all_words(match_object)
          ['extol', 'siscowet', 'nevo', 'driftweed']
          >>> match_object['times']
          [[1, 2, 5, 4], [4, 1, 3, 1], [1, 2, 5, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[57, 61, 65, 67, 72, 76], [28, 33, 35, 37, 42, 45]]
          >>> match_object = time_per_word_match(['tomtate', 'holland', 'nursedom', 'epidictical', 'defortify'], p)
          >>> get_all_words(match_object)
          ['tomtate', 'holland', 'nursedom', 'epidictical', 'defortify']
          >>> match_object['times']
          [[4, 4, 2, 5, 4], [5, 2, 2, 5, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[25], [24], [2]]
          >>> match_object = time_per_word_match([], p)
          >>> get_all_words(match_object)
          []
          >>> match_object['times']
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[42]]
          >>> match_object = time_per_word_match([], p)
          >>> get_all_words(match_object)
          []
          >>> match_object['times']
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[84, 87, 88, 89, 90], [39, 43, 45, 49, 51], [52, 53, 57, 59, 63]]
          >>> match_object = time_per_word_match(['pharyngognathous', 'metamerically', 'toxone', 'nucleiform'], p)
          >>> get_all_words(match_object)
          ['pharyngognathous', 'metamerically', 'toxone', 'nucleiform']
          >>> match_object['times']
          [[3, 1, 1, 1], [4, 2, 4, 2], [1, 4, 2, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[13, 16, 20, 22, 27, 29]]
          >>> match_object = time_per_word_match(['missile', 'tillot', 'douser', 'twankingly', 'eccentrate'], p)
          >>> get_all_words(match_object)
          ['missile', 'tillot', 'douser', 'twankingly', 'eccentrate']
          >>> match_object['times']
          [[3, 4, 2, 5, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[70]]
          >>> match_object = time_per_word_match([], p)
          >>> get_all_words(match_object)
          []
          >>> match_object['times']
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[67, 68, 73, 74, 79], [12, 17, 20, 21, 25], [55, 58, 62, 66, 67]]
          >>> match_object = time_per_word_match(['unambiguously', 'standing', 'cameroon', 'unpretendingly'], p)
          >>> get_all_words(match_object)
          ['unambiguously', 'standing', 'cameroon', 'unpretendingly']
          >>> match_object['times']
          [[1, 5, 1, 5], [5, 3, 1, 4], [3, 4, 4, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[54, 57], [76, 80], [24, 25]]
          >>> match_object = time_per_word_match(['megascleric'], p)
          >>> get_all_words(match_object)
          ['megascleric']
          >>> match_object['times']
          [[3], [4], [1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[6, 11], [91, 95], [60, 63]]
          >>> match_object = time_per_word_match(['designee'], p)
          >>> get_all_words(match_object)
          ['designee']
          >>> match_object['times']
          [[5], [4], [3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[14, 15, 20, 24, 25]]
          >>> match_object = time_per_word_match(['dextrousness', 'whirley', 'coldly', 'compendiary'], p)
          >>> get_all_words(match_object)
          ['dextrousness', 'whirley', 'coldly', 'compendiary']
          >>> match_object['times']
          [[1, 5, 4, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[21, 23, 24]]
          >>> match_object = time_per_word_match(['plowfoot', 'caducicorn'], p)
          >>> get_all_words(match_object)
          ['plowfoot', 'caducicorn']
          >>> match_object['times']
          [[2, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[61, 66, 69, 74, 79, 80]]
          >>> match_object = time_per_word_match(['signist', 'plash', 'unbraceleted', 'runner', 'nickeline'], p)
          >>> get_all_words(match_object)
          ['signist', 'plash', 'unbraceleted', 'runner', 'nickeline']
          >>> match_object['times']
          [[5, 3, 5, 5, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[7, 9, 12, 15, 18], [53, 54, 58, 63, 64], [28, 30, 35, 36, 41]]
          >>> match_object = time_per_word_match(['ergastoplasmic', 'sulphurage', 'audibility', 'deuteride'], p)
          >>> get_all_words(match_object)
          ['ergastoplasmic', 'sulphurage', 'audibility', 'deuteride']
          >>> match_object['times']
          [[2, 3, 3, 3], [1, 4, 5, 1], [2, 5, 1, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[22, 26, 31, 32, 37, 39, 40]]
          >>> match_object = time_per_word_match(['uncontestable', 'millage', 'unbudging', 'hydrostatic', 'enterospasm', 'ectypography'], p)
          >>> get_all_words(match_object)
          ['uncontestable', 'millage', 'unbudging', 'hydrostatic', 'enterospasm', 'ectypography']
          >>> match_object['times']
          [[4, 5, 1, 5, 2, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[26, 31], [40, 44]]
          >>> match_object = time_per_word_match(['remissful'], p)
          >>> get_all_words(match_object)
          ['remissful']
          >>> match_object['times']
          [[5], [4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[89, 91, 93, 95, 98, 100, 101], [83, 88, 92, 93, 95, 96, 98], [48, 50, 54, 56, 60, 64, 67]]
          >>> match_object = time_per_word_match(['sacculus', 'sarcodous', 'microbiological', 'ruddy', 'gobble', 'pozzuolana'], p)
          >>> get_all_words(match_object)
          ['sacculus', 'sarcodous', 'microbiological', 'ruddy', 'gobble', 'pozzuolana']
          >>> match_object['times']
          [[2, 2, 2, 3, 2, 1], [5, 4, 1, 2, 1, 2], [2, 4, 2, 4, 4, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[86, 87], [90, 94]]
          >>> match_object = time_per_word_match(['monothelious'], p)
          >>> get_all_words(match_object)
          ['monothelious']
          >>> match_object['times']
          [[1], [4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[74, 76, 78, 83]]
          >>> match_object = time_per_word_match(['boy', 'leaverwood', 'bounteousness'], p)
          >>> get_all_words(match_object)
          ['boy', 'leaverwood', 'bounteousness']
          >>> match_object['times']
          [[2, 2, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[16, 17, 20, 21, 25, 26], [46, 49, 52, 57, 61, 63], [96, 97, 98, 100, 103, 108]]
          >>> match_object = time_per_word_match(['impedient', 'allochiral', 'hear', 'snur', 'myosarcomatous'], p)
          >>> get_all_words(match_object)
          ['impedient', 'allochiral', 'hear', 'snur', 'myosarcomatous']
          >>> match_object['times']
          [[1, 3, 1, 4, 1], [3, 3, 5, 4, 2], [1, 1, 2, 3, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[89, 91], [37, 39], [63, 67]]
          >>> match_object = time_per_word_match(['sulphurproof'], p)
          >>> get_all_words(match_object)
          ['sulphurproof']
          >>> match_object['times']
          [[2], [2], [4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[62], [50], [26]]
          >>> match_object = time_per_word_match([], p)
          >>> get_all_words(match_object)
          []
          >>> match_object['times']
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[44, 47, 51, 56, 58, 60], [4, 7, 11, 16, 19, 22]]
          >>> match_object = time_per_word_match(['neoza', 'detinet', 'repolymerization', 'alchemy', 'caphar'], p)
          >>> get_all_words(match_object)
          ['neoza', 'detinet', 'repolymerization', 'alchemy', 'caphar']
          >>> match_object['times']
          [[3, 4, 5, 2, 2], [3, 4, 5, 3, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[56, 61]]
          >>> match_object = time_per_word_match(['deediness'], p)
          >>> get_all_words(match_object)
          ['deediness']
          >>> match_object['times']
          [[5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[60, 62, 65, 68], [55, 56, 59, 60], [89, 92, 97, 100]]
          >>> match_object = time_per_word_match(['outstartle', 'varicosed', 'ventilator'], p)
          >>> get_all_words(match_object)
          ['outstartle', 'varicosed', 'ventilator']
          >>> match_object['times']
          [[2, 3, 3], [1, 3, 1], [3, 5, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 4, 9, 14, 17, 22, 27]]
          >>> match_object = time_per_word_match(['evaporability', 'ultradolichocephalic', 'kinetophone', 'supernaturalness', 'schout', 'woodlander'], p)
          >>> get_all_words(match_object)
          ['evaporability', 'ultradolichocephalic', 'kinetophone', 'supernaturalness', 'schout', 'woodlander']
          >>> match_object['times']
          [[3, 5, 5, 3, 5, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5]]
          >>> match_object = time_per_word_match([], p)
          >>> get_all_words(match_object)
          []
          >>> match_object['times']
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[11], [37], [36]]
          >>> match_object = time_per_word_match([], p)
          >>> get_all_words(match_object)
          []
          >>> match_object['times']
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[54, 55, 58, 62], [74, 76, 81, 82], [41, 43, 46, 47]]
          >>> match_object = time_per_word_match(['payable', 'jaunt', 'oleostearin'], p)
          >>> get_all_words(match_object)
          ['payable', 'jaunt', 'oleostearin']
          >>> match_object['times']
          [[1, 3, 4], [2, 5, 1], [2, 3, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[33, 34], [39, 40]]
          >>> match_object = time_per_word_match(['entropium'], p)
          >>> get_all_words(match_object)
          ['entropium']
          >>> match_object['times']
          [[1], [1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[72, 77, 82, 85, 90, 91], [5, 9, 14, 17, 21, 22]]
          >>> match_object = time_per_word_match(['stookie', 'withsave', 'subchoroid', 'briefing', 'upbelch'], p)
          >>> get_all_words(match_object)
          ['stookie', 'withsave', 'subchoroid', 'briefing', 'upbelch']
          >>> match_object['times']
          [[5, 5, 3, 5, 1], [4, 5, 3, 4, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[29, 34], [69, 70], [71, 72]]
          >>> match_object = time_per_word_match(['battlewise'], p)
          >>> get_all_words(match_object)
          ['battlewise']
          >>> match_object['times']
          [[5], [1], [1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[8, 10, 15, 18, 23, 26], [3, 7, 12, 13, 16, 17], [86, 89, 90, 95, 98, 101]]
          >>> match_object = time_per_word_match(['muscoid', 'reliquidation', 'broad', 'tugging', 'retardant'], p)
          >>> get_all_words(match_object)
          ['muscoid', 'reliquidation', 'broad', 'tugging', 'retardant']
          >>> match_object['times']
          [[2, 5, 3, 5, 3], [4, 5, 1, 3, 1], [3, 1, 5, 3, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[71, 73, 75, 80, 84], [3, 8, 10, 14, 16]]
          >>> match_object = time_per_word_match(['hexatomic', 'trophobiosis', 'parascenium', 'gibbet'], p)
          >>> get_all_words(match_object)
          ['hexatomic', 'trophobiosis', 'parascenium', 'gibbet']
          >>> match_object['times']
          [[2, 2, 5, 4], [5, 2, 4, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2], [83], [56]]
          >>> match_object = time_per_word_match([], p)
          >>> get_all_words(match_object)
          []
          >>> match_object['times']
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[9, 13, 18, 19, 23, 26, 29], [85, 89, 92, 94, 97, 102, 105], [5, 9, 12, 13, 14, 15, 18]]
          >>> match_object = time_per_word_match(['unimpressed', 'unexcusableness', 'bismuthyl', 'adapt', 'refutable', 'fluoridize'], p)
          >>> get_all_words(match_object)
          ['unimpressed', 'unexcusableness', 'bismuthyl', 'adapt', 'refutable', 'fluoridize']
          >>> match_object['times']
          [[4, 5, 1, 4, 3, 3], [4, 3, 2, 3, 5, 3], [4, 3, 1, 1, 1, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[82, 86], [16, 18]]
          >>> match_object = time_per_word_match(['ab'], p)
          >>> get_all_words(match_object)
          ['ab']
          >>> match_object['times']
          [[4], [2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[77, 82, 83, 88, 92]]
          >>> match_object = time_per_word_match(['theophysical', 'penceless', 'bromothymol', 'reticuloramose'], p)
          >>> get_all_words(match_object)
          ['theophysical', 'penceless', 'bromothymol', 'reticuloramose']
          >>> match_object['times']
          [[5, 1, 5, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[90, 91, 93, 97, 98], [64, 68, 70, 73, 78], [95, 100, 103, 108, 113]]
          >>> match_object = time_per_word_match(['beshag', 'monument', 'appressor', 'tutu'], p)
          >>> get_all_words(match_object)
          ['beshag', 'monument', 'appressor', 'tutu']
          >>> match_object['times']
          [[1, 2, 4, 1], [4, 2, 3, 5], [5, 3, 5, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[86], [26], [8]]
          >>> match_object = time_per_word_match([], p)
          >>> get_all_words(match_object)
          []
          >>> match_object['times']
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[25, 26, 30], [50, 54, 59], [52, 55, 60]]
          >>> match_object = time_per_word_match(['confidentiality', 'inclementness'], p)
          >>> get_all_words(match_object)
          ['confidentiality', 'inclementness']
          >>> match_object['times']
          [[1, 4], [4, 5], [3, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[58, 63]]
          >>> match_object = time_per_word_match(['sardius'], p)
          >>> get_all_words(match_object)
          ['sardius']
          >>> match_object['times']
          [[5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[77, 81, 85, 89]]
          >>> match_object = time_per_word_match(['bluehearts', 'repugnatorial', 'bescorch'], p)
          >>> get_all_words(match_object)
          ['bluehearts', 'repugnatorial', 'bescorch']
          >>> match_object['times']
          [[4, 4, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[75, 78, 80]]
          >>> match_object = time_per_word_match(['efflorescency', 'presay'], p)
          >>> get_all_words(match_object)
          ['efflorescency', 'presay']
          >>> match_object['times']
          [[3, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[53, 54, 59, 61], [47, 50, 54, 56]]
          >>> match_object = time_per_word_match(['myologist', 'dualistic', 'becense'], p)
          >>> get_all_words(match_object)
          ['myologist', 'dualistic', 'becense']
          >>> match_object['times']
          [[1, 5, 2], [3, 4, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[85, 90, 93, 95, 98, 102, 105], [5, 10, 12, 13, 14, 18, 22], [91, 94, 97, 100, 102, 105, 108]]
          >>> match_object = time_per_word_match(['tentacle', 'nonrestitution', 'interventional', 'demiditone', 'chrysophilite', 'idiosyncratically'], p)
          >>> get_all_words(match_object)
          ['tentacle', 'nonrestitution', 'interventional', 'demiditone', 'chrysophilite', 'idiosyncratically']
          >>> match_object['times']
          [[5, 3, 2, 3, 4, 3], [5, 2, 1, 1, 4, 4], [3, 3, 3, 2, 3, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[95, 98, 100, 103], [1, 3, 8, 13]]
          >>> match_object = time_per_word_match(['clique', 'spuriae', 'introspectable'], p)
          >>> get_all_words(match_object)
          ['clique', 'spuriae', 'introspectable']
          >>> match_object['times']
          [[3, 2, 3], [2, 5, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[10, 15, 19, 24, 28, 31]]
          >>> match_object = time_per_word_match(['epicotyledonary', 'hiro', 'tremolo', 'ringgiving', 'pignoratitious'], p)
          >>> get_all_words(match_object)
          ['epicotyledonary', 'hiro', 'tremolo', 'ringgiving', 'pignoratitious']
          >>> match_object['times']
          [[5, 4, 5, 4, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[31, 36, 39, 42, 44, 47, 50]]
          >>> match_object = time_per_word_match(['wickerworker', 'disdiaclastic', 'tutoyer', 'fibrilliferous', 'undiscernedly', 'gloomily'], p)
          >>> get_all_words(match_object)
          ['wickerworker', 'disdiaclastic', 'tutoyer', 'fibrilliferous', 'undiscernedly', 'gloomily']
          >>> match_object['times']
          [[5, 3, 3, 2, 3, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[7]]
          >>> match_object = time_per_word_match([], p)
          >>> get_all_words(match_object)
          []
          >>> match_object['times']
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[87]]
          >>> match_object = time_per_word_match([], p)
          >>> get_all_words(match_object)
          []
          >>> match_object['times']
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[37, 40, 43, 44, 48, 53]]
          >>> match_object = time_per_word_match(['quadratical', 'principiate', 'archinfamy', 'cacomixle', 'endonuclear'], p)
          >>> get_all_words(match_object)
          ['quadratical', 'principiate', 'archinfamy', 'cacomixle', 'endonuclear']
          >>> match_object['times']
          [[3, 3, 1, 4, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[69]]
          >>> match_object = time_per_word_match([], p)
          >>> get_all_words(match_object)
          []
          >>> match_object['times']
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 8]]
          >>> match_object = time_per_word_match(['subframe'], p)
          >>> get_all_words(match_object)
          ['subframe']
          >>> match_object['times']
          [[5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[40], [49]]
          >>> match_object = time_per_word_match([], p)
          >>> get_all_words(match_object)
          []
          >>> match_object['times']
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[8, 12, 16, 21, 26, 30]]
          >>> match_object = time_per_word_match(['waling', 'sycophantishly', 'mistresshood', 'lazzarone', 'define'], p)
          >>> get_all_words(match_object)
          ['waling', 'sycophantishly', 'mistresshood', 'lazzarone', 'define']
          >>> match_object['times']
          [[4, 4, 5, 5, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[31, 35], [97, 102], [27, 29]]
          >>> match_object = time_per_word_match(['donary'], p)
          >>> get_all_words(match_object)
          ['donary']
          >>> match_object['times']
          [[4], [5], [2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5], [86], [1]]
          >>> match_object = time_per_word_match([], p)
          >>> get_all_words(match_object)
          []
          >>> match_object['times']
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[79]]
          >>> match_object = time_per_word_match([], p)
          >>> get_all_words(match_object)
          []
          >>> match_object['times']
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[59], [68], [75]]
          >>> match_object = time_per_word_match([], p)
          >>> get_all_words(match_object)
          []
          >>> match_object['times']
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
    },
    {
      'cases': [
        {
          'code': r"""
          >>> test.swap_implementations(cats) # Make sure the abstraction barrier isn't crossed!
          >>> p = [[1, 4, 6, 7], [0, 4, 6, 9]]
          >>> words = ['This', 'is', 'fun']
          >>> match_object = cats.time_per_word_match(words, p)
          >>> cats.get_word(match_object, 0)
          'This'
          >>> cats.get_time(match_object, 0, 0)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import cats
      >>> import tests.abstraction_check as test # Make sure the abstraction barrier isn't crossed!
      """,
      'teardown': r"""
      >>> test.restore_implementations(cats)
      """,
      'type': 'doctest'
    }
  ]
}
