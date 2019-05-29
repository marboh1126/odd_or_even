import requests

def message(mes):
    url = "https://notify-api.line.me/api/notify"
    token = '2NzIXwunO4od12fya0b02W1Hhx5qfrqwnUIyX0njjEk'
    headers = {"Authorization" : "Bearer "+ token}

    payload = {"message" :  mes}
    #files = {"imageFile": open("prof.jpg", "rb")} #バイナリで画像ファイルを開きます。対応している形式はPNG/JPEGです。

    r = requests.post(url ,headers = headers ,params=payload)

if __name__ == '__main__':
    massage()
