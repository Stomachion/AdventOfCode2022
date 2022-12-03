import sys

def read_txt_list(txt_file_name):
    txt_file = open(txt_file_name, "r")
    
    txt_list = []
    for line in txt_file:
        txt_list.append(line.rstrip())
    
    txt_file.close()
    return txt_list 


def translate_strategy(strategy, trans_dict ):
    trans_strategy = []
    for game in strategy:
        mytable = game.maketrans(trans_dict)
        trans_strategy.append(game.translate(mytable))
    return trans_strategy
    

def decode_RPS_strategy(RPS_strategy):
    for i in range(len(RPS_strategy)):   

        if RPS_strategy[i][2] == "X":
            if RPS_strategy[i][0] == "R":
               RPS_strategy[i] = RPS_strategy[i].replace("X", "S")
            elif RPS_strategy[i][0] == "P":
                             RPS_strategy[i] = RPS_strategy[i].replace("X", "R")
            elif RPS_strategy[i][0] == "S":
               RPS_strategy[i] = RPS_strategy[i].replace("X", "P")
        
        elif RPS_strategy[i][2] == "Y":
            RPS_strategy[i] = RPS_strategy[i].replace("Y", RPS_strategy[i][0])
        
        elif RPS_strategy[i][2] == "Z":
            if RPS_strategy[i][0] == "R":
               RPS_strategy[i] = RPS_strategy[i].replace("Z", "P")
            elif RPS_strategy[i][0] == "P":
                             RPS_strategy[i] = RPS_strategy[i].replace("Z", "S")
            elif RPS_strategy[i][0] == "S":
               RPS_strategy[i] = RPS_strategy[i].replace("Z", "R")


def compute_shape_score(RPS_games):
    
    shape_scoure = int(0)
    
    for game in RPS_games:
        if game[2] == "R":
            shape_scoure += 1
        elif game[2] == "P":
            shape_scoure += 2
        elif game[2] == "S":
            shape_scoure += 3

    return shape_scoure


def compute_games_score(RPS_games):
    games_score = int(0)

    for game in RPS_games:
        if game[0] == game[2]:
            games_score += 3
        elif game[0] == "R":
            if game[2] == "P":
                games_score += 6
        elif game[0] == "P":
            if game[2] == "S":
                games_score += 6
        elif game[0] == "S":
            if game[2] == "R":
                games_score += 6

    return games_score


def compute_score(strategy):
    shape_score =compute_shape_score(strategy)
    game_score = compute_games_score(strategy)
    return shape_score + game_score


# Defining main function
def main():
    
    RPS_strategy_file = str(sys.argv[1])
    RPS_strategy = read_txt_list(RPS_strategy_file)

    trans_dict_opponent = {'A':'R','B':'P','C':'S'}
    interpreted_strategy = translate_strategy(RPS_strategy, trans_dict_opponent)
    trans_dict_you = {'X':'R','Y':'P','Z':'S'}
    interpreted_strategy = translate_strategy(interpreted_strategy, trans_dict_you)
    print("Your score ", compute_score(interpreted_strategy))

    translate_strategy = interpreted_strategy = translate_strategy(RPS_strategy, trans_dict_opponent)


    #decode_RPS_strategy(RPS_strategy)



# main
if __name__=="__main__":
    main()