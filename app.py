from flask import Flask, jsonify, request
import json, os, uuid
from datetime import datetime

app = Flask(__name__)
FILES = {"fiches":"droit_data.json","lexique":"lexique.json","faq":"faq.json","quiz":"quiz_lmd.json","forum":"forum224.json"}

def load(f,default):
    if not os.path.exists(f): return default
    try: return json.load(open(f,"r",encoding="utf-8"))
    except: return default
def save(f,d): json.dump(d, open(f,"w",encoding="utf-8"), ensure_ascii=False, indent=2)

FORUM_INIT = [
    {"id":"1","role":"Professeur","nom":"Prof. Camara","matiere":"Constitutionnel","msg":"Bienvenue dans le cercle! Posez vos questions L1 ici, je réponds chaque soir à 20h","time":"Aujourd'hui 08:00","likes":12},
    {"id":"2","role":"Juge","nom":"Juge TPI Dixinn","matiere":"Procédure","msg":"Astuce du terrain: Au TPI, si vous venez sans mise en demeure, le juge va vous renvoyer. Faites toujours mise en demeure d'abord!","time":"Aujourd'hui 09:15","likes":24},
    {"id":"3","role":"Étudiant","nom":"Mamadou L2","matiere":"Pénal","msg":"Svp c'est quoi la différence entre vol et escroquerie? Je confonds toujours 😭","time":"Aujourd'hui 10:30","likes":3},
    {"id":"4","role":"Docteur","nom":"Dr. Diallo - Droit OHADA","matiere":"OHADA","msg":"Mamadou: Vol = tu prends sans consentement. Escroquerie = la personne te donne VOLONTAIREMENT parce que tu l'as trompée. Ex: Vol=arracher téléphone. Escroquerie=te vendre un faux iPhone.","time":"Aujourd'hui 10:45","likes":18},
]

