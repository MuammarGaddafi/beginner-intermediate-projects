class Player : 
    
    valid_symbols=[]
    def __init__ (self) :
      self.name=""
      self.symbol=""

    def choose_name(self) : 
       while True :
          self.name=input("entrer le nom qui contient seulement des caracteres : ")
          if self.name.isalpha() :
             print(f"votre nom alors est {self.name}")
             break
          print("invalide")
       
    def choose_symbol(self) :
      symbol_list=['X' , 'O']
      while True :
         if Player.valid_symbols != [] :
            symbol= set(symbol_list) - set(Player.valid_symbols)
            self.symbol=next(iter(symbol)) # it s for converting the character in the set to a char :  iter(my_set) creates an iterator over the set, next(...) grabs the first (and only) item, 
            print(f"votre symbol est {self.symbol} car l'autre est reservé ")
            break
         else :
            symbol=input(f"entrer un symbol dans {symbol_list} : ")
            if symbol.upper() in symbol_list :
               self.symbol=symbol.upper()
               print(f"votre symbole alors est {self.symbol}")
               Player.valid_symbols.append(self.symbol)
               break
            
            print("invalide")

class Menu : # we have main menu and end game menu, this class contains methods that controll what would be shown depending the case

   def display_main_menu(self) : # this would show the start game and quit game options
      menu_text= """
      welcome to my x o game! 
      1. start game 
      2. quit game 
      enter your choice
      """
      while True :
         choice=input(menu_text)
         if choice in ["1","2"] :
            break
         print("invalid entry")
      return choice # so the menu methods would return the appropriate choices then we would act depending on it in the game class


   def display_endgame_menu(self) : # this would show the restart game and quit game options
      menu_text= """
      Game over ! 
      1. restart game 
      2. quit game 
      enter your choice
      """
      while True :
         choice=input(menu_text)
         if choice in ["1","2"] :
            print("yes")
            break
         print("invalid entry")
      return choice

class Board : # this class would contain the board and the methods controlling it  
   def __init__(self):
      self.boardValues=["1","2","3","4","5","6","7","8","9"] # the board would be a list way easier to fill and control in this simple game, so the matrix there is an overkill
   
   def display_board(self) : # we would display it in the tic tac toe draw format
      print("+-----"*3 + "+")
      for i in range (0,9,3) :
         print("|  "+"  |  ".join(self.boardValues[i:i+3])+"  |")
         print("+-----"*3+"+")

   
   def isValid_move(self,entry) :
      return (self.boardValues[entry-1] not in ['X','O'] ) # it will return true or false, depending on it we will update the board
      
   def update_board(self,entry,thesymbol) :
         self.boardValues[entry-1]=thesymbol
   
   def reset_board (self) :
      self.boardValues=["1","2","3","4","5","6","7","8","9"]   


class Game : # this class is for the main module of the game and defining the game logic
   def __init__(self): # we would create attributes from every game main components
      self.players=[Player(),Player()] # we would create a players list 
      self.board=Board()
      self.menu=Menu()
      # so as we see it is a composition, because every thing related to the game object : all of them created for game object, so they are not independent they all are created in the game class
      self.current_player_index=0
   
   
   
   def start_game(self) :
      choice=self.menu.display_main_menu()
      if choice == "1" :
         self.set_players()
         self.play_game()
      else :
         self.quit_game()
   
   
   
   
   def play_game(self) : # this function is a loop that keeps our game working 
      while True : 
         self.play_turn() # this is a method to control the players turns to play, also with the display and the validation of a move
         winner , won = self.check_win() # unpacking check win returns
         if won == True : # to verify if someone has won 
            self.board.display_board() 
            print(f" {self.players[1-self.current_player_index].name} with symbol {winner} YOU HAVE WON THE GAME !!")
            print("-"*30)
            choice=self.menu.display_endgame_menu()
            if choice=="1" :
               self.restart_game() # this is a method to restart the game 
            else : 
               self.quit_game()
               break # to quit the loop
         elif self.check_draw() :
            print(" IT IS A DRAW !! ")
            print("-"*30)
            choice=self.menu.display_endgame_menu()
            if choice=="1" :
               self.restart_game() # this is a method to restart the game 
            else : 
               self.quit_game()
               break # to quit the loop   


   def set_players(self) :
      for number, element in  enumerate (self.players, start=1) :
         print(f" player{number} ")
         element.choose_name()
         element.choose_symbol()
         print('-'*30) # this is for making a barrier between entring the two players details for more clarity
   
   
   
   
   def quit_game(self) :
      print("thank you for visiting us")


   
   
   def play_turn(self) :
      current_player=self.players[self.current_player_index]
      self.board.display_board()
      position=int(input(f"player {current_player.name} with symbol {current_player.symbol} choose a position according to its number  "))
      # now the user would choose the position 
      while True :

         if str(position) not in self.board.boardValues or self.board.isValid_move(position)==False : 
            position=int(input("re entrez une position valide "))
            self.board.display_board()
         else : 
            self.board.update_board(position,current_player.symbol)
            break
      self.current_player_index=1-self.current_player_index

   
   
   
   def check_win(self) : 

      winning_combinations=[ [0,3,6] , [1,4,7] , [2,5,8] , [0,1,2] , [3,4,5] , [6,7,8] , [0,4,8] , [2,4,6] ] # we made those combinations based on indexes not the showed values of the board

      won=False
      winner=None
      for element in winning_combinations :
         if (self.board.boardValues[element[0]] == self.board.boardValues[element[1]] == self.board.boardValues[element[2]]) : # check if this combination elements has the same value
            won=True
            winner=self.board.boardValues[element[0]]
            break
      return(winner , won)

   
   
   
   
   def check_draw(self) : 
      winner , won = self.check_win() # we need the won attribute to make sure that no one has won
      carry_on=True
      for element in self.board.boardValues : 
         if element not in ['X' , 'O'] :
            return(False)
      if carry_on==True and won==False :
         return(True)




game=Game()
game.start_game()








       
      
    

