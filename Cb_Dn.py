import requests
import urllib.request

class Coub:
    def __init__(self):
        self.error = 'Error. Check internet connection and check coub.com link'

    def connect(self, url, formt):
        url = url.replace("https://coub.com/view/", "http://coub.com//api/v2/coubs/")
        data = requests.get(url).json()
        print("Started Download Of " + formt)
        return data

    def dl(self, directlink, fn):
        opener = urllib.request.build_opener()
        opener.addheaders = [("User-agent", "Mozilla/5.0")]
        dldata = opener.open(directlink)
        self.saveData(dldata, fn)

    def saveData(self, dldata, fn):
        if fn[-3:] == 'mp4':
            with open(fn, 'wb') as f:
                f.write(b'\x00\x00' + dldata.read()[2:])
        if fn[-3:] == 'mp3':
            with open(fn, 'wb') as f:
                f.write(dldata.read())

    def fileName(self, data, ftype, addlink):

        if addlink:
            fn = data["permalink"] + '.' + ftype
        else:
            fn = data["permalink"] + '.' + ftype

        if addlink == "no utf-8":
            fn = data["permalink"] + '.' + ftype
        return fn

    def video(self, url, addlink=True, audio=False):
        if audio:
            formt = "audio"
        else:
            formt = "video"
        try:
            data = self.connect(url, formt)
            try:
                directlink = data["file_versions"]["html5"][formt]["high"]["url"]
            except:
                directlink = data["file_versions"]["html5"][formt]["med"]["url"]
            fn = self.fileName(data, directlink[-3:], addlink)
            self.dl(directlink, fn)
        except:
            print(self.error)

    def audio(self, url, addlink=True):
        self.video(url, addlink, audio=True)







