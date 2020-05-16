
def flag_image():
    return [
        ["flag_image"],
        {}, {"P41": "?flag_image"}, {}, {}
    ]


def citizens_count():
    return [
        ["citizens_count", "year"],
        {"p"}, {"P1082": "?citizens_count"}, {}, {"P585": "?year"},
        "ORDER BY DESC(?year)"
    ]