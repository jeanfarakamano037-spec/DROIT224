from flask import Flask, jsonify, request, send_from_directory, Response
import json, os, uuid
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads_droit'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
DATA_FILE = "droit_data.json"
QUIZ_FILE = "quiz_data.json"

# --- PROGRAMME LMD GUINÉEN OFFICIEL ---
PROGRAMME = {
    "L1": {
        "S1": ["Introduction au Droit", "Droit Constitutionnel 1", "Histoire du Droit", "Science Politique", "Méthodologie Juridique", "Anglais Juridique"],
        "S2": ["Droit Civil 1 (Personnes)", "Droit Constitutionnel 2", "Droit Administratif 1", "Relations Internationales", "Économie Politique", "Institutions Judiciaires"]
    },
    "L2": {
        "S3": ["Droit Civil 2 (Obligations)", "Droit Pénal Général", "Droit Administratif 2", "Droit Commercial", "Finances Publiques", "Droit du Travail"],
        "S4": ["Droit Civil 3 (Biens)", "Procédure Pénale", "Droit Fiscal", "Droit International Public", "Droit des Libertés", "Comptabilité"]
    },
    "L3": {
        "S5": ["Droit Civil 4 (Contrats Spéciaux)", "Droit des Sociétés", "Procédure Civile", "Droit International Privé", "Contentieux Administratif", "Option Privé/Public"],
        "S6": ["Régime des Obligations", "Voies d'Exécution", "Droit Bancaire", "Mémoire + Stage", "Droit OHADA", "Droit Pénal Spécial"]
    }
}

def load_json(f, default):
    if not os.path.exists(f): return default
    try:
        with open(f,"r",encoding="utf-8") as x: return json.load(x)
    except: return default
def save_json(f, data):
    with open(f,"w",encoding="utf-8") as x: json.dump(data,x,ensure_ascii=False,indent=2)

def initial_fiches():
    return [
        {
            "id": "f1",
            "niveau": "L1", "semestre": "S1", "matiere": "Introduction au Droit",
            "titre": "C'est quoi le Droit en 5 minutes?",
            "auteur": "DROIT224 Team",
            "type": "FICHE",
            "contenu": "Le Droit = ensemble de règles qui organisent la vie en société. 2 branches: Droit Public (État-citoyen) et Droit Privé (entre citoyens). Sources: Constitution, Loi, Coutume, Jurisprudence. Objectif L1: Comprendre la pyramide de Kelsen!",
            "likes": 124, "downloads": 89
        },
        {
            "id": "f2",
            "niveau": "L1", "semestre": "S1", "matiere": "Droit Constitutionnel 1",
            "titre": "Les Institutions Guinéennes",
            "auteur": "DROIT224 Team",
            "type": "FICHE",
            "contenu": "Constitution Guinéenne 2020: Président, Assemblée Nationale (CNT actuellement), Cour Suprême, Cour Constitutionnelle. Principe: Séparation des pouvoirs de Montesquieu. À retenir: Article 1: Guinée = État unitaire laïc.",
            "likes": 98, "downloads": 112
        },
        {
            "id": "f3",
            "niveau": "L1", "semestre": "S1", "matiere": "Méthodologie Juridique",
            "titre": "Comment réussir sa L1 Droit - Méthode",
            "auteur": "Jean Farakamano",
            "type": "MÉTHODE",
            "contenu": "1. Fiche = pas recopiage! 2. Arrêt = Faits + Procédure + Question + Solution. 3. Dissertation: Intro (accroche+problématique), 2 parties, 2 sous-parties, Conclusion. Secret: Lis 1h par jour, pas 10h la veille!",
            "likes": 210, "downloads": 156
        }
    ]

