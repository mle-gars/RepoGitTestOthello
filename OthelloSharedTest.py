import random
import csv
import copy

# Object used to create new boards


class Board:
    def __init__(self, size):
        self.size = size
        self.board = []

    # Used to fill the "board" property with a list with a length equal to the "size" property
    def create_board(self):
        for y_pos in range(self.size):
            for x_pos in range(self.size):
                #  Create a Tile instance
                #  Gives it the coordinates (depending on x_pos and y_pos)
                #  Add it to the board property
                if x_pos != 0 and x_pos != 7 and y_pos != 0 and y_pos != 7:
                    self.board.append(Tile(x_pos, y_pos, "🟩", "🟩"))
                else:
                    self.board.append(Tile(x_pos, y_pos, "X", "🟩"))
        self.place_initial_pawns()

    #  This will print the game board, depending on the data_type
    #  Data types are "Coordinates", "Type" and "Content"
    def draw_board(self, data_type):
        display_board = []
        line_breaker = 0
        print([0, ' 0', ' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7'])
        for board_index in self.board:
            if (board_index.x_pos == 0):
                display_board.append(board_index.y_pos)
            if data_type == "Coordinates":
                display_board.append([board_index.x_pos, board_index.y_pos])
            elif data_type == "Type":
                display_board.append(board_index.type)
            else:
                display_board.append(board_index.content)
            line_breaker += 1
            if line_breaker > 7:
                print(display_board)
                line_breaker = 0
                display_board = []
        print("\n")

    # Place the 4 initial pawns at the center of the board (2 white and 2 black)
    def place_initial_pawns(self):
        #  We pick the 4 central tiles
        #  And place 2 black pawns and 2 white pawns
        self.board[27].content = "⚪"
        self.board[28].content = "⚫"
        self.board[35].content = "⚫"
        self.board[36].content = "⚪"
        
        # self.board[11].content = "⚫"
        # self.board[9].content = "⚪"
        # self.board[10].content = "⚪"
        # self.board[11].content = "⚪"
        
        # self.board[10].content = "⚫"
        # self.board[18].content = "⚪"
        # self.board[19].content = "⚪"
        # self.board[26].content = "⚪"
        # self.board[35].content = "⚪"
        # self.board[36].content = "⚪"
        # self.board[37].content = "⚫"
        

    # Check if the position in inside the board
    # Return true or false depending if it is inside or not
    def is_on_board(self, x_pos, y_pos):
        if x_pos < 0 or x_pos > 7 or y_pos < 0 or y_pos > 7:
            return False
        else:
            return True

    # Check if the tile is an empty tile ("🟩")
    # Return true or false depending if it is empty or not
    def is_tile_empty(self, x_pos, y_pos):
        if self.board[(x_pos) + y_pos * 8].content == "🟩":
            return True
        else:
            return False

    # Takes a position (x_pos, y_pos) and a color
    # Try to simulate the move
    # Returns either false if the move is not valid
    # Or returns which pawns will change color if true
    # The returned list will contain [numbers_of_pawns_to_change, [direction_x, direction_y]]
    def is_legal_move(self, x_pos, y_pos, color):

        # North / Nort-East / East / South-East / South / South-West / West / North-West
        directions = [
            [0, -1],
            [1, -1],
            [1, 0],
            [1, 1],
            [0, 1],
            [-1, 1],
            [-1, 0],
            [-1, -1],
        ]

        # Opposite of the color of the placed pawn
        if color == "⚪":
            awaited_color = "⚫"
        else:
            awaited_color = "⚪"

        current_x_pos = x_pos
        current_y_pos = y_pos
        is_legal = False
        # [number_of_tile_to_flip, direction]
        # Si on a un pion noir placé en 2,3, on veut:
        # [[1, [1, 0]]
        tiles_to_flip = []

        if (not self.is_tile_empty(current_x_pos, current_y_pos) or not self.is_on_board(current_x_pos, current_y_pos)):
            return False

        # Check for every direction
        for current_dir in directions:
            number_of_tiles_to_flip = 1
            # Get your original coordinates + the direction modifier
            current_x_pos = x_pos + current_dir[0]
            current_y_pos = y_pos + current_dir[1]
            # Check if the new position is on the board and empty
            if self.is_on_board(current_x_pos, current_y_pos):
                #  Get the tile informations
                current_index = self.board[current_x_pos + current_y_pos * 8]
                # If the tile contains a pawn of the opposite color, continue on the line
                while current_index.content == awaited_color:
                    current_x_pos += current_dir[0]
                    current_y_pos += current_dir[1]
                    if self.is_on_board(current_x_pos, current_y_pos):
                        current_index = self.board[current_x_pos +
                                                   current_y_pos * 8]
                        # If the line ends with a pawn of your color, then the move is legal
                        if current_index.content == color:
                            is_legal = True
                            tiles_to_flip.append(
                                [number_of_tiles_to_flip, current_dir])
                            break
                    else:
                        break
                    number_of_tiles_to_flip += 1

        if is_legal:
            return tiles_to_flip
        else:
            return False

    # Takes a position (x_pos, y_pos), an array with a number of tiles to flip and a direction, and a color
    # The array should be obtained with the "is_legal_move" function
    # Doesn't return anything, but will change the color of the tiles selected by "tiles_to_flip"
    def flip_tiles(self, x_pos, y_pos, tiles_to_flip, color):
        # x_pos and y_pos = new pawn position
        # tiles_to_flip = list containing the number of pawn to flip and a direction
        # ex: [
        # [1, [1, 0]],
        # ] means we're changing 1 pawn to the right
        # color = the new color of the pawns to flip
        for current_dir in tiles_to_flip:
            current_x_pos = x_pos + current_dir[1][0]
            current_y_pos = y_pos + current_dir[1][1]
            for nb_tile in range(current_dir[0]):
                current_index = self.board[current_x_pos + current_y_pos * 8]
                current_index.content = color
                current_x_pos += current_dir[1][0]
                current_y_pos += current_dir[1][1]

