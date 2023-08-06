# Importing Libraries 
import os
import time
import requests

# Range parameter
start = 884734153994440005004773979322597349785 # 30 percent
end = 1156960047531190775775473665268011918950 # 70 percent

# Telegram function for notification
def telegram_send(chat):
  bot_token = "6164636818:AAEgHAPXUbax8AOtMtMRDmr4a3nAhlrwB_U"
  bot_chat_id = "380163757"
  chat_message = 'https://api.telegram.org./bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id +'&text=' + chat # type: ignore
  response = requests.get(chat_message)
  return response.json() 

# Running a command function
def run(command):
    os.system(command)

# Path to file list of public key to check
cd = os.getcwd()
path = f"{cd}/pubkey.txt"

# Turn integer number into bitcoin hexadecimal
def int_to_hex(value):
    hex = format(value, '064x')
    return hex

# main function
def main():
    run('clear')
    range_start = int_to_hex(start)
    range_end = int_to_hex(end)
    command_to_execute = f'keyhunt -m bsgs -f {path} -t 1024 -r {range_start}:{range_end} -q -n 0x4000000000000 -k 16384 -B sequential -s 10 -S'
    run(command_to_execute)
    time.sleep(1)
  
# Run the main function  
if __name__ == '__main__':
    start = time.time()
    main()
    result = round(time.time() - start, 2) 
    telegram_send(f"RUN FINISHED!!!\n\nRange : {start} - {end}\n\nRuntime : {result} seconds")
