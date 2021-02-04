from flask import Flask, request, render_template, url_for
import sqlite3 
import smtplib
from flask_mail import Mail, Message



app = Flask(__name__, static_url_path='/static')  


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = "amena9729@gmail.com"
app.config['MAIL_PASSWORD'] = "*****************"
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail=Mail(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')    

@app.route('/requestor/')
def requestor():
    return render_template('request.html')


@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/user-signup')    
def signup():
    return render_template('user-signup.html')

@app.route('/useracc',methods = ['POST','GET'])
def useracc():
    if request.method == 'POST':
        try:
            name = request.form["name"]
            email = request.form["email"] 
            Number = request.form["Number"]
            age = request.form["age"] 
            Address = request.form["Address"]
            print(name)
            
            with sqlite3.connect("newdb.db") as conn:
                cur = conn.cursor()
                cur.execute('''INSERT INTO useracc (name,email,Number,age,Address)
                  VALUES (?,?,?,?,?)''',(name,email,Number,age,Address)) 
            print('insert executed')
            conn.commit()  
        except:
            conn.rollback()
        finally:
            return render_template('accountaccepted.html')    


@app.route('/userdash',methods = ['POST', 'GET'])
def addrec3():
   if request.method == 'POST':
       try:
           emailid = request.form['email']
           password = request.form['password']  
           with sqlite3.connect("newdb.db") as conn:
               cur = conn.cursor()
               cur.execute(''' INSERT INTO user_login (mail,password) VALUES (?,?)''',(emailid,password)) 
               print('insert executed')
               conn.commit()

       except:
           conn.rollback()
       finally:
           return render_template('user-dash.html')

         
@app.route('/userdash')
def user_dash():
    return render_template('user-dash.html')    

@app.route('/userdon',methods = ['POST', 'GET'])
def addrec4():
   if request.method == 'POST':
       try:
           donorname = request.form.get['name']
           donoremail = request.form.get['email']
           donornumber = request.form.get['no']
           donoraddress = request.form.get['addr']
           donatingmedicine = request.form.get['medname']
           donatinggenericname = request.form.get['Gename']
           donatingquantity = request.form.get['quantity']
           recieversmail  = request.form.get['recmail']
           with sqlite3.connect("newdb.db") as conn:
               cur = conn.cursor()            
               cur.execute(''' INSERT INTO donation (name,email,num, addr, med, gen, quantity, reciever)
                VALUES (?,?,?,?,?,?,?,?)''', (donorname,donoremail,donornumber,donoraddress,donatingmedicine,donatinggenericname,donatingquantity,recieversmail))    
               print('inserted')
               conn.commit()
       except:
           conn.rollback()
       finally:
           return render_template('user-dash.html')       


@app.route('/ngo-dlist')
def ngodlist():
    return render_template('ngo-dlist.html') 

@app.route('/exec')
def exec():
    return render_template('exec.html')        

#SHOW THE LIST OF REQUEST
@app.route('/don-list')
def list():
   conn = sqlite3.connect("newdb.db")
   conn.row_factory = sqlite3.Row
   
   cur = conn.cursor()
   cur.execute("select * FROM req")
  
   rows = cur.fetchall()
   conn.close()
   
   return render_template("list.html",rows = rows)  

 
@app.route('/user-don')
def user_don():
    return render_template('user-don.html')

@app.route('/reg-ngo')
def reg_ngo():
    return render_template('reg-ngo.html')    

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
       try:
         n = request.form['name']
         e = request.form['email']
         no = request.form['no']
         a = request.form['addr']
         med = request.form['medname']
         gen = request.form['Gename']
         q = request.form['quantity']
         
         with sqlite3.connect("newdb.db") as conn:
            cur = conn.cursor()
         
            
            cur.execute('''INSERT INTO req (name,email,num, addr, med, gen, quantity) 
               VALUES (?,?,?,?,?,?,?)''',(n,e,no,a,med,gen,q))    
            print('insert executed')
            conn.commit()

       except e:
           
           conn.rollback()
           e = "recorded unsuccessfully"
           print(e)
           #msg =e
      
       finally:
           return render_template('rec.html')
          
        
@app.route('/don-list')
def don_list():
    return render_template('list.html')    

@app.route('/ngo-req')
def ngo_req():
    return render_template('ngo-req.html')    


@app.route('/admin')
def admin():
    return render_template('admin.html')  

@app.route('/admindash',methods = ('GET','POST'))
def admindash():
    if request.method == 'POST':
        try:
            email = request.form['email']
            password = request.form['password']
            f = request.form['unsuccessfull']   
            
            with sqlite3.connect("newdb.db") as conn:
                cur = conn.cursor()
                cur.execute(''' INSERT INTO adminlogin (email,password) VALUES (?,?)''',(email,password)) 
                print('insert executed')
                conn.commit()

        except f:
           
           conn.rollback()
           f = "recorded unsuccessfully"
           print(f)
           #msg =e
      
        finally:
            return render_template('admin-dash.html')      

@app.route('/reg-ngos') 
def reg_ngos():
    return render_template('reg-ngos.html')                      

@app.route('/admin-donlist')
def admindon_list():
   conn = sqlite3.connect("newdb.db")
   conn.row_factory = sqlite3.Row
   
   cur = conn.cursor()
   cur.execute("select * FROM req")
  
   rows = cur.fetchall()
   conn.close()
   
   return render_template("admin_donlist.html",rows = rows) 

@app.route('/ngoadding')
def add_ngo():
    return render_template('add_ngo.html')

@app.route('/add_ngo',methods=["POST","GET"])
def add_ngolist():
    if request.method == "POST":
        try:
            name = request.form['name']
            email = request.form['email']
            cnumber = request.form['no']
            adress = request.form['addr']

            with sqlite3.connect('newdb.db') as conn:
                cur = conn.cursor()
                cur.execute(''' INSERT INTO add_ngo (name,Email,Number,Address) VALUES (?,?,?,?)''',(name,email,cnumber,adress))
                conn.commit
        except:
            conn.rollback

        finally:
            return render_template("ngorec.html")               

    

@app.route('/user-list')
def user_list():
   conn = sqlite3.connect("newdb.db")
   conn.row_factory = sqlite3.Row
   
   cur = conn.cursor()
   cur.execute("select * FROM useracc")
  
   rows = cur.fetchall()
   conn.close()
   
   return render_template("user-list.html",rows = rows) 




if __name__ == "__main__":
    app.run(debug=True)   
