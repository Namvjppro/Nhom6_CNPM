from os import path
import time
from connect_Sql_Server import connectSQL
con = connectSQL()
print(con.read('select * from SV;'))
print(path.exists("ok2.pdf"))
from urllib import request
'''# Define the remote file to retrieve
remote_url = 'https://drive.google.com/uc?id=1fIsA7K9KxYqNFXxqLF8Q9qqIMauqhCWi&export=download'
            #https://drive.google.com/file/d/1fIsA7K9KxYqNFXxqLF8Q9qqIMauqhCWi/view?usp=sharing
url =  'https://drive.google.com/uc?id=1i-ESjrST4rn9zqEzbY16BZFzBZ_EDC_a&export=download'
# Define the local filename to save data
local_file = 'local_copy.yml'
# Download remote and save locally
request.urlretrieve(url, local_file)
print("ok")'''
start = time.time()



