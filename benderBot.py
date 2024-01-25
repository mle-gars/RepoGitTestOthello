import random
import csv
import json

class Xx_Bender_Destroyer_30_xX :
    def __init__(self):
        self.name = "Xx_Bender_Destroyer_3.0_xX"
        

    def check_valid_moves(self, base_board, base_game):
        
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


        bonus_matrix_20_moins = [100, -10, 5, 2, 2, 5, -10, 100,
                                -10, -20, 2, 2, 2, 2, -20, -10,
                                5, 2, 20, 15, 15, 20, 2, 5,
                                2, 2, 15, 0, 0, 15, 2, 2,
                                2, 2, 15, 0, 0, 15, 2, 2,
                                5, 2, 20, 15, 15, 20, 2, 5,
                                -10, -20, 2, 2, 2, 2, -20, -10,
                                100, -10, 5, 2, 2, 5, -10, 100]
        
      
        bonus_matrix_20_plus = [100, -20, 5, 2, 2, 5, -20, 100,
                                -20, -30, 2, 2, 2, 2, -30, -20,
                                5, 2, 2, 1, 1, 2, 2, 5,
                                2, 2, 1, 0, 0, 1, 2, 2,
                                2, 2, 1, 0, 0, 1, 2, 2,
                                5, 2, 2, 1, 1, 2, 2, 5,
                                -20, -30, 2, 2, 2, 2, -30, -20,
                                100, -20, 5, 2, 2, 5, -20, 100]

  
        if current_part <= 16:
            bonus_matrix = bonus_matrix_20_moins
            
        else:
            bonus_matrix = bonus_matrix_20_plus
            
        for tile in range(len(new_board.board)):
            new_board.board[tile].weight = bonus_matrix[tile]
                
        current_part += 1
        
        
        

        # chibrax = self.minmax(2,base_board,base_game,True)
        
        # print(chibrax)
        
        for tile_index in base_board.board:
            move_to_check = base_board.is_legal_move(tile_index.x_pos, tile_index.y_pos, base_game.active_player)
            if move_to_check:
                valid_moves.append(move_to_check)
                
                if (tile_index.x_pos, tile_index.y_pos) in [(0, 0), (0, 7), (7, 0), (7, 7)]:
                    return (tile_index.x_pos, tile_index.y_pos)
                
                
                # if current_part <= 10:
                #     if (tile_index.x_pos, tile_index.y_pos) in [(2, 3), (2, 4), (3, 2), (4, 2),(5, 3), (5, 4), (3, 5), (4, 5)]:
                #         return (tile_index.x_pos, tile_index.y_pos)
                
                # if (tile_index.x_pos, tile_index.y_pos) in [(6, 7), (7,7), (7, 6), (5, 7),(6,6),(7,5),(4,7),(5,6),(6,5),(7,4)]:
                #     return (tile_index.x_pos, tile_index.y_pos)
                    
                if (tile_index.x_pos, tile_index.y_pos) in [(2, 0), (3, 0), (4, 0), (5, 0), (0, 2), (0, 3),
                                                            (0, 4), (0, 5), (7, 2), (7, 3), (7, 4), (7, 5), (2, 7),
                                                            (3, 7), (4, 7), (5, 7)]:
                    return(tile_index.x_pos, tile_index.y_pos)
                
                
                number_of_flip = 0
                
                for move_to_check_index in range(len(move_to_check)):
                    # print("score")
                    # print(move_to_check[move_to_check_index][0])
                    number_of_flip = number_of_flip + move_to_check[move_to_check_index][0]

                # print(new_board.board[cpt_tile].weight)
                number_of_flip += new_board.board[cpt_tile].weight
                
                if current_part <= 6:
                    if number_of_flip < 2 and number_of_flip > 0:
                        return (tile_index.x_pos, tile_index.y_pos)
                        
                    
                if number_of_flip > biggest_number_of_flip:
                    biggest_number_of_flip = number_of_flip
                    best_coordinates = [[tile_index.x_pos, tile_index.y_pos, biggest_number_of_flip]]
                elif number_of_flip == biggest_number_of_flip:
                    best_coordinates.append([tile_index.x_pos, tile_index.y_pos, biggest_number_of_flip])

            
                
            cpt_tile += 1 

        best_coordinates = random.choices(best_coordinates)
        best_coordinates = best_coordinates[0]
        return best_coordinates
    



    benderBot = Xx_Bender_Destroyer_30_xX()



    move_coordinates = benderBot.check_valid_moves(othello_board, othello_game)