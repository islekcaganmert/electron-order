class Orbit:
    def __init__(self, head, letter, top):
        self.head = head
        self.letter = letter
        self.top = top

    def render(self):
        return f'{self.head}{self.letter}<span style="vertical-align:top;font-size:0.6em">{self.top}</span>'


def calculate_orbits(count: (int, str)) -> list[Orbit]:
    orbits = []
    maxed = [
        [1, 's', 2],
        [2, 's', 2],
        [2, 'p', 6],
        [3, 's', 2],
        [3, 'p', 6],
        [4, 's', 2],
        [3, 'd', 10],
        [4, 'p', 6],
        [5, 's', 2],
    ]
    elements = {
        'he': 2,
        'li': 3,
        'be': 4,
        'b': 5,
        'c': 6,
        'n': 7,
        'o': 8,
        'f': 9,
        'ne': 10,
        'na': 11,
        'mg': 12,
        'al': 13,
        'si': 14,
        'p': 15,
        's': 16,
        'cl': 17,
        'ar': 18,
        'k': 19,
        'ca': 20,
        'sc': 21,
        'ti': 22,
        'v': 23,
        'cr': 24,
        'mn': 25,
        'fe': 26,
        'co': 27,
        'ni': 28,
        'cu': 29,
        'zn': 30,
        'ga': 31,
        'ge': 32,
        'as': 33,
        'se': 34,
        'br': 35,
        'kr': 36,
        'rb': 37,
        'sr': 38,
    }
    exceptions = {
        "24": [Orbit(*i) for i in [[1, 's', 2], [2, 's', 2], [2, 'p', 6], [3, 's', 2], [3, 'p', 6], [3, 'd', 5], [4, 's', 1]]],
        "29": [Orbit(*i) for i in [[1, 's', 2], [2, 's', 2], [2, 'p', 6], [3, 's', 2], [3, 'p', 6], [3, 'd', 10], [4, 's', 1]]],
        "42": [Orbit(*i) for i in [[1, 's', 2], [2, 's', 2], [2, 'p', 6], [3, 's', 2], [3, 'p', 6], [3, 'd', 10], [4, 's', 2], [4, 'p', 6], [4, 'd', 5], [5, 's', 1]]],
    }
    if isinstance(count, str):
        count = elements[count.lower()]
    if str(count) in exceptions:
        return exceptions[str(count)]
    while count > 0:
        current_orbit = maxed.pop(0)
        if count >= current_orbit[1]:
            orbits.append(Orbit(*current_orbit))
            count -= current_orbit[1]
        else:
            orbits.append(Orbit(current_orbit[0], current_orbit[1], count))
            count = 0
    return orbits