@app.route("/")
def home(): 
    return """
<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>DROIT224 V3 - CERCLE</title><style>
*{margin:0;padding:0;box-sizing:border-box}body{background:#050510;color:#fff;font-family:Arial}
.header{text-align:center;padding:18px;background:radial-gradient(#1a1a4a,#000);border-bottom:2px solid #f9c00f;position:sticky;top:0;z-index:30}
.tabs{display:flex;gap:5px;padding:8px;background:#0a0a1a;overflow-x:auto;position:sticky;top:78px;z-index:20}
.tabs button{padding:8px 12px;border-radius:20px;border:1px solid #222;background:#151530;color:#aaa;font-size:10px;font-weight:800;white-space:nowrap}
.tabs button.active{background:#f9c00f;color:#000}
.view{display:none;padding:12px}.view.active{display:block}
.card{background:#10102a;border:1px solid #1a1a3a;border-radius:14px;padding:12px;margin:8px 0}
.badge{padding:3px 8px;border-radius:20px;font-size:8px;font-weight:900;color:#000}
.role-Professeur{background:#00e5ff} .role-Juge{background:#ff1744;color:#fff} .role-Avocat{background:#76ff03} .role-Docteur{background:#d500f9;color:#fff} .role-Étudiant{background:#f9c00f} .role-Enseignant{background:#ff9100}
.forum-msg{border-left:3px solid #f9c00f;margin:10px 0;background:#0f0f2a}
.forum-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px}
input,select,textarea{width:100%;padding:10px;margin:4px 0;border-radius:10px;border:1px solid #222;background:#111;color:#fff}
.btn{padding:10px 14px;border-radius:25px;border:none;font-weight:800;background:#f9c00f;color:#000}
.quiz-opt{padding:10px;border:1px solid #222;border-radius:10px;margin:5px 0}
</style></head><body>
<div class="header"><h1 style="color:#f9c00f;font-weight:900;letter-spacing:1px">DROIT224 WORLD V3</h1><p style="font-size:8px;letter-spacing:2px;color:#aaa">CERCLE DES JURISTES • L1 L2 L3 • LEXIQUE • DOSSIERS • QUIZ • FORUM LIVE</p></div>
<div class="tabs">
<button class="active" onclick="showTab('cours',this)">📚 COURS</button>
<button onclick="showTab('lexique',this)">📖 LEXIQUE</button>
<button onclick="showTab('dossiers',this)">📂 DOSSIERS</button>
<button onclick="showTab('quiz',this)">🎮 QUIZ</button>
<button onclick="showTab('faq',this)">❓ FAQ</button>
<button onclick="showTab('forum',this)" style="border-color:#f9c00f;color:#f9c00f">💬 CERCLE LIVE 🔴</button>
</div>

<div id="cours" class="view active"><div id="gridCours"></div></div>
<div id="lexique" class="view"><input id="sLex" placeholder="Cherche mot..." oninput="loadAll()"><div id="gridLex"></div><div class="card"><input id="lexT" placeholder="Terme"><input id="lexD" placeholder="Définition simple"><button class="btn" onclick="addLex()">Ajouter</button></div></div>
<div id="dossiers" class="view"><div class="card" style="border-color:#f9c00f"><select id="typeDos"><option>Licenciement</option><option>Dette</option><option>Terre</option><option>Divorce</option><option>Vol/Escroquerie</option></select><textarea id="descDos" placeholder="Ton problème"></textarea><button class="btn" onclick="analyser()">Analyser</button><div id="resDos"></div></div></div>
<div id="quiz" class="view"><select id="ql"><option>L1</option><option>L2</option><option>L3</option></select><button class="btn" onclick="startQuiz()">Commencer</button><div id="qz"></div></div>
<div id="faq" class="view"><div id="gridFaq"></div><input id="fq" placeholder="Question"><textarea id="fr" placeholder="Réponse"></textarea><button class="btn" onclick="addFaq()">Poster</button></div>

<div id="forum" class="view">
<div class="card" style="background:linear-gradient(135deg,#1a1a4a,#000);border:2px solid #f9c00f;text-align:center"><h3>💬 CERCLE DES JURISTES 224 🔴 LIVE</h3><p style="font-size:10px;color:#aaa;margin-top:6px">Étudiants • Professeurs • Juges • Avocats • Docteurs<br>Tout le monde s'entraide ici!</p><div style="display:flex;gap:6px;justify-content:center;margin-top:8px;flex-wrap:wrap"><span class="badge role-Étudiant">Étudiant</span><span class="badge role-Professeur">Professeur</span><span class="badge role-Juge">Juge</span><span class="badge role-Avocat">Avocat</span><span class="badge role-Docteur">Docteur</span></div></div>

<div class="card"><h4>✍️ Poster dans le cercle</h4><select id="forumRole"><option>Étudiant</option><option>Professeur</option><option>Juge</option><option>Avocat</option><option>Docteur</option><option>Enseignant</option></select><input id="forumNom" placeholder="Ton nom ex: Mamadou L2"><select id="forumMat"><option>Droit Général</option><option>Constitutionnel</option><option>Civil</option><option>Pénal</option><option>OHADA</option><option>Procédure</option><option>Travail</option></select><textarea id="forumMsg" placeholder="Ta question ou ton explication... Ex: Svp qui peut m'expliquer la QPC simplement?"></textarea><button class="btn" onclick="postForum()" style="width:100%">🚀 Poster dans le cercle</button></div>

<div id="gridForum"></div>
</div>

<script>
let D={}; async function loadAll(){let [f,l,q,fo,fa]=await Promise.all([fetch('/api/fiches').then(r=>r.json()),fetch('/api/lexique').then(r=>r.json()),fetch('/api/quiz').then(r=>r.json()),fetch('/api/forum').then(r=>r.json()),fetch('/api/faq').then(r=>r.json())]); D={fiches:f,lex:l,quiz:q,forum:fo,faq:fa}; renderCours(); renderLex(); renderForum(); renderFaq();}
function showTab(id,btn){document.querySelectorAll('.view').forEach(v=>v.classList.remove('active'));document.getElementById(id).classList.add('active');document.querySelectorAll('.tabs button').forEach(b=>b.classList.remove('active'));btn.classList.add('active');}
function renderCours(){let h='';(D.fiches||[]).forEach(f=>h+=`<div class=card><small style=color:#f9c00f>${f.niveau} ${f.matiere}</small><h4>${f.titre}</h4><p style=color:#888;font-size:12px>${(f.contenu||'').slice(0,100)}...</p></div>`);document.getElementById('gridCours').innerHTML=h;}
function renderLex(){let q=(document.getElementById('sLex')?.value||'').toLowerCase();let list=D.lex||[];if(q)list=list.filter(l=>l.terme.toLowerCase().includes(q));let h='';list.forEach(l=>h+=`<div class=card><b>${l.terme}</b> <span class=badge style=background:#f9c00f>${l.niveau||'L1'}</span><p style=color:#aaa;font-size:12px;margin-top:4px>${l.def}</p></div>`);document.getElementById('gridLex').innerHTML=h;}
function renderFaq(){let h='';(D.faq||[]).forEach(f=>h+=`<div class=card><b>Q: ${f.q}</b><p style=color:#f9c00f;font-size:12px;margin-top:6px>R: ${f.r}</p></div>`);document.getElementById('gridFaq').innerHTML=h;}
function renderForum(){let h='';(D.forum||[]).slice().reverse().forEach(m=>{h+=`<div class="card forum-msg"><div class=forum-header><div><span class="badge role-${m.role}">${m.role}</span> <b style=font-size:13px>${m.nom}</b> <small style=color:#666;font-size:10px>• ${m.matiere}</small></div><small style=color:#666;font-size:9px>${m.time}</small></div><p style=font-size:13px;line-height:1.5;margin:8px 0>${m.msg}</p><div style=display:flex;gap:10px><small style=color:#f9c00f>❤️ ${m.likes||0} likes</small><small style=color:#666;cursor:pointer onclick=likeForum('${m.id}')>👍 J'aime</small><small style=color:#00e5ff;cursor:pointer>💬 Répondre</small></div></div>`});document.getElementById('gridForum').innerHTML=h;}
async function addLex(){await fetch('/api/lexique',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({terme:lexT.value,def:lexD.value})});loadAll();}
async function addFaq(){await fetch('/api/faq',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({q:fq.value,r:fr.value})});loadAll();}
async function postForum(){let d={role:forumRole.value,nom:forumNom.value,matiere:forumMat.value,msg:forumMsg.value};if(!d.nom||!d.msg)return alert('Mets ton nom et message!');await fetch('/api/forum',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)});forumMsg.value='';loadAll();}
function analyser(){let t=typeDos.value;let m={"Licenciement":"Travailleur: Inspection du Travail puis Tribunal du Travail","Dette":"TPI: Mise en demeure huissier obligatoire","Terre":"TPI Foncier + Conservation","Divorce":"TPI Famille","Vol/Escroquerie":"Plainte + Tribunal Correctionnel"};resDos.innerHTML=`<div class=card style=background:#111;margin-top:10px><b>${t}</b><br><small>${m[t]||'Voir un avocat'}</small></div>`;}
let cq=[], qi=0, sc=0;function startQuiz(){let lvl=ql.value;cq=D.quiz[lvl]||[];qi=0;sc=0;showQ();}
function showQ(){if(qi>=cq.length){qz.innerHTML=`<h3>${sc}/${cq.length} - ${sc==cq.length?'🏆 OR':sc>=2?'🥈 ARGENT':'🥉 BRONZE'}</h3><button class=btn onclick=startQuiz()>Rejouer</button>`;return}let q=cq[qi];let h=`<h4>${q.q}</h4>`;q.options.forEach((o,i)=>h+=`<div class=quiz-opt onclick="if(${i}==${q.rep})sc++;qi++;showQ()" style=cursor:pointer>${o}</div>`);qz.innerHTML=h;}
loadAll(); setInterval(loadAll,15000);
</script></body></html>
"""

@app.route("/api/fiches", methods=["GET","POST"])
def fiches_api():
    if request.method=="POST":
        d=request.get_json(); f=load(FILES["fiches"],[]); f.insert(0,{"id":uuid.uuid4().hex[:4],"niveau":d.get("niveau","L1"),"matiere":d.get("matiere",""),"titre":d.get("titre",""),"contenu":d.get("contenu",""),"auteur":d.get("auteur","")}); save(FILES["fiches"],f); return jsonify({"ok":True})
    return jsonify(load(FILES["fiches"],[]))

@app.route("/api/lexique", methods=["GET","POST"])
def lex_api():
    if request.method=="POST":
        d=request.get_json(); l=load(FILES["lexique"],[]); l.insert(0,{"terme":d.get("terme",""),"def":d.get("def",""),"niveau":"L1"}); save(FILES["lexique"],l); return jsonify({"ok":True})
    return jsonify(load(FILES["lexique"],[]))

@app.route("/api/faq", methods=["GET","POST"])
def faq_api():
    if request.method=="POST":
        d=request.get_json(); fa=load(FILES["faq"],[]); fa.insert(0,{"q":d.get("q",""),"r":d.get("r","")}); save(FILES["faq"],fa); return jsonify({"ok":True})
    return jsonify(load(FILES["faq"],[]))

@app.route("/api/quiz")
def quiz_api(): return jsonify(load(FILES["quiz"],{"L1":[],"L2":[],"L3":[]}))

@app.route("/api/forum", methods=["GET","POST"])
def forum_api():
    if request.method=="POST":
        d=request.get_json()
        allf=load(FILES["forum"], FORUM_INIT)
        allf.append({"id":uuid.uuid4().hex[:6],"role":d.get("role","Étudiant"),"nom":d.get("nom","Anonyme"),"matiere":d.get("matiere","Général"),"msg":d.get("msg",""),"time":datetime.now().strftime("%H:%M"),"likes":0})
        save(FILES["forum"], allf)
        return jsonify({"ok":True})
    return jsonify(load(FILES["forum"], FORUM_INIT))

@app.route("/api/forum/like/<fid>", methods=["POST"])
def like(fid):
    allf=load(FILES["forum"], FORUM_INIT)
    for m in allf:
        if m["id"]==fid: m["likes"]=m.get("likes",0)+1
    save(FILES["forum"], allf)
    return jsonify({"ok":True})

if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)))
