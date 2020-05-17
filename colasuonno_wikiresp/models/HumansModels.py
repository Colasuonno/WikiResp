
def birth_death():
    return {
        "labels": ["birth", "death"],
        "conditions":  {
            "0": {
                "startVar": "?id",
                "conditions": "p:P1082",
                "endVar": "?prop"
            },
            "1": {
                "startVar": "?id",
                "conditions": "wdt:P1082",
                "endVar": "?citizens_count"
            }

        },
        "optional_conditions": {
            "0": {
                "startVar": "?prop",
                "conditions": "pq:P585",
                "endVar": "?year"
            }
        },
        "last": "ORDER BY DESC(?year)",
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
