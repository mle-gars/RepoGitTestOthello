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
        
        
        
        
        
        
        
        
        
        # elif number_of_flip == biggest_number_of_flip:
                #     best_coordinates.append((tile_index.x_pos, tile_index.y_pos))
        # print(biggest_number_of_flip)
        # print(best_coordinates)
                # print(best_coordinates)
                
                
                
                
                
                
                # print("cumule")
                # print(number_of_flip)
                # print(biggest_number_of_flip)
                # best_coordinates = [(tile_index.x_pos, tile_index.y_pos)]
                # if best_coordinates == [(2,2)] or best_coordinates == [(3,2)] or best_coordinates == [(4,2)] or best_coordinates == [(5,2)] or best_coordinates == [(2,3)] or best_coordinates == [(5,3)] or best_coordinates == [(2,4)] or best_coordinates == [(5,4)] or best_coordinates == [(2,5)] or best_coordinates == [(3,5)] or best_coordinates == [(4,5)] or best_coordinates == [(5,5)]:
                #     best_coordinates = best_coordinates[0]
                #     return best_coordinates
                
                
                
                
                
        for tile_index in base_board.board:
            move_to_check = base_board.is_legal_move(tile_index.x_pos, tile_index.y_pos, base_game.active_player)
            if move_to_check:
                check_valid.append(move_to_check)