# Used to create each tile of your board
# Contains a position (x, y), a type to check if it's a boder tile or not, and a content to check if there is a pawn inside the tile


class Tile:
    #   Type is used to check if its an "🟩" empty tile or a "X" border tile
    #   Content is used to check if a pawn is placed o (Empty), B (Black), W (White)
    def __init__(self, x_pos, y_pos, type, content):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.type = type
        self.content = content

# Used to create new ruleset
# Contains the score, the active player, the game_over check and functions allowing to interact with the game


class Game:
    def __init__(self):
        self.score_black = 2
        self.score_white = 2
        self.active_player = "⚫"
        self.is_game_over = False
        self.winner = "Noone"

    # Place a pawn on the board (checks if the move is legal before placing it)
    # It takes a position (x, y), a Board object instance and a color
    # The function will automatically check if the move is valid or not
    def place_pawn(self, x_pos, y_pos, board_instance, color):
        if not board_instance.is_on_board(x_pos, y_pos):
            print("Coordinates outside the board")
        else:
            if board_instance.board[(x_pos) + y_pos * 8].content == "🟩":
                tiles_to_flip = board_instance.is_legal_move(
                    x_pos, y_pos, color)
                if not tiles_to_flip:
                    print("Invalid move")
                else:
                    board_instance.board[(x_pos) + y_pos * 8].content = color
                    board_instance.flip_tiles(
                        x_pos, y_pos, tiles_to_flip, color)
                    print(f"Pion placé en {x_pos}, {y_pos}")
                    self.update_score(board_instance)
                    self.change_active_player()
                    self.check_for_valid_moves(board_instance)
                    board_instance.draw_board("Content")
            else:
                print("There is already a pawn here")

    # Change the active player color from black to white or white to black
    def change_active_player(self):
        # Prend self.active_player et change la couleur du joueur actif
        if self.active_player == "⚫":
            self.active_player = "⚪"
            print("C'est au tour du joueur blanc")
        else:
            self.active_player = "⚫"
            print("C'est au tour du joueur noir")

    # Update the players score after a successful move
    def update_score(self, board_instance):
        # Count all the black & white pawns, and update the scores
        w_score = 0
        b_score = 0
        for tile_index in board_instance.board:
            if tile_index.content == "⚪":
                w_score += 1
            elif tile_index.content == "⚫":
                b_score += 1
        self.score_black = b_score
        self.score_white = w_score

    # Check for a valid move, and end the game if there is none for the current player
    def check_for_valid_moves(self, board_instance):
        is_game_over = True
        for tile_index in board_instance.board:
            move_to_check = board_instance.is_legal_move(
                tile_index.x_pos, tile_index.y_pos, self.active_player)
            if move_to_check != False:
                is_game_over = False

        if is_game_over:
            self.check_for_winner()
            self.is_game_over = True

    # Compare the score, and print the winner's color
    def check_for_winner(self):
        print("Partie terminée !")
        print("Le joueur noir a: " + str(self.score_black) + " points")
        print("Le joueur white a: " + str(self.score_white) + " points")
        if (self.score_black > self.score_white):
            print("Le joueur noir a gagné !")
            self.winner = "⚫"
        elif (self.score_white > self.score_black):
            print("Le joueur blanc a gagné !")
            self.winner = "⚪"
        else:
            print("Égalité !")

