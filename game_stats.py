import os

class GameStats:
    """Track statistics for Alien Invasion."""
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = self.load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    # def load_high_score(self):
    #     try:
    #         current_dir = os.path.dirname(__file__)
    #         file_path = os.path.join(current_dir, "high_score.txt")
    #         with open(file_path, encoding="utf-8") as file:
    #             return int(file.read())
    #     except FileNotFoundError:
    #         return 0
    #     except Exception as e:
    #         print(f"An error occurred: {e}")
    #         return 0

    def load_high_score(self):
        try:
            current_dir = os.path.dirname(__file__)
            file_path = os.path.join(current_dir, "high_score.txt")

            with open(file_path, encoding="utf-8") as file:
                contents = file.read().strip()  # Strip any extra whitespace or newlines

                if contents:  # Only attempt to convert if contents are non-empty
                    return int(contents)
                else:
                    return 0  # If the file is empty, return 0 as the high score

        except FileNotFoundError:
            return 0  # File doesn't exist, return default score of 0

        except ValueError:
            print("The high score file contains invalid data. Resetting to 0.")
            return 0  # File contains invalid data, return 0 as fallback

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return 0  # Catch any other exceptions, return 0 as fallback

    def _save_high_score(self):
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, "high_score.txt")

        high_score = (
            self.high_score
        )  # Assuming self.stats.high_score holds the high score

        try:
            with open(file_path, mode="w", encoding="utf-8") as file:
                file.write(str(high_score))
                print(f"High score {high_score} successfully saved to the file!")
        except Exception as e:
            print(f"An error occurred while saving the high score: {e}")
