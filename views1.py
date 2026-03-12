import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
@app.route('/login', methods=['GET','POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "pass":
        logger.info("admin logged in successfully")
        return redirect(url_for('index'))
    else:
        logger.warning("Invalid login attempt")
        return render_template("login.html")
