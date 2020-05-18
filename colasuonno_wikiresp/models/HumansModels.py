
def birth_death():
    return {
        "labels": ["birth", "death", "description"],
        "conditions":  {
            "0": {
                "startVar": "?id",
                "conditions": "wdt:P31 wd:Q5",
                "endVar": ""
            },
            "1": {
                "startVar": "?id",
                "conditions": "wdt:P569",
                "endVar": "?birth"
            },
            "2": {
                "startVar": "?id",
                "conditions": "schema:description",
                "endVar": "?description"
            },
            "3": {
                "startVar": "",
                "conditions": "FILTER ( lang(?description) = \"{lang_ind}\" )",
                "endVar": ""
            }

        },
        "optional_conditions": {
            "0": {
                "startVar": "?id",
                "conditions": "wdt:P570",
                "endVar": "?death"
            }
        },
        "last": "",
        "limit": 10
    }


def languages_spoken():
    return {
        "labels": ["languages_spokenLabel"],
        "conditions":  {
            "0": {
                "startVar": "?id",
                "conditions": "wdt:P31 wd:Q5",
                "endVar": ""
            },
            "1": {
                "startVar": "?id",
                "conditions": "wdt:P1412",
                "endVar": "?languages_spoken"
            },

        },
        "optional_conditions": {
        },
        "last": "",
        "limit": 10
    }


def father_mother():
    return [
        ["father", "mother"],
        {"P31": "Q5"}, {}, {}, {"P22": "?father", "P25": "?mother"}
    ]
