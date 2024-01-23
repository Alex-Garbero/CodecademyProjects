class Player:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance

    def bet(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            print(f"{self.name}, insufficient funds")
            return 0

    def receive_winnings(self, winnings):
        self.balance += winnings

class Casino:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def play_game(self, player, bet_amount):
        import random

        result = random.choice(["win", "lose"])

        if result == "win":
            winnings = bet_amount * 2
            player.receive_winnings(winnings)
            print(f"{player.name} wins {winnings}! {player.name} now has {player.balance}")
        else:
            print(f"{player.name} loses {bet_amount}! {player.name} now has {player.balance}")

# Instantiate the Casino
casino = Casino()

# Create players
player1 = Player("Alice", 1000)
player2 = Player("Bob", 1500)

# Add players to the casino
casino.add_player(player1)
casino.add_player(player2)

# Set bet amount
bet_amount = 50

# Play the game for each player
for player in casino.players:
    bet = player.bet(bet_amount)
    if bet > 0:
        casino.play_game(player, bet)

# Remove players from the casino
casino.remove_player(player1)
casino.remove_player(player2)
