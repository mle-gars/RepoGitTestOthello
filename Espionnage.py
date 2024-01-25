Nom du Bot : Babaaaa

Groupe 2

Hanane YAYA
Oumar SALL
Rama Jahel KIBEKE



# Classe du Bot

class Babaaa:
   
    def __init__(self):
        self.name = "Babaaaaa"


    def check_valid_moves_test(self, board, game,depth):
        matrice_list = [
            100, -25,  50,  50,  50,  50, -25, 100,
            -25, -50, -15, -15, -15, -15, -50, -25,
             50, -15,  10,  10,  10,  10, -15,  50,
             50, -15,  10, 'X', 'X',  10, -15,  50,
             50, -15,  10, 'X', 'X',  10, -15,  50,
             50, -15,  10,  10,  10,  10, -15,  50,
            -25, -50, -15, -15, -15, -15, -50, -25,
            100, -25,  50,  50,  50,  50, -25,  100
        ]
        newboard = deepcopy(board)
        matrice_list = self.initialize_matrix(newboard,matrice_list, game.active_player)
        max_points = -10000
        playable_moves = []
        final_max_point = 0
        points_per_move = []
        final_playable_moves = []
        turn = game.score_black + game.score_white - 4
        for index in range(len(board.board)):
            square_info = board.is_legal_move(board.board[index].x_pos, board.board[index].y_pos, game.active_player)
            if square_info != False:
                points_per_case = 0
                #ajout du poids en fonction de la case
                weight = newboard.board[index].content
                #On calcule le nombre de points en fonctions de la position et de la direction
                #square_direction /points_per_case /
                for square_direction in range(len(square_info)):
                    if(turn < 20):
                        points_per_case -= square_info[square_direction][0]
                    else:
                        points_per_case += square_info[square_direction][0]


                points_per_case += weight
                #On récupère le coup qui rapporte le maximum de points
                if max_points == points_per_case:
                    playable_moves.append([board.board[index].x_pos, board.board[index].y_pos,max_points])
                elif max_points < points_per_case:
                    max_points  = points_per_case
                    playable_moves = [[board.board[index].x_pos, board.board[index].y_pos,max_points]]
       
       
        if depth > 0:
            depth -=1
            playable_moves = self.best_moves(playable_moves, board, game, depth)
            # 2 list for the points / final moves
            # Get the points value and store them
            for move in playable_moves:
                points_per_move.append(move[2])
            # Check for the maximum value
            final_max_point = max(points_per_move)
            # Only fill the final list with the highest score moves
            for move in playable_moves:
                if(move[2] == final_max_point):
                    final_playable_moves.append(move)
            return random.choice(final_playable_moves)
        return random.choice(playable_moves)
   
    def best_moves(self,playable_moves, board, game, depth):
        for index in playable_moves:
            # Init copy board / game
            new_board = deepcopy(board)
            new_game = deepcopy(game)
            # Place pawn, recursive call for check_valid_moves
            #print(index)
            new_game.place_pawn(index[0], index[1], new_board, new_game.active_player)
            if new_game.is_game_over == False:
                opponent_points = self.check_valid_moves_test(new_board, new_game, depth)
            # Tile score update
                index.append(index[2]-opponent_points[2])
                index.pop(2)
        return playable_moves


    # function allow to initialize a bord with a matrix
    def initialize_matrix(self,table,matrice_list,color):
        if color == table.board[0].content :
            matrice_list[1] = 75
            matrice_list[8] = 75
        if color == table.board[7].content :
            matrice_list[6] = 75
            matrice_list[15] = 75
        if color == table.board[56].content :
            matrice_list[48] = 75
            matrice_list[57] = 75
        if color == table.board[63].content :
            matrice_list[55] = 75
            matrice_list[62] = 75
       
        if color == table.board[1].content:
            step = 1
            while matrice_list[step] != 100 and matrice_list[step+1]<len(matrice_list):
                if matrice_list[step] == 75 and color == table.board[step].content:
                    matrice_list[step+1] = 75
                step +=1
       
        if color == table.board[57].content:
            step = 57
            while matrice_list[step] != 100 and matrice_list[step+1]<len(matrice_list):
                if matrice_list[step] == 75 and color == table.board[step].content:
                    matrice_list[step+1] = 75
                step +=1
       
        #Pas de 8
               
        if color == table.board[8].content:
            step = 8
            while matrice_list[step+8] != 100 and matrice_list[step+1]<len(matrice_list):
                if matrice_list[step] == 75 and color == table.board[step].content:
                    matrice_list[step+8] = 75
                step +=8
       
        if color == table.board[15].content:
            step = 15
            while matrice_list[step+8] != 100 and matrice_list[step+1]<len(matrice_list):
                if matrice_list[step] == 75 and color == table.board[step].content:
                    matrice_list[step+8] = 75
                step +=8


        #Pas de -1
               
        if color == table.board[6].content:
            step = 6
            while matrice_list[step] != 100 and matrice_list[step+1]>0:
                if matrice_list[step] == 75 and color == table.board[step].content:
                    if step-1 >0:
                        matrice_list[step-1] = 75
                step -=1


        #Pas de -8
               
        if color == table.board[48].content:
            step = 48
            while matrice_list[step] != 100 and matrice_list[step+1]>0:
                if matrice_list[step] == 75 and color == table.board[step].content:
                    if step-8 >0:
                        matrice_list[step-8] = 75
                step -=8
       
        if color == table.board[55].content:
            step = 55
            while matrice_list[step] != 100 and matrice_list[step+1]>0:
                if matrice_list[step] == 75 and color == table.board[step].content:
                    if step-8 >0:
                        matrice_list[step-8] = 75
                step -=8


       
        for index in range(len(table.board)):                
            if table.board[index].content != 'X':
                table.board[index].content = matrice_list[index]
        return matrice_list





# Création du Bot

babaa = Babaaa()

# Exécution du Bot

move_coordinates = babaa.check_valid_moves_test(othello_board, othello_game, 2)

