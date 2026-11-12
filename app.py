import os, json, urllib.request
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

BASE_DROIT = {
    "tribunal": "TRIBUNAL EN GUINEE: Juridiction qui juge. TPI dans chaque prefecture, Cour d'Appel Conakry/Kankan, Cour Supreme. Saisine: requete 50.000 GNF, audience, jugement 1-2 ans. Source: Code procedure civile Guinee.",
    "contrat": "CONTRAT: Accord entre 2 personnes qui cree des obligations. Conditions: consentement libre, capacite, objet licite. Si non respecte: mise en demeure 8 jours, puis TPI. Source: Code civil Art 1101 + OHADA.",
    "mariage": "MARIAGE EN GUINEE: Union legale devant officier etat civil. 18 ans, consentement, dot. Regimes: communaute ou separation. Divorce: TPI, pension, garde enfants. Source: Code civil Guinee.",
    "vol": "VOL: Prendre bien d'autrui sans consentement. Peine: 6 mois a 5 ans + amende 500k a 5M GNF. Avec violence: 5 a 10 ans. Plainte gendarmerie, parquet, TPI. Source: Code penal guineen.",
    "terrain": "TERRAIN / FONCIER: Proprietaire = Titre Foncier ou acte notarie. Voisin construit sur ton terrain: 1-Bornage, 2-Mise en demeure huissier 50k, 3-Plainte TPI foncier, 4-Expulsion + dommages. Ne detruis pas toi-meme. Source: Code foncier Guinee.",
    "jurisprudence": "JURISPRUDENCE: Decisions des juges qui deviennent exemples. Guinee: Cour Supreme et CCJA pour OHADA. Aide a prevoir comment le juge va decider ton cas.",
    "divorce": "DIVORCE: Fin mariage par jugement TPI. Motifs: adultere, violence, abandon. Procedure: requete avocat, conciliation, jugement, pension, garde, partage biens. 6 mois a 2 ans.",
    "salaire": "SALAIRE / TRAVAIL: SMIG 550.000 GNF. CDI ou CDD. Licenciement: preavis, indemnite. Si non paye: Inspection du Travail puis Tribunal du Travail gratuit. Source: Code du Travail Guinee.",
    "ohada": "OHADA: Organisation pour l'Harmonisation en Afrique du Droit des Affaires. 17 pays dont Guinee. Actes Uniformes: droit commercial, societes, suretes, recouvrement, arbitrage. Juge: CCJA a Abidjan."
}

def moteur_faq_vrai(q):
    api_key = os.environ.get("GEMINI_API_KEY", "")
    if api_key:
        try:
            prompt = f"Tu es un professeur de droit guineen expert en droit guineen et OHADA. Reponds en francais simple, precis, avec articles, peines, procedure a Conakry, exemples concrets Guinee. Question: {q}. Donne definition, textes, conditions, procedure, sanctions, conseils pratiques. Max 300 mots."
            data = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode()
            req = urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}", data=data, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=20) as r:
                res = json.loads(r.read())
                txt = res["candidates"][0]["content"]["parts"][0]["text"]
                return txt + " | Source: AI Gemini - Droit Guineen & OHADA"
        except Exception as e:
            pass
    ql = q.lower().strip()
    for mot in sorted(BASE_DROIT.keys(), key=lambda x: -len(x)):
        if mot in ql:
            return BASE_DROIT[mot]
    return f"REPONSE DROIT224 pour '{q}': Analyse droit guineen et OHADA: 1- Definition, 2- Textes Constitution 2020 Code civil Code penal Code travail Actes OHADA, 3- Procedure mise en demeure 8j huissier 50k, conciliation, requete TPI 50k, audience jugement 1-2 ans, appel 1 mois, cassation Cour Supreme ou CCJA 2 mois. Consulte avocat Barreau Conakry."

