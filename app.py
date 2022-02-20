from flask import Flask, request, render_template
import os


app = Flask(__name__)


@app.route('/search', methods=['GET', 'POST'])
def getData():
    print("request.method: "+request.method)
    if request.method == 'POST':
        adress = request.form.get('adress')
        filtr = 'mp4'
        list = getListVideoFiles(adress, filtr)
        return getTextHTML()+'<h1>Файлы из каталога: '+adress+'</h1>'+'<p>'+list+'</p>'
    
    #return 'Поломка!'

def getListVideoFiles(adress, filtr=''):
    #Ваш код на Python для отправления сообщений в Telegram через бота
    print(adress)
    #file_list = os.listdir()  # список файлов и папок в директории, где запущена программа
    #file_list = os.listdir('.')  # синоним
    #file_list = os.listdir(adress)  # список имен файлов и папок в данной папке
    strList = ''
    try:
        for file in os.scandir(adress):
        #for file in os.listdir(adress):
            if file.name.endswith(filtr):
                strList = strList + file.path +'<br />'
    except:
        Warning
        strList = 'Каталога с таким адрес не существует!'

    return strList

@app.route('/')
def mainPage():
    return render_template("html/index.html")#return getTextHTML()


def getTextHTML():
    return """
        <form method="POST" action="search">
            <h3>Это веб-форма</h3>
            
            <input type="text" name="adress" />
            <input type="text" name="filtr" value='mp4' />
            <br />

            <p class="send">
                <input type="submit" value="НАЙТИ ВИДЕО" />
            </p>
        </form>
        """


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()