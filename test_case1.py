import unittest
import time
from Prompt_Templates import chat_prompt.format_prompt  # Import your recipe generation function

class TestRecipeSpeed(unittest.TestCase):

    def test_recipe_generation_speed(self):
        # Define input parameters for the recipe generation function
        cooking_time = '60 min'
        recipe_request = 'Quick Snake'
        dietary_preference = 'Vegan'

        # Measure the time taken to generate the recipe
        start_time = time.time()
        generated_recipe = generate_recipe(cooking_time, recipe_request, dietary_preference)
        end_time = time.time()

        # Calculate the time taken in seconds
        time_taken = end_time - start_time

        # Define the maximum allowed time for recipe generation (adjust as needed)
        max_allowed_time = 1.0  # 1 second

        # Assert that the time taken is less than the maximum allowed time
        self.assertLess(time_taken, max_allowed_time, f"Recipe generation took {time_taken:.2f} seconds, which exceeds the allowed time of {max_allowed_time} seconds.")

if __name__ == '__main__':
    unittest.main()
