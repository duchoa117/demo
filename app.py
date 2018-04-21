from flask import*
from gmail import GMail, Message
import os # operating system
import mlab
from  werkzeug.utils import secure_filename
from models.picture_caption import *
mlab.connect()

app = Flask(__name__)
UPLOAD_FOLDER = "static/media/"

ALLOWED_EXTENSIONS = set(['txt', 'jpg','png', 'jpeg', 'gif', 'pdf' ])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_filed(filename):
    check_1 = "." in filename
    check_2 = filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    return check_1 and check_2
# finish mission:
@app.route("/")
def index():
    return "aasd"
@app.route('/finish', methods = ["GET", "POST"])
def finish():
    if request.method == "GET":
        return render_template('finish.html')
    elif request.method == "POST":
        form = request.form
        caption = form["caption"]
        file = request.files["picture"]
        file_name = file.filename
        print(file_name)
        if file  and allowed_filed(file_name):
            file_name = secure_filename(file_name)

            file.save(os.path.join(app.config["UPLOAD_FOLDER"], file_name))
            new_pictur_caption = Picture_caption(
            caption = caption,
            picture = file_name,
            username = "hòa"
            )
            new_pictur_caption.save()
            # picture_link = "../static/media/" + file_name
        mission = """
            <h3><strong>N&agrave;y người anh h&ugrave;ng <img src="https://html-online.com/editor/tinymce4_6_5/plugins/emoticons/img/smiley-kiss.gif" alt="kiss" />, nhiệm vụ tiếp theo của bạn l&agrave; :</strong></h3>
<h3 style="text-align: center;"><strong>"{{..}}"</strong></h3>
<p><span style="color: #0000ff;"><strong>Ch&uacute;c bạn th&agrave;nh c&ocirc;ng =))</strong></span></p>
                """
        gmail = GMail('duchoapc99techkids@gmail.com', 'duchoa119')
        message = Message("This is your MISSION",to = "duchoapc99@gmail.com", html= mission)
        gmail.send(message)
        return redirect(url_for("share", username = "Hòa", day = 1, caption = caption, picture = file_name))
        # return render_template("share.html",link_share = )
    # return redirect("share",picture_link = picture_link)
# @app.route("/share/<caption>/<picture_link>")
# def share(caption,picture_link):
# @app.route('/Congratulations/<user>/<day>/<caption>/<picture>')
# @app.route("/share/<username>/<day>/<caption>/<picture>")
@app.route("/share/<username>/<day>/<caption>/<picture>")
def share(username,day,caption,picture):
    print(picture)
    return render_template("share.html",username = username, day = day, caption = caption, picture = picture)


if __name__ == '__main__':
  app.run( debug=True)
