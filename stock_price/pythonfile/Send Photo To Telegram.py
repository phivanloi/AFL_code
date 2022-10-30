import requests
import glob
import os.path

folder_path = r'C:\\Program Files\\AmiBroker\\ExportedImages'
file_type = r'\*png'
files = glob.glob(folder_path + file_type)
max_file = max(files, key=os.path.getctime)
min_file = min(files, key=os.path.getctime)

files = {'photo': open(max_file, 'rb')}
         
TelegramAPI_ID = "1200942736:AAEG8y9qyJ7aHefUm4vt_xKqkNBxfKd3qCc";
TelgramCHAT_ID = "@Victor_AlgoTrading";

resp = requests.post("https://api.telegram.org/bot"+ TelegramAPI_ID + "/sendPhoto?chat_id="+TelgramCHAT_ID, files=files)

print(resp)
print(max_file)
print(min_file)
# print(os.path.getctime)