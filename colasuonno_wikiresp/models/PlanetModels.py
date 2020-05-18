def radius():
    return {
        "labels": ["radiusLabel", "radiusUnitLabel", "image", "orbitPeriod", "orbitPeriodUnitLabel",
                   "distanceFromEarth", "distanceFromEarthUnitLabel", "mass", "massUnitLabel",
                   "orbitInclination", "orbitInclinationUnitLabel", "area", "areaUnitLabel"],
        "conditions": {
            "0": {
                "startVar": "?id",
                "conditions": "wdt:P31",
                "endVar": "?instance"
            },
            "1": {
                "startVar": "?instance",
                "conditions": "wdt:P279",
                "endVar": "?sub"
            },
            "2": {
                "startVar": "?ss",
                "conditions": "wdt:P279 wd:Q634",
                "endVar": ""
            },
            "3": {
                "startVar": "?id",
                "conditions": "wdt:P18",
                "endVar": "?image"
            },
            "4": {
                "startVar": "?id",
                "conditions": "p:P2146/psv:P2146 [ wikibase:quantityAmount ?orbitPeriod; wikibase:quantityUnit",
                "endVar": "?orbitPeriodUnit]"
            },
            "5": {
                "startVar": "?id",
                "conditions": "p:P2067/psv:P2067 [ wikibase:quantityAmount ?mass; wikibase:quantityUnit",
                "endVar": "?massUnit]"
            },
            "6": {
                "startVar": "?id",
                "conditions": "p:P2045/psv:P2045 [ wikibase:quantityAmount ?orbitInclination; wikibase:quantityUnit",
                "endVar": "?orbitInclinationUnit]"
            },
            "7": {
                "startVar": "?id",
                "conditions": "p:P2120/psv:P2120 [ wikibase:quantityAmount ?radius; wikibase:quantityUnit",
                "endVar": "?radiusUnit]"
            },
        },
        "optional_conditions": {
            "0": {
                "startVar": "?id",
                "conditions": "p:P2583/psv:P2583 [ wikibase:quantityAmount ?distanceFromEarth; wikibase:quantityUnit",
                "endVar": "?distanceFromEarthUnit]"
            },
            "1": {
                "startVar": "?id",
                "conditions": "p:P2046/psv:P2046 [ wikibase:quantityAmount ?area; wikibase:quantityUnit",
                "endVar": "?areaUnit]"
            },
        },
        "last": "",
        "limit": 1
    }
