from flask import Flask, render_template, request, redirect, url_for

from flask_mail import Mail, Message

app = Flask(__name__)
# Looking to send emails in production? Check out our Email API/SMTP product!
app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '2b616fe31843d5'
app.config['MAIL_PASSWORD'] = '4efb03dc5e6c76'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mail', methods = ['GET', 'POST'])
def send_mail():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        msg = Message(
            'Hola Alejo,a tienes un nuevo contacto desde la web:',
            body=f'Nombre: {name} \nCorreo: <{email}>\n\nEscribio: \n\n{message}',
            sender=email,
            recipients=['alejomergen47@gmail.com']
        )
        mail.send(msg)
        return render_template('send_mail.html')
    
    return redirect(url_for('index'))