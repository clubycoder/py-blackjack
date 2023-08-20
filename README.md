# Blackjack in Python

Simple terminal blackjack against the house.
* No splits
* No doubling down
* Player starts with $100
* Just get to 21 or under or bust
* The house will hit if under 17

The tries to keep it simple, but does use multiple classes
and inheritance.

```bash
python3 blackjack.py
```

```
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
You have $120
Bet or q to quit > 20
[ House - Score = ? ]
┌─────┐ ╔═════╗ 
│4    │ ║ ┌─\ ║ 
│  ♠  │ ║ │ │ ║ 
│    4│ ║ \─┘ ║ 
└─────┘ ╚═════╝ 
[ Player - Score = 20 ]
┌─────┐ ┌─────┐ 
│Q    │ │J    │ 
│  ♦  │ │  ♥  │ 
│    Q│ │    J│ 
└─────┘ └─────┘ 
Hit? (y or n) > n
[ House - Score = 7 ]
┌─────┐ ┌─────┐ 
│4    │ │3    │ 
│  ♠  │ │  ♥  │ 
│    4│ │    3│ 
└─────┘ └─────┘ 
[ House - Score = 15 ]
┌─────┐ ┌─────┐ ┌─────┐ 
│4    │ │3    │ │8    │ 
│  ♠  │ │  ♥  │ │  ♦  │ 
│    4│ │    3│ │    8│ 
└─────┘ └─────┘ └─────┘ 
[ House - Score = 25 ]
┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ 
│4    │ │3    │ │8    │ │10   │ 
│  ♠  │ │  ♥  │ │  ♦  │ │  ♦  │ 
│    4│ │    3│ │    8│ │   10│ 
└─────┘ └─────┘ └─────┘ └─────┘ 
House busts!
```
