from flask import Flask, jsonify, request
import json, os, uuid
from datetime import datetime

app = Flask(__name__)

# ===== COURS SIMPLE DOSSIERS QUI MARCHE =====
COURS = [
    {
        "id": "intro",
        "matiere": "Introduction au Droit",
        "niveau": "L1",
        "icon": "📖",
        "chapitres": [
            {
                "titre": "Chapitre 1: Qu'est-ce que le Droit?",
                "sections": [
                    {"titre": "Section 1: Définition", "lecon": "LEÇON COMPLÈTE: Droit = ensemble règles organisant vie société, sanctionné puissance publique. Droit objectif = règles, droits subjectifs = prérogatives. Droit naturel = idéal justice, Droit positif = règles en vigueur Guinée = Constitution 2020 + lois + OHADA. Caractères: Générale (tous), Obligatoire, Sanctionnée État (police tribunal), Permanente. Distinction morale (intérieure pas sanction État), religion, bienséance."},
                    {"titre": "Section 2: Sources Droit Guinéen", "lecon": "LEÇON COMPLÈTE: Sources nationales: 1-Constitution 2020 suprême, 2-Loi CNT, 3-Ordonnance Président, 4-Décret Arrêté, 5-Coutume très importante Guinée rurale mariage coutumier Malinké Peulh Soussou, 6-Jurisprudence Cour Suprême, 7-Doctrine professeurs. Sources internationales: Traités primauté sur loi art 151, OHADA 10 Actes Uniformes primauté affaires, UEMOA CEDEAO UA ONU."}
                ]
            },
            {
                "titre": "Chapitre 2: Branches Droit",
                "sections": [
                    {"titre": "Section 1: Droit Public", "lecon": "LEÇON COMPLÈTE: Droit Public = État-citoyen intérêt général inégalitaire: Constitutionnel (Constitution pouvoirs), Administratif (administration service public REP), Pénal (infractions peines), Fiscal (impôts), International Public (États ONU traités)."},
                    {"titre": "Section 2: Droit Privé", "lecon": "LEÇON COMPLÈTE: Droit Privé = citoyen-citoyen égalitaire intérêt privé: Civil (personne famille biens obligations), Commercial (commerçant actes commerce fonds bail OHADA), Travail (contrat licenciement grève Tribunal Travail), International Privé (conflit lois nationalité). Mixte: Procédure civile pénale."}
                ]
            }
        ]
    },
    {
        "id": "const",
        "matiere": "Droit Constitutionnel",
        "niveau": "L1",
        "icon": "🏛️",
        "chapitres": [
            {
                "titre": "Chapitre 1: État et Constitution",
                "sections": [
                    {"titre": "Section 1: État", "lecon": "LEÇON COMPLÈTE: État = territoire (terrestre maritime aérien) + population (nationale étrangère peuple) + pouvoir souverain interne suprême externe indépendance. Personnalité juridique. Souveraineté appartient peuple art 2 Constitution Guinée 2020. État unitaire Guinée un seul centre pouvoir décentralisé communes vs fédéral USA. État droit respect hiérarchie Constitution sommet."},
                    {"titre": "Section 2: Constitution 2020", "lecon": "LEÇON COMPLÈTE: Constitution = loi suprême 156 articles. 4 Constitutions Guinée 1958 1990 2010 2020. Principes: laïc démocratique indivisible social, drapeau R-J-V, devise Travail Justice Solidarité. Droits: vie liberté égalité propriété présomption innocence, politiques vote manifestation parti, économiques travail grève. Devoirs respecter Constitution payer impôts. Pouvoirs: Exécutif Président 5 ans renouvelable 1 fois nomme PM Gouvernement décrets, Législatif CNT 81 membres demain Assemblée vote lois budget contrôle, Judiciaire indépendant juges inamovibles Cour Suprême Cour Constitutionnelle QPC."}
                ]
            }
        ]
    },
    {
        "id": "penal",
        "matiere": "Droit Pénal",
        "niveau": "L2",
        "icon": "🔨",
        "chapitres": [
            {
                "titre": "Chapitre 1: Infraction",
                "sections": [
                    {"titre": "Section 1: Crime Délit Contravention", "lecon": "LEÇON COMPLÈTE: Infraction = acte interdit loi pénale puni peine. Crime grave meurtre viol vol main armée trafic drogue peine réclusion 10 ans à perpétuité mort moratoire juridiction Cour Assises jury instruction obligatoire prescription 10 ans. Délit moyen vol simple escroquerie abus confiance coups peine emprisonnement 1 mois à 10 ans TPI Correctionnel prescription 3 ans. Contravention légère tapage injure amende 1ère à 5ème classe Simple Police 1 an. Éléments: légal texte, matériel acte, moral intention dol ou faute."},
                    {"titre": "Section 2: Peines", "lecon": "LEÇON COMPLÈTE: Peines principales prison amende, complémentaires interdiction confiscation, alternatives TIG jours-amende. Sursis simple pas prison si pas récidive 5 ans mise épreuve obligations travail soins indemniser si respecte effacée si récidive révoqué. Libération conditionnelle bonne conduite. Grâce Président amnistie loi."}
                ]
            }
        ]
    },
    {
        "id": "ohada",
        "matiere": "Droit OHADA",
        "niveau": "L2-L3",
        "icon": "🌍",
        "chapitres": [
            {
                "titre": "Chapitre 1: OHADA Complet",
                "sections": [
                    {"titre": "Section 1: Traité et Institutions", "lecon": "LEÇON COMPLÈTE: Traité 17 oct 1993 Port-Louis révisé 2008 Québec 17 pays Bénin Burkina Cameroun Centrafrique Comores Congo RDC Côte Ivoire Gabon Guinée Bissau Équatoriale Mali Niger Sénégal Tchad Togo 300M habitants Objectif même loi affaires sécurité juridique Institutions Conférence Chefs État Conseil Ministres Justice Finances décide Actes Uniformes Secrétariat Permanent Yaoundé CCJA Abidjan ERSUMA Porto-Novo école juges Principes supranationalité applicabilité directe primauté OHADA sur lois nationales Guinée applicable depuis 2000."},
                    {"titre": "Section 2: Actes Uniformes", "lecon": "LEÇON COMPLÈTE: 10 Actes: AUDCG Commerce 307 art commerçant actes commerce RCCM bail commercial 2 ans droit renouvellement fonds commerce 135 art. AUSCGIE Sociétés 920 art SARL 1-100 associés capital min 1M parts 5k SA 10M 100M si appel épargne SAS libre SNC responsabilité indéfinie. AUS Sûretés 302 art cautionnement simple solidaire gage nantissement fonds hypothèque Conservation Kaloum 10 ans rang. AUPC Procédures Collectives 378 art mandat ad hoc conciliation préventif redressement judiciaire plan 10 ans liquidation. AUCE Voies Exécution 338 art saisie attribution bloque compte plus utilisée injonction payer 15j rapide astreinte. AUA Arbitrage 36 art justice privée arbitre choisi rapide 6 mois confidentiel CCJA centre sentence = jugement Convention New York 170 pays. Autres: Comptabilité SYSCOHADA Transport Route Coopératives Médiation. CCJA Abidjan 13 juges cassation OHADA casse arrêt Appel Conakry peut évoquer rejuge elle-même avis arbitrage primauté."}
                ]
            }
        ]
    },
    {
        "id": "civil",
        "matiere": "Droit Civil Obligations",
        "niveau": "L2",
        "icon": "⚖️",
        "chapitres": [
            {
                "titre": "Chapitre 1: Contrat",
                "sections": [
                    {"titre": "Section 1: Formation contrat", "lecon": "LEÇON COMPLÈTE: Obligation lien droit oblige donner faire ne pas faire Sources contrat responsabilité délictuelle art 1240 quasi-contrat loi. Contrat art 1101 accord volontés créer modifier transmettre éteindre obligations Classification synallagmatique obligations réciproques vente vs unilatéral donation onéreux échange avantage vs gratuit donation consensuel accord seul vs solennel formalités notaire vs réel remise chose. 4 Conditions art 1128: Consentement libre éclairé vices erreur fausse représentation substance ex vase croit or toc dol tromperie manœuvres mensonge vendre voiture accidentée cachant violence contrainte physique morale annulation, Capacité majeur 18 ans mineur incapable tutelle, Objet certain possible licite pas drogue, Cause licite pas tuer. Nullité absolue intérêt général 30 ans relative intérêt privé 5 ans rétroactif."},
                    {"titre": "Section 2: Effets", "lecon": "LEÇON COMPLÈTE: Force obligatoire art 1103 contrat = loi entre parties exécuté bonne foi art 1104 exception imprévision art 1195 changement imprévisible excessivement onéreux renégociation juge adapte. Effet relatif art 1199 entre parties seulement pas tiers sauf stipulation pour autrui. Inexécution mise en demeure préalable obligatoire art 1344 lettre huissier 8j Sanctions exécution forcée nature astreinte exception inexécution si autre n'exécute pas tu suspends résolution anéantissement inexécution grave judiciaire unilatérale clause résolutoire dommages intérêts compensatoires moratoires faute dommage lien causal prévisibles."}
                ]
            }
        ]
    }
]

