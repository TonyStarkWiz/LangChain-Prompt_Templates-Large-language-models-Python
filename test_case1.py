import unittest
from unittest.mock import patch
from Prompt_Templates import chat_prompt.format_prompt  # Import your recipe generation function

class TestRecipeAccuracy(unittest.TestCase):

    @patch('builtins.open', return_value=open('api_jupyter.txt', 'r'))
    @patch('langchain.llms.OpenAI')
    @patch('langchain.chat_models.ChatOpenAI')
    @patch('openai.ChatCompletion.create')
    def test_recipe_accuracy(self, mock_openai_chat, mock_chat_openai, mock_openai, mock_open):
        # Set up your mocked responses from OpenAI
        mock_openai.return_value.api_key = 'your_mocked_api_key'
        mock_openai_chat.return_value.choices[0].message['content'] = 'Your mocked OpenAI response'
        mock_chat_openai.return_value.content = 'Your mocked ChatOpenAI response'

        # Call your function that generates the recipe
        generated_recipe = chat_prompt.format_prompt(cooking_time='60 min',
                          recipe_request='Quick Snake',
                          dietary_preference='Vegan').to_messages()

        # Define the expected recipe content based on the mocked responses
        expected_recipe = 
        Ingredients:

        Instructions:


        # Strip whitespace and newlines for accurate comparison
        generated_recipe_stripped = generated_recipe.strip()
        expected_recipe_stripped = expected_recipe.strip()

        # Assert if the generated recipe matches the expected recipe
        self.assertEqual(generated_recipe_stripped, expected_recipe_stripped)

if __name__ == '__main__':
    unittest.main()
