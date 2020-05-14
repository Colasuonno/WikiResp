

def birth_death():
    return [
        ["birth", "death"],
        {"P31": "Q5"}, {"P19": "?birth"}, {}, {"P20": "?death"}
    ]


def languages_spoken():
    return [
        ["languages_spoken"],
        {"P31": "Q5"}, {"P1412": "?languages_spoken"}, {}, {}
    ]


def father_mather():
    return [
        ["father", "mother"],
        {"P31": "Q5"}, {}, {}, {"P22": "?father", "P25": "?mother"}
    ]


