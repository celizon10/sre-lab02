from flask import Flask, render_template, json, request, redirect, session
# from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# app = Flask(__name__)
# mysql = MySQL(app)

# MySQL configurations
# app.config['MYSQL_DATABASE_USER'] = 'admin'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'adminpassword'  
# app.config['MYSQL_DATABASE_DB'] = 'BucketList'
# app.config['MYSQL_DATABASE_HOST'] = 'awslabproject.cj4geok6kpbh.us-east-2.rds.amazonaws.com'
# app.config['MYSQL_DATABASE_PORT'] = 3306
# mysql.init_app(app)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:adminpassword@awslabproject.cj4geok6kpbh.us-east-2.rds.amazonaws.com:3306/BucketList'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.secret_key = 'app secret key'



@app.route('/')
def main():
    return render_template('index.html')


@app.route('/signup')
def showSignUp():
    return render_template('signup.html')


@app.route('/signin')
def showSignin():
    return render_template('signin.html')


@app.route('/api/validateLogin', methods=['POST'])
def validateLogin():
    try:
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        
        user = User.query.filter_by(email=_email).first()
        
        if user:
            if user.password == _password:
                session['user'] = user.id
                return redirect('/userhome')
            else:
                return render_template('error.html', error='Wrong Email address or Password')
        else:
            return render_template('error.html', error='User not found')
    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/api/signup', methods=['POST'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:
            user = User.query.filter_by(email=_email).first()
            if user:
                return render_template('error.html', error='Email already exists')
            
            new_user = User(name=_name, email=_email, password=_password)
            db.session.add(new_user)
            db.session.commit()
            session['user'] = new_user.id
            return redirect('/userhome')
        else:
            return render_template('error.html', error='Enter all the required fields')

    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/userhome')
def userHome():
    if session.get('user'):
        return render_template('userhome.html')
    else:
        return render_template('error.html', error='Unauthorized Access')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)

# from flask import Flask, request

# app = Flask(__name__)

# stores = [
#     {
#         "name": "My Store",
#         "items": [
#             {
#             "name": "Chair",
#             "price": 15.99
#             }
#         ]
        
#     }
# ]


# @app.get('/store') # 'http://12.7.0.0.1:5000/store'
# def get_stores():
#     return {"stores": stores}

