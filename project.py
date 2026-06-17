import pymysql

con=pymysql.connect(host='localhost',user='root',password='punitha',db='expenses')
def add():
     id=input('Enter id:')
     title=input('Enter title:')
     amount=input('Enter amount:')
     category=input('Enter category:')
     q="insert into details(id,title,amount,category)values(%s,%s,%s,%s)"
     cur=con.cursor()
     cur.execute(q,(id,title,amount,category))
     con.commit()
     cur.close()
     print("Added succcesfully")

def view():
     q=("select*from details")
     cur=con.cursor()
     cur.execute(q)
     r=cur.fetchall()
     for row in r:
          print(row)
        
               
def edit():
     id=input('Enter id:')
     amount=input('Enter new amount:')
     q="update details set amount=%s where id=%s"
     cur=con.cursor()
     cur.execute(q,(amount,id))
     con.commit()
     print ('updated succecfully')

def delete():
     id=input('Enter id:')
     q="delete from details where id=%s"
     cur=con.cursor()
     cur.execute(q,(id))
     con.commit()
     cur.close()
     print('Deleted sucsesfully')

def total():
     cur=con.cursor()
     cur.execute("select SUM(amount)from details")
     result=cur.fetchone()
     print("total expenses:",result[0])

while True:
     print('\n\ndashboard')
     print('1.insert\n2.view\n3.Edit\n4.delete\n5.total\n6.close')
     ch=input('Enter: ')
     if  ch.isdigit():
       ch=int(ch)
     if ch==1:
          print('\nadding')
          add()
     elif ch==2:
          print('\nviewing')

          view()
     elif ch==3:
          print('\n updating')
          edit()
     elif ch==4:
          print('\ndeleting')
          delete()
     elif ch==5:
          print('\ntotal')
          total()
     else:
          print('invalid ch')