class Bot:
    def __init__(self, learning_rate=0.4, discount_factor=0.9, exploration_rate=0.01):
        self.name = "Xx_Bender_Destroyer_3.0_xX"
        self.q_values = {}  # Q-values for state-action pairs
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate

    # BOT FUNCTIONS

    def state_key(self, base_board, base_game):
        key = (tuple(tile.content for tile in base_board.board), base_game.active_player)
        return key

    def update_q_values(self, state_key, action, reward, next_state_key):
        q_values = self.q_values.get(state_key, {})
        next_q_values = self.q_values.get(next_state_key, {})

        current_q = q_values.get(action, 0)
        max_future_q = max(next_q_values.values(), default=0)

        new_q = current_q + self.learning_rate * (reward + self.discount_factor * max_future_q - current_q)
        q_values[action] = new_q

        self.q_values[state_key] = q_values

    def choose_action(self, valid_moves, othello_board, othello_game):
        # Epsilon-greedy strategy for exploration
        if random.uniform(0, 1) < self.exploration_rate:
            return random.choice(valid_moves) if valid_moves else None
        else:
            # Choose the action with the highest Q-value or a random action if no Q-values are available
            state_key = self.state_key(othello_board, othello_game)
            q_values = self.q_values.get(state_key, {})

            if not q_values:
                # If no Q-values are available, choose a random action
                return random.choice(valid_moves) if valid_moves else None

            max_action = max(q_values, key=q_values.get, default=random.choice(valid_moves))

            # Ensure the action is always a tuple
            return max_action if isinstance(max_action, tuple) else (max_action,)

    def learn_and_play(self, othello_board, othello_game):
        state_key = self.state_key(othello_board, othello_game)
        valid_moves = self.check_valid_moves(othello_board, othello_game)
        action = self.choose_action(valid_moves, othello_board, othello_game)

        # Print the action to help debug
        print("Action:", action)

        # Ensure action is a tuple
        if not isinstance(action, tuple):
            action = (action, 0)  # Assuming 0 as the second element, you can modify as needed

        # Store current scores
        self.last_black_score = othello_game.score_black
        self.last_white_score = othello_game.score_white

        # Print the action just before calling place_pawn
        print("Before place_pawn, action:", action)
        

        othello_game.place_pawn(action[0], action[1], othello_board, othello_game.active_player)
        reward = self.get_reward(othello_board, othello_game)
        next_state_key = self.state_key(othello_board, othello_game)

        self.update_q_values(state_key, action, reward, next_state_key)

    def check_valid_moves(self, base_board, base_game):
        valid_moves = []
        new_board = Board(8)
        new_board.create_board()
        bonus_matrix = [100, -10, 11, 6, 6, 11, -10, 100,
                        -10, -20, 1, 2, 2, 1, -20, -10,
                        10, 1, 5, 4, 4, 5, 1, 10,
                        6, 2, 4, 2, 2, 4, 2, 6,
                        6, 2, 4, 2, 2, 4, 2, 6,
                        10, 1, 5, 4, 4, 5, 1, 10,
                        -10, -20, 1, 2, 2, 1, -20, -10,
                        100, -10, 11, 6, 6, 11, -10, 100]

        for tile_index in base_board.board:
            move_to_check = base_board.is_legal_move(tile_index.x_pos, tile_index.y_pos, base_game.active_player)
            if move_to_check:
                valid_moves.append((tile_index.x_pos, tile_index.y_pos))

        # Update weights of valid moves based on the bonus matrix
        valid_moves_with_weights = [(move[0], move[1], bonus_matrix[move[0] + move[1] * 8]) for move in valid_moves]

        return valid_moves_with_weights

        # if len(best_coordinates) > 1:

        #     for coordinates in best_coordinates:
        #         # print(coordinates)
        #         if coordinates[0] == 0 or coordinates[1] == 0 or coordinates[0] == (len(base_board.board) - 1) or coordinates[1] == (len(base_board.board) - 1):
        #             best_coordinates_on_border = (coordinates[0],coordinates[1])
        #             print("J'ai un coup en border")
        #             return best_coordinates_on_border
        #     print("1")
        #     print(best_coordinates)
        #     return random.choice(best_coordinates)
        # print("2")
        # print(best_coordinates)
        # best_coordinates = (best_coordinates[0])
        # return best_coordinates
    
    def get_reward(self, base_board, base_game):
        # Check if the game is over and provide a reward based on the outcome
        if base_game.is_game_over:
            if base_game.winner == self.name:
                return 10  # High positive reward for winning
            else:
                return -10  # High negative reward for losing

        # Calculate the change in scores
        black_score_change = base_game.score_black - self.last_black_score
        white_score_change = base_game.score_white - self.last_white_score

        # Provide a reward based on score changes
        reward = black_score_change - white_score_change

        return reward
    