@app.route("/manifest.json")
def manifest():
    return jsonify({
        "name": "DROIT224 WORLD", "short_name": "DROIT224",
        "description": "L1-L3 Droit Guinéen - Fiches, Quiz, Annales",
        "start_url": "/", "display": "standalone",
        "background_color": "#0a0a2a", "theme_color": "#f9c00f",
        "icons": [{"src": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=192","sizes":"192x192","type":"image/png"}]
    })

@app.route("/sw.js")
def sw():
    return Response("self.addEventListener('install',e=>self.skipWaiting());self.addEventListener('activate',e=>self.clients.claim());", mimetype="application/javascript")

@app.route("/")
def home():
    return """
<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>DROIT224 WORLD</title><link rel="manifest" href="/manifest.json"><meta name="theme-color" content="#0a0a2a">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}body{background:#050510;color:#fff;font-family:Inter,Arial;padding-bottom:20px}
.header{background:radial-gradient(ellipse at top,#1a1a4a 0%,#000 70%);padding:28px 15px;text-align:center;border-bottom:1px solid #1a1a3a}
.header h1{font-size:32px;font-weight:900;letter-spacing:2px;background:linear-gradient(#f9c00f,#ff8c00);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.header p{color:#666;font-size:10px;letter-spacing:4px;margin-top:6px}
.levels{display:flex;gap:10px;padding:12px;background:#0a0a1a;position:sticky;top:0;z-index:20;overflow-x:auto}
.levels button{background:#151530;color:#888;border:1px solid #222;padding:10px 22px;border-radius:25px;font-weight:900;font-size:13px;white-space:nowrap}
.levels button.active{background:#f9c00f;color:#000}
.semesters{display:flex;gap:8px;padding:0 12px 12px;background:#0a0a1a;position:sticky;top:50px;z-index:10}
.semesters button{background:#10102a;color:#666;border:1px solid #1e1e4a;padding:7px 16px;border-radius:20px;font-size:11px;font-weight:700}
.semesters button.active{background:#fff;color:#000}
.install-banner{display:none;background:linear-gradient(90deg,#f9c00f,#ff8c00);color:#000;padding:12px 14px;margin:10px 14px;border-radius:12px;justify-content:space-between;align-items:center;font-weight:900;font-size:12px}
.install-banner.show{display:flex}
.matiere-bar{display:flex;gap:8px;overflow-x:auto;padding:12px 14px;background:#08081a;border-bottom:1px solid #151535}
.matiere-bar button{background:#11112a;color:#888;border:1px solid #222;padding:8px 14px;border-radius:20px;font-size:11px;white-space:nowrap}
.matiere-bar button.active{background:#f9c00f;color:#000;border-color:#f9c00f}
.grid{display:grid;grid-template-columns:1fr;gap:12px;padding:14px}
.card{background:#10102a;border-radius:16px;padding:16px;border:1px solid #1a1a3a;cursor:pointer;transition:0.2s}
.card:hover{border-color:#f9c00f;transform:translateY(-3px)}
.card h4{font-size:14px;font-weight:700}
.card small{color:#f9c00f;font-size:10px;font-weight:900;letter-spacing:1px}
.card p{color:#888;font-size:12px;margin:8px 0;line-height:1.5;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.card-meta{display:flex;gap:12px;margin-top:10px;font-size:10px;color:#555}
.badge{font-size:9px;background:#f9c00f;color:#000;padding:3px 8px;border-radius:20px;font-weight:900}
.uploadBox{background:#0a0a1a;margin:14px;padding:18px;border-radius:16px;border:1px dashed #222}
input,select,textarea{width:100%;padding:11px;margin:6px 0;border-radius:10px;border:1px solid #222;background:#111;color:#fff;outline:none;font-size:13px}
textarea{height:90px}
.modal{position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0.92);z-index:100;display:none;overflow-y:auto;padding:20px}
.modal-content{background:#0f0f2a;border-radius:18px;padding:20px;max-width:650px;margin:20px auto;border:1px solid #222}
.btn{padding:10px 18px;border-radius:25px;border:none;font-weight:800;cursor:pointer;font-size:12px}
.btn-gold{background:#f9c00f;color:#000}
.btn-dark{background:#1e1e3a;color:#fff;border:1px solid #333}
</style></head><body>
<div class="header"><h1>DROIT224 WORLD</h1><p>L1 • L2 • L3 • SYSTÈME LMD GUINÉEN</p></div>
<div class="install-banner" id="installBanner"><span>📲 Installer DROIT224?</span><div><button onclick="installApp()" style="background:#000;color:#f9c00f;padding:6px 14px;border-radius:20px;border:none;font-weight:900;margin-right:6px">INSTALLER</button><button onclick="hideBanner()" style="background:transparent;color:#000;border:1px solid #000;padding:5px 10px;border-radius:20px">Plus tard</button></div></div>
<div class="levels"><button class="active" onclick="setLevel('L1',this)">L1 DROIT</button><button onclick="setLevel('L2',this)">L2 DROIT</button><button onclick="setLevel('L3',this)">L3 DROIT</button></div>
<div class="semesters" id="semBar"></div>
<div class="matiere-bar" id="matiereBar"></div>
<div style="margin:10px 14px;background:linear-gradient(90deg,#11112a,#1a1500);border:1px solid #2a2200;padding:10px 14px;border-radius:12px;display:flex;justify-content:space-between;align-items:center"><span style="font-size:11px;color:#f9c00f;font-weight:700" id="stats">Chargement...</span><span style="font-size:10px;color:#555">LIVE</span></div>
<div class="grid" id="grid"></div>
<div class="uploadBox">
<div style="font-size:11px;letter-spacing:2px;color:#f9c00f;font-weight:900;margin-bottom:10px">CONTRIBUER • AJOUTER UNE FICHE</div>
<select id="niveau"><option>L1</option><option>L2</option><option>L3</option></select>
<select id="semestre"><option>S1</option><option>S2</option><option>S3</option><option>S4</option><option>S5</option><option>S6</option></select>
<input id="matiere" placeholder="Matière: ex: Droit Civil">
<input id="titre" placeholder="Titre fiche: ex: Les vices du consentement">
<select id="type"><option>FICHE</option><option>MÉTHODE</option><option>ANNALE</option><option>CODE</option><option>QUIZ</option></select>
<textarea id="contenu" placeholder="Contenu de la fiche (2-3 paragraphes clairs)..."></textarea>
<input id="auteur" placeholder="Ton nom / promo: ex: Abdoul L1 Sonfonia">
<button onclick="upload()" style="width:100%;background:#f9c00f;padding:13px;border-radius:30px;font-weight:900;margin-top:8px;border:none;color:#000">PUBLIER LA FICHE</button>
<p id="status" style="margin-top:8px;font-size:11px;text-align:center;color:#888"></p>
</div>
<div class="modal" id="modal"><div class="modal-content"><button onclick="closeModal()" style="float:right;background:#1a1a3a;color:#fff;border:1px solid #333;padding:6px 14px;border-radius:20px">✕</button><div id="modalContent"></div></div></div>
<script>
let deferredPrompt;
window.addEventListener('beforeinstallprompt', e=>{e.preventDefault();deferredPrompt=e;document.getElementById('installBanner').classList.add('show');});
function installApp(){if(deferredPrompt){deferredPrompt.prompt();deferredPrompt.userChoice.then(()=>{deferredPrompt=null;hideBanner();});}}
function hideBanner(){document.getElementById('installBanner').classList.remove('show');}
if('serviceWorker' in navigator){navigator.serviceWorker.register('/sw.js');}
let allFiches=[]; let currentLevel='L1'; let currentSem='S1'; let currentMatiere='ALL';
const prog = """+json.dumps(PROGRAMME)+""";
async function load(){let r=await fetch('/api/fiches');allFiches=await r.json();renderSem();renderMatiere();render();document.getElementById('stats').innerText=`📚 ${allFiches.length} fiches • ${prog.L1.S1.length+prog.L1.S2.length} matières L1`;}
function renderSem(){
 let sems = Object.keys(prog[currentLevel]);
 let h=''; sems.forEach((s,i)=>{h+=`<button class="${s==currentSem?'active':''}" onclick="setSem('${s}',this)">${s}</button>`;});
 if(!sems.includes(currentSem)) currentSem=sems[0];
 document.getElementById('semBar').innerHTML=h;
}
function renderMatiere(){
 let matieres = prog[currentLevel][currentSem] || [];
 let h=`<button class="${currentMatiere=='ALL'?'active':''}" onclick="setMatiere('ALL',this)">TOUT</button>`;
 matieres.forEach(m=>{h+=`<button class="${currentMatiere==m?'active':''}" onclick="setMatiere('${m}',this)">${m.split(' ')[0]} ${m.split(' ')[1]||''}</button>`;});
 document.getElementById('matiereBar').innerHTML=h;
}
function render(){
 let list = allFiches.filter(f=>f.niveau==currentLevel && f.semestre==currentSem);
 if(currentMatiere!='ALL') list = list.filter(f=>f.matiere==currentMatiere);
 let h=''; list.forEach(f=>{
  h+=`<div class="card" onclick="openFiche('${f.id}')"><small>${f.niveau} • ${f.semestre} • ${f.matiere} • ${f.type}</small><h4>${f.titre}</h4><p>${f.contenu}</p><div class="card-meta"><span>👍 ${f.likes||0}</span><span>⬇️ ${f.downloads||0}</span><span>✍️ ${f.auteur}</span><span class="badge">${f.type}</span></div></div>`;
 });
 if(list.length==0) h=`<div style="padding:30px;text-align:center;color:#555"><p>Aucune fiche pour ${currentMatiere} encore.</p><p style="font-size:11px;margin-top:8px">Sois le premier à contribuer! 👇</p></div>`;
 document.getElementById('grid').innerHTML=h;
}
function setLevel(l,btn){document.querySelectorAll('.levels button').forEach(b=>b.classList.remove('active'));btn.classList.add('active');currentLevel=l;currentSem=Object.keys(prog[l])[0];currentMatiere='ALL';renderSem();renderMatiere();render();}
function setSem(s,btn){document.querySelectorAll('.semesters button').forEach(b=>b.classList.remove('active'));btn.classList.add('active');currentSem=s;currentMatiere='ALL';renderMatiere();render();}
function setMatiere(m,btn){document.querySelectorAll('.matiere-bar button').forEach(b=>b.classList.remove('active'));btn.classList.add('active');currentMatiere=m;render();}
function openFiche(id){
 let f=allFiches.find(x=>x.id==id);if(!f)return;
 document.getElementById('modalContent').innerHTML=`<small style="color:#f9c00f;font-weight:900">${f.niveau} • ${f.semestre} • ${f.matiere}</small><h2 style="margin:10px 0">${f.titre}</h2><p style="color:#888;font-size:11px">Par ${f.auteur} • ${f.type}</p><hr style="border:0;border-top:1px solid #222;margin:14px 0"><p style="line-height:1.8;font-size:14px;white-space:pre-wrap">${f.contenu}</p><div style="margin-top:20px;display:flex;gap:8px"><button onclick="like('${f.id}')" class="btn btn-gold">👍 Utile (${f.likes||0})</button><button onclick="downloadFiche('${f.id}')" class="btn btn-dark">⬇️ Télécharger</button><button onclick="shareFiche('${f.id}')" class="btn btn-dark">📲 Partager</button></div>`;
 document.getElementById('modal').style.display='block';
 fetch('/api/download/'+id,{method:'POST'});
}
function closeModal(){document.getElementById('modal').style.display='none';}
async function like(id){let r=await fetch('/api/like/'+id,{method:'POST'});let j=await r.json();let f=allFiches.find(x=>x.id==id);if(f)f.likes=j.total;render();if(document.getElementById('modal').style.display=='block')openFiche(id);}
async function downloadFiche(id){
 let f=allFiches.find(x=>x.id==id);let blob=new Blob([f.titre+"\\n\\n"+f.contenu+"\\n\\nSource: DROIT224 WORLD"],{type:'text/plain'});let url=URL.createObjectURL(blob);let a=document.createElement('a');a.href=url;a.download=f.titre+'.txt';a.click();
}
function shareFiche(id){let f=allFiches.find(x=>x.id==id);if(navigator.share){navigator.share({title:f.titre,text:f.contenu.substring(0,100)+'...',url:location.href});}else{prompt('Copie ce lien:',location.href);}}
async function upload(){
 let niveau=document.getElementById('niveau').value;let semestre=document.getElementById('semestre').value;let matiere=document.getElementById('matiere').value;let titre=document.getElementById('titre').value;let type=document.getElementById('type').value;let contenu=document.getElementById('contenu').value;let auteur=document.getElementById('auteur').value;
 if(!matiere||!titre||!contenu||!auteur) return alert('Remplis tout!');
 document.getElementById('status').innerText='Publication...';
 let r=await fetch('/upload',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({niveau,semestre,matiere,titre,type,contenu,auteur})});
 let j=await r.json();document.getElementById('status').innerText=j.message;if(j.success){load();document.getElementById('titre').value='';document.getElementById('contenu').value='';}
}
load();
</script></body></html>
    """

@app.route("/api/fiches")
def api(): return jsonify(load_json(DATA_FILE, initial_fiches()))

@app.route("/api/like/<fid>", methods=["POST"])
def like(fid):
    fiches=load_json(DATA_FILE, initial_fiches()); total=0
    for f in fiches:
        if f["id"]==fid: f["likes"]=f.get("likes",0)+1; total=f["likes"]
    save_json(DATA_FILE,fiches); return jsonify({"total":total})

@app.route("/api/download/<fid>", methods=["POST"])
def dl(fid):
    fiches=load_json(DATA_FILE, initial_fiches())
    for f in fiches:
        if f["id"]==fid: f["downloads"]=f.get("downloads",0)+1
    save_json(DATA_FILE,fiches); return jsonify({"ok":True})

@app.route("/upload", methods=["POST"])
def upload():
    data=request.get_json()
    if not data: return jsonify({"success":False,"message":"Données manquantes"})
    fiches=load_json(DATA_FILE, initial_fiches())
    fiches.insert(0,{
        "id": uuid.uuid4().hex[:8],
        "niveau": data.get("niveau","L1"),
        "semestre": data.get("semestre","S1"),
        "matiere": data.get("matiere","Général"),
        "titre": data.get("titre","")[:120],
        "type": data.get("type","FICHE"),
        "contenu": data.get("contenu","")[:3000],
        "auteur": data.get("auteur","Anonyme")[:40],
        "likes": 0, "downloads": 0
    })
    save_json(DATA_FILE,fiches)
    return jsonify({"success":True,"message":f"✅ Fiche '{data.get('titre')}' publiée en {data.get('niveau')} {data.get('semestre')}!"})

if __name__=="__main__":
    app.run(host="0.0.0.0",port=int(os.environ.get("PORT",5000)))
