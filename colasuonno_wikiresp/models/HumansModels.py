

def birth_death():
    return {
        "labels": ["birth", "death"],
        "conditions":  {"P31": "Q5"},
        "assignments": {"P19": "?birth"},
        "optional_conditions": {},
        "optional_assignments": {"P20": "?death"},
        "type": "DirectWikiQuery"
    }


def languages_spoken():
    return [
        ["languages_spoken"],
        {"P31": "Q5"}, {"P1412": "?languages_spoken"}, {}, {}
    ]


def father_mother():
    return [
        ["father", "mother"],
        {"P31": "Q5"}, {}, {}, {"P22": "?father", "P25": "?mother"}
    ]


