from flask import Flask
from flask_mail import Mail 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'enter some random passphrase' 
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io' 
app.config['MAIL_PORT'] = '465' # (or try 2525) 
app.config['MAIL_USERNAME'] = '26af7e7bab4e70' 
app.config['MAIL_PASSWORD'] = '58a2d5c17f1a0f' 
 
mail = Mail(app) 
from app import views