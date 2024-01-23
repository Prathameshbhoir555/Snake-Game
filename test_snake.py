import pytest
from snake import SNAKE, FRUIT, MAIN, Vector2

# Assuming your game file is named 'your_snake_game_file.py'

@pytest.fixture
def initialize_game():
    game = MAIN()
    return game

def test_snake_initialization():
    snake = SNAKE()
    assert len(snake.body) == 3
    assert snake.direction == Vector2(0, 0)
    assert snake.new_block is False

def test_fruit_initialization():
    fruit = FRUIT()
    assert hasattr(fruit, 'pos')

def test_game_update(initialize_game):
    game = initialize_game
    initial_snake_length = len(game.snake.body)
    initial_fruit_position = game.fruit.pos

    # Assuming that the snake moves right by default
    game.update()

    assert len(game.snake.body) == initial_snake_length
    assert game.fruit.pos != initial_fruit_position

# Add more tests as needed based on the functionality of your game.