class OtherBot:
    def __init__(self):
        self.name = "Xx_Bender_Destroyer_1.0_xX"

    # BOT FUNCTIONS

    def check_valid_moves(self, base_board, base_game):

        number_of_flip = 0
        biggest_number_of_flip = 0
        valid_moves = []
        best_coordinates = []
        best_coordinates_on_border = []
        check_valid = []

        for tile_index in base_board.board:
            move_to_check = base_board.is_legal_move(tile_index.x_pos, tile_index.y_pos, base_game.active_player)
            if move_to_check:
                check_valid.append(move_to_check)
                # print(check_valid)
                for move_to_check_index in range(len(move_to_check)):
                    number_of_flip = 0
                    number_of_flip += move_to_check[move_to_check_index][0]
                    
                    if number_of_flip > biggest_number_of_flip:
                        biggest_number_of_flip = number_of_flip
                        best_coordinates = [(tile_index.x_pos, tile_index.y_pos)]
                        # print(best_coordinates)
                    elif number_of_flip == biggest_number_of_flip:
                        best_coordinates.append((tile_index.x_pos, tile_index.y_pos))
                        
                
                
        # print(biggest_number_of_flip)
        # print(best_coordinates)
        
                        
        if len(best_coordinates) > 1:

            for coordinates in best_coordinates:
                # print(coordinates)
                if coordinates[0] == 0 or coordinates[1] == 0 or coordinates[0] == (len(base_board.board) - 1) or coordinates[1] == (len(base_board.board) - 1):
                    best_coordinates_on_border = (coordinates[0],coordinates[1])
                    # print("J'ai un coup en border")
                    return best_coordinates_on_border
            return random.choice(best_coordinates)
        
        best_coordinates = (best_coordinates[0])
        return best_coordinates          


def play_games(number_of_games):
    white_victories = 0
    black_victories = 0
    
    for current_game in range(number_of_games):
        # Create a new board & a new game instances
        othello_board = Board(8)
        othello_game = Game()

        # Fill the board with tiles
        othello_board.create_board()

        # Draw the board
        othello_board.draw_board("Content")

        # Create 2 bots
        myBot = Bot()
        otherBot = OtherBot()

        # Loop until the game is over


        while not othello_game.is_game_over:
            # First player / bot logic goes here
            if (othello_game.active_player == "⚫"):
                myBot.learn_and_play(othello_board, othello_game)

            # Second player / bot logic goes here
            else:
                move_coordinates = otherBot.check_valid_moves(othello_board, othello_game)
                othello_game.place_pawn(move_coordinates[0], move_coordinates[1], othello_board, othello_game.active_player)
    
        if(othello_game.winner == "⚫"):
            black_victories += 1
        elif(othello_game.winner == "⚪"):
            white_victories += 1
        
    
    print("End of the games, showing scores: ")
    print("Black player won " + str(black_victories) + " times")
    print("White player won " + str(white_victories) + " times")
        

play_games(150)