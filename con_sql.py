import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = '192.168.0.102,1433' 
database = 'nhom_6' 
username = 'sa' 
password = 'Nam06081998' 
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';Database='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()
cursor.execute("select * from SV where MaSv = 'Nam';")
l = [i for i in cursor]
print(l)