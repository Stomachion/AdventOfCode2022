import sys

def read_txt_list(txt_file_name):
    txt_file = open(txt_file_name, "r")
    
    txt_list = []
    for line in txt_file:
        txt_list.append(line.rstrip())
    
    txt_file.close()
    return txt_list 


def interprete_RPS_strategy(RPS_strategy):
    for i in range(len(RPS_strategy)):   
        RPS_strategy[i] = RPS_strategy[i].replace("A", "R")
        RPS_strategy[i] = RPS_strategy[i].replace("B", "P")
        RPS_strategy[i] = RPS_strategy[i].replace("C", "S")
        RPS_strategy[i] = RPS_strategy[i].replace("X", "R")
        RPS_strategy[i] = RPS_strategy[i].replace("Y", "P")
        RPS_strategy[i] = RPS_strategy[i].replace("Z", "S")


def decode_RPS_strategy(RPS_strategy):
    for i in range(len(RPS_strategy)):   
        RPS_strategy[i] = RPS_strategy[i].replace("A", "R")
        RPS_strategy[i] = RPS_strategy[i].replace("B", "P")
        RPS_strategy[i] = RPS_strategy[i].replace("C", "S")

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


# Defining main function
def main():
    
    RPS_strategy_file = str(sys.argv[1])
    RPS_strategy = read_txt_list(RPS_strategy_file)
    decode_RPS_strategy(RPS_strategy)

    shape_score =compute_shape_score(RPS_strategy)
    game_score = compute_games_score(RPS_strategy)
    total_score = shape_score + game_score

    print("Your score", shape_score, " + " , game_score, " = ", total_score)


# main
if __name__=="__main__":
    main()