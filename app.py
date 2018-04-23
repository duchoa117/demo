from flask import*
from flask_mail import *
from gmail import *
import os # operating system
import mlab
import base64
from  werkzeug.utils import secure_filename
from models.classes import *
mlab.connect()

app = Flask(__name__)
app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'duchoapc99techkids@gmail.com',
    MAIL_PASSWORD = 'duchoa119',
))

mail = Mail(app)


ALLOWED_EXTENSIONS = set(['txt', 'jpg','png', 'jpeg', 'gif', 'pdf' ])

def allowed_filed(filename):
    check_1 = "." in filename
    check_2 = filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    return check_1 and check_2
# finish mission:*************
@app.route("/")
def index():

    mail = GMail(username="duchoapc99techkids@gmail.com", password="duchoa119")
    msg = Message("test",to= "duchoapc99@gmail.com", html="Test")
    mail.send(msg)
    return render_template("congratulation.html")

@app.route('/finish', methods = ["GET", "POST"])
def finish():
    if request.method == "GET":
        return render_template('finish.html')
    elif request.method == "POST":
        form = request.form
        caption = form["caption"]
        # file = request.files["picture"]***************
        image = request.files['image']
        image_name = image.filename
        image_bytes = base64.b64encode(image.read())
        image_string = image_bytes.decode()
        session["image"] = image_bytes
        if image  and allowed_filed(image_name):
            # file_name = "hoa"+"1."+ str(file_name.rsplit(".", 1)[1].lower())********
            # file.save(os.path.join(app.config["UPLOAD_FOLDER"], file_name))********
            mission_updated = UserMission.objects(user = session["user_id"], completed = False).first()
            mission_updated.update(set__caption = caption, set__image = image_string, completed = True)
            mission_updated.save()

#         mission = """
#             <h3><strong>N&agrave;y người anh h&ugrave;ng <img src="https://html-online.com/editor/tinymce4_6_5/plugins/emoticons/img/smiley-kiss.gif" alt="kiss" />, nhiệm vụ tiếp theo của bạn l&agrave; :</strong></h3>
# <h3 style="text-align: center;"><strong>"{{..}}"</strong></h3>
# <p><span style="color: #0000ff;"><strong>Ch&uacute;c bạn th&agrave;nh c&ocirc;ng =))</strong></span></p>
#                 """
#         app.config.update(dict(
#         DEBUG = True,
#         MAIL_SERVER = 'smtp.gmail.com',
#         MAIL_PORT = 587,
#         MAIL_USE_TLS = True,
#         MAIL_USE_SSL = False,
#         MAIL_USERNAME = 'duchoapc99techkids@gmail.com',
#         MAIL_PASSWORD = 'duchoa119',
#                             ))
#         msg = Message(mission, sender="duchoapc99techkids@gmail.com", recipients=["duchoapc99@gmail.com","quy.dc98@gmail.com"])
#         mail.send(msg)
        return redirect(url_for("share", username = UserMission(user = sessiom["user_id"]).user.username, day = 1, caption = caption, image_bytes = image_bytes))

@app.route("/share/<username>/<day>/<caption>")
def share(username,day,caption):
    image = session['image']
    print(picture)
    return render_template("share.html",username = username, day = day, caption = caption, image = image)

@app.route('/test')
def test():
    return "TEST ROUTER"


if __name__ == '__main__':
  app.run( debug=True)
