from config import *
import user
from flask import Flask, render_template,request, send_file


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",refresh=WEBSERVER_REFRESH,hide_code="",stylesheet="style.css")


@app.route("/api/proxy")
def api_proxy():
        return user.get_recent(USER)

@app.route("/embed")
def embed():
    hide_code="<script>\n"
    hide_buttons = request.args.get("hide_buttons")
    if hide_buttons==None:
        pass
    else:
        hide_code +="hideButtons()\n"
    dark_mode = request.args.get("dark_mode")
    if dark_mode==None:
        pass
    else:
        hide_code+="toggleDarkMode()\n"
    hide_code+="</script>"
    return render_template("index.html",refresh=WEBSERVER_REFRESH,hide_code=hide_code,stylesheet="embed.css")

@app.route("/style/style.css")
def style():
    return send_file("templates/style.css")

@app.route("/style/embed.css")
def embed_style():
    return send_file("templates/embed.css")

@app.route("/script/index.js")
def js():
    return send_file("templates/index.js")


if __name__ == "__main__":
    app.run(port=port,debug=debug)