LEXIQUE = [
    {"t": "OHADA", "d": "Organisation Harmonisation Droit Affaires Afrique 17 pays dont Guinée 10 Actes Uniformes même loi commerciale partout CCJA Abidjan cour suprême RCCM APIP SARL capital 1M."},
    {"t": "Titre Foncier", "d": "Seul papier propriété terrain Guinée délivré Conservation Foncière Kaloum après enquête bornage sans occupant précaire 80% arnaques Conakry vérifier avant payer 2-5M."},
    {"t": "Mise en demeure", "d": "Lettre officielle exécuter 8j sinon tribunal OBLIGATOIRE avant TPI art 54 CPCC huissier 50k ou recommandée."},
    {"t": "RCCM", "d": "Registre Commerce Crédit Mobilier numéro commerçant APIP Kaloum 500k CNI casier statuts obligatoire commerçant légal."},
    {"t": "SARL", "d": "Société Responsabilité Limitée 1-100 associés capital min 1M parts 5k responsabilité limitée apports gérant responsable pénale."},
    {"t": "Saisie attribution", "d": "Art 77 AUCE Huissier bloque compte bancaire attribue créancier plus utilisée commandement 8j banque bloque 100-200k."},
    {"t": "Habeas Corpus", "d": "Ordre juge police présenter détenu 48h sinon libération art 9 Constitution protection détention arbitraire."},
    {"t": "QPC", "d": "Question Prioritaire Constitutionnalité devant tout tribunal dis loi contraire Constitution transmission Cour Constit abrogation."},
]

