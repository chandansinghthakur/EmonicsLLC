from flask import Flask, render_template, request, redirect, url_for, session
import pyodbc

app = Flask(__name__)
app.secret_key = 'Jaimatadi@12345' 

# Set up the SQL Server connection
server = 'EMNOI-NOT-072\SQLEXPRESS'
database = 'EmonicsLLC'
username = 'sa'
password = 'India@998#'
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

users = {'chandan1@emonics.com': 'password1', 'user2': 'password2'}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(CASE WHEN Emp_status='Live' THEN Emp_status END) AS Live_Employees,		COUNT(CASE WHEN Working_status='Home' THEN Working_status END) AS WFH,COUNT(CASE WHEN Working_status='Office' THEN Working_status END) AS WFO,COUNT(CASE WHEN Gender='Male' THEN Gender END) AS Male,COUNT(CASE WHEN Gender='Female' THEN Gender END) AS Female,COUNT(CASE WHEN Division = 'Healthcare' and Department='Support' THEN Division END) AS Healthcare_Support,COUNT(CASE WHEN Department = 'Recruiter' THEN Department END) AS Recruiter,COUNT(CASE WHEN Division = 'Healthcare' and Department = 'Recruiter' THEN Department END) AS Healthcare_Recruiter,COUNT(CASE WHEN Division not in ('Healthcare', 'Bench Sales') and Department = 'Recruiter' THEN Department END) AS SI_Recruiter,COUNT(CASE WHEN Division = 'Bench Sales' and Department = 'Recruiter' THEN Department END) AS Bench_Sales_Recruiter,COUNT(CASE WHEN Department = 'Account Manager' THEN Department END) AS Account_Manager,COUNT(CASE WHEN Division = 'Healthcare' and Department = 'Account Manager' THEN Department END) AS Healthcare_Account_Manager,COUNT(CASE WHEN Division not in ('Healthcare', 'Bench Sales') and Department = 'Account Manager' THEN Department END) AS SI_Account_Manager,COUNT(CASE WHEN Division = 'Bench Sales' and Department = 'Account Manager' THEN Department END) AS Bench_Account_Manager,COUNT(CASE WHEN Division = 'Bench Sales' THEN Division END) AS Bench_Sales,COUNT(CASE WHEN Department = 'Support' THEN Department END) AS Support,COUNT(CASE WHEN Division <> 'Healthcare' and Department='Support' THEN Division END) AS SI_Support FROM Employees where Emp_status='Live'")  # Replace YourTable with your actual table name
            rows = cursor.fetchall()
            return render_template('home1.html', data=rows)
        elif username in users and users[username] != password:
            return render_template('loginFailed.html')

        
    return render_template('loginPage.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/home1')
def home():
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(CASE WHEN Emp_status='Live' THEN Emp_status END) AS Live_Employees,		COUNT(CASE WHEN Working_status='Home' THEN Working_status END) AS WFH,COUNT(CASE WHEN Working_status='Office' THEN Working_status END) AS WFO,COUNT(CASE WHEN Gender='Male' THEN Gender END) AS Male,COUNT(CASE WHEN Gender='Female' THEN Gender END) AS Female,COUNT(CASE WHEN Division = 'Healthcare' and Department='Support' THEN Division END) AS Healthcare_Support,COUNT(CASE WHEN Department = 'Recruiter' THEN Department END) AS Recruiter,COUNT(CASE WHEN Division = 'Healthcare' and Department = 'Recruiter' THEN Department END) AS Healthcare_Recruiter,COUNT(CASE WHEN Division not in ('Healthcare', 'Bench Sales') and Department = 'Recruiter' THEN Department END) AS SI_Recruiter,COUNT(CASE WHEN Division = 'Bench Sales' and Department = 'Recruiter' THEN Department END) AS Bench_Sales_Recruiter,COUNT(CASE WHEN Department = 'Account Manager' THEN Department END) AS Account_Manager,COUNT(CASE WHEN Division = 'Healthcare' and Department = 'Account Manager' THEN Department END) AS Healthcare_Account_Manager,COUNT(CASE WHEN Division not in ('Healthcare', 'Bench Sales') and Department = 'Account Manager' THEN Department END) AS SI_Account_Manager,COUNT(CASE WHEN Division = 'Bench Sales' and Department = 'Account Manager' THEN Department END) AS Bench_Account_Manager,COUNT(CASE WHEN Division = 'Bench Sales' THEN Division END) AS Bench_Sales,COUNT(CASE WHEN Department = 'Support' THEN Department END) AS Support,COUNT(CASE WHEN Division <> 'Healthcare' and Department='Support' THEN Division END) AS SI_Support FROM Employees where Emp_status='Live'")  # Replace YourTable with your actual table name
    rows = cursor.fetchall()
    return render_template('home1.html', data=rows)

@app.route('/index')
def index():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Employees order by DOJ desc')  # Replace YourTable with your actual table name
    rows = cursor.fetchall()
    return render_template('index.html', data=rows)

@app.route('/about')
def about():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Employees where Emp_status='Live' order by DOJ desc")  # Replace YourTable with your actual table name
    rows = cursor.fetchall()
    return render_template('about.html',data=rows) 

@app.route('/summary')
def summary():
    cursor = conn.cursor()
    cursor.execute("SELECT DOJ,Emp_code, User_name, Reporting_manager, Designation, Division, Email_id, Primary_Extn_Number, Primary_Vonage_Number,Gender FROM Employees where Emp_status='Live' order by DOJ desc")  # Replace YourTable with your actual table name
    rows = cursor.fetchall()
    return render_template('summary.html',data=rows)


@app.route('/page1')
def page1():
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(CASE WHEN Emp_status='Live' THEN Emp_status END) AS Live_Employees,		COUNT(CASE WHEN Working_status='Home' THEN Working_status END) AS WFH,COUNT(CASE WHEN Working_status='Office' THEN Working_status END) AS WFO,COUNT(CASE WHEN Gender='Male' THEN Gender END) AS Male,COUNT(CASE WHEN Gender='Female' THEN Gender END) AS Female,COUNT(CASE WHEN Division = 'Healthcare' and Department='Support' THEN Division END) AS Healthcare_Support,COUNT(CASE WHEN Department = 'Recruiter' THEN Department END) AS Recruiter,COUNT(CASE WHEN Division = 'Healthcare' and Department = 'Recruiter' THEN Department END) AS Healthcare_Recruiter,COUNT(CASE WHEN Division not in ('Healthcare', 'Bench Sales') and Department = 'Recruiter' THEN Department END) AS SI_Recruiter,COUNT(CASE WHEN Division = 'Bench Sales' and Department = 'Recruiter' THEN Department END) AS Bench_Sales_Recruiter,COUNT(CASE WHEN Department = 'Account Manager' THEN Department END) AS Account_Manager,COUNT(CASE WHEN Division = 'Healthcare' and Department = 'Account Manager' THEN Department END) AS Healthcare_Account_Manager,COUNT(CASE WHEN Division not in ('Healthcare', 'Bench Sales') and Department = 'Account Manager' THEN Department END) AS SI_Account_Manager,COUNT(CASE WHEN Division = 'Bench Sales' and Department = 'Account Manager' THEN Department END) AS Bench_Account_Manager,COUNT(CASE WHEN Division = 'Bench Sales' THEN Division END) AS Bench_Sales,COUNT(CASE WHEN Department = 'Support' THEN Department END) AS Support,COUNT(CASE WHEN Division <> 'Healthcare' and Department='Support' THEN Division END) AS SI_Support FROM Employees where Emp_status='Live'")  # Replace YourTable with your actual table name
    rows = cursor.fetchall()
    return render_template('page1.html',data=rows)

@app.route('/sep')
def sep():
    cursor = conn.cursor()
    cursor.execute("SELECT DOJ,DOL, Emp_code, User_name, Reporting_manager, Designation, Division, Email_id, Primary_Extn_Number, Primary_Vonage_Number,Gender FROM Employees where Emp_status='Left' order by DOL desc")
    rows = cursor.fetchall()
    return render_template('sep.html', data=rows)

@app.route('/database_entry_form', methods=['GET', 'POST'])
def database_entry_form():
    if request.method == "POST":
        Emp_status = request.form['Emp_status']
        # Emp_status = [{'Emp_status':'Live'}, {'Emp_status':'Left'}]
        Working_status = request.form['Working_status']
        # Working_status = [{'Working_status': 'Office', 'Working_status':'Home'}]
        DOJ = request.form['DOJ']
        Emp_code = request.form['Emp_code']
        User_name = request.form['User_name']
        Reporting_manager = request.form['Reporting_manager']
        Division = request.form['Division']
        # Division = [{'Division':'SI'}, {'Division':'Healthcare'}, {'Division': 'Bench Sales'}]
        Designation = request.form['Designation']
        Email_id = request.form['Email_id']
        Assigned_ATS = request.form['Assigned_ATS']
        Primary_Extn_Number = request.form['Primary_Extn_Number']
        Primary_Vonage_Number = request.form['Primary_Vonage_Number']
        Department = request.form['Department']
        Personal_Number = request.form['Personal_Number']
        Personal_Email_ID = request.form['Personal_Email_ID']
        TEAM = request.form['TEAM']
        Super_Team = request.form['Super_Team']
        Gender = request.form['Gender']
        
        insert_query = '''INSERT INTO Employees (Emp_status,Working_status,DOJ,Emp_code,User_name,Reporting_manager,Division,Designation,Email_id,Assigned_ATS,Primary_Extn_Number,Primary_Vonage_Number,Department,Personal_Number,Personal_Email_ID,TEAM,Super_Team,Gender) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'''

        cursor = conn.cursor()
        cursor.execute(insert_query,(Emp_status,Working_status,DOJ,Emp_code,User_name,Reporting_manager,Division,Designation,Email_id,Assigned_ATS,Primary_Extn_Number,Primary_Vonage_Number,Department,Personal_Number,Personal_Email_ID,TEAM,Super_Team,Gender))
        conn.commit()
        return redirect(url_for('database_entry_form'))
    
    return render_template("database_entry_form.html")



@app.route('/update_status', methods=['GET', 'POST'])
def update_status():
    if request.method == "POST":
        Emp_status = request.form['Emp_status']
        DOL = request.form['DOL']
        Remark = request.form['Remark']
        Email_ID = request.form['Email_ID']
        Emp_code = request.form['Emp_code']

        cursor = conn.cursor()
        update_query = f"UPDATE employees SET Emp_status = ?, DOL = ?,Remark=?  WHERE (Email_ID = ? and Emp_code=?)"
        cursor.execute(update_query, (Emp_status, DOL, Remark, Email_ID,Emp_code))
        conn.commit()

    return render_template('update_status.html')






if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)
