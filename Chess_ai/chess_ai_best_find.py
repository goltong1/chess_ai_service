from random import*
import time
import copy
#chess engine for q learning ai
def move(board,piece,move_x,move_y):
    cordinate=find(board,piece)
    now_x=cordinate[0]
    now_y=cordinate[1]
    if move_x>7 or move_x<0 or move_y>7 or move_y<0:
        return -1
    if check(board,piece,now_x,now_y,move_x,move_y):
        piece=board[now_y][now_x]
        board[now_y][now_x]=32
        die_piece=board[move_y][move_x]
        if (piece>7 and piece<=15 and move_y==7) or (piece>15 and piece<24 and move_y==0):
            piece=piece*-1
        board[move_y][move_x]=piece
        return reward_calculation(die_piece)

    else:
        return -1
def reward_calculation(die_piece):
    if 7<die_piece and die_piece<24:
        return 1
    elif die_piece==1 or die_piece==6 or die_piece==25 or die_piece==30:
        return 3
    elif die_piece==2 or die_piece==5 or die_piece==26 or die_piece==29:
        return 3
    elif die_piece==0 or die_piece==7 or die_piece==24 or die_piece==31:
        return 5
    elif die_piece==3 or die_piece==27:
        return 9
    elif die_piece==4 or die_piece==28:
        return 1000
    else:
        return 0
def check(board,piece,now_x,now_y,move_x,move_y):
    if now_x==-1 or (now_x==move_x and now_y==move_y)or move_x>7 or move_y>7:
        return 0
    elif piece>7 and piece<=15:
        if board[now_y][now_x]>=0:
            return pawn_check(board,now_x,now_y,move_x,move_y,1) #블랙 1, 화이트 -1
        else:
            return queen_check(board,now_x,now_y,move_x,move_y,1)
    elif piece>15 and piece<24:
        if board[now_y][now_x]>=0:
            return pawn_check(board,now_x,now_y,move_x,move_y,-1)
        else:
            return queen_check(board,now_x,now_y,move_x,move_y,-1)
    elif piece==1 or piece==6:
        return knight_check(board,now_x,now_y,move_x,move_y,1)
    elif piece==25 or piece==30:
        return knight_check(board,now_x,now_y,move_x,move_y,-1)
    elif piece==2 or piece==5:
        return bishop_check(board,now_x,now_y,move_x,move_y,1)
    elif piece==26 or piece==29:
        return bishop_check(board,now_x,now_y,move_x,move_y,-1)
    elif piece==0 or piece==7:
        return rook_check(board,now_x,now_y,move_x,move_y,1)
    elif piece==24 or piece==31:
        return rook_check(board,now_x,now_y,move_x,move_y,-1)
    elif piece==3:
        return queen_check(board,now_x,now_y,move_x,move_y,1)
    elif piece==27:
        return queen_check(board,now_x,now_y,move_x,move_y,-1)
    elif piece==4:
        return king_check(board,now_x,now_y,move_x,move_y,1)
    elif piece==28:
        return king_check(board,now_x,now_y,move_x,move_y,-1)
    else:
        return 0
def pawn_check(board,now_x,now_y,move_x,move_y,WB): 
    if WB*(move_y-now_y)==1 and abs(move_x-now_x)==0 and board[move_y][move_x]>=32:
        return 1
    elif WB*(move_y-now_y)==1 and abs(move_x-now_x)==1:
        if WB==1:
            if board[move_y][move_x]>15 and board[move_y][move_x]<32:
                return 1
        else:
            if board[move_y][move_x]<16 and board[move_y][move_x]>=0:
                return 1
    elif move_y-now_y==2 and abs(move_x-now_x)==0 and board[move_y][move_x]>=32 and now_y==1 and board[move_y-1][move_x]>=32:
        return 1
    elif now_y-move_y==2 and abs(move_x-now_x)==0 and board[move_y][move_x]>=32 and now_y==6 and board[move_y+1][move_x]>=32:
        return 1
    else:
        return 0
def knight_check(board,now_x,now_y,move_x,move_y,WB):
    if (abs(move_y-now_y)==2 and abs(move_x-now_x)==1) or (abs(move_y-now_y)==1 and abs(move_x-now_x)==2):
        if board[move_y][move_x]>=32:
            return 1
        elif WB==1:
            if board[move_y][move_x]>15 and board[move_y][move_x]<32:
                return 1
        else:
            if board[move_y][move_x]<16 and board[move_y][move_x]>=0:
                return 1
    else:
        return 0

def bishop_check(board,now_x,now_y,move_x,move_y,WB):
    if abs(move_y-now_y)==abs(move_x-now_x):
        if board[move_y][move_x]==32 or (WB==1 and board[move_y][move_x]>15 and board[move_y][move_x]<32) or (WB==-1 and board[move_y][move_x]<16 and board[move_y][move_x]>=0):
            check_x=move_x
            check_y=move_y
            if move_x>now_x and move_y>now_y:
                check_x=move_x-1
                check_y=move_y-1
                while check_x!=now_x and check_y!=now_y:
                    if board[check_y][check_x]!=32:
                        break;
                    check_x=check_x-1
                    check_y=check_y-1
            elif move_x<now_x and move_y>now_y:
                check_x=move_x+1
                check_y=move_y-1
                while check_x!=now_x and check_y!=now_y:
                    if board[check_y][check_x]!=32:
                        break;
                    check_x=check_x+1
                    check_y=check_y-1
            elif move_x>now_x and move_y<now_y:
                check_x=move_x-1
                check_y=move_y+1
                while check_x!=now_x and check_y!=now_y:
                    if board[check_y][check_x]!=32:
                        break;
                    check_x=check_x-1
                    check_y=check_y+1
            elif move_x<now_x and move_y<now_y:
                check_x=move_x+1
                check_y=move_y+1
                while check_x!=now_x and check_y!=now_y:
                    if board[check_y][check_x]!=32:
                        break;
                    check_x=check_x+1
                    check_y=check_y+1
            if check_x==now_x and check_y==now_y:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0

def rook_check(board,now_x,now_y,move_x,move_y,WB):
    if (abs(move_y-now_y)>0 and abs(move_x-now_x)==0) or (abs(move_y-now_y)==0 and abs(move_x-now_x)>0) :
        if board[move_y][move_x]==32 or (WB==1 and board[move_y][move_x]>15 and board[move_y][move_x]<32) or (WB==-1 and board[move_y][move_x]<16 and board[move_y][move_x]>=0):
            check_x=move_x
            check_y=move_y
            if move_y-now_y>0:
                check_y=move_y-1
                while check_y!=now_y:
                    if board[check_y][check_x]!=32:
                        break;
                    check_y=check_y-1
                if check_y==now_y:
                    return 1
                else:
                    return 0
            elif move_y-now_y<0:
                check_y=move_y+1
                while check_y!=now_y:
                    if board[check_y][check_x]!=32:
                        break;
                    check_y=check_y+1
                if check_y==now_y:
                    return 1
                else:
                    return 0
            elif move_x-now_x>0:
                check_x=move_x-1
                while check_x!=now_x:
                    if board[check_y][check_x]!=32:
                        break;
                    check_x=check_x-1
                if check_x==now_x:
                    return 1
                else:
                    return 0
            elif move_x-now_x<0:
                check_x=move_x+1
                while check_x!=now_x:
                    if board[check_y][check_x]!=32:
                        break;
                    check_x=check_x+1
                if check_x==now_x:
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    else:
        return 0
            
def queen_check(board,now_x,now_y,move_x,move_y,WB):
    return rook_check(board,now_x,now_y,move_x,move_y,WB) or bishop_check(board,now_x,now_y,move_x,move_y,WB)
def king_check(board,now_x,now_y,move_x,move_y,WB):
    if board[move_y][move_x]==32 or (WB==1 and board[move_y][move_x]>15 and board[move_y][move_x]<32) or (WB==-1 and board[move_y][move_x]<16 and board[move_y][move_x]>=0):
        if (abs(move_x-now_x)==1 and abs(move_y-now_y)==1) or (abs(move_x-now_x)==1 and abs(move_y-now_y)==0) or (abs(move_x-now_x)==0 and abs(move_y-now_y)==1):
            return 1
        else:
            return 0
    else:
        return 0
def find(board,piece):
    result=[-1,-1]
    for y in range(0,8):
        for x in range(0,8):
            if abs(board[y][x])==piece:
                result[0]=x
                result[1]=y
                return result

    return result

def castling(board,king,rook):
    if find(board,king)[0]!=-1 and find(board,rook)[0]!=-1:
        cord_k=find(board,king)
        cord_r=find(board,rook)
        if king>15 and rook>15 and cord_k==[4,7] and (cord_r==[0,7] or cord_r==[7,7]):
            if cord_k[0]>cord_r[0]:
                side=1
                cord_chk=[0,7]
            else:
                side=0
                cord_chk=[7,7]
            while True:
                cord_chk[0]=int(cord_chk[0]+abs(cord_k[0]-cord_r[0])/(cord_k[0]-cord_r[0]))
                if board[cord_chk[1]][cord_chk[0]]<32:
                    if cord_chk==cord_k:
                        board[cord_k[1]][cord_k[0]]=32
                        board[cord_r[1]][cord_r[0]]=32
                        if side:
                            board[7][2]=king
                            board[7][3]=rook
                        else:
                            board[7][6]=king
                            board[7][5]=rook
                        return 1
                    break;

        elif king<16 and rook<16 and cord_k==[4,0] and (cord_r==[0,0] or cord_r==[7,0]):
            if cord_k[0]>cord_r[0]:
                side=1
                cord_chk=[0,0]
            else:
                side=0
                cord_chk=[7,0]
            while True:
                cord_chk[0]=int(cord_chk[0]+abs(cord_k[0]-cord_r[0])/(cord_k[0]-cord_r[0]))
                if board[cord_chk[1]][cord_chk[0]]<32:
                    if cord_chk==cord_k:
                        board[cord_k[1]][cord_k[0]]=32
                        board[cord_r[1]][cord_r[0]]=32
                        if side:
                            board[0][2]=king
                            board[0][3]=rook
                        else:
                            board[0][6]=king
                            board[0][5]=rook
                        return 1
                    break;

        else:
            return 0
    return 0
        
def piece_exist(board,x,y):
    if board[y][x]!=32:
        return abs(board[y][x])
    else:
        return -1
def read_field(board):
    field_index=[0,0,0,0]
    for y in range(0,8):
        for x in range(0,8):
            if board[y][x]!=32:
                field_index[int(y/2)]=field_index[int(y/2)]+1
    return field_index




def random_piece_move(board,piece):
    cases=[]
    now=find(board,abs(piece))
    for x in range(0,8):
        for y in range(0,8):
            if check(board,piece,now[0],now[1],x,y):
                cases.append([piece,x,y])
    return choice(cases)
def find_best_move(board,turn,n):
    if not(turn) and board==[
               [0,1,2,3,4,5,6,7],
               [8,9,10,11,12,13,14,15],
               [32,32,32,32,32,32,32,32],
               [32,32,32,32,32,32,32,32],
               [32,32,32,32,20,32,32,32],
               [32,32,32,32,32,32,32,32],
               [16,17,18,19,32,21,22,23],
               [24,25,26,27,28,29,30,31]]:
        return [12,4,3]
    if not(turn) and board==[
               [0,1,2,3,4,5,6,7],
               [8,9,10,11,12,13,14,15],
               [32,32,32,32,32,32,32,32],
               [32,32,32,32,32,32,32,32],
               [32,32,32,19,32,32,32,32],
               [32,32,32,32,32,32,32,32],
               [16,17,18,32,20,21,22,23],
               [24,25,26,27,28,29,30,31]]:
        return [11,3,3]
    if not(turn) and board==[
               [0,1,2,3,4,5,6,7],
               [8,9,10,11,32,13,14,15],
               [32,32,32,32,32,32,32,32],
               [32,32,32,32,12,32,32,32],
               [32,32,32,32,20,32,32,32],
               [32,32,32,32,32,30,32,32],
               [16,17,18,19,32,21,22,23],
               [24,25,26,27,28,29,32,31]]:
        return [1,2,2]
    if not(turn) and board==[
               [0,1,2,3,4,5,6,7],
               [8,9,10,32,12,13,14,15],
               [32,32,32,32,32,32,32,32],
               [32,32,32,11,32,32,32,32],
               [32,32,18,19,32,32,32,32],
               [32,32,32,32,32,32,32,32],
               [16,17,32,32,20,21,22,23],
               [24,25,26,27,28,29,30,31]]:
        return [12,4,2]
    if turn:
        piece_h=16
    else:
        piece_h=0
    cases=[]
    for piece in range(piece_h,piece_h+16):
        now=find(board,abs(piece))
        for x in range(0,8):
            if now[0]==-1:
                break;
            for y in range(0,8):
                if check(board,piece,now[0],now[1],x,y):
                    cases.append([piece,x,y])
    best=-10000
    bests=[]
    for case in cases:
        tmp_board=copy.deepcopy(board)
        reward=move(tmp_board,case[0],case[1],case[2])
        if turn and reward>4:
            return case
        if n<3:
            next_best=find_best_move(tmp_board,not(turn),n+1)
            reward=reward-move(tmp_board,next_best[0],next_best[1],next_best[2])
        if reward>best:
            best_index=case
            best=reward
            bests=[]
            bests.append(case)
        elif reward==best:
            bests.append(case)
    best_index=choice(bests)
    if n==1:
        print(best)
    return best_index
