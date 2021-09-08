import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
class connectSQL:
    def __init__(self):
        self.con = conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.0.102,1433;Database=nhom_6;UID=sa;PWD=Nam06081998')
        self.cursor = conn.cursor()
    def read (self,s):
        self.cursor.execute(s)
        l = [i for i in self.cursor]
        return l
    def insert(self,s):
        self.cursor.execute(s)
        self.con.commit()
    def update(self,s):
        self.cursor.execute(s)
        self.con.commit()
'''s = connectSQL()
x = s.read("select thoi_gian_online, Note from  Danh_Sach_Sv_learning where MaSV = '100';")
l = [i for i in x]
print(l[0][0])
print(l[0][1])'''
'''server = '192.168.0.102,1433' 
database = 'nhom_6' 
username = 'sa' 
password = 'Nam06081998' 
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';Database='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()
cursor.execute("select * from SV where MaSv = '10';")
l = [i for i in cursor]
print(l[0][0])'''
