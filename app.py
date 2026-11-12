from flask import Flask, jsonify, request
import json, os, uuid, re
from datetime import datetime
app = Flask(__name__)

# ============ COURS APPROFONDIS - VRAIS POLYCOPIÉS ============
COURS = [
{
"n":"L1","s":"S1","m":"Introduction Droit","t":"COURS COMPLET: Qu'est-ce que le Droit? Définition, Branches, Sources",
"c":"""CHAPITRE 1: DÉFINITION DU DROIT\nLe Droit est l'ensemble des règles qui organisent la vie en société et dont le respect est assuré par la puissance publique.\n\nCARACTÈRES DE LA RÈGLE DE DROIT:\n1. Générale: s'applique à tous (pas à une personne)\n2. Abstraite: vise des situations, pas un cas précis\n3. Obligatoire: tu DOIS respecter, sinon sanction\n4. Sanctionnée par l'État: Police, Tribunal, Prison\n\n2 GRANDES BRANCHES:\nA) DROIT PUBLIC: Règles entre État et citoyen. Ex: Droit Constitutionnel (Constitution), Droit Administratif (Administration), Droit Pénal (crimes). But: intérêt général.\nB) DROIT PRIVÉ: Règles entre citoyens. Ex: Droit Civil (famille, contrat), Droit Commercial (commerçants), Droit du Travail (patron-employé). But: intérêt privé.\n\nSOURCES DU DROIT GUINÉEN:\n1. Constitution 2020: Loi suprême, au dessus de tout\n2. Loi: votée par CNT, promulguée par Président\n3. Ordonnance: Président légifère urgence\n4. Décret/Arrêté: Exécutif\n5. Coutume: Habitude devenue obligatoire (ex: mariage coutumier en Guinée rurale)\n6. Jurisprudence: Décisions Cour Suprême qui font référence\n7. Doctrine: Avis professeurs\n8. OHADA: Pour affaires, 10 Actes Uniformes au dessus loi nationale\n\nBUT DU DROIT: Assurer ordre, paix, justice, sécurité, progrès. Sans Droit = loi du plus fort, anarchie.""",
"a":"Prof. Camara - UGLC Sonfonia","pdf":""
},
{
"n":"L1","s":"S1","m":"Constitutionnel","t":"COURS COMPLET: Constitution Guinéenne 2020 - Tout comprendre",
"c":"""CHAPITRE 1: QU'EST-CE QU'UNE CONSTITUTION?\nConstitution = Loi suprême d'un pays. Au dessus de toutes les autres lois. C'est le contrat entre peuple et dirigeants.\n\nCONSTITUTIONS GUINÉENNES:\n1958: 1ère Constitution indépendance Sékou Touré\n1990: 2ème Constitution ouverture démocratique\n2010: 3ème Constitution Alpha Condé\n2020: 4ème Constitution actuelle (référendum 22 mars 2020)\n\nCONTENU CONSTITUTION 2020:\nTITRE 1 - Principes: Guinée État laïc, démocratique, indivisible. Langue officielle français. Drapeau Rouge-Jaune-Vert.\nTITRE 2 - Droits et Devoirs (art 5-50): \n- Droits civils: vie, liberté, égalité, propriété, présomption innocence\n- Droits politiques: vote, éligibilité, manifestation, parti politique\n- Droits économiques: travail, grève, propriété\n- Devoirs: respecter Constitution, payer impôts, défendre patrie\n\nTITRE 3 - Pouvoirs:\n1. EXÉCUTIF: Président de la République (élu 5 ans renouvelable 1 fois), nomme Premier Ministre, Gouvernement, Décrets\n2. LÉGISLATIF: CNT (Conseil National Transition) actuellement, bientôt Assemblée Nationale. Vote lois, budget, contrôle Gouvernement\n3. JUDICIAIRE: Cours et Tribunaux. Indépendant! Juges inamovibles. Cour Suprême au sommet, Cour Constitutionnelle juge constitutionnalité lois\n\nRÉVISION CONSTITUTION: Procédure très difficile: Initiative Président ou 2/3 CNT, puis référendum peuple. But: empêcher dictature.\n\nCONTRÔLE CONSTITUTIONNALITÉ: QPC (Question Prioritaire) permet à tout citoyen devant TPI de dire 'cette loi est contraire Constitution'. Si Cour Constit dit oui, loi annulée!""",
"a":"Dr. Diallo - Constitutionnaliste","pdf":""
},
{
"n":"L1","s":"S2","m":"Droit Civil","t":"COURS COMPLET: La Personne - Physique et Morale - Capacité",
"c":"""CHAPITRE 1: PERSONNE PHYSIQUE\nPersonne physique = être humain. Devient sujet de droit dès naissance vivante et viable. Même bébé a des droits! Fin personnalité = mort (même mort cérébrale).\n\nATTRIBUTS:\n1. Nom: nom famille + prénom. Droit de changer via tribunal\n2. Prénom: choisi parents, peut changer\n3. Domicile: lieu principal habitation, important pour assignation TPI\n4. Nationalité: Guinéenne par filiation (père/mère guinéen) ou naturalisation\n5. Patrimoine: ensemble biens et dettes\n\nCAPACITÉ JURIDIQUE:\nCapacité jouissance: avoir des droits (tout le monde, même bébé)\nCapacité exercice: exercer soi-même droits. Mineur <18 ans = incapable, représenté par parents/tuteur. Majeur protégé: sous tutelle si fou.\n\nPERSONNE MORALE:\nGroupement qui a personnalité juridique distincte membres. Types: Société (SARL, SA), Association, État, Commune, Syndicat.\nCréation: immatriculation RCCM pour sociétés, déclaration pour associations.\nAvantage: peut posséder, contracter, aller au tribunal. Responsabilité limitée: associés SARL risquent seulement apport.\n\nExemple Guinée: Si tu crées SARL DROIT224, SARL peut acheter voiture à son nom, pas toi. Si SARL dette, créancier ne peut saisir ta maison perso, seulement biens SARL.""",
"a":"Prof. Camara","pdf":""
},
{
"n":"L2","s":"S3","m":"Droit Pénal Général","t":"COURS COMPLET: Infraction, Responsabilité, Peines",
"c":"""CHAPITRE 1: INFRACTION\nInfraction = acte ou omission interdit par loi pénale et puni d'une peine.\n\nCLASSIFICATION TRIPARTITE:\n1. CRIME: Infraction grave. Peine = réclusion criminelle 10 ans à perpétuité ou mort (même si moratoire). Ex: meurtre art 201 CP, viol art 321, vol à main armée, trafic drogue, détournement deniers publics. Juridiction: Cour d'Assises avec jury populaire. Instruction obligatoire. Prescription 10 ans.\n2. DÉLIT: Infraction moyenne. Peine = emprisonnement 1 mois à 10 ans + amende. Ex: vol simple, escroquerie, abus confiance, coups blessures, diffamation. Juridiction: Tribunal Correctionnel TPI. Prescription 3 ans.\n3. CONTRAVENTION: Faute légère. Peine = amende 1ère à 5ème classe (5.000 à 1M GNF). Ex: tapage nocturne, injure non publique, divagation animaux. Juridiction: Tribunal Simple Police. Prescription 1 an.\n\nÉLÉMENTS CONSTITUTIFS INFRACTION:\nIl faut 3 éléments cumulés:\n- Élément LÉGAL: texte qui prévoit infraction (principe légalité: pas d'infraction sans loi)\n- Élément MATÉRIEL: acte concret (tuer, voler, frapper)\n- Élément MORAL: intention (dol) ou faute (imprudence). Sans intention, pas infraction sauf contravention.\n\nRESPONSABILITÉ PÉNALE:\nPersonne physique: responsable si discernement. Cause irresponsabilité: démence, minorité <13 ans irresponsable, contrainte.\nPersonne morale: société peut être condamnée pénalement depuis Code pénal 2016! Peine = amende + dissolution.\n\nPEINES:\nPeines principales: prison, amende, mort (moratoire)\nPeines complémentaires: interdiction séjour, confiscation, interdiction droits civiques\nPeines alternatives: travail intérêt général, jours-amende\n\nEn Guinée: Sursis = tu ne fais pas prison si pas récidive 5 ans. Libération conditionnelle = sors avant fin peine si bonne conduite.""",
"a":"Procureur TPI Dixinn","pdf":""
},
{
"n":"L2","s":"S3","m":"OHADA","t":"COURS COMPLET: OHADA - Pourquoi c'est la Révolution pour Guinée?",
"c":"""OHADA = Organisation pour l'Harmonisation en Afrique du Droit des Affaires. Traité signé 17 oct 1993 Port-Louis (Maurice), révisé 2008 Québec.\n\nPAYS MEMBRES (17): Bénin, Burkina Faso, Cameroun, Centrafrique, Comores, Congo, Congo RDC, Côte d'Ivoire, Gabon, Guinée, Guinée-Bissau, Guinée Équatoriale, Mali, Niger, Sénégal, Tchad, Togo. 300 millions habitants!\n\nOBJECTIF: Même loi affaires partout! Un commerçant guinéen à Conakry a même loi que commerçant sénégalais à Dakar. Fini chaque pays sa loi. Sécurité investisseurs étrangers.\n\n10 ACTES UNIFORMES (Lois OHADA):\n1. AUDCG - Droit Commercial Général: définit commerçant, acte commerce, RCCM, bail commercial, fonds commerce, intermédiaires\n2. AUSCGIE - Sociétés et GIE: SARL, SA, SNC, SCS, SAS, GIE. Création, fonctionnement, dissolution\n3. AUS - Sûretés: garanties: cautionnement, gage, nantissement, hypothèque, propriété retenue\n4. AUPC - Procédures Collectives: redressement judiciaire, liquidation biens (faillite)\n5. AUCE - Voies Exécution: saisies, injonction payer, expulsion\n6. AUA - Arbitrage: régler litige sans tribunal, par arbitre choisi\n7. AUCM - Comptabilité et Information Financière (SYSCOHADA)\n8. AUTM - Transport marchandises par route\n9. AUSCM - Sociétés Coopératives\n10. AUM - Médiation\n\nCCJA - CŒUR SYSTÈME:\nCour Commune Justice et Arbitrage à Abidjan. 13 juges, 9 membres. Rôle:\n- Juge cassation: si Cour Appel Conakry juge mal OHADA, pourvoi CCJA, CCJA casse et peut évoquer (rejuge elle-même!)\n- Avis consultatif\n- Centre arbitrage\nDécisions CCJA s'imposent à tous pays, primauté sur lois nationales!\n\nEN GUINÉE CONCRÈTEMENT:\n- Pour créer SARL: va APIP, RCCM OHADA, capital 1M min\n- Pour prêt banque: banque demande hypothèque inscrite Conservation Foncière + cautionnement\n- Litige commercial: TPI commerce applique OHADA, appel Conakry, cassation Abidjan CCJA\n- Très important pour investisseurs: même règles connues\n\nAVANTAGE GUINÉE: Attire investisseurs, sécurise affaires, modernise droit. INCONVÉNIENT: Juges guinéens pas toujours formés OHADA, lent.""",
"a":"Dr. Barry - Spécialiste OHADA - Avocat CCJA","pdf":"https://biblio.ohada.org/"
},
]

LEXIQUE_MASSIF = [
    {"t":"Habeas Corpus","d":"Ordre donné à police de présenter détenu devant juge en 48h. Si pas, libération immédiate. Protection contre détention arbitraire. Art 9 Constitution Guinée 2020. Si tu es gardé plus 48h sans juge, ton avocat demande Habeas Corpus au Président TPI.","cat":"Pénal"},
    {"t":"QPC","d":"Question Prioritaire de Constitutionnalité. Devant tout tribunal (TPI), tu peux dire: cette loi qui m'est appliquée est contraire à Constitution. Le juge transmet à Cour Suprême puis Cour Constitutionnelle. Si inconstitutionnelle, loi abrogée pour tout le monde! Puissant outil citoyen.","cat":"Const"},
    {"t":"OHADA","d":"Organisation Harmonisation Droit Affaires Afrique. 17 pays dont Guinée. 10 Actes Uniformes = même loi commerciale partout. CCJA Abidjan = Cour suprême OHADA. RCCM à APIP. SARL capital 1M. Révolution pour business africain. Traité 1993.","cat":"OHADA"},
    {"t":"Titre Foncier","d":"Seul document qui prouve propriété terrain en Guinée. Délivré par Conservation Foncière Kaloum après enquête, bornage. Sans Titre Foncier, tu es simple occupant précaire, pas propriétaire! 80% arnaques Conakry = faux titres. Toujours vérifier à Kaloum avant payer. Coût 2-5M, délai 6 mois. Imprescriptible.","cat":"Foncier"},
    {"t":"Mise en Demeure","d":"Lettre officielle qui met en demeure adversaire exécuter obligation dans délai (8 jours). OBLIGATOIRE avant saisir TPI Guinée art 54 CPCC. Si tu sautes, juge déclare irrecevable! Par huissier (50k) ou lettre recommandée. Doit mentionner: obligation, délai, menace tribunal.","cat":"Procédure"},
    {"t":"RCCM","d":"Registre Commerce et Crédit Mobilier. Numéro unique commerçant. Obtenu à APIP Guinée (Agence Promotion Investissements Privés) à Kaloum. Pièces: CNI, casier, statuts, 500k. Obligatoire pour être commerçant légal. Sans RCCM: pas accès marchés publics, banques, pas qualité commerçant devant tribunal.","cat":"OHADA"},
    {"t":"SARL","d":"Société à Responsabilité Limitée. Forme la plus utilisée Guinée. 1 à 100 associés, capital min 1.000.000 GNF depuis 2014 (avant 5M). Responsabilité limitée aux apports: si SARL dette 100M, tu perds seulement ton apport 1M, pas maison perso. Gérant responsable pénalement. Création: statuts notaire + RCCM APIP + NIF.","cat":"OHADA"},
    {"t":"Sursis","d":"Condamnation pénale mais dispense exécution prison. Sursis simple: pas prison si pas nouvelle infraction 5 ans. Sursis avec mise à l'épreuve: obligations (travail, soins, indemniser victime). Si tu respectes, condamnation non avenue (effacée casier). Si récidive, sursis révoqué + nouvelle peine.","cat":"Pénal"},
    {"t":"Astreinte","d":"Condamnation à payer somme par jour/sem de retard si tu n'exécutes pas jugement. Ex: Juge ordonne libérer maison sous astreinte 200k GNF/jour. Si tu restes 10 jours, 2M! Très efficace pour forcer exécution. Fixée par juge, liquidée ensuite. Art 33 AUCE OHADA.","cat":"Procédure"},
    {"t":"Pourvoi Cassation","d":"Recours devant Cour Suprême (ou CCJA pour OHADA) contre arrêt Cour d'Appel. Ne rejuge pas faits, seulement si droit mal appliqué. Délai 2 mois. Effet non suspensif (arrêt s'exécute quand même sauf sursis). Cour Suprême casse et renvoie autre Cour Appel, ou évoque et juge elle-même (CCJA).","cat":"Procédure"},
    {"t":"Garde à vue","d":"Mesure police qui retient suspect au commissariat pour enquête. Durée Guinée: 48h renouvelable 1 fois sur autorisation Procureur (96h total). Terrorisme/drogue 72h x2. Droits: informer famille, avocat dès 1ère heure, médecin, silence, nourriture, pas violences. PV garde à vue obligatoire. Si dépassement = nullité procédure + libération.","cat":"Pénal"},
    {"t":"Nullité","d":"Sanction acte juridique qui ne respecte pas conditions validité. Nullité absolue: viole intérêt général (ex: contrat drogue) = tout le monde peut demander, pas de confirmation, prescription 30 ans. Nullité relative: viole intérêt privé (ex: vice consentement) = seule victime peut demander, confirmable, 5 ans. Effet rétroactif: acte censé jamais existé.","cat":"Civil"},
]

FAQ_BASE = [
    {"q":"Prison pour dette Guinée?","r":"NON! ABSOLUMENT INTERDIT! Art 11 Pacte International Droits Civils et Politiques ratifié par Guinée + Art 2 Constitution. Pas de prison pour dette contractuelle (crédit, loyer, dette argent). Seule exception: dette alimentaire (pension enfants) ou amende pénale. Si créancier te menace prison pour dette, c'est menace illégale, porte plainte pour chantage. Va voir huissier pour échelonnement.","tags":"dette prison"},
    {"q":"Patron ne paie pas salaire 3 mois?","r":"Procédure Guinée: 1) Mise en demeure par huissier (50k) avec décompte salaires. 2) Inspection du Travail à Kaloum/Matam (gratuit) - Inspecteur convoque patron, tente conciliation. 3) Si échec, Tribunal du Travail TPI (requête simple 20k). Pièces: contrat, bulletins, attestation collègues. Tu obtiendras: salaires arriérés + dommages intérêts pour licenciement abusif si viré + certificat. Délai prescription 1 an. Ne démissionne pas, fais constater!","tags":"travail salaire licenciement"},
    {"q":"Terrain acheté vendeur veut reprendre?","r":"Tout dépend titre: Si tu as Titre Foncier à ton nom à Conservation Foncière Kaloum = tu es propriétaire inattaquable, vendeur ne peut rien, c'est propriété absolue art 544 Code civil. Si tu as seulement acte vente coutumier (papier quartier) = tu es occupant précaire, très vulnérable! Vendeur peut revendre à autre! ACTION URGENTE: Va Conservation Foncière Kaloum avec acte coutumier + CNI + 2 témoins, demande enquête et Titre Foncier. Coût 2-5M, 6 mois mais sécurité. ASTUCE: Avant acheter, va Kaloum vérifier si terrain pas déjà titré à autre! 80% arnaques Conakry.","tags":"foncier terrain titre"},
    {"q":"Coût avocat Guinée?","r":"Barème indicatif Conakry 2024: Consultation cabinet 200-500k GNF (30 min). Lettre mise en demeure avocat 500k-1M. TPI affaire civile simple 2-5M. Correctionnel (vol) 3-8M. Cour Assises (crime) 10-30M. Si pauvre: Aide juridictionnelle! Va Barreau Guinée Maison Avocat Kaloum, demande aide, ils désignent avocat gratuit si ressources <1M/mois. Ou Défenseur Droits Humains ONDH. Fac Droit UGLC a clinique juridique gratuite étudiants M2!","tags":"avocat coût aide"},
    {"q":"Police frappé en garde à vue?","r":"TORTURE INTERDITE! Art 6 Constitution 2020 + Convention Torture. Que faire: 1) Dès sortie, va CHU Donka/Ignace Deen pour certificat médical (décrit coups, ITT). Photos blessures. 2) Plainte au Procureur TPI (plainte contre X policier) + Inspection Générale Police. 3) Saisir ONDH Guinée (Org Nat Droits Humains) + Avocats sans Frontières. 4) Si garde à vue en cours, avocat demande médecin + informe famille. Nullité procédure possible. Courage!","tags":"garde vue torture police"},
    {"q":"Vol vs Escroquerie différence?","r":"VOL art 373 CP: soustraction frauduleuse chose d'autrui contre son gré, sans son accord. Ex: arracher téléphone, cambrioler. Violence ou discrétion. Peine 1-5 ans. ESCROQUERIE art 394 CP: tu remets toi-même chose volontairement mais parce que on t'a trompé par ruse, mensonge, manœuvre. Ex: on te vend faux iPhone 15 à la place vrai, faux billet, promesse emploi contre argent. Tu donnes car trompé. Peine 1-5 ans aussi mais éléments différents. Recel = acheter chose volée en sachant volée.","tags":"vol escroquerie recel"},
    {"q":"Créer entreprise SARL Guinée?","r":"Étapes APIP Guinée (Kaloum près Port): 1) Recherche nom (50k). 2) Statuts chez notaire (modèle APIP) 300k + capital 1M min déposé. 3) Dépôt APIP: formulaire + CNI associés + casier + statuts + 500k RCCM. 4) NIF à Direction Impôts gratuit. 5) CNSS déclaration. Délai 48-72h. Total ~1,5-2M. Avantage SARL: responsabilité limitée, crédibilité. Après: compte bancaire pro, facture avec RCCM/NIF. Si commerce, patente Mairie.","tags":"sarl entreprise rccm apip"},
    {"q":"OHADA c'est quoi concrètement?","r":"Pour commerçant guinéen: 1) Pour créer business, tu vas APIP, on t'applique loi OHADA même qu'au Sénégal. SARL capital 1M (pas 10M). 2) Si tu prêtes argent, tu prends hypothèque inscrite Conservation + caution. 3) Si client ne paie pas, injonction de payer rapide (15 jours) au TPI, pas besoin long procès. 4) Si litige avec fournisseur ivoirien, même loi, CCJA Abidjan juge en dernier. But: sécuriser affaires, attirer investisseurs. 10 Actes Uniformes à connaître surtout AUDCG, AUSCGIE, AUS, AUCE.","tags":"ohada apip rccm ccja"},
]

FORUM_INIT = [{"id":"1","role":"Professeur","nom":"Prof Camara","mat":"OHADA","msg":"Bienvenue V6! Cours complets + Dossiers Justice multi-analyses! Postez vos cas!","time":"10:00","likes":5,"reps":[]}]

def intelligent_answer(q):
    q_low=q.lower()
    # 1. Lexique exact
    for lex in LEXIQUE_MASSIF:
        if lex["t"].lower() in q_low or q_low in lex["t"].lower() or lex["t"].split()[0].lower() in q_low.split():
            return f"📖 LEXIQUE - {lex['t']}: {lex['d']}"
    # 2. FAQ tags
    for f in FAQ_BASE:
        if any(word in q_low for word in f["tags"].split() if len(word)>3) or any(m in q_low for m in f["q"].lower().split() if len(m)>4):
            return f"❓ FAQ - {f['r']}"
    # 3. Réponses intelligentes génériques droit
    if "dette" in q_low and "prison" in q_low: return "NON prison pour dette! Interdit en Guinée sauf pension alimentaire. Voir FAQ détaillée."
    if "terrain" in q_low or "foncier" in q_low or "titre" in q_low: return "FONCIER GUINÉE: Seul Titre Foncier Conservation Kaloum = preuve propriété! Sans ça, danger! 80% arnaques Conakry. Procédure: acte coutumier + enquête Kaloum + bornage + Titre 2-5M. Toujours vérifier avant acheter!"
    if "ohada" in q_low: return "OHADA = 17 pays même loi affaires. 10 Actes Uniformes. SARL capital 1M, RCCM APIP, CCJA Abidjan cour suprême, hypothèque Conservation. Révolution business Afrique!"
    if "sarl" in q_low or "entreprise" in q_low or "rccm" in q_low: return "SARL Guinée: 1-100 associés, capital min 1M GNF, statuts notaire 300k, RCCM APIP 500k, NIF gratuit, 48h. Responsabilité limitée aux apports. Gérant responsable pénal."
    if "licenci" in q_low or "salaire" in q_low or "travail" in q_low: return "TRAVAIL: Mise en demeure huissier 50k, puis Inspection Travail Kaloum gratuit, puis Tribunal Travail. Garde contrat bulletins. Délai 1 an. Ne démissionne pas!"
    if "garde" in q_low and "vue" in q_low: return "GARDE À VUE Guinée: 48h renouvelable 96h max. Droits: avocat 1ère heure, médecin, famille, silence, pas violences. Dépassement = nullité + libération."
    if "avocat" in q_low and "coût" in q_low: return "Avocat Conakry: consultation 200-500k, TPI 2-5M, Assises 10-30M. Si pauvre: aide juridictionnelle Barreau Kaloum gratuit."
    if "vol" in q_low or "escroquerie" in q_low: return "VOL = prend sans ton accord (arracher). ESCROQUERIE = tu donnes car trompé (faux iPhone). Recel = acheter volé en sachant volé = même peine voleur!"
    # Fallback intelligent
    return f"🤖 DROIT224 INTELLIGENT analyse: Ta question '{q}' concerne le Droit. Pour te répondre précisément, j'ai besoin de mots-clés: Titre Foncier, OHADA, SARL, Licenciement, Dette, Garde à vue, Vol, etc. Ou pose dans FAQ/Dossier, un Prof/Juge/Docteur va analyser ton cas en détail avec plusieurs points de vue! En attendant: Pour tout problème, 1-Mise en demeure, 2-Inspection/Conciliation, 3-TPI. Garde toujours preuves écrites!"

@app.route("/")
def home():
    return """
<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>DROIT224 V6 ULTRA</title><style>
*{margin:0;padding:0;box-sizing:border-box}body{background:#050510;color:#fff;font-family:Arial}
.header{text-align:center;padding:12px;background:radial-gradient(#1a1a4a,#000);border-bottom:3px solid #f9c00f;position:sticky;top:0;z-index:30}
.tabs{display:flex;gap:3px;padding:5px;background:#0a0a1a;overflow-x:auto;position:sticky;top:60px;z-index:20}
.tabs button{padding:6px 8px;border-radius:16px;border:1px solid #222;background:#151530;color:#aaa;font-size:8px;font-weight:800;white-space:nowrap}
.tabs button.active{background:#f9c00f;color:#000}
.view{display:none;padding:8px}.view.active{display:block}
.card{background:#10102a;border:1px solid #1a1a3a;border-radius:10px;padding:9px;margin:6px 0}
.badge{padding:2px 6px;border-radius:10px;font-size:7px;font-weight:900;color:#000}
.role-Professeur{background:#00e5ff}.role-Juge{background:#ff1744;color:#fff}.role-Avocat{background:#76ff03}.role-Docteur{background:#d500f9;color:#fff}.role-Étudiant{background:#f9c00f}.role-Enseignant{background:#ff9100}.role-Juriste{background:#fff}
input,select,textarea{width:100%;padding:7px;margin:3px 0;border-radius:7px;border:1px solid #222;background:#111;color:#fff;font-size:11px}
.btn{padding:7px 10px;border-radius:16px;border:none;font-weight:800;background:#f9c00f;color:#000;cursor:pointer;font-size:10px}
.opt{padding:7px;border:1px solid #222;border-radius:7px;margin:3px 0;cursor:pointer;font-size:11px}.opt:hover{border-color:#f9c00f}
.small{font-size:11px;color:#bbb;line-height:1.5;white-space:pre-wrap}
.dossier-analyses{margin-left:10px;border-left:2px solid #f9c00f;padding-left:8px;margin-top:8px}
</style></head><body>
<div class="header"><h1 style="color:#f9c00f;font-size:18px">DROIT224 V6 ULTRA</h1><p style="font-size:6px;color:#aaa">COURS APPROFONDIS • PDF • OHADA • LEXIQUE IA • FAQ IA • DOSSIERS MULTI-ANALYSES • CERCLE</p></div>
<div class="tabs">
<button class="active" onclick="showTab('cours',this)">📚 COURS COMPLETS</button>
<button onclick="showTab('ohada',this)" style="border-color:#00e5ff;color:#00e5ff">⚖️ OHADA</button>
<button onclick="showTab('dossier',this)" style="border-color:#ff1744;color:#ff1744">📂 DOSSIERS JUSTICE</button>
<button onclick="showTab('lex',this)">📖 LEXIQUE IA</button>
<button onclick="showTab('quiz',this)">🎮 QUIZ</button>
<button onclick="showTab('faq',this)">❓ FAQ IA</button>
<button onclick="showTab('forum',this)">💬 CERCLE</button>
</div>

<div id="cours" class="view active">
<div style="display:flex;gap:3px"><select id="fNiv" onchange="renderCours()"><option value="">Tous L1 L2 L3</option><option>L1</option><option>L2</option><option>L3</option></select><input id="fSearch" placeholder="Matière..." oninput="renderCours()"></div>
<div id="gridCours"></div>
<div class="card" style="border:2px dashed #f9c00f"><h4>➕ Ajouter Cours / PDF (Étudiant, Prof, Docteur, Juriste)</h4><select id="cNiv"><option>L1</option><option>L2</option><option>L3</option></select><select id="cMat"><option>Introduction Droit</option><option>Constitutionnel</option><option>Civil</option><option>Pénal</option><option>OHADA</option><option>Commercial</option><option>Travail</option><option>Foncier</option><option>Procédure</option></select><input id="cTitre" placeholder="Titre cours ex: Cours complet Bail commercial OHADA"><textarea id="cCont" rows="6" placeholder="Contenu complet du cours... Colle tout ton polycopié ici (500 mots min)"></textarea><input id="cPdf" placeholder="Lien PDF (optionnel) ex: https://drive.google.com/..."><select id="cRole"><option>Étudiant</option><option>Professeur</option><option>Enseignant</option><option>Docteur</option><option>Juriste</option><option>Avocat</option><option>Juge</option></select><input id="cNom" placeholder="Ton nom ex: Mamadou L2 / Prof Camara"><button class="btn" style="width:100%" onclick="addCours()">📤 Publier Cours / PDF</button></div>
</div>

<div id="ohada" class="view"><div class="card" style="border:2px solid #00e5ff;background:#001a2a"><h3 style="color:#00e5ff;font-size:14px">⚖️ DROIT OHADA - 10 ACTES UNIFORMES</h3><p class="small">17 pays même loi! CCJA Abidjan = Cour Suprême</p></div><div id="gridOhada"></div></div>

<div id="dossier" class="view">
<div class="card" style="border:2px solid #ff1744;background:#1a0000"><h4>📂 TRAITEMENT DOSSIERS JUSTICE - ANALYSE MULTI-EXPERTS</h4><p class="small">Poste ton problème juridique, plusieurs experts vont analyser: Étudiant, Prof, Juge, Docteur, Avocat!</p><select id="dType"><option>Licenciement</option><option>Dette non payée</option><option>Terre / Foncier</option><option>Divorce</option><option>Vol / Escroquerie</option><option>Accident</option><option>Loyer impayé</option><option>Contrat non respecté</option></select><textarea id="dDesc" rows="3" placeholder="Décris ton cas en détail: qui, quoi, quand, preuves..."></textarea><input id="dNom" placeholder="Ton nom"><button class="btn" style="background:#ff1744;color:#fff;width:100%" onclick="postDossier()">🚀 Soumettre Dossier à Analyse</button><div id="dAuto"></div></div>
<div id="gridDossier"></div>
</div>

<div id="lex" class="view"><div class="card" style="border:2px solid #00e5ff"><h4>🤖 LEXIQUE INTELLIGENT - Connaît TOUT le Droit</h4><input id="lexIn" placeholder="Tape mot: Habeas, QPC, OHADA, Titre Foncier, RCCM, SARL..." oninput="searchLex()"><div id="lexAuto"></div></div><div id="gridLex"></div><div class="card" style="border:1px dashed #00e5ff"><input id="lexT" placeholder="Nouveau terme"><input id="lexD" placeholder="Définition simple"><button class="btn" style="background:#00e5ff" onclick="addLex()">Ajouter terme</button></div></div>

<div id="quiz" class="view"><div class="card" style="text-align:center;border:2px solid #f9c00f"><select id="qLvl"><option>L1</option><option>L2</option><option>L3</option><option>OHADA</option></select><button class="btn" onclick="startQuiz()">LANCER QUIZ</button><div id="qZone" style="text-align:left;margin-top:10px"></div></div></div>

<div id="faq" class="view"><div class="card" style="border:2px solid #76ff03;background:#001a00"><h4>🤖 FAQ INTELLIGENTE - Répond à TOUT en Droit</h4><input id="faqAsk" placeholder="Pose question: dette, prison, terrain, OHADA, licenciement..."><button class="btn" style="background:#76ff03" onclick="askFaq()">Demander à DROIT224 IA</button><div id="faqAuto"></div></div><div id="gridFaq"></div><div class="card" style="border:2px dashed #76ff03"><h4>➕ Compléter / Ajouter Réponse (Collaboratif)</h4><input id="faqQ" placeholder="Question"><textarea id="faqR" placeholder="Ta réponse / complément expert..."></textarea><input id="faqNom" placeholder="Nom + rôle ex: Avocat Barry"><button class="btn" style="width:100%;background:#76ff03" onclick="addFaq()">✅ Ajouter Réponse</button></div></div>

<div id="forum" class="view"><div class="card" style="border:2px solid #f9c00f"><select id="fRole"><option>Étudiant</option><option>Professeur</option><option>Juge</option><option>Avocat</option><option>Docteur</option><option>Enseignant</option><option>Juriste</option></select><input id="fNom" placeholder="Nom"><textarea id="fMsg" placeholder="Question ou cours"></textarea><button class="btn" style="width:100%" onclick="postForum()">Poster Cercle</button></div><div id="gridForum"></div></div>

<script>
let DB={};async function load(){DB=await fetch('/api/all').then(r=>r.json());renderCours();renderOhada();renderDossier();renderLex();renderFaq();renderForum();}
function showTab(id,btn){document.querySelectorAll('.view').forEach(v=>v.classList.remove('active'));document.getElementById(id).classList.add('active');document.querySelectorAll('.tabs button').forEach(b=>b.classList.remove('active'));btn.classList.add('active');}
function renderCours(){let niv=fNiv.value,s=fSearch.value.toLowerCase();let list=DB.cours||[];if(niv)list=list.filter(c=>c.n==niv);if(s)list=list.filter(c=>c.m.toLowerCase().includes(s)||c.t.toLowerCase().includes(s)||c.c.toLowerCase().includes(s));let h='';list.forEach(c=>{h+=`<div class=card><span class=badge style=background:#f9c00f>${c.n} ${c.s}</span> <small style=color:#00e5ff>${c.m}</small><h4 style=margin:5px 0;font-size:13px>${c.t}</h4><p class=small>${c.c}</p>${c.pdf?`<p style=margin-top:6px><a href="${c.pdf}" target="_blank" style=color:#00e5ff>📄 Voir PDF: ${c.pdf}</a></p>`:''}<small style=color:#555>Par ${c.a} - ${c.role||''}</small></div>`});gridCours.innerHTML=h;}
function renderOhada(){let h='';(DB.ohada||[]).forEach(o=>h+=`<div class=card style=border-left:3px solid #00e5ff><h4 style=color:#00e5ff;font-size:13px>${o.t}</h4><p class=small style=margin-top:6px>${o.c}</p></div>`);gridOhada.innerHTML=h;}
function renderDossier(){let h='';(DB.dossiers||[]).slice().reverse().forEach(d=>{h+=`<div class=card style=border:1px solid #ff1744"><div style=display:flex;justify-content:space-between><b style=font-size:12px>📂 ${d.type}</b><small style=color:#666>${d.time} par ${d.nom}</small></div><p class=small style=margin:6px 0><b>Cas:</b> ${d.desc}</p><div style=background:#111;padding:6px;border-radius:6px;margin:6px 0"><small style=color:#f9c00f><b>🤖 Analyse Auto DROIT224:</b> ${d.auto||''}</small></div><div class=dossier-analyses>${(d.analyses||[]).map(a=>`<div style=margin:6px 0;padding:6px;background:#0a0a1a;border-radius:6px"><span class="badge role-${a.role}">${a.role}</span> <b style=font-size:11px>${a.nom}</b><p class=small style=margin-top:4px>${a.msg}</p></div>`).join('')}</div><div style=display:flex;gap:4px;margin-top:8px"><select id=role-${d.id} style=width:30%;font-size:9px"><option>Étudiant</option><option>Professeur</option><option>Juge</option><option>Avocat</option><option>Docteur</option><option>Enseignant</option><option>Juriste</option></select><input id=name-${d.id} placeholder="Nom" style=width:25%;font-size:9px"><input id=msg-${d.id} placeholder="Ton analyse..." style=width:45%;font-size:9px"><button class=btn style=padding:4px 6px;font-size:8px" onclick=analyseDossier('${d.id}')>Analyser</button></div></div>`});gridDossier.innerHTML=h;}
function renderLex(){let h='';(DB.lexique||[]).forEach(l=>h+=`<div class=card><b style=font-size:12px>${l.t}</b> <span class=badge style=background:#00e5ff>${l.cat}</span><p class=small style=margin-top:4px>${l.d}</p></div>`);gridLex.innerHTML=h;}
async function searchLex(){let q=lexIn.value;if(q.length<2){lexAuto.innerHTML='';renderLex();return}let res=await fetch('/api/search?q='+encodeURIComponent(q)).then(r=>r.json());lexAuto.innerHTML=`<div class=card style=background:#002a2a;border-color:#00e5ff;margin-top:8px"><b>🤖 LEXIQUE IA répond:</b><p class=small style=margin-top:6px">${res.ans}</p></div>`;let filt=(DB.lexique||[]).filter(l=>l.t.toLowerCase().includes(q.toLowerCase())||l.d.toLowerCase().includes(q.toLowerCase()));let hh='';filt.slice(0,10).forEach(l=>hh+=`<div class=card><b>${l.t}</b><p class=small>${l.d}</p></div>`);if(filt.length)gridLex.innerHTML=hh;}
function renderFaq(){let h='';(DB.faq||[]).forEach(f=>h+=`<div class=card><b style=font-size:12px>Q: ${f.q}</b><p style=color:#76ff03;margin-top:6px" class=small>R: ${f.r}</p></div>`);gridFaq.innerHTML=h;}
async function askFaq(){let q=faqAsk.value;if(!q)return;let res=await fetch('/api/search?q='+encodeURIComponent(q)).then(r=>r.json());faqAuto.innerHTML=`<div class=card style=background:#001a00;border-color:#76ff03;margin-top:10px"><b>🤖 DROIT224 IA répond (connaît tout):</b><p class=small style=margin-top:6px">${res.ans}</p></div>`;}
async function addFaq(){let d={q:faqQ.value,r:faqR.value,nom:faqNom.value};if(!d.q||!d.r)return alert('Q et R');await fetch('/api/faq',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)});load();}
async function addLex(){let d={t:lexT.value,d:lexD.value};if(!d.t)return;await fetch('/api/lexique',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)});load();}
async function addCours(){let d={n:cNiv.value,m:cMat.value,t:cTitre.value,c:cCont.value,pdf:cPdf.value,role:cRole.value,nom:cNom.value};if(!d.t||!d.c)return alert('Titre et contenu obligatoires!');await fetch('/api/cours',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)});cTitre.value='';cCont.value='';cPdf.value='';load();alert('Cours publié!');}
async function postDossier(){let d={type:dType.value,desc:dDesc.value,nom:dNom.value};if(!d.desc)return alert('Décris cas');let res=await fetch('/api/search?q='+encodeURIComponent(d.type+' '+d.desc)).then(r=>r.json());d.auto=res.ans;await fetch('/api/dossiers',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)});dDesc.value='';load();}
async function analyseDossier(id){let role=document.getElementById('role-'+id).value,nom=document.getElementById('name-'+id).value,msg=document.getElementById('msg-'+id).value;if(!nom||!msg)return alert('Nom et analyse');await fetch('/api/dossiers/analyse',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({id,role,nom,msg})});load();}
let cq=[],qi=0,sc=0;function startQuiz(){let lvl=qLvl.value;cq=DB.quiz[lvl]||[];qi=0;sc=0;showQ();}
function showQ(){if(qi>=cq.length){qZone.innerHTML=`<h2 style=text-align:center>${sc}/${cq.length}</h2><div style=text-align:center;font-size:36px">${sc==cq.length?'🏆 OR':sc>=3?'🥈 ARGENT':'🥉 BRONZE'}</div><button class=btn onclick=startQuiz()>Rejouer</button>`;return}let q=cq[qi];let h=`<h4 style=margin:10px 0;font-size:12px>Q${qi+1}/${cq.length}: ${q.q}</h4>`;q.o.forEach((o,i)=>h+=`<div class=opt onclick=checkQ(${i})>${o}</div>`);qZone.innerHTML=h;}
function checkQ(i){let q=cq[qi];let ok=i==q.r;if(ok)sc++;qZone.innerHTML+=`<div class=card style=background:${ok?'#001a00':'#1a0000'};margin-top:8px"><b>${ok?'✅':'❌'} ${q.e}</b><br><button class=btn onclick="qi++;showQ()" style=margin-top:6px>Suivant</button></div>`;}
function renderForum(){let h='';(DB.forum||[]).slice().reverse().forEach(m=>{h+=`<div class=card style=border-left:3px solid #f9c00f"><span class="badge role-${m.role}">${m.role}</span> <b style=font-size:11px>${m.nom}</b> <small style=color:#666">${m.time}</small><p class=small style=margin:6px 0">${m.msg}</p></div>`});gridForum.innerHTML=h;}
async function postForum(){let d={role:fRole.value,nom:fNom.value,msg:fMsg.value};if(!d.nom||!d.msg)return;await fetch('/api/forum',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)});fMsg.value='';load();}
load();setInterval(load,20000);
</script></body></html>
"""

# API
def load_j(f,d):
    if not os.path.exists(f): return d
    try: return json.load(open(f,"r",encoding="utf-8"))
    except: return d
def save_j(f,d): json.dump(d, open(f,"w",encoding="utf-8"), ensure_ascii=False, indent=2)

COURS_LIST = COURS
OHADA_LIST = [
    {"t":"OHADA - Introduction","c":"Traité 1993, 17 pays, 10 Actes Uniformes, CCJA Abidjan cour suprême. But: même loi affaires Afrique. En Guinée: APIP applique OHADA."},
    {"t":"AUDCG - Commerce Général","c":"Définit commerçant, acte commerce, RCCM, bail commercial (2 ans min, renouvellement), fonds commerce, intermédiaires. RCCM à APIP obligatoire."},
    {"t":"AUSCGIE - Sociétés","c":"SARL 1-100 associés capital 1M, SA capital 10M, SAS libre. Création: statuts notaire + RCCM APIP + NIF. Gérant responsable pénal."},
    {"t":"AUS - Sûretés","c":"Garanties: cautionnement (personne garant), gage, nantissement fonds commerce, hypothèque immeuble (inscrite Conservation Kaloum), propriété retenue."},
    {"t":"AUPC - Procédures Collectives","c":"Entreprise difficulté: mandat ad hoc, redressement (sauver), liquidation (vendre). Déclaration cessation paiements 30 jours obligatoire."},
    {"t":"AUCE - Voies Exécution","c":"Récupérer argent après jugement: saisie attribution (banque), vente (meubles), immobilière (maison), rémunération (salaire), injonction payer rapide 15 jours."},
    {"t":"AUA - Arbitrage","c":"Régler litige sans tribunal, arbitre choisi, sentence = jugement. Rapide 6 mois, confidentiel, expert. CCJA centre arbitrage. Préféré étrangers."},
    {"t":"CCJA Abidjan","c":"Cour Commune Justice Arbitrage. 13 juges. Cassation OHADA: casse arrêt Appel Conakry mal jugé OHADA. Peut évoquer rejuge elle-même. Décisions primauté sur lois nationales."},
]
QUIZ_DATA = {
    "L1":[{"q":"Constitution 2020 = quelle République?","o":["3e","4e","5e"],"r":1,"e":"4e République référendum 2020"},{"q":"Garde à vue max?","o":["24h","48h renouvelable","7j"],"r":1,"e":"48h x2 =96h"},{"q":"Sans quoi pas TPI?","o":["Mise en demeure","Avocat","500k"],"r":0,"e":"Mise en demeure obligatoire"},{"q":"OHADA pays?","o":["10","17","54"],"r":1,"e":"17"},{"q":"Majorité Guinée?","o":["16","18","21"],"r":1,"e":"18 ans"}],
    "L2":[{"q":"Crime jugé par?","o":["TPI","Assises","Suprême"],"r":1,"e":"Crime=Assises"},{"q":"Contrat conditions?","o":["2","4","6"],"r":1,"e":"4: consentement capacité objet cause"},{"q":"SARL capital min?","o":["100k","1M","10M"],"r":1,"e":"1M depuis 2014"},{"q":"Recel =?","o":["Vol","Acheter volé sachant volé","Rien"],"r":1,"e":"Même peine voleur"},{"q":"CCJA où?","o":["Conakry","Abidjan","Dakar"],"r":1,"e":"Abidjan"}],
    "L3":[{"q":"Cour Suprême juge?","o":["Faits","Droit","Deux"],"r":1,"e":"Juge droit seulement"},{"q":"Titre Foncier faux?","o":["Valable","Danger","Gratuit"],"r":1,"e":"80% arnaques"},{"q":"Clause léonine?","o":["Valable","Nulle","Oblig"],"r":1,"e":"Interdite"},{"q":"Pourvoi délai?","o":["15j","2 mois","1 an"],"r":1,"e":"2 mois"},{"q":"Prescription terrain?","o":["5","10","30 ans"],"r":2,"e":"30 ans"}],
    "OHADA":[{"q":"OHADA =?","o":["Harmonisation Droit Affaires","Humanitaire","Douane"],"r":0,"e":"Harmonisation Droit Affaires"},{"q":"Sociétés =?","o":["AUDCG","AUSCGIE","AUCE"],"r":1,"e":"AUSCGIE"},{"q":"RCCM à?","o":["Mairie","APIP","TPI"],"r":1,"e":"APIP"},{"q":"Hypothèque où?","o":["Mairie","Conservation","APIP"],"r":1,"e":"Conservation Kaloum"},{"q":"Arbitrage avantage?","o":["Lent","Rapide confidentiel","Gratuit"],"r":1,"e":"6 mois vs 2 ans TPI"}],
}

@app.route("/api/all")
def all_api():
    dossiers=load_j("dossiers_v6.json", [])
    cours_extra=load_j("cours_extra_v6.json", [])
    lex_extra=load_j("lex_extra_v6.json", [])
    faq_extra=load_j("faq_extra_v6.json", [])
    all_cours=COURS_LIST + cours_extra
    all_lex=LEXIQUE_MASSIF + lex_extra
    all_faq=FAQ_BASE + faq_extra
    return jsonify({"cours":all_cours,"ohada":OHADA_LIST,"lexique":all_lex,"quiz":QUIZ_DATA,"faq":all_faq,"dossiers":dossiers,"forum":load_j("forum_v6.json", FORUM_INIT)})

@app.route("/api/search")
def search_api():
    q=request.args.get("q","")
    ans=intelligent_answer(q)
    return jsonify({"ans":ans})

@app.route("/api/cours", methods=["POST"])
def cours_post():
    d=request.get_json()
    extra=load_j("cours_extra_v6.json", [])
    extra.insert(0,{"n":d.get("n","L1"),"s":"S1","m":d.get("m","Général"),"t":d.get("t",""),"c":d.get("c",""),"a":f"{d.get('nom','')} ({d.get('role','')})","pdf":d.get("pdf",""),"role":d.get("role","")})
    save_j("cours_extra_v6.json", extra)
    return jsonify({"ok":True})

@app.route("/api/lexique", methods=["POST"])
def lex_post():
    d=request.get_json()
    extra=load_j("lex_extra_v6.json", [])
    extra.insert(0,{"t":d.get("t",""),"d":d.get("d",""),"cat":"Ajouté"})
    save_j("lex_extra_v6.json", extra)
    return jsonify({"ok":True})

@app.route("/api/faq", methods=["POST"])
def faq_post():
    d=request.get_json()
    extra=load_j("faq_extra_v6.json", [])
    extra.insert(0,{"q":d.get("q",""),"r":f"{d.get('r','')} (Ajouté par {d.get('nom','Anonyme')} le {datetime.now().strftime('%d/%m/%Y')})","tags":d.get("q","")})
    save_j("faq_extra_v6.json", extra)
    return jsonify({"ok":True})

@app.route("/api/dossiers", methods=["POST"])
def dossiers_post():
    d=request.get_json()
    alld=load_j("dossiers_v6.json", [])
    alld.append({"id":uuid.uuid4().hex[:5],"type":d.get("type",""),"desc":d.get("desc",""),"nom":d.get("nom",""),"time":datetime.now().strftime("%d/%m %H:%M"),"auto":d.get("auto",""),"analyses":[]})
    save_j("dossiers_v6.json", alld)
    return jsonify({"ok":True})

@app.route("/api/dossiers/analyse", methods=["POST"])
def dossier_analyse():
    d=request.get_json()
    alld=load_j("dossiers_v6.json", [])
    for dos in alld:
        if dos["id"]==d.get("id"):
            dos.setdefault("analyses",[]).append({"role":d.get("role",""),"nom":d.get("nom",""),"msg":d.get("msg","")})
    save_j("dossiers_v6.json", alld)
    return jsonify({"ok":True})

@app.route("/api/forum", methods=["GET","POST"])
def forum_api():
    if request.method=="POST":
        d=request.get_json()
        allf=load_j("forum_v6.json", FORUM_INIT)
        allf.append({"id":uuid.uuid4().hex[:5],"role":d.get("role",""),"nom":d.get("nom",""),"msg":d.get("msg",""),"time":datetime.now().strftime("%H:%M")})
        save_j("forum_v6.json", allf)
        return jsonify({"ok":True})
    return jsonify(load_j("forum_v6.json", FORUM_INIT))

if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)))
