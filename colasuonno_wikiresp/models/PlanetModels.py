

def radius():
    return {
        "labels": ["radiusLabel", "unitLabel"],
        "conditions":  {
            "0": {
                "startVar": "?id",
                "conditions": "p:P2120/psv:P2120 [ wikibase:quantityAmount ?radius; wikibase:quantityUnit",
                "endVar": "?unit]"
            }
        },
        "optional_conditions": {},
        "last": "",
        "type": "DirectWikiQuery"
    }


