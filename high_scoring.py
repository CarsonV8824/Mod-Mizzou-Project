from saving import Database_manager

class Highscores:
    # Initialize with player name and score
    def __init__(self, name, score):
        
        # Store name and score, and create a database manager instance
        self.name = name
        self.score = score
        self.db = Database_manager()

    def update_hs(self):
        # Read existing high scores from the database
        data = self.db.read()
        x = 0
        for i, j in data[1].items():
            x += 1
            if self.score >= j:
                data_items = list(data[1].items())
                data_items.insert(x, (self.name, self.score))
                data_items.pop()
                data[1] = dict(data_items)
        self.db.update(data)