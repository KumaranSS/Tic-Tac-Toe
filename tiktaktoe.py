#!/usr/bin/env python
# coding: utf-8

# In[4]:


from IPython.display import  clear_output

def display_board(board):
    
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print( '- - -')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print( '- - -')
    print(board[1]+'|'+board[2]+'|'+board[3])


# In[5]:


the_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(the_board)


# In[6]:


def player_input():
    marker = ''
    
    while not (marker=='X' or marker =='O'):
        marker =input('Enter X or O').upper()
    
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


# In[7]:


def marker(board,mark,position):
    board[position]=mark


# In[8]:


def win(board,mark):
   return ((board[1]==board[2]==board[3]==mark) or (board[4]==board[5]==board[6]==mark) or (board[7]==board[8]==board[9]==mark) or
    (board[7]==board[4]==board[1]==mark) or (board[8]==board[5]==board[2]==mark) or (board[9]==board[6]==board[3]==mark) or
    (board[1]==board[5]==board[9]==mark) or (board[3]==board[5]==board[7]==mark) )


# In[9]:


import random
def random_input():
    flip = random.randint(0,1)
    if flip==0:
        return 'Player 1'
    else :
        return 'Player 2'


# In[10]:


def space(board,position):
    return board[position]==''


# In[11]:


def full(board,position):
    for i in range(1,10):
        if space(board,i):
            return False
    return True


# In[12]:


def choose_input(board):
    position=0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space(board,position):
        position = int(input('Choose a position from 1 to 9'))
    return position


# In[13]:


def replay():
    
    choice = input("Want to play again? Yes:No")
    return choice=='Yes'


# In[ ]:


print("welcome to tic-tac-toe")
while True:
    
    the_board = ['']*10
    player1_marker,player2_marker=player_input()
    turn =random_input()
    print(turn + 'will go first')
    play_game = input('Enter Y or N')
    if play_game=='Y':
        game_mode=True
    else:
        game_mode=False
   
    while game_mode:
        
        if turn =='Player 1':
            display_board(the_board)
            position = choose_input(the_board)
            marker(the_board,player1_marker,position)
            
            if win(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 wins')
                game_mode=False
            else:
                if full(the_board,position):
                    display_board(the_board)
                    print('Tie game')
                    game_mode=False
                else:
                    turn='Player 2'
                    
        
        else :
            display_board(the_board)
            position = choose_input(the_board)
            marker(the_board,player2_marker,position)
            
            if win(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 wins')
                game_mode=False
            else:
                if full(the_board,position):
                    display_board(the_board)
                    print('Tie game')
                    game_mode=False
                else:
                    turn='Player 1'
                    
                    
    if not replay():
        break


# In[ ]:




