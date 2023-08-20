suits = ["♥", "♦", "♣", "♠"]
faces = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "K": 10,
    "Q": 10,
    "A": 11
}

turned_graphic_lines = [
    "╔═════╗",
    "║ ┌─\\ ║",
    "║ │ │ ║",
    "║ \\─┘ ║",
    "╚═════╝"
]


class Card:
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face
        self.graphic_lines = [
            "┌─────┐",
            "│%-2s   │" % (self.face),
            "│  %s  │" % (self.suit),
            "│   %2s│" % (self.face),
            "└─────┘"
        ]
        self.turned = False

    def get_value(self):
        return faces[self.face]

    def get_graphic_line(self, line_num):
        if self.turned:
            return turned_graphic_lines[line_num]
        return self.graphic_lines[line_num]


cards = []
for suit in suits:
    for face in faces.keys():
        cards.append(Card(suit, face))