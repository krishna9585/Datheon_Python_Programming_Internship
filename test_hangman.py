import unittest
from unittest.mock import patch

import hangman


class HangmanTests(unittest.TestCase):

    def test_display_word_hides_letters(self):
        result = hangman.display_word("python", {"p", "o"})
        self.assertEqual(result, "p _ _ _ o _")

    def test_display_word_reveals_guessed_letters(self):
        result = hangman.display_word("python", set("python"))
        self.assertEqual(result, "p y t h o n")

    def test_valid_letter(self):
        with patch("builtins.input", return_value="P"):
            self.assertEqual(hangman.get_letter(), "p")

    def test_rejects_multiple_letters(self):
        with patch("builtins.input", return_value="ab"):
            self.assertIsNone(hangman.get_letter())

    def test_rejects_numbers(self):
        with patch("builtins.input", return_value="5"):
            self.assertIsNone(hangman.get_letter())

    def test_win(self):
        # The secret word is fixed so the test is repeatable.
        with patch("hangman.random.choice", return_value="a"):
            with patch("builtins.input", side_effect=["a"]):
                with patch("builtins.print") as output:
                    hangman.play_game()

                    messages = " ".join(
                        str(call) for call in output.call_args_list
                    )
                    self.assertIn("You won!", messages)

    def test_loss(self):
        # Six distinct wrong letters for the word "a".
        with patch("hangman.random.choice", return_value="a"):
            with patch(
                "builtins.input",
                side_effect=list("bcdefg")
            ):
                with patch("builtins.print") as output:
                    hangman.play_game()

                    messages = " ".join(
                        str(call) for call in output.call_args_list
                    )
                    self.assertIn("Game over!", messages)
                    self.assertIn("The correct word was:", messages)


if __name__ == "__main__":
    unittest.main()