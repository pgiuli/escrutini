from flask import Flask
from flask import render_template
import escons
import time

app = Flask(__name__)

@app.route('/') #Use template to display the list
def display_escons():
    diccionari, perc_escrutat = escons.get_escons()
    if diccionari == 'Error':
        return render_template('error.html', data=time.ctime())

    independencia = 'no'
    suma_indepe = 0

    suma_indepe += diccionari['CUP'] + diccionari['JUNTS+'] + diccionari['ERC']

    if suma_indepe > 68:
        independencia = 'sí'

    escons_list = [(k, int(v)) for k, v in diccionari.items()]
    escons_list = [item for item in escons_list if item[1] != 0]
    return render_template('index.html', llista=escons_list, independencia=independencia, data=time.ctime(), perc_escrutat=perc_escrutat)

if __name__ == '__main__':
    app.run(debug=True)