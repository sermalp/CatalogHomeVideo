from flask import Flask, request, render_template
import os


app = Flask(__name__)

@app.route('/search', methods=['GET', 'POST'])
def getData():
    if request.method == 'POST':
        dict_data = {}
        dict_data['adress'] = request.form.get('adress')
        dict_data['list_video'] = getListVideoFiles(dict_data['adress'], 'mp4')
        dict_data['title'] = 'Страница списка видео'
        return render_template("html/block_video.html", data=dict_data)


@app.route('/')
def mainPage():
    dict_data = {}
    dict_data['title'] = 'Страница списка видео'
    return render_template("html/index.html", data=dict_data)#return getTextHTML()


def getListVideoFiles(adress, filtr=''):
    #формирует список видео файлов в каталоге
    strList = []
    try:
        for file in os.scandir(adress):
            if file.name.endswith(filtr):
                dictVideoFile = {}
                dictVideoFile['path'] = file.path
                dictVideoFile['name'] = file.name
                strList.append(dictVideoFile)
                
    except:
        Warning('Каталога с адресом ('+adress+') не существует!')
        #strList = 'Каталога с адресом ('+adress+') не существует!'

    return strList


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