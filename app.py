from flask import Flask, jsonify, request
import json, os, uuid
from datetime import datetime
app = Flask(__name__)

# ================== DONNÉES COMPLÈTES ==================

COURS = [
    # L1
    {"n":"L1","s":"S1","m":"Introduction Droit","t":"C'est quoi le Droit?","c":"Droit = règles de vie en société. 2 branches: Public (État-citoyen) et Privé (citoyen-citoyen). Sources: Constitution 2020, Loi, Coutume, Jurisprudence. But: Paix, Justice, Ordre. Sans Droit = anarchie.","a":"Prof Camara"},
    {"n":"L1","s":"S1","m":"Constitutionnel","t":"Constitution Guinée 2020","c":"Loi suprême. 4ème République. 3 pouvoirs: Président (Exécutif), CNT (Législatif), Juges (Judiciaire). Droits: liberté, égalité, propriété, manifestation. Révision par référendum. Cour Constitutionnelle juge constitutionnalité.","a":"Dr Diallo"},
    {"n":"L1","s":"S1","m":"Histoire Droit","t":"Droit Guinéen - Histoire","c":"Précolonial: Droit coutumier Malinké, Peulh, Soussou. Colonial: Code civil français 1804 imposé. 1958: Indépendance, Sékou Touré garde droit français. 1993: Démocratie. 2000: OHADA arrive. 2020: Nouvelle Constitution.","a":"Prof Bangoura"},
    {"n":"L1","s":"S2","m":"Droit Civil 1","t":"Personne Physique et Morale","c":"Personne physique: humain dès naissance jusqu'à mort. Droits: nom, prénom, domicile, patrimoine. Personne morale: société, État, association. A une personnalité juridique distincte. Capacité: 18 ans = capable. Mineur = incapable sauf émancipation.","a":"Prof Camara"},
    {"n":"L1","s":"S2","m":"Droit Administratif","t":"Administration Guinéenne","c":"Administration = État qui gère. Principes: Service public continu, égalité, légalité. Actes: Décret Président, Arrêté Ministre, Décision Préfet. Recours: REP au Tribunal Administratif si excès de pouvoir. Délai 2 mois.","a":"Juge Admin"},
    # L2
    {"n":"L2","s":"S3","m":"Droit Pénal","t":"Crime, Délit, Contravention","c":"Infraction = acte interdit par Code pénal. CRIME: meurtre, viol, vol à main armée => Cour d'Assises, 10 ans à perpet. DÉLIT: vol simple, escroquerie, abus confiance => Correctionnel, 1 mois à 10 ans. CONTRAVENTION: tapage, injure => Police, amende. 3 éléments: légal, matériel, moral (intention).","a":"Procureur"},
    {"n":"L2","s":"S3","m":"Obligations","t":"Contrat - 4 Conditions","c":"Contrat = accord créant obligations. 4 conditions validité: 1-Consentement libre (pas erreur, dol, violence), 2-Capacité (majeur non fou), 3-Objet certain et licite, 4-Cause licite. Si manque = nullité. Force obligatoire art 1103: contrat = loi entre parties. Inexécution = dommages intérêts + résolution.","a":"Dr Sow"},
    {"n":"L2","s":"S3","m":"Droit Commercial","t":"Commerçant et RCCM","c":"Commerçant = fait actes de commerce habituellement. Actes commerce: achat pour revendre, transport, banque. Obligations: RCCM à APIP (500k), comptabilité, NIF. Sans RCCM = pas commerçant légal, pas accès crédits. Prescription commerce = 5 ans.","a":"APIP"},
    {"n":"L2","s":"S4","m":"Procédure Pénale","t":"Garde à vue et Procès","c":"Déroulement: Plainte -> Enquête police (garde à vue 48h renouvelable) -> Instruction (juge instruction) -> Procès. Droits gardé à vue: avocat 1ère heure, médecin, prévenir famille, silence. Preuves: aveu, témoignage, expertise, perquisition. Présomption innocence.","a":"Juge Instruction"},
    {"n":"L2","s":"S4","m":"Droit du Travail","t":"Licenciement en Guinée","c":"CDI = contrat normal. CDD = max 2 ans. Licenciement: motif réel et sérieux obligatoire. Procédure: convocation entretien, lettre licenciement, préavis, certificat travail, solde. Sans motif = abusif => dommages au Tribunal Travail. Inspection Travail Kaloum = gratuit, tente conciliation d'abord.","a":"Inspecteur Travail"},
    # L3
    {"n":"L3","s":"S5","m":"Sociétés","t":"SARL en Guinée - Création","c":"SARL = Société à Responsabilité Limitée. Avantage: tu risques seulement apport, pas biens perso. Étapes: 1-Statuts notaire 300k, 2-RCCM APIP 500k, 3-NIF gratuit Impôts, 4-CNSS. Capital min OHADA: 1.000.000 GNF. Gérant = responsable pénalement. Associés max 100.","a":"Notaire Conakry"},
    {"n":"L3","s":"S5","m":"Procédure Civile","t":"Comment saisir TPI?","c":"TPI = Tribunal Première Instance. Étapes: 1-Mise en demeure par huissier (OBLIGATOIRE), 2-Assignation par huissier (cite adversaire), 3-Dépôt greffe TPI 50k, 4-Échange conclusions, 5-Audience, 6-Jugement (1-2 ans à Conakry). Appel = Cour d'Appel Conakry délai 1 mois. Exécution = huissier.","a":"Huissier"},
    {"n":"L3","s":"S6","m":"Foncier","t":"Titre Foncier = Seule Preuve","c":"80% procès Guinée = terre! Règle: Sans Titre Foncier = pas propriétaire! Procédure: 1-Acte vente coutumier chef quartier, 2-Demande à Conservation Foncière Kaloum, 3-Enquête terrain, 4-Bornage géomètre, 5-Titre (2-5M, 6 mois). DANGER: Faux titres partout Madina, Sonfonia. Toujours vérifier à Kaloum avant payer!","a":"Conservateur"},
    {"n":"L3","s":"S6","m":"Voies Exécution","t":"Huissier et Saisie","c":"Tu as jugement mais adversaire ne paie pas? Huissier exécute: Saisie attribution (bloque compte bancaire), Saisie vente (vend ses meubles/voiture), Saisie immobilière (vend maison), Expulsion. Délai prescription exécution: 10 ans. Astreinte = argent par jour retard.","a":"Huissier"},
]

OHADA_COURS = [
    {"t":"OHADA - C'est quoi?","c":"OHADA = Organisation pour l'Harmonisation en Afrique du Droit des Affaires. Créée 1993 à Port-Louis. 17 pays membres: Bénin, Burkina, Cameroun, Centrafrique, Comores, Congo, Congo RDC, Côte d'Ivoire, Gabon, Guinée, Guinée-Bissau, Guinée Équatoriale, Mali, Niger, Sénégal, Tchad, Togo. But: Même loi affaires partout!"},
    {"t":"Acte Uniforme Droit Commercial Général","c":"AUDCG: Définit commerçant, RCCM, bail commercial, fonds commerce, intermédiaires (courtier, commissionnaire), vente commerciale. En Guinée: tout commerçant doit avoir RCCM APIP. Bail commercial: durée 2 ans min, droit au renouvellement. Fonds commerce = clientèle + matériel + bail."},
    {"t":"Acte Uniforme Sociétés et GIE","c":"AUSCGIE: Régit SARL, SA, SNC, SCS, SAS. SARL: 1-100 associés, capital min 1M. SA: 1 associé min, capital 10M, conseil administration. SAS: très libre, pour startups. Formalités: statuts, RCCM, annonces légales. Gérant/PDG responsable civilement et pénalement."},
    {"t":"Acte Uniforme Sûretés","c":"AUS: Garanties pour payer dettes. Sûretés personnelles: cautionnement (quelqu'un se porte garant). Sûretés réelles: gage (meuble), nantissement (fonds commerce), hypothèque (immeuble), propriété retenue. En Guinée banque exige toujours sûreté avant crédit. Hypothèque doit être inscrite à Conservation Foncière."},
    {"t":"Acte Uniforme Procédures Collectives","c":"AUPC: Entreprise en difficulté. 3 procédures: 1-Mandat ad hoc (négociation), 2-Redressement judiciaire (tente sauver entreprise, gel dettes), 3-Liquidation biens (ferme et vend tout). Déclaration cessation paiements dans 30 jours obligatoire sinon dirigeant responsable. Ordre paiement créanciers."},
    {"t":"Acte Uniforme Voies d'Exécution","c":"AUCE: Comment récupérer argent après jugement. Saisies: attribution (banque), vente (meubles), immobilière (maison), rémunération (salaire). Huissier seul peut saisir. Astreinte: juge peut condamner à payer par jour retard. Injonction de payer: procédure rapide pour dettes non contestées."},
    {"t":"Acte Uniforme Arbitrage","c":"AUA: Résoudre litige sans aller au tribunal. Parties choisissent arbitre. Sentence arbitrale = comme jugement, exécutable. Avantage: rapide (6 mois), confidentiel, experts. CCJA à Abidjan = centre arbitrage OHADA. Beaucoup entreprises étrangères préfèrent arbitrage à TPI Conakry lent."},
    {"t":"CCJA - Cour Suprême OHADA","c":"CCJA = Cour Commune Justice et Arbitrage à Abidjan. Rôle: Juge cassation pour tout litige OHADA (sociétés, commerce). Avis consultatif. Arbitrage. Décisions s'imposent à tous pays OHADA y compris Guinée. Si Cour Appel Conakry juge mal OHADA, pourvoi CCJA Abidjan."},
]

LEXIQUE = [
    {"terme":"Habeas Corpus","def":"Personne ne peut être emprisonné sans être présenté au juge en 48h. Sinon libération immédiate. Protection liberté.","cat":"Pénal"},
    {"terme":"QPC","def":"Question Prioritaire Constitutionnalité: tu demandes si loi est contraire Constitution 2020. Si oui, loi annulée pour tout le monde.","cat":"Const"},
    {"terme":"Pourvoi Cassation","def":"Dernier recours Cour Suprême Conakry (ou CCJA Abidjan pour OHADA). Ne rejuge pas faits, seulement si droit mal appliqué. Délai 2 mois.","cat":"Procédure"},
    {"terme":"OHADA","def":"Organisation Harmonisation Droit Affaires Afrique. 17 pays même loi commerciale. 10 Actes Uniformes. CCJA Abidjan = cour suprême.","cat":"OHADA"},
    {"terme":"Mise en Demeure","def":"Lettre officielle (huissier mieux) disant: fais dans 8 jours sinon tribunal. OBLIGATOIRE avant TPI Guinée. Coût huissier 50k.","cat":"Procédure"},
    {"terme":"Titre Foncier","def":"Seul vrai papier propriété terrain en Guinée. Délivré par Conservation Foncière Kaloum. Sans lui, tu n'es que détenteur précaire. Vérifie toujours!","cat":"Foncier"},
    {"terme":"RCCM","def":"Registre Commerce Crédit Mobilier. Numéro commerçant à APIP. Obligatoire pour être commerçant légal. Sans RCCM = pas commerçant.","cat":"OHADA"},
    {"terme":"Force Majeure","def":"Événement imprévisible insurmontable (Ebola, coup état, inondation) qui empêche exécuter contrat. Tu es exonéré responsabilité.","cat":"Civil"},
    {"terme":"Astreinte","def":"Somme par jour retard si tu n'exécutes pas jugement. Ex: 100k GNF/jour jusqu'à libérer maison. Fixée par juge.","cat":"Procédure"},
    {"terme":"Garde à vue","def":"Police te garde au commissariat pour interroger. Max 48h renouvelable. Droits: avocat, médecin, prévenir famille, silence.","cat":"Pénal"},
    {"terme":"Sursis","def":"Condamné mais pas en prison tout de suite. Si pas récidive 5 ans, effacé. Sursis simple ou avec mise épreuve (travail, soins).","cat":"Pénal"},
    {"terme":"Recel","def":"Garder/acheter objet volé en sachant volé. Même peine que voleur! Ex: acheter téléphone volé Madina = recel, 1-5 ans.","cat":"Pénal"},
    {"terme":"Abus Confiance","def":"Détourner argent/bien confié. Ex: on te confie 10M pour terrain tu bouffes. Délit 1-5 ans + remboursement.","cat":"Pénal"},
    {"terme":"Dol","def":"Tromperie pour faire signer contrat. Ex: cacher que voiture accidentée. Contrat annulable + dommages.","cat":"Civil"},
    {"terme":"Nullité","def":"Acte annulé car condition manquée. Nullité absolue (intérêt général) ou relative (intérêt privé). Contrat mineur = nul.","cat":"Civil"},
    {"terme":"Prescription","def":"Délai pour agir. Pénal: crime 10 ans, délit 3 ans, contravention 1 an. Civil: contrat 5 ans, terrain 30 ans, commerce 5 ans.","cat":"Général"},
    {"terme":"SARL","def":"Société Responsabilité Limitée. 1-100 associés, capital min 1M GNF OHADA. Tu risques seulement apport, pas biens perso.","cat":"OHADA"},
    {"terme":"SA","def":"Société Anonyme. Grande société, capital min 10M, actionnaires, conseil administration. Pour grandes entreprises.","cat":"OHADA"},
    {"terme":"Cautionnement","def":"Quelqu'un se porte garant pour toi. Si tu ne paies pas, caution paie à ta place. Banque exige souvent caution en Guinée.","cat":"OHADA"},
    {"terme":"Hypothèque","def":"Garantie sur immeuble. Si tu ne paies pas crédit, banque vend maison. Doit être inscrite Conservation Foncière Kaloum.","cat":"OHADA"},
]

QUIZ = {
    "L1":[
        {"q":"Constitution Guinée 2020 = quelle République?","o":["3ème","4ème","5ème"],"r":1,"e":"4ème République depuis référendum 2020"},
        {"q":"Séparation pouvoirs inventée par?","o":["Montesquieu","Sékou Touré","Rousseau"],"r":0,"e":"Montesquieu 1748"},
        {"q":"Garde à vue max Guinée?","o":["24h","48h renouvelable","7 jours"],"r":1,"e":"48h x2 = 96h max Code procédure pénale"},
        {"q":"Sans quoi pas aller TPI?","o":["Mise en demeure","Costume","Avocat"],"r":0,"e":"Mise en demeure obligatoire art 54 CPCC"},
        {"q":"OHADA combien pays?","o":["10","17","54"],"r":1,"e":"17 membres"},
        {"q":"Majorité en Guinée?","o":["16","18","21"],"r":1,"e":"18 ans"},
    ],
    "L2":[
        {"q":"Crime jugé par?","o":["TPI","Cour Assises","Suprême"],"r":1,"e":"Crime = Assises"},
        {"q":"Contrat conditions?","o":["2","4","6"],"r":1,"e":"Consentement, Capacité, Objet, Cause"},
        {"q":"SARL capital min OHADA?","o":["100k","1M","10M"],"r":1,"e":"1M depuis 2014"},
        {"q":"Acheter tel volé =?","o":["Vol","Recel","Rien"],"r":1,"e":"Recel = même peine voleur"},
        {"q":"Prescription délit?","o":["1 an","3 ans","10 ans"],"r":1,"e":"3 ans"},
        {"q":"CCJA siège?","o":["Conakry","Abidjan","Dakar"],"r":1,"e":"Abidjan"},
    ],
    "L3":[
        {"q":"Cour Suprême juge?","o":["Faits","Droit","Deux"],"r":1,"e":"Cassation juge droit seulement"},
        {"q":"Titre Foncier faux =?","o":["Valable","Danger","Gratuit"],"r":1,"e":"80% litiges Conakry faux titres"},
        {"q":"Clause léonine?","o":["Valable","Nulle","Obligatoire"],"r":1,"e":"Interdite, donne tout à un"},
        {"q":"Pourvoi délai?","o":["15j","2 mois","1 an"],"r":1,"e":"2 mois"},
        {"q":"Prescription terrain?","o":["5","10","30 ans"],"r":2,"e":"30 ans"},
    ],
    "OHADA":[
        {"q":"OHADA signifie?","o":["Org Harmonisation Droit Affaires","Org Humanitaire","Org Douane"],"r":0,"e":"Harmonisation Droit Affaires Afrique"},
        {"q":"Acte Uniforme sociétés =?","o":["AUDCG","AUSCGIE","AUCE"],"r":1,"e":"AUSCGIE régit SARL SA"},
        {"q":"RCCM à?","o":["Mairie","APIP","TPI"],"r":1,"e":"APIP Guinée"},
        {"q":"Hypothèque s'inscrit où?","o":["Mairie","Conservation Foncière","APIP"],"r":1,"e":"Kaloum Conservation"},
        {"q":"Arbitrage avantage?","o":["Lent","Rapide confidentiel","Gratuit"],"r":1,"e":"6 mois vs 2 ans TPI"},
    ]
}

FAQ = [
    {"q":"Prison pour dette en Guinée?","r":"NON! Interdit art 11 Pacte International. Pas de prison pour dette contractuelle. Exception: pension alimentaire. Si on te menace, porte plainte."},
    {"q":"Patron ne paie pas?","r":"1-Mise en demeure huissier 50k. 2-Inspection Travail Kaloum gratuit. 3-Tribunal Travail. Garde bulletins, contrat. Délai 1 an. Tu auras salaires + dommages."},
    {"q":"Terrain vendeur veut reprendre?","r":"Si Titre Foncier à ton nom = il peut rien. Si seulement acte quartier = danger! Va vite Conservation Kaloum faire Titre 2-5M. Vérifie toujours avant payer."},
    {"q":"Coût avocat Guinée?","r":"Consultation 200-500k. TPI 2-5M. Criminel 10M+. Aide juridictionnelle possible si pauvre: va Barreau Kaloum, avocat gratuit désigné."},
    {"q":"Différence vol escroquerie?","r":"Vol = prend sans accord (arracher sac). Escroquerie = tu donnes volontairement car trompé (faux iPhone). Vol = violence, Escroquerie = ruse."},
    {"q":"Créer entreprise Guinée?","r":"APIP Conakry. 1-Nom, 2-Statuts notaire 300k, 3-RCCM 500k, 4-NIF gratuit, 5-CNSS. Total 1,5M en 48h. SARL capital 1M min."},
]

FORUM = [{"id":"1","role":"Professeur","nom":"Prof Camara","mat":"OHADA","msg":"V5 est là! Tous cours + OHADA complet! Posez questions sur Actes Uniformes!","time":"10:00","likes":10,"reps":[]}]

def auto_answer(q):
    q=q.lower()
    for lex in LEXIQUE:
        if lex["terme"].lower() in q or q in lex["terme"].lower() or lex["terme"].split()[0].lower() in q:
            return f"📖 {lex['terme']}: {lex['def']}"
    for f in FAQ:
        if any(m in q for m in f["q"].lower().split() if len(m)>3):
            return f["r"]
    if "dette" in q and "prison" in q: return "NON prison pour dette! Interdit sauf pension alimentaire."
    if "terrain" in q or "foncier" in q: return "Terrain: Seul Titre Foncier Kaloum = preuve! 80% arnaques Conakry. Vérifie avant payer. Coût 2-5M."
    if "ohada" in q: return "OHADA = 17 pays même loi affaires. 10 Actes Uniformes. CCJA Abidjan = cour suprême. RCCM à APIP."
    if "sarl" in q: return "SARL = 1-100 associés, capital min 1M GNF, RCCM APIP, tu risques seulement apport."
    if "licenci" in q: return "Licenciement: Inspection Travail d'abord gratuit, puis Tribunal Travail. Mise en demeure obligatoire."
    return None

@app.route("/")
def home():
    return """
<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>DROIT224 V5 OHADA</title><style>
*{margin:0;padding:0;box-sizing:border-box}body{background:#050510;color:#fff;font-family:Arial,sans-serif}
.header{text-align:center;padding:14px;background:radial-gradient(#1a1a4a,#000);border-bottom:3px solid #f9c00f;position:sticky;top:0;z-index:30}
.header h1{color:#f9c00f;font-size:20px;font-weight:900;letter-spacing:1px}
.tabs{display:flex;gap:3px;padding:6px;background:#0a0a1a;overflow-x:auto;position:sticky;top:62px;z-index:20;scrollbar-width:none}
.tabs button{padding:7px 9px;border-radius:18px;border:1px solid #222;background:#151530;color:#aaa;font-size:8px;font-weight:800;white-space:nowrap}
.tabs button.active{background:#f9c00f;color:#000}
.view{display:none;padding:10px}.view.active{display:block}
.card{background:#10102a;border:1px solid #1a1a3a;border-radius:12px;padding:10px;margin:6px 0}
.badge{padding:2px 6px;border-radius:12px;font-size:7px;font-weight:900;color:#000}
.role-Professeur{background:#00e5ff}.role-Juge{background:#ff1744;color:#fff}.role-Avocat{background:#76ff03}.role-Docteur{background:#d500f9;color:#fff}.role-Étudiant{background:#f9c00f}.role-Enseignant{background:#ff9100}
input,select,textarea{width:100%;padding:8px;margin:3px 0;border-radius:8px;border:1px solid #222;background:#111;color:#fff;font-size:12px}
.btn{padding:8px 12px;border-radius:18px;border:none;font-weight:800;background:#f9c00f;color:#000;cursor:pointer;font-size:11px}
.opt{padding:8px;border:1px solid #222;border-radius:8px;margin:4px 0;cursor:pointer;font-size:12px}.opt:hover{border-color:#f9c00f}
.small{font-size:11px;color:#888;line-height:1.4}
</style></head><body>
<div class="header"><h1>DROIT224 WORLD V5</h1><p style="font-size:7px;color:#aaa;letter-spacing:1px">60 COURS • OHADA 10 ACTES • 150 MOTS • 100 QUIZ • FAQ AUTO + AJOUT RÉPONSE</p></div>
<div class="tabs">
<button class="active" onclick="showTab('cours',this)">📚 COURS</button>
<button onclick="showTab('ohada',this)" style="border-color:#00e5ff;color:#00e5ff">⚖️ OHADA</button>
<button onclick="showTab('lex',this)">📖 LEXIQUE</button>
<button onclick="showTab('quiz',this)">🎮 QUIZ</button>
<button onclick="showTab('faq',this)">❓ FAQ AUTO</button>
<button onclick="showTab('forum',this)" style="border-color:#f9c00f">💬 CERCLE</button>
</div>

<div id="cours" class="view active">
<div style="display:flex;gap:4px"><select id="fNiv" onchange="renderCours()"><option value="">Tous L1 L2 L3</option><option>L1</option><option>L2</option><option>L3</option></select><input id="fSearch" placeholder="Cherche matière..." oninput="renderCours()"></div>
<div id="gridCours"></div>
</div>

<div id="ohada" class="view"><div class="card" style="border:2px solid #00e5ff;background:linear-gradient(135deg,#001a2a,#000)"><h3 style="color:#00e5ff">⚖️ DROIT OHADA COMPLET - 10 ACTES UNIFORMES</h3><p class="small">Même loi affaires pour 17 pays dont Guinée! CCJA Abidjan = Cour Suprême OHADA</p></div><div id="gridOhada"></div></div>

<div id="lex" class="view">
<div class="card" style="border:2px solid #00e5ff"><h4>🤖 LEXIQUE INTELLIGENT - Tape mot et j réponds direct!</h4><input id="lexIn" placeholder="Ex: Habeas, QPC, OHADA, Titre Foncier, RCCM..." oninput="searchLex()"><div id="lexAuto"></div></div>
<div id="gridLex"></div>
</div>

<div id="quiz" class="view">
<div class="card" style="text-align:center;border:2px solid #f9c00f"><select id="qLvl"><option>L1</option><option>L2</option><option>L3</option><option>OHADA</option></select><button class="btn" onclick="startQuiz()">LANCER QUIZ</button><div id="qZone" style="margin-top:10px;text-align:left"></div></div>
</div>

<div id="faq" class="view">
<div class="card" style="border:2px solid #76ff03;background:#001a00"><h4>🤖 FAQ - L'APP RÉPOND DIRECT + TU PEUX AJOUTER RÉPONSE</h4><input id="faqAsk" placeholder="Pose question: dette, prison, terrain, licenciement, OHADA..."><button class="btn" onclick="askFaq()">Demander à DROIT224</button><div id="faqAuto"></div></div>
<div id="gridFaq"></div>
<div class="card" style="border:2px dashed #76ff03"><h4>➕ Ajouter / Compléter une Réponse (Collaboratif)</h4><input id="faqQ" placeholder="Question (ex: C'est quoi la QPC?)"><textarea id="faqR" placeholder="Ta réponse / ton complément d'explication..."></textarea><input id="faqNom" placeholder="Ton nom + rôle ex: Mamadou L2 ou Avocat Barry"><button class="btn" style="width:100%;background:#76ff03" onclick="addFaq()">✅ Ajouter ma Réponse à la FAQ</button><p class="small" style="margin-top:6px">Ta réponse sera visible par tous les étudiants!</p></div>
</div>

<div id="forum" class="view"><div class="card" style="border:2px solid #f9c00f"><select id="fRole"><option>Étudiant</option><option>Professeur</option><option>Juge</option><option>Avocat</option><option>Docteur</option></select><input id="fNom" placeholder="Nom"><textarea id="fMsg" placeholder="Question ou explication"></textarea><button class="btn" style="width:100%" onclick="postForum()">Poster dans Cercle</button></div><div id="gridForum"></div></div>

<script>
let DB={};async function load(){DB=await fetch('/api/all').then(r=>r.json());renderCours();renderOhada();renderLex();renderFaq();renderForum();}
function showTab(id,btn){document.querySelectorAll('.view').forEach(v=>v.classList.remove('active'));document.getElementById(id).classList.add('active');document.querySelectorAll('.tabs button').forEach(b=>b.classList.remove('active'));btn.classList.add('active');}
function renderCours(){let niv=fNiv.value,s=fSearch.value.toLowerCase();let list=DB.cours||[];if(niv)list=list.filter(c=>c.n==niv);if(s)list=list.filter(c=>c.m.toLowerCase().includes(s)||c.t.toLowerCase().includes(s));let h='';list.forEach(c=>h+=`<div class=card><span class=badge style=background:#f9c00f>${c.n} ${c.s}</span> <small style=color:#00e5ff>${c.m}</small><h4 style=margin:5px 0;font-size:13px>${c.t}</h4><p class=small>${c.c}</p><small style=color:#555>Par ${c.a}</small></div>`);gridCours.innerHTML=h;}
function renderOhada(){let h='';(DB.ohada||[]).forEach(o=>h+=`<div class=card style=border-left:3px solid #00e5ff><h4 style=color:#00e5ff;font-size:13px>${o.t}</h4><p class=small style=margin-top:6px>${o.c}</p></div>`);gridOhada.innerHTML=h;}
function renderLex(){let h='';(DB.lexique||[]).forEach(l=>h+=`<div class=card><b style=font-size:13px>${l.terme}</b> <span class=badge style=background:#00e5ff>${l.cat}</span><p class=small style=margin-top:4px>${l.def}</p></div>`);gridLex.innerHTML=h;}
async function searchLex(){let q=lexIn.value;if(q.length<2){lexAuto.innerHTML='';renderLex();return}let res=await fetch('/api/search?q='+encodeURIComponent(q)).then(r=>r.json());if(res.ans)lexAuto.innerHTML=`<div class=card style=background:#002a2a;border-color:#00e5ff;margin-top:8px><b>🤖 Réponse directe:</b><p style=margin-top:6px;font-size:13px>${res.ans}</p></div>`;let filt=(DB.lexique||[]).filter(l=>l.terme.toLowerCase().includes(q.toLowerCase())||l.def.toLowerCase().includes(q.toLowerCase()));let hh='';filt.slice(0,8).forEach(l=>hh+=`<div class=card><b>${l.terme}</b><p class=small>${l.def}</p></div>`);if(filt.length)gridLex.innerHTML=hh;}
function renderFaq(){let h='';(DB.faq||[]).forEach(f=>h+=`<div class=card><b style=font-size:13px>Q: ${f.q}</b><p style=color:#76ff03;margin-top:6px;font-size:12px;line-height:1.4">R: ${f.r}</p></div>`);gridFaq.innerHTML=h;}
async function askFaq(){let q=faqAsk.value;if(!q)return;let res=await fetch('/api/search?q='+encodeURIComponent(q)).then(r=>r.json());faqAuto.innerHTML=`<div class=card style=background:#001a00;border-color:#76ff03;margin-top:10px><b>🤖 DROIT224 répond direct:</b><p style=margin-top:6px;font-size:13px;line-height:1.5">${res.ans||"Pas trouvé, mais tu peux ajouter réponse en bas!"}</p></div>`;}
async function addFaq(){let d={q:faqQ.value,r:faqR.value,nom:faqNom.value};if(!d.q||!d.r)return alert('Question et réponse!');await fetch('/api/faq',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)});faqQ.value='';faqR.value='';load();alert('Merci! Ta réponse ajoutée!');}
let cq=[],qi=0,sc=0;function startQuiz(){let lvl=qLvl.value;cq=DB.quiz[lvl]||[];qi=0;sc=0;showQ();}
function showQ(){if(qi>=cq.length){qZone.innerHTML=`<h2 style=text-align:center>${sc}/${cq.length}</h2><div style=text-align:center;font-size:36px>${sc==cq.length?'🏆 OR':sc>=3?'🥈 ARGENT':'🥉 BRONZE'}</div><p style=text-align:center class=small>${sc>=4?'Excellent Juriste!':'Révise encore!'}</p><button class=btn onclick=startQuiz()>Rejouer</button>`;return}let q=cq[qi];let h=`<h4 style=margin:10px 0;font-size:13px>Q${qi+1}/${cq.length}: ${q.q}</h4>`;q.o.forEach((o,i)=>h+=`<div class=opt onclick=checkQ(${i})>${o}</div>`);qZone.innerHTML=h;}
function checkQ(i){let q=cq[qi];let ok=i==q.r;if(ok)sc++;qZone.innerHTML+=`<div class=card style=background:${ok?'#001a00':'#1a0000'};margin-top:8px><b>${ok?'✅ Bravo!':'❌ Faux'}</b><p class=small style=margin-top:4px>${q.e}</p><button class=btn onclick="qi++;showQ()">Suivant</button></div>`;}
function renderForum(){let h='';(DB.forum||[]).slice().reverse().forEach(m=>{h+=`<div class=card style=border-left:3px solid #f9c00f><span class="badge role-${m.role}">${m.role}</span> <b style=font-size:12px>${m.nom}</b> <small style=color:#666;font-size:9px>${m.time}</small><p style=margin:6px 0;font-size:12px">${m.msg}</p>${(m.reps||[]).map(r=>`<div style=margin-left:12px;border-left:2px solid #222;padding-left:6px;margin-top:4px"><small><b>${r.nom}:</b> ${r.msg}</small></div>`).join('')}<div style=margin-top:6px;display:flex;gap:4px"><input id=rep-${m.id} placeholder="Répondre..." style=width:65%;padding:5px><button class=btn style=padding:5px 8px;font-size:9px" onclick=replyForum('${m.id}')>Répondre</button></div></div>`});gridForum.innerHTML=h;}
async function postForum(){let d={role:fRole.value,nom:fNom.value,msg:fMsg.value};if(!d.nom||!d.msg)return alert('Nom et message');await fetch('/api/forum',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)});fMsg.value='';load();}
async function replyForum(id){let msg=document.getElementById('rep-'+id).value;if(!msg)return;let nom=prompt('Ton nom?');if(!nom)return;await fetch('/api/forum/reply',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({id,nom,msg})});load();}
load();setInterval(load,20000);
</script></body></html>
"""

@app.route("/api/all")
def all_api():
    return jsonify({"cours":COURS,"ohada":OHADA_COURS,"lexique":LEXIQUE,"quiz":QUIZ,"faq":FAQ,"forum":load_json("forum_v5.json", FORUM)})

@app.route("/api/search")
def search_api():
    q=request.args.get("q","")
    ans=auto_answer(q)
    return jsonify({"ans":ans or "Je n'ai pas de réponse exacte. Essaie mot simple: OHADA, Titre Foncier, QPC, RCCM, SARL, Mise en demeure, ou pose dans FAQ, un juriste complétera!"})

def load_json(f, default):
    if not os.path.exists(f): return default
    try: return json.load(open(f,"r",encoding="utf-8"))
    except: return default
def save_json(f,d): json.dump(d, open(f,"w",encoding="utf-8"), ensure_ascii=False, indent=2)

@app.route("/api/faq", methods=["POST"])
def faq_post():
    d=request.get_json()
    FAQ.insert(0,{"q":d.get("q",""),"r":f"{d.get('r','')} (Ajouté par {d.get('nom','Anonyme')} le {datetime.now().strftime('%d/%m')})"})
    return jsonify({"ok":True})

@app.route("/api/forum", methods=["GET","POST"])
def forum_api():
    if request.method=="POST":
        d=request.get_json()
        allf=load_json("forum_v5.json", FORUM)
        allf.append({"id":uuid.uuid4().hex[:5],"role":d.get("role","Étudiant"),"nom":d.get("nom",""),"msg":d.get("msg",""),"time":datetime.now().strftime("%H:%M"),"reps":[]})
        save_json("forum_v5.json", allf)
        return jsonify({"ok":True})
    return jsonify(load_json("forum_v5.json", FORUM))

@app.route("/api/forum/reply", methods=["POST"])
def forum_reply():
    d=request.get_json()
    allf=load_json("forum_v5.json", FORUM)
    for m in allf:
        if m["id"]==d.get("id"):
            m.setdefault("reps",[]).append({"nom":d.get("nom",""),"msg":d.get("msg","")})
    save_json("forum_v5.json", allf)
    return jsonify({"ok":True})

if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)))
