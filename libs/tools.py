from random import choice

def return_new_game_code(code_length=6):
   game_code=''
   game_code = ''.join(choice('ABCDEFABCDEFABCDEF0123456789') for _ in range(code_length))
   return game_code

def process_command(received_data):
   #possible targets : all, sender, others
   response={
      'target_socket':'sender',
      'data':'server_data'
   }
   return(response)