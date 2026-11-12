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
    {"q":"Terrain vendeur veut reprendre?","r":"Si Titre Foncier à ton nom = il peut rien. Si seulement acte quartier = danger! Va vite Conservation Kaloum faire Titre 2-5M. Vérifie toujours
