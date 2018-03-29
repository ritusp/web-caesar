from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
           <!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method="post">
      <label for="rot">Rotate by:</label><input type="number" name="rot" value="0">
      <textarea type="text" name="text">{0}</textarea>
      <input type="submit" value="Submit Query">
      </form>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    r=int(request.form["rot"])
    t=request.form["text"]
    rs=rotate_string(t,r)
    return form.format(rs)

@app.route("/")
def index():
    return form.format("")

app.run()