COURS = {
    "L1": [("Introduction au Droit", "Notion droit, regles, sources, organisation judiciaire Guinee"), ("Droit Constitutionnel", "Constitution 2020, institutions, President, Assemblee, Cour Supreme"), ("Droit Civil - Personnes", "Personnalite, etat civil, domicile, capacite"), ("Histoire du Droit", "Droit coutumier guineen, colonisation, independance 1958")],
    "L2": [("Droit des Obligations", "Contrat, responsabilite, preuve, prescription"), ("Droit Penal General", "Infraction, peine, elements constitutifs, excuses"), ("Droit Administratif", "Acte administratif, recours, responsabilite Etat"), ("Droit Commercial OHADA", "Commercant, acte de commerce, bail commercial")],
    "L3": [("Droit Foncier", "Titre foncier, domaine national, bornage, litiges"), ("Droit des Societes OHADA", "SARL, SA, creation, gerance, dissolution"), ("Droit du Travail", "Contrat, salaire, licenciement, Inspection Travail"), ("Procedure Civile", "Saisine TPI, audience, voies de recours, execution")]
}

DICT = [("Acte authentique","Acte dresse par notaire, force probante"),("Appel","Recours contre jugement TPI devant Cour d'Appel sous 1 mois"),("Assignation","Acte huissier pour convoquer devant tribunal"),("Bail","Contrat location terrain/maison"),("Cassation","Recours devant Cour Supreme ou CCJA"),("Dot","Don coutumier lors mariage guineen"),("Huissier","Officier qui signifie actes, saisies"),("Mise en demeure","Lettre pour exiger paiement sous 8 jours"),("Parquet","Ministere public, Procureur"),("Titre Foncier","Preuve supreme propriete terrain Guinee")]

QUIZ_Q = [
    ("C'est quoi l'OHADA ?", ["Organisation Droit des Affaires Afrique","Club de foot","Banque"], 0),
    ("Delai d'appel d'un jugement TPI ?", ["1 mois","1 an","10 jours"], 0),
    ("SMIG en Guinee ?", ["550.000 GNF","100.000 GNF","1.000.000 GNF"], 0),
    ("Ou va la cassation OHADA ?", ["CCJA Abidjan","TPI Conakry","Gendarmerie"], 0),
]

HTML = r"""
<!DOCTYPE html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>
<title>DROIT224</title>
<style>
body{font-family:Arial;margin:0;background:#0a1526;color:white}
header{text-align:center;padding:16px;background:#0a1526}header h1{color:#ffc107;margin:0;font-size:32px}header p{font-size:11px;letter-spacing:1px;color:#ccc}
.btn-app{background:#ff8c00;color:white;border:0;padding:10px 18px;border-radius:20px;font-weight:bold;cursor:pointer}
nav{display:flex;gap:6px;overflow-x:auto;padding:10px;background:#0a1526;border-top:2px solid #ffc107;white-space:nowrap}nav button{padding:8px 14px;border-radius:20px;border:0;cursor:pointer;font-weight:bold;background:#1a2a44;color:white}nav button.active{background:#ffc107;color:black}nav button.faq{background:#0f0;border:1px solid lime}
.card{margin:12px;background:#0f2a5a;border:1px solid #ffc107;border-radius:14px;padding:14px}
.card.cyan{border-color:#00e5ff}.card.green{border-color:#00ff66}
h2{margin:6px 0}input,select,textarea{width:100%;padding:12px;border-radius:10px;border:1px solid #333;margin:6px 0;font-size:15px;box-sizing:border-box}
.ask{width:100%;padding:13px;background:#f5a623;border:0;border-radius:10px;font-weight:bold;font-size:16px;cursor:pointer}
#res{white-space:pre-wrap;background:#fff;color:#111;padding:14px;border-radius:10px;margin-top:10px;line-height:1.6}
.mat{background:rgba(255,255,255,.08);padding:10px;border-radius:10px;margin:6px 0}
.qbox{background:#fff;color:#111;padding:12px;border-radius:10px;margin:8px 0}
.small{font-size:13px;color:#ddd}
</style></head>
<body>
<header><h1>DROIT224</h1><p>L1 • L2 • L3 • OHADA • DICTIONNAIRE A-Z • FAQ AI</p><button class="btn-app" onclick="alert('App DROIT224 - Ajoute a ecran accueil depuis Chrome: Menu > Ajouter a ecran accueil')">📱 TÉLÉCHARGER L'APP DROIT224</button></header>
<nav>
<button onclick="show('cours')" id="b-cours" class="active">📚 COURS L1 L2 L3</button>
<button onclick="show('ohada')" id="b-ohada">⚖️ OHADA</button>
<button onclick="show('dico')" id="b-dico">📖 DICTIONNAIRE A-Z</button>
<button onclick="show('quiz')" id="b-quiz">🎯 QUIZ</button>
<button onclick="show('faq')" id="b-faq" class="faq">❓ FAQ</button>
<button onclick="show('dossiers')" id="b-dossiers">📁 DOSSIERS</button>
<button onclick="show('cercle')" id="b-cercle">👥 CERCLE</button>
</nav>

<div id="cours"><div class="card"><h3>📚 Cours - Choisis ta Licence</h3></div>
<div class="card" onclick="toggle('l1')"><h2>🎓 LICENCE 1</h2><p>Introduction Droit, Constitutionnel - Clique pour voir matières</p><div id="l1" style="display:none"></div></div>
<div class="card cyan" onclick="toggle('l2')"><h2 style="color:#00e5ff">🎓 LICENCE 2</h2><p>Obligations, Pénal - Clique pour voir matières</p><div id="l2" style="display:none"></div></div>
<div class="card green" onclick="toggle('l3')"><h2 style="color:#00ff66">🎓 LICENCE 3</h2><p>Foncier, Sociétés OHADA - Clique pour voir matières</p><div id="l3" style="display:none"></div></div>
<div class="card" style="border-style:dashed"><h3>➕ DÉPÔT DE COURS - Étudiant / Professeur / Enseignant / Docteur / Juge / Avocat</h3><p class="small">Dépose ton cours PDF ou leçon, quantité illimitée, avec ton nom et prénom. Il apparaîtra pour tous!</p><input placeholder="Nom et Prénom * ex: Mamadou Diallo"><input placeholder="Prénom (si séparé)"><select><option>Étudiant</option><option>Professeur</option><option>Enseignant</option><option>Docteur</option><option>Juge</option><option>Avocat</option></select><select><option>Licence 1</option><option>Licence 2</option><option>Licence 3</option><option>OHADA</option></select><input placeholder="Titre du cours"><textarea placeholder="Description / Résumé"></textarea><button class="ask" onclick="alert('Merci! Ton cours sera publié après vérification.')">📤 Déposer mon cours</button></div>
</div>

<div id="ohada" style="display:none"><div class="card"><h2>⚖️ OHADA</h2><p>Organisation pour l'Harmonisation en Afrique du Droit des Affaires - 17 pays dont Guinée.</p><div class="mat"><b>Acte Uniforme Droit Commercial:</b> Commerçant, acte de commerce, registre RCCM, bail commercial.</div><div class="mat"><b>Sociétés Commerciales:</b> SARL, SA, SNC, création, statuts, gérance, dissolution.</div><div class="mat"><b>Sûretés:</b> Hypothèque, nantissement, caution.</div><div class="mat"><b>Recouvrement:</b> Injonction de payer, saisie.</div><div class="mat"><b>Arbitrage:</b> CCJA à Abidjan, sentence, exequatur.</div><div class="mat"><b>Procédures Collectives:</b> Règlement préventif, redressement, liquidation.</div></div></div>

<div id="dico" style="display:none"><div class="card"><h2>📖 Dictionnaire A-Z</h2><input id="dicoSearch" onkeyup="filterDico()" placeholder="Cherche un mot: tribunal, contrat..."><div id="dicoList"></div></div></div>

<div id="quiz" style="display:none"><div class="card"><h2>🎯 Quiz Droit</h2><div id="quizBox"></div><button class="ask" onclick="loadQuiz()">Nouveau Quiz</button></div></div>

<div id="faq" style="display:none"><div class="card"><h2>❓ FAQ - VRAI AI 🤖</h2><p class="small">Pose ta question en français simple. L'IA répond avec droit guinéen + OHADA.</p><input id="q" placeholder="Ex: c'est quoi un tribunal ?"><button class="ask" onclick="ask()">Demander à l'IA 🤖</button><div id="res">Tape ta question et clique Demander...</div><p class="small">Powered by Gemini AI + Droit Guinéen & OHADA</p></div></div>

<div id="dossiers" style="display:none"><div class="card"><h2>📁 Dossiers - Modèles</h2><div class="mat"><b>Mise en demeure:</b><br>Je soussigné... vous mets en demeure de payer / libérer sous 8 jours, à défaut saisine TPI.</div><div class="mat"><b>Plainte:</b><br>À Monsieur le Procureur TPI Conakry, Objet: plainte pour vol / escroquerie / abus...</div><div class="mat"><b>Contrat de bail:</b><br>Entre bailleur et locataire, loyer, durée, caution, obligations.</div><div class="mat"><b>Requête TPI:</b><br>À Monsieur le Président TPI, demande d'audience pour litige foncier / divorce / dette.</div></div></div>

<div id="cercle" style="display:none"><div class="card"><h2>👥 Cercle DROIT224</h2><p>Communauté étudiants, profs, avocats, juges Guinée. Pose ta question, entraide, partage cours.</p><input placeholder="Ton nom"><textarea placeholder="Ta question pour le Cercle..."></textarea><button class="ask" onclick="alert('Publié dans le Cercle!')">Publier dans le Cercle</button><div class="mat"><b>Mamadou - L2:</b> Quelqu'un a résumé Droit des Obligations? 🙏</div><div class="mat"><b>Fatoumata - L3:</b> J'ai eu 15 en Foncier avec les fiches DROIT224!</div></div></div>

<script>
const COURS = {{ cours|tojson }};
const DICT = {{ dico|tojson }};
const QUIZ = {{ quiz|tojson }};
function show(id){['cours','ohada','dico','quiz','faq','dossiers','cercle'].forEach(x=>document.getElementById(x).style.display=x==id?'block':'none');document.querySelectorAll('nav button').forEach(b=>b.classList.remove('active'));document.getElementById('b-'+id)?.classList.add('active')}
function toggle(id){let e=document.getElementById(id);if(e.innerHTML==''){let key=id.toUpperCase();e.innerHTML=COURS[key].map(m=>`<div class='mat'><b>${m[0]}</b><br><span class='small'>${m[1]}</span></div>`).join('')}e.style.display=e.style.display=='none'?'block':'none'}
function renderDico(list){document.getElementById('dicoList').innerHTML=list.map(d=>`<div class='mat'><b>${d[0]}</b> - ${d[1]}</div>`).join('')}
function filterDico(){let v=document.getElementById('dicoSearch').value.toLowerCase();renderDico(DICT.filter(d=>d[0].toLowerCase().includes(v)||d[1].toLowerCase().includes(v)))}
renderDico(DICT);
let qi=0,score=0;
function loadQuiz(){qi=0;score=0;showQuiz()}
function showQuiz(){if(qi>=QUIZ.length){document.getElementById('quizBox').innerHTML=`<h3>Score: ${score}/${QUIZ.length} 🎉</h3><p>Continue, tu progresses!</p>`;return}let q=QUIZ[qi];document.getElementById('quizBox').innerHTML=`<div class='qbox'><b>Q${qi+1}: ${q[0]}</b><br>${q[1].map((c,i)=>`<button onclick='ans(${i})' style='display:block;width:100%;margin:6px 0;padding:10px;border-radius:8px;border:1px solid #ddd;text-align:left'>${c}</button>`).join('')}</div>`}
function ans(i){if(i==QUIZ[qi][2]){score++;alert('✅ Bonne réponse!')}else{alert('❌ Mauvaise. Bonne réponse: '+QUIZ[qi][1][QUIZ[qi][2]])}qi++;showQuiz()}
loadQuiz();
async function ask(){let q=document.getElementById('q').value;if(!q)return alert('Ecris ta question');document.getElementById('res').innerText='⏳ IA réfléchit...';let r=await fetch('/api/faq',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({q:q})});let d=await r.json();document.getElementById('res').innerText=d.reponse}
</script></body></html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, cours=COURS, dico=DICT, quiz=QUIZ_Q)

@app.route("/api/faq", methods=["POST"])
def api_faq():
    data = request.get_json() or {}
    q = data.get("q", "")
    return jsonify({"reponse": moteur_faq_vrai(q)})

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
