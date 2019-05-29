from flask import Flask, render_template, request
import line
import weather



app = Flask(__name__)

# http://127.0.0.1:5000をルートとして、("")の中でアクセスポイント指定
# @app.route("hoge")などで指定すると、http://127.0.0.1:5000/hogeでの動作を記述できる。
@app.route("/", methods = ["POST"])
def hello():
    name = '{}'.format(request.form["name"])
    return render_template('hello.html', title = 'flask test', name = name)

@app.route("/answer", methods = ["GET", "POST"])
def answer():
    if request.method == "GET":
        return """
        下に整数を入力してください。奇数か偶数か判定します
        <form action="/answer" method="POST">
        <input name="num"></input>
        </form>"""
    else:
        return """
        {}は{}です！""".format(str(request.form["num"]), ["偶数", "奇数"][int(request.form["num"]) % 2])

@app.route("/hi", methods = ["GET", "POST"])
def hi():
    if  request.method == "GET":
        return """
        下にメッセージを入力してください。Line notifyにて送信します。
        <form action="/hi" method = "POST">
        <input name="mes"></input>
        </form>
        """
        line.message(request.form["mes"])

    else:
        line.message(request.form["mes"])
        return 'メッセージ「{}」が送信されました'.format(request.form["mes"])

@app.route("/what_is_weather_today", methods = ["GET", "POST"])
def weather_today():
    weather.main()
    return 'Line notifyにより本日の天気が送信されました'


if __name__ == "__main__":
    # webサーバー立ち上げ
    app.run(debug = True, port = 5000)