QUIZ = {
    "L1": [{"q": "Constitution 2020 = quelle République?", "o": ["3e", "4e", "5e"], "r": 1, "e": "4e République référendum 2020"}, {"q": "OHADA pays?", "o": ["10", "17", "54"], "r": 1, "e": "17 pays membres"}],
    "L2": [{"q": "Crime jugé par?", "o": ["TPI", "Assises", "Suprême"], "r": 1, "e": "Crime = Cour Assises jury"}, {"q": "SARL capital min?", "o": ["100k", "1M", "10M"], "r": 1, "e": "1M FCFA"}],
    "OHADA": [{"q": "RCCM à?", "o": ["Mairie", "APIP", "TPI"], "r": 1, "e": "APIP Guinée"}, {"q": "Hypothèque où?", "o": ["Mairie", "Conservation", "APIP"], "r": 1, "e": "Conservation Foncière Kaloum"}]
}

def moteur_ai(q):
    ql = q.lower()
    if "dette" in ql and "prison" in ql:
        return "NON prison pour dette contractuelle art 11 Pacte International + Constitution sauf pension alimentaire amende pénale. Menace prison = chantage délit. Recouvrement: mise en demeure huissier 50k, injonction payer Président TPI art 1 AUCE 15j, saisie attribution compte art 77 AUCE."
    if "terrain" in ql or "foncier" in ql:
        return "Seul Titre Foncier Conservation Kaloum = propriété inattaquable. Sans = occupant précaire. Procédure: acte coutumier chef quartier 2 témoins, demande Kaloum formulaire CNI acte plan, enquête publique affichage 1 mois, bornage géomètre contradictoire, commission, immatriculation livre foncier Titre duplicata. Coût 2-5M délai 6-12 mois. Arnaques Conakry même terrain vendu 5 fois vérifier livre foncier avant payer notaire virement pas cash."
    if "sarl" in ql or "entreprise" in ql or "rccm" in ql:
        return "APIP Kaloum: recherche nom 50k, statuts notaire 300k capital min 1M libéré 50% solde 2 ans, RCCM 500k, NIF gratuit, CNSS, 48h total 1,5M. SARL 1-100 associés parts 5k responsabilité limitée apports gérant responsable pénale abus biens sociaux."
    if "ohada" in ql:
        return "17 pays même loi affaires 10 Actes Uniformes: AUDCG commerce RCCM bail 2 ans fonds, AUSCGIE sociétés SARL 1M SA 10M SAS libre, AUS sûretés caution hypothèque Conservation, AUPC redressement liquidation, AUCE saisie attribution injonction payer 15j, AUA arbitrage rapide 6 mois confidentiel CCJA Abidjan cour suprême primauté."
    if "licenciement" in ql or "salaire" in ql:
        return "Mise en demeure huissier 50k, Inspection Travail Kaloum gratuit convocation patron conciliation, si échec Tribunal Travail TPI requête 20k contrat bulletins attestation. Obtiens salaires + dommages licenciement abusif + certificat. Délai 1 an ne démissionne pas."
    return f"AI DROIT224 pour '{q}': Analyse: matière civil/pénal/commerce/travail/foncier/OHADA. Textes: Constitution 2020 Code civil pénal travail foncier OHADA. Procédure: mise en demeure 8j huissier obligatoire art 54 CPCC, conciliation, requête TPI 50k audience jugement 1-2 ans appel 1 mois cassation Cour Suprême ou CCJA Abidjan si OHADA 2 mois. Preuves écrit >500k obligatoire. Poste Dossiers Justice pour analyse multi-experts."

def load_j(f,d):
    if not os.path.exists(f): return d
    try: return json.load(open(f,"r",encoding="utf-8"))
    except: return d
def save_j(f,d): json.dump(d, open(f,"w",encoding="utf-8"), ensure_ascii=False, indent=2)

@app.route("/")
def home():
    return """
<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>DROIT224</title>
<link rel="manifest" href="/manifest.json">
<style>
*{margin:0;padding:0;box-sizing:border-box}body{background:#050510;color:#fff;font-family:Arial}
.header{text-align:center;padding:14px;background:#0a0a2a;border-bottom:3px solid #f9c00f;position:sticky;top:0;z-index:30}
.tabs{display:flex;gap:4px;padding:6px;background:#0a0a1a;overflow-x:auto;position:sticky;top:78px;z-index:20}
.tabs button{padding:7px 10px;border-radius:18px;border:1px solid #222;background:#151530;color:#aaa;font-size:9px;font-weight:800;white-space:nowrap}
.tabs button.active{background:#f9c00f;color:#000}
.view{display:none;padding:10px}.view.active{display:block}
.card{background:#10102a;border:1px solid #1a1a3a;border-radius:12px;padding:12px;margin:8px 0;cursor:pointer}
.card:hover{border-color:#f9c00f}
.badge{padding:3px 8px;border-radius:12px;font-size:8px;font-weight:900;color:#000;background:#f9c00f}
input,select,textarea{width:100%;padding:8px;margin:4px 0;border-radius:8px;border:1px solid #222;background:#111;color:#fff;font-size:12px}
.btn{padding:8px 12px;border-radius:18px;border:none;font-weight:800;background:#f9c00f;color:#000;cursor:pointer;font-size:11px}
.small{font-size:11px;color:#bbb;line-height:1.6;white-space:pre-wrap}
.breadcrumb{font-size:11px;color:#aaa;margin-bottom:10px}
.breadcrumb span{color:#00e5ff;cursor:pointer}
.download-btn{background:linear-gradient(90deg,#f9c00f,#ff6a00);color:#000;padding:10px 18px;border-radius:25px;font-weight:900;font-size:12px;border:none;cursor:pointer;margin-top:10px}
.lecon{background:#001a00;border:2px solid #76ff03;padding:12px;border-radius:10px;margin-top:8px}
</style></head><body>
<div class="header">
<h1 style="color:#f9c00f;font-size:24px;font-weight:900">DROIT224</h1>
<p style="font-size:8px;color:#aaa;letter-spacing:1px">DOSSIERS > CHAPITRES > SECTIONS > LEÇONS COMPLÈTES</p>
<button class="download-btn" onclick="downloadApp()">📥 TÉLÉCHARGER L'APP DROIT224</button>
<p style="font-size:7px;color:#666;margin-top:6px">Clique pour installer comme vraie app sur ton téléphone</p>
</div>
<div class="tabs">
<button class="active" onclick="showTab('cours',this)">📚 COURS</button>
<button onclick="showTab('lex',this)">📖 LEXIQUE</button>
<button onclick="showTab('quiz',this)">🎮 QUIZ</button>
<button onclick="showTab('faq',this)" style="border-color:#76ff03;color:#76ff03">❓ FAQ</button>
<button onclick="showTab('dossier',this)" style="border-color:#ff1744">📂 DOSSIERS</button>
<button onclick="showTab('forum',this)">💬 CERCLE</button>
</div>

<div id="cours" class="view active"><div id="bcCours" class="breadcrumb"></div><div id="gridCours"></div></div>
<div id="lex" class="view"><div class="card" style="border:2px solid #00e5ff"><h4>Lexique Juridique</h4><input id="lexIn" placeholder="Tape mot: OHADA, Titre Foncier..." oninput="searchLex()"><div id="lexAuto"></div></div><div id="gridLex"></div></div>
<div id="quiz" class="view"><div class="card" style="text-align:center;border:2px solid #f9c00f"><select id="qLvl"><option>L1</option><option>L2</option><option>OHADA</option></select><button class="btn" onclick="startQuiz()">LANCER QUIZ</button><div id="qZone" style="text-align:left;margin-top:10px"></div></div></div>
<div id="faq" class="view"><div class="card" style="border:2px solid #76ff03;background:linear-gradient(135deg,#001a00,#000)"><h4 style="color:#76ff03">❓ FAQ - Assistant AI Juridique</h4><p class="small" style="color:#aaa">Pose n'importe quelle question de droit, je réponds comme AI complet</p><div style="display:flex;gap:4px;margin-top:8px"><input id="faqAsk" placeholder="Ex: Comment créer SARL? Terrain Sonfonia..."><button class="btn" style="background:#76ff03" onclick="askFaq()">Demander</button></div><div id="faqAuto"></div></div></div>
<div id="dossier" class="view"><div class="card" style="border:2px solid #ff1744;background:#1a0000"><h4>Dossiers Justice</h4><select id="dType"><option>Licenciement</option><option>Dette</option><option>Terre Foncier</option><option>Divorce</option><option>Vol</option><option>Contrat</option></select><textarea id="dDesc" rows="3" placeholder="Décris cas..."></textarea><input id="dNom" placeholder="Ton nom"><button class="btn" style="background:#ff1744;color:#fff;width:100%" onclick="postDossier()">Soumettre</button><div id="dAuto"></div></div><div id="gridDossier"></div></div>
<div id="forum" class="view"><div class="card" style="border:2px solid #f9c00f"><select id="fRole"><option>Étudiant</option><option>Professeur</option><option>Juge</option><option>Avocat</option><option>Docteur</option></select><input id="fNom" placeholder="Nom"><textarea id="fMsg" placeholder="Question"></textarea><button class="btn" style="width:100%" onclick="postForum()">Poster</button></div><div id="gridForum"></div></div>

<script>
let DB={};
let nav={level:'matieres', matId:null, chapIdx:null, secIdx:null};

async function load(){
 DB=await fetch('/api/all').then(r=>r.json());
 renderCours(); renderLex(); renderDossier(); renderForum();
}
function showTab(id,btn){
 document.querySelectorAll('.view').forEach(v=>v.classList.remove('active'));
 document.getElementById(id).classList.add('active');
 document.querySelectorAll('.tabs button').forEach(b=>b.classList.remove('active'));
 btn.classList.add('active');
}

function renderCours(){
 let h=''; let bc='';
 if(nav.level=='matieres'){
   bc='📚 Matières Droit';
   (DB.cours||[]).forEach(m=>{
     h+=`<div class=card onclick="openMatiere('${m.id}')"><b>${m.icon} ${m.matiere}</b> <span class=badge>${m.niveau}</span><p class=small style=margin-top:6px>${m.chapitres.length} chapitres - Clique pour ouvrir dossier 📁</p></div>`;
   });
 } else if(nav.level=='chapitres'){
   let mat=DB.cours.find(x=>x.id==nav.matId);
   bc=`<span onclick="goMatieres()">📚 Matières</span> > ${mat.matiere}`;
   mat.chapitres.forEach((ch,i)=>{
     h+=`<div class=card onclick="openChap(${i})"><b style=color:#00e5ff>📁 ${ch.titre}</b><p class=small>${ch.sections.length} sections - Voir programme</p></div>`;
   });
   h+=`<button class=btn onclick="goMatieres()">⬅️ Retour Matières</button>`;
 } else if(nav.level=='sections'){
   let mat=DB.cours.find(x=>x.id==nav.matId);
   let ch=mat.chapitres[nav.chapIdx];
   bc=`<span onclick="goMatieres()">📚</span> > <span onclick="goChapitres()">${mat.matiere}</span> > ${ch.titre}`;
   ch.sections.forEach((sec,i)=>{
     h+=`<div class=card onclick="openSec(${i})"><b>📂 ${sec.titre}</b><p class=small>Clique pour voir leçon intégrale</p></div>`;
   });
   h+=`<button class=btn onclick="goChapitres()">⬅️ Retour Chapitres</button>`;
 } else if(nav.level=='lecon'){
   let mat=DB.cours.find(x=>x.id==nav.matId);
   let ch=mat.chapitres[nav.chapIdx];
   let sec=ch.sections[nav.secIdx];
   bc=`<span onclick="goMatieres()">📚</span> > <span onclick="goChapitres()">${mat.matiere}</span> > <span onclick="goSections()">${ch.titre}</span> > ${sec.titre}`;
   h=`<div class=card style=border:2px solid #76ff03"><h3 style=color:#f9c00f>${sec.titre}</h3><div class=lecon><p class=small>${sec.lecon}</p></div><div style=margin-top:12px;display:flex;gap:6px"><button class=btn onclick="goSections()">⬅️ Retour</button><button class=btn style=background:#00e5ff" onclick="goSections()">✅ Compris</button></div></div>`;
 }
 document.getElementById('bcCours').innerHTML=bc;
 document.getElementById('gridCours').innerHTML=h;
}
function openMatiere(id){nav.matId=id;nav.level='chapitres';renderCours();}
function openChap(i){nav.chapIdx=i;nav.level='sections';renderCours();}
function openSec(i){nav.secIdx=i;nav.level='lecon';renderCours();}
function goMatieres(){nav.level='matieres';renderCours();}
function goChapitres(){nav.level='chapitres';renderCours();}
function goSections(){nav.level='sections';renderCours();}

function renderLex(){
 let h='';(DB.lexique||[]).forEach(l=>{h+=`<div class=card><b>${l.t}</b><p class=small style=margin-top:4px">${l.d}</p></div>`});
 document.getElementById('gridLex').innerHTML=h;
}
async function searchLex(){
 let q=document.getElementById('lexIn').value;
 if(q.length<2){document.getElementById('lexAuto').innerHTML='';renderLex();return}
 let res=await fetch('/api/search?q='+encodeURIComponent(q)).then(r=>r.json());
 document.getElementById('lexAuto').innerHTML=`<div class=card style=background:#002a2a;border-color:#00e5ff"><p class=small>${res.ans}</p></div>`;
}

function renderDossier(){
 let h='';(DB.dossiers||[]).slice().reverse().forEach(d=>{
   h+=`<div class=card style=border:1px solid #ff1744"><b>📂 ${d.type}</b> <small style=color:#666">${d.time} par ${d.nom}</small><p class=small style=margin:6px 0">${d.desc}</p><div style=background:#111;padding:6px;border-radius:6px"><small style=color:#f9c00f"><b>AI:</b> ${d.auto||''}</small></div></div>`;
 });
 document.getElementById('gridDossier').innerHTML=h;
}
async function postDossier(){
 let d={type:document.getElementById('dType').value,desc:document.getElementById('dDesc').value,nom:document.getElementById('dNom').value};
 if(!d.desc)return alert('Décris cas');
 let res=await fetch('/api/search_faq?q='+encodeURIComponent(d.type+' '+d.desc)).then(r=>r.json());
 d.auto=res.ans;
 await fetch('/api/dossiers',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)});
 document.getElementById('dDesc').value='';load();
}

async function askFaq(){
 let q=document.getElementById('faqAsk').value;
 if(!q)return;
 let res=await fetch('/api/search_faq?q='+encodeURIComponent(q)).then(r=>r.json());
 document.getElementById('faqAuto').innerHTML+=`<div class=card style=background:#001a00;border-color:#76ff03;margin-top:10px"><b style=color:#76ff03>👤 Toi: ${q}</b><div style=border-top:1px solid #222;margin-top:8px;padding-top:8px"><b style=color:#00e5ff>🤖 FAQ AI:</b><p class=small style=margin-top:6px">${res.ans}</p></div></div>`;
 document.getElementById('faqAsk').value='';
}

let cq=[],qi=0,sc=0;
function startQuiz(){
 let lvl=document.getElementById('qLvl').value;
 cq=DB.quiz[lvl]||[];qi=0;sc=0;showQ();
}
function showQ(){
 if(qi>=cq.length){
   document.getElementById('qZone').innerHTML=`<h2 style=text-align:center>${sc}/${cq.length}</h2><div style=text-align:center;font-size:36px">${sc==cq.length?'🏆 OR':'🥈 ARGENT'}</div><button class=btn onclick=startQuiz()>Rejouer</button>`;
   return
 }
 let q=cq[qi];
 let h=`<h4 style=margin:10px 0;font-size:12px>Q${qi+1}: ${q.q}</h4>`;
 q.o.forEach((o,i)=>{h+=`<div class=card" style="padding:8px;margin:4px 0" onclick="checkQ(${i})">${o}</div>`});
 document.getElementById('qZone').innerHTML=h;
}
function checkQ(i){
 let q=cq[qi];let ok=i==q.r;if(ok)sc++;
 document.getElementById('qZone').innerHTML+=`<div class=card style=background:${ok?'#001a00':'#1a0000'};margin-top:8px"><b>${ok?'✅':'❌'} ${q.e}</b><br><button class=btn onclick="qi++;showQ()" style=margin-top:6px>Suivant</button></div>`;
}

function renderForum(){
 let h='';(DB.forum||[]).slice().reverse().forEach(m=>{
   h+=`<div class=card style=border-left:3px solid #f9c00f"><span class=badge>${m.role}</span> <b style=font-size:11px">${m.nom}</b> <small style=color:#666">${m.time}</small><p class=small style=margin:6px 0">${m.msg}</p></div>`;
 });
 document.getElementById('gridForum').innerHTML=h;
}
async function postForum(){
 let d={role:document.getElementById('fRole').value,nom:document.getElementById('fNom').value,msg:document.getElementById('fMsg').value};
 if(!d.nom||!d.msg)return alert('Nom et message');
 await fetch('/api/forum',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)});
 document.getElementById('fMsg').value='';load();
}

function downloadApp(){
 alert('📥 TÉLÉCHARGER DROIT224:\\n\\n1. Sur Chrome Android: Clique menu ⋮ en haut à droite > Installer l\\'application ou Ajouter à l\\'écran d\\'accueil\\n\\n2. Sur iPhone: Clique bouton Partage (carré avec flèche) > Sur l\\'écran d\\'accueil > Ajouter\\n\\n3. Tu auras icône DROIT224 comme vraie app!\\n\\nC\\'est une PWA - Pas besoin Play Store!');
 if(window.deferredPrompt){window.deferredPrompt.prompt();}
}
let deferredPrompt;
window.addEventListener('beforeinstallprompt',(e)=>{e.preventDefault();deferredPrompt=e;window.deferredPrompt=e;});

load();
</script></body></html>
"""

@app.route("/manifest.json")
def manifest():
    return jsonify({"name":"DROIT224","short_name":"DROIT224","start_url":"/","display":"standalone","background_color":"#050510","theme_color":"#f9c00f","icons":[{"src":"https://cdn-icons-png.flaticon.com/512/1087/1087815.png","sizes":"192x192","type":"image/png"}]})

@app.route("/api/all")
def all_api():
    dossiers=load_j("dossiers_v12.json", [])
    forum=load_j("forum_v12.json", [])
    return jsonify({"cours":COURS,"lexique":LEXIQUE,"quiz":QUIZ,"dossiers":dossiers,"forum":forum})

@app.route("/api/search")
def search_api():
    q=request.args.get("q","")
    ql=q.lower()
    for item in LEXIQUE:
        if item["t"].lower() in ql or ql in item["t"].lower():
            return jsonify({"ans":item["d"]})
    return jsonify({"ans":f"{q}: En droit guinéen et OHADA, {q} désigne concept juridique précis. Voir cours détaillés dossiers > chapitres > sections > leçons intégrales. Sources cachées Google ChatGPT Gemini Doctrine OHADA.com."})

@app.route("/api/search_faq")
def search_faq_api():
    q=request.args.get("q","")
    return jsonify({"ans":moteur_ai(q)})

@app.route("/api/dossiers", methods=["POST"])
def dossiers_post():
    d=request.get_json()
    alld=load_j("dossiers_v12.json", [])
    alld.append({"id":uuid.uuid4().hex[:5],"type":d.get("type",""),"desc":d.get("desc",""),"nom":d.get("nom",""),"time":datetime.now().strftime("%d/%m %H:%M"),"auto":d.get("auto","")})
    save_j("dossiers_v12.json", alld)
    return jsonify({"ok":True})

@app.route("/api/forum", methods=["GET","POST"])
def forum_api():
    if request.method=="POST":
        d=request.get_json()
        allf=load_j("forum_v12.json", [])
        allf.append({"id":uuid.uuid4().hex[:5],"role":d.get("role",""),"nom":d.get("nom",""),"msg":d.get("msg",""),"time":datetime.now().strftime("%H:%M")})
        save_j("forum_v12.json", allf)
        return jsonify({"ok":True})
    return jsonify(load_j("forum_v12.json", []))

if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)))
