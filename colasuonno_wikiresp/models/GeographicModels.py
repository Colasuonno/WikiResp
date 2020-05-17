
def flag_image():
    return [
        ["flag_image"],
        {}, {"P41": "?flag_image"}, {}, {}
    ]


def citizens_count():
    return {
        "labels": ["citizens_count", "citizens_countLabel", "year"],
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
