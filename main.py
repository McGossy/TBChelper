from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)


class SearchForm(FlaskForm):
    search = StringField('Search')
    submit = SubmitField('Search')


app.config['SECRET_KEY'] = '382bfk3028fh378aj38fah238bz1aq1p'

terms =  {'AC': 'Terokkar Forest: Auchindoun: Auchenai Crypts[65-57] 5-man',
         'ARC': 'Netherstorm: Tempest Keep: The Arcatraz[70-72] 5-man',
         'AQ20': 'Silithus: Ruins of Ahn\'Qiraj[60-65] 20-man',
         'AQ40': 'Silithus: Temple of Ahn\'Qiraj[60-65] 40-man',
         'BF': 'Hellfire Peninsula: Hellfire Citadel: Blood Furnace[61-63] 5-man',
         'BFD': 'Burning Steppes: Blackrock Mountain', #come back to this one
         'BM': 'Tanaris: Caverns of Time: Black Morass[67-72] 5-man',
         'BOT': 'Netherstorm: Tempest Keep: Botanica[70-72] 5-man',
         'BRD': 'Burning Steppes: Blackrock Mountain: Blackrock Depths', #come back to this one
         'BT': 'Shadowmoon Valley: Black Temple[70] 25-man',
         'BWL': 'Burning Steppes: Blackwing Lair[60-62] 40-man', #ask about this in relation to BFD
         'DM': 'Feralas: Dire Maul[56-60] 5-man, or Westfall: The Deadmines[15-20] 5-man',
         'CRYPTS': 'Terokkar Forest, Auchenai Crypts[65-67] 5-man',
         'GL': 'Blade\'s Edge Mountains: Gruul\'s Lair[70] 5-man',
         'GNOMER': 'Dun Morogh: Gnomeregan[24-33] 5-man',
         'KARA': 'Deadwind Pass: Karazhan[70] 10-man',
         'KZ': 'Deadwind Pass: Karazhan[70] 10-man',
        'LBRS': 'Burning Steppes: Blackrock Mountain: Lower Blackrock Spire[] 10-man',
         'MAG': 'Hellfire Penisula: Hellfire Citadel: Magtheridon\'s Lair[70] 25-man',
         'MC': 'Burning Steppes: Blackrock Mountain: Molten Core[60-62] 40-man',
         'MECH': 'Netherstorm: Tempest Keep: The Mechanar[69-72] 5-man',
         'MGT': 'Isle of Quel\'Danas: Magistars\' Terrace[70] 5-man',
         'MRT': 'Isle of Quel\'Danas: Magistars\' Terrace[70] 5-man',
         'MT': 'Terokkar Forest: Auchindoun: Mana-Tombs[64-66] 5-man',
         'NAXX': 'Eastern Plaguelands, Naxxramas[60-70] 40-man',
         'OH': 'Tanaris: Cavern\'s of Time: Old Hillsbrad Foothills[66-68] 5-man',
         'OHB': 'Tanaris: Cavern\'s of Time: Old Hillsbrad Foothills[66-68] 5-man',
         'ONY': 'Dustwallow Marsh, Onyxia\'s Lair[60-62] 40-man',
         'OL': 'Dustwallow Marsh, Onyxia\'s Lair[60-62] 40-man',
         'RAMPS': 'Hellfire Penisula: Hellfire Citadel: Hellfire Ramparts[60-62]5-man',
         'RAQ': 'Silithus: Ruins of Ahn\'Qiraj[55-60] 20-man',
         'RFC': 'Durotar: Orgrimmar: Ragefire Chasm[13-15] 5-man',
         'RFD': 'The Barrens: Razorfen Downs[35-40] 5-man',
         'RFK': 'The Barrens: Razorfen Kraul[25-35] 5-man',
         'SCHOLO': 'Western Plaguelands, Scholomance[58-60] 5-man',
         'SETH': 'Terokkar Forest: Auchindoun: Sethekk Halls[67-69] 5-man',
         'SETH HALLS': 'Terokkar Forest: Auchindoun: Sethekk Halls[67-69] 5-man',
         'SH': 'Hellfire Penisula: Hellfire Citadel: The Shattered Halls[70-72] 5-man',
         'SFK': 'Silverpine Forest, Shadowfang Keep[18-25] 5-man',
         'SL': 'Terokkar Forest: Auchindoun: Shadow Labyrinth[70-72] 5-man',
         'SLAB': 'Terokkar Forest: Auchindoun: Shadow Labyrinth[70-72] 5-man',
         'SM': 'Tirisfal Glades: Scarley Monastery[30-40] 5-man',
         'SP': 'Zangarmarsh: Coilfang Reservoir: The Slave Pens[62-64] 5-man',
         'SSC': 'Zangarmarsh: Coilfang Reservoir: Sepentshrine Cavern[70] 25-man',
         'ST': 'Swamp of Sorrows: Sunken Temple[44-50] 5-man', #unsure about this one
         'STOCKS': 'Stormwind City: The Stockade[23-26] 5-man',
         'STK': 'Stormwind City: The Stockade[23-26] 5-man',
         'STKS': 'Stormwind City: The Stockade[23-26] 5-man',
         'STRAT': 'Eastern Plaguelands: Stratholme[55-60] 5-man',
         'SV': 'Zangarmarsh: Coilfang Reservoir: The Steamvault[70-72] 5-man',
         'UB': 'Zangarmarsh: Coilfang Reservoir: The Underbog[63-65] 5-man',
         'UBRS': 'Burning Steppes: Blackrock Mountain: Upper Blackrock Spire[53-60] 5-man',
         'ULDA': 'Badlands: Uldaman[35-45] 5-man',
         'WC': 'The Barrens: Wailing Caverns[15-21] 5-man',
         'ZA': 'Ghostlands: Zul\'Aman[70] 10-man',
         'ZF': 'Tanaris: Zul\'Farrak[43-47] 5-man',
         'ZG': 'Stranglethorn Vale: Zul\'Gurub[60-62] 20-man'}

global data

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='All Dungeons', terms=terms)
@app.route("/search", methods=['GET', 'POST'])
def search():
    global data
    form = SearchForm()
    if form.validate_on_submit():
        form.search.data = form.search.data.upper()
        if form.search.data in terms:
            data = form.search.data
            return redirect(url_for('search_r'))
    return render_template('search.html', title='Dungeon Search', terms=terms, form=form)
@app.route("/search_results")
def search_r():
    return render_template('search_results.html', title='Search Results', terms=terms, data=data)

@app.route("/all_dungeons")
def all_dg():
    return render_template('home.html', title='All Dungeons', terms=terms)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(debug=True)