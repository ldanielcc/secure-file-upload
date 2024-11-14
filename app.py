from flask import Flask, request, render_template, redirect, url_for, flash, session # type: ignore
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user # type: ignore
from flask_debugtoolbar import DebugToolbarExtension # type: ignore
from models.user_model import users, User
from werkzeug.utils import secure_filename # type: ignore
import os

app = Flask(__name__)
app.secret_key = 'my_super_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads/'
#app.debug = True
#toolbar = DebugToolbarExtension(app)

if not os.path.exists('uploads'):
    os.makedirs('uploads')

# Login Manager Configuration
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"  # Redirect to login page if user isn't authenticated
login_manager.session_protection = "strong"  # Optional: helps protect against session hijacking

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    # Ensure user_id is treated as a string and matches the dictionary keys
    user = users.get(user_id)
    print(f"Loading user from user_loader: {user_id} -> {user.username if user else 'None'}")
    return user


# Define allowed file extensions
ALLOWED_EXTENSIONS = {'txt', 'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Routes
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(f"Attempted login with username: {username}, password: {password}")

        if not username or not password:
            flash("Username and password are required")
            return render_template('login.html')

        # Check if the user exists and the password matches
        user = next((u for u in users.values() if u.username == username), None)
        
        if user and user.check_password(password):  # Assuming password hashing
            login_user(user, remember=True)
            print(f"User {user.username} logged in successfully.")
            print(f"Session user ID after login: {session.get('_user_id')}")
            return redirect(url_for('home'))
        else:
            flash("Invalid username or password")
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    if current_user.is_authenticated:
        print(f"User logged out: {current_user.username}")
    logout_user()
    session.clear()  # Clear all session data after logging out
    return redirect(url_for('login'))

@app.route('/')
@login_required
def home():
    print(f"Accessing home page, user: {current_user.username}, authenticated: {current_user.is_authenticated}")
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
@login_required
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(url_for('home'))

    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('home'))

    if not allowed_file(file.filename):
        flash('Invalid file type')
        return redirect(url_for('home'))

    # Secure the filename before saving
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    flash('File uploaded successfully')
    return redirect(url_for('home'))

# Run the Flask App
if __name__ == "__main__":
    app.run(debug=True)
