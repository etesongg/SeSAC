from flask import Flask, render_template
from flask import request, redirect, session, url_for, flash
from datetime import timedelta

app = Flask(__name__)

app.secret_key = "this_is_my_secrey_key"
app.permanent_session_lifetime = timedelta(minutes=1)

users = {
    'user1': {'password': 'password123'},
    'user2': {'password': 'abc123'}
}

@app.route('/')
def home():
    username = None
    if 'username' in session:
        username = session['username']
        flash("Login에 성공하였습니다.")
    
    return render_template('index.html', username=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # 더미 데이터베이스에서 사용자 정보를 확인
        if username in users and users[username]['password'] == password:
            # 로그인 성공한 경우 세션에 사용자 정보를 저장
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash("Login에 실패하였습니다.")
        
    return render_template('login.html')

@app.route('/logout')
def logout():
    # 세션에서 사용자 정보를 제거하여 로그아웃 처리
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

# 미션1. 랜더탬플릿 통해서 첫 화면에 login/logout 추가(부트스트랩 nav 통해서 메뉴에 login/logout)
# 로그인 성공실패 여부를 flash 메세지를 통해 처리
# 디자인 적용해서 flash 메시지 색상 다르게 해보기(성공시 초록, 실패시 빨강)
