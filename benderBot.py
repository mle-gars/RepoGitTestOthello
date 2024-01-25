import random
from copy import deepcopy
import copy
import time

class Xx_Bender_Destroyer_30_xX:
    def __init__(self):
        self.name = "Xx_Bender_Destroyer_3.0_xX"
        

    def check_valid_moves(self, base_board, base_game, depth):
        
        cpt_tile = 0
        number_of_flip = 0
        biggest_number_of_flip = -21
        lowest_number_of_flip = 10
        valid_moves = []
        best_coordinates = []
        best_coordinates_on_border = []
        check_valid = []
        new_board = Board(8)
        new_board.create_board()
        current_part = 1
        best_move = []
        score = 0

        bonus_matrix_20_moins = [100, -10, 5, 2, 2, 5, -10, 100,
                                -10, -20, 2, 2, 2, 2, -20, -10,
                                5, 2, 1, 1, 1, 12, 2, 5,
                                2, 2, 1, 0, 0, 1, 2, 2,
                                2, 2, 1, 0, 0, 1, 2, 2,
                                5, 2, 2, 1, 1, 1, 2, 5,
                                -10, -20, 2, 2, 2, 2, -20, -10,
                                100, -10, 5, 2, 2, 5, -10, 100]
        
      
        bonus_matrix_20_plus = [100, -10, 5, 2, 2, 5, -10, 100,
                                -10, -20, 2, 2, 2, 2, -20, -10,
                                5, 2, 12, 10, 10, 12, 2, 5,
                                2, 2, 10, 0, 0, 10, 2, 2,
                                2, 2, 10, 0, 0, 10, 2, 2,
                                5, 2, 12, 10, 10, 12, 2, 5,
                                -10, -20, 2, 2, 2, 2, -20, -10,
                                100, -10, 5, 2, 2, 5, -10, 100]

  
        if current_part <= 20:
            bonus_matrix = bonus_matrix_20_moins
            
        else:
            bonus_matrix = bonus_matrix_20_moins
            
        for tile in range(len(new_board.board)):
            new_board.board[tile].weight = bonus_matrix[tile]
                
        current_part += 2
        
        
        

        # chibrax = self.minmax(2,base_board,base_game,True)
        
        # print(chibrax)
        
        for tile_index in base_board.board:
            move_to_check = base_board.is_legal_move(tile_index.x_pos, tile_index.y_pos, base_game.active_player)
            if move_to_check:
                valid_moves.append(move_to_check)
                
                number_of_flip = 0
                
                for move_to_check_index in range(len(move_to_check)):
                    # print("score")
                    # print(move_to_check[move_to_check_index][0])
                    number_of_flip = number_of_flip + move_to_check[move_to_check_index][0]

                # print(new_board.board[cpt_tile].weight)
                number_of_flip += new_board.board[cpt_tile].weight
                

                    
                if number_of_flip > biggest_number_of_flip:
                    biggest_number_of_flip = number_of_flip
                    best_coordinates = [[tile_index.x_pos, tile_index.y_pos, biggest_number_of_flip]]
                elif number_of_flip == biggest_number_of_flip:
                    best_coordinates.append([tile_index.x_pos, tile_index.y_pos, biggest_number_of_flip])
                
                    
                
            cpt_tile += 1 
        if base_game.is_game_over:
            return None
        
        if depth >= 0:
            
            # Check if best_coordinates is not empty before trying to access its elements
            if best_coordinates:
                for best_coordinates_index in best_coordinates:
                    # print(best_coordinates)
                    temp_board = copy.deepcopy(base_board)
                    temp_game = copy.deepcopy(base_game)

                    temp_game.place_pawn(best_coordinates_index[0], best_coordinates_index[1], temp_board, temp_game.active_player)
                    if base_game.is_game_over:
                        break
                    # print(depth)
                    opponent_points = self.check_valid_moves(temp_board, temp_game, depth - 1)
                
                    # Check if opponent_points is not empty and has at least 3 elements before accessing its elements
                    # print('best coor')
                    # print(best_coordinates_index)
                    # print('best oppo')
                    # print(opponent_points)
                    if opponent_points:
                        
                        best_coordinates_index[2] -= opponent_points[2]
                        score = best_coordinates_index[2]
                           
                    best_move = max(best_coordinates, key=lambda x: x[2])
                    return [best_move[0],best_move[1],score]
        
        
        return best_coordinates[0]

                    
                    # print(best_move)

                
                # print(best_move)
        
        return best_move
    
    
    
    # def minmax(self, depth, board, game, maximizing_player):
    #     if depth == 0 or game.is_game_over:
    #         return self.evaluate_board(board, game), None

    #     valid_moves = self.get_valid_moves(board, game)
    #     best_move = None

    #     if maximizing_player:
    #         max_eval = float('-inf')

    #         for move in valid_moves:
    #             temp_board = copy.deepcopy(board)
    #             temp_game = copy.deepcopy(game)

    #             temp_game.place_pawn(move[0], move[1], temp_board, game.active_player)
    #             eval, _ = self.minmax(depth - 1, temp_board, temp_game, False)

    #             if eval > max_eval:
    #                 max_eval = eval
    #                 best_move = move

    #         return max_eval, best_move

    #     else:
    #         min_eval = float('inf')

    #         for move in valid_moves:
    #             temp_board = copy.deepcopy(board)
    #             temp_game = copy.deepcopy(game)

    #             temp_game.place_pawn(move[0], move[1], temp_board, game.active_player)
    #             eval, _ = self.minmax(depth - 1, temp_board, temp_game, True)

    #             if eval < min_eval:
    #                 min_eval = eval
    #                 best_move = move

    #         return min_eval, best_move

        
        
        
    # def get_valid_moves(self, board100, game100):
    #     valid_moves = []
    #     for tile_index in board100.board:
    #             move_to_check = board100.is_legal_move(tile_index.x_pos, tile_index.y_pos, game100.active_player)
    #             if move_to_check:
    #                 valid_moves.append([tile_index.x_pos, tile_index.y_pos])
    #     return valid_moves
    
    
    # def evaluate_board(self, board1000, game1000):
    #     return game1000.score_black - game1000.score_white



    benderBot = Xx_Bender_Destroyer_30_xX()



    move_coordinates = benderBot.check_valid_moves(othello_board, othello_game, 3)