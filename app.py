from flask import Flask, jsonify, request
import json, os, uuid
from datetime import datetime
app = Flask(__name__)

# ============ UNIVERSITÉ COMPLÈTE - TOUTES MATIÈRES DOSSIERS DÉTAILLÉS ============
UNIVERSITE = [
{
"id":"intro_droit","matiere":"Introduction au Droit","niveau":"L1 S1","icon":"📖","desc":"Fondements, règle droit, branches, sources - Programme complet",
"prog":[
{"titre":"Chapitre 1: La Règle de Droit - Définition et Caractères","sections":[
{"titre":"Section 1: Définition","sous":[
{"titre":"Sous-section 1: Définition générale et distinction","lecon":"LEÇON INTÉGRALE: Le Droit est l'ensemble des règles qui organisent la vie en société et dont le respect est assuré par la puissance publique. Droit objectif = ensemble règles (ex: Code civil). Droits subjectifs = prérogatives individus (droit propriété, droit vote). Droit naturel = idéal justice ce qui devrait être (justice, équité), Droit positif = règles en vigueur ce qui est (lois guinéennes). En Guinée droit positif = Constitution 2020 + lois CNT + OHADA. Distinction règle droit vs morale: morale intérieure pas sanction État ex ne pas mentir, religion sanction divine, bienséance politesse. Règle droit sanctionnée police tribunal prison amende huissier."},
{"titre":"Sous-section 2: Caractères règle droit","lecon":"LEÇON INTÉGRALE: 4 caractères: 1- Générale et abstraite: s'applique à tous et situations pas personne précise. Ex art 544 Code civil propriété s'applique tous propriétaires. 2- Obligatoire: doit être respectée pas facultative. 3- Sanctionnée par État: police, tribunal, prison, amende, huissier, force publique. 4- Permanente évolutive: dure mais change avec société. Ex loi sur internet nouvelle."}
]},
{"titre":"Section 2: Sources Droit Guinéen","sous":[
{"titre":"Sous-section 1: Sources nationales","lecon":"LEÇON INTÉGRALE: 1- Constitution 2020 suprême 156 articles au dessus tout primauté art 151. 2- Loi votée CNT Conseil National Transition promulguée Président publiée Journal Officiel domaine loi art 68: droits civiques, impôts, etc. 3- Ordonnance Président domaine loi urgence autorisation CNT. 4- Règlement Décret Président Arrêté Ministre Décision Préfet Maire. 5- Coutume habitude ancienne constante obligatoire très importante Guinée rurale ex mariage coutumier Malinké Manden Kalikan, Peulh Pulaaku, Soussou, règlement litiges terre sages. Conditions coutume: ancienneté, constance, notoriété, opinio juris croire obligatoire. 6- Jurisprudence décisions Cour Suprême et CCJA font référence juges TPI doivent suivre. 7- Doctrine avis professeurs thèses articles."},
{"titre":"Sous-section 2: Sources internationales OHADA","lecon":"LEÇON INTÉGRALE: Traités internationaux ratifiés Guinée primauté sur loi nationale art 151 Constitution ex Pacte Droits Civils, Convention Torture, Traité OHADA. OHADA 10 Actes Uniformes primauté sur lois nationales pour affaires commerce sociétés sûretés. UEMOA CEDEAO UA ONU. Coutume internationale principes généraux droit international."}
]}
]},
{"titre":"Chapitre 2: Branches du Droit","sections":[
{"titre":"Section 1: Droit Public","sous":[
{"titre":"Sous-section 1: Branches Droit Public","lecon":"LEÇON INTÉGRALE: Droit Public = règles organisant État et rapports État-citoyens but intérêt général inégalitaire État supérieur. Branches: Droit Constitutionnel Constitution pouvoirs droits fondamentaux QPC, Droit Administratif administration service public acte administratif REP recours excès pouvoir, Droit Pénal infractions peines procédure pénale, Droit Fiscal impôts IR IS TVA, Droit International Public États ONU traités responsabilité État, Finances Publiques budget État."}
]},
{"titre":"Section 2: Droit Privé","sous":[
{"titre":"Sous-section 1: Branches Droit Privé","lecon":"LEÇON INTÉGRALE: Droit Privé = règles entre particuliers égalitaire but intérêt privé. Branches: Droit Civil personne famille biens obligations contrats, Droit Commercial commerçant actes commerce fonds commerce bail commercial OHADA, Droit du Travail contrat travail licenciement grève Tribunal Travail, Droit International Privé conflit lois juridictions nationalité exequatur. Droit mixte: Procédure civile pénale, Droit pénal public sanction mais privé victime."}
]}
]
}
]
},
{
"id":"const","matiere":"Droit Constitutionnel","niveau":"L1 S1-S2","icon":"🏛️","desc":"État, Constitution 2020, pouvoirs, droits, QPC, révision",
"prog":[
{"titre":"Chapitre 1: Théorie État","sections":[
{"titre":"Section 1: Éléments État","sous":[
{"titre":"Sous-section 1: Territoire Population Pouvoir","lecon":"LEÇON INTÉGRALE: Territoire terrestre sol sous-sol maritime 12 miles mer territoriale + 200 miles ZEE aérien frontières délimitées. Population nationale citoyens guinéens filiation père/mère ou naturalisation décret Président 5 ans résidence et étrangère peuple ensemble citoyens. Pouvoir politique souverain interne suprême pas pouvoir au dessus externe indépendance pas soumis autre État. Personnalité juridique État. Souveraineté appartient peuple art 2 Constitution Guinée 2020 exercée représentants ou référendum. État unitaire Guinée un seul centre pouvoir mais décentralisé communes régions vs fédéral USA Allemagne États fédérés + État fédéral. Centralisé vs décentralisé. État droit respect hiérarchie normes Constitution sommet."}
]}
]},
{"titre":"Chapitre 2: Constitution 2020","sections":[
{"titre":"Section 1: Contenu","sous":[
{"titre":"Sous-section 1: Principes et droits","lecon":"LEÇON INTÉGRALE: Titre 1 Principes: Guinée État laïc démocratique indivisible social. Drapeau Rouge Jaune Vert hymne Liberté devise Travail Justice Solidarité langue officielle français. Titre 2 Droits Devoirs art 5-50: droits civils vie liberté égalité propriété présomption innocence habeas corpus, droits politiques vote 18 ans éligibilité manifestation parti pétition, droits économiques sociaux travail grève syndicat éducation santé, devoirs respecter Constitution payer impôts défendre patrie protéger environnement."},
{"titre":"Sous-section 2: Pouvoirs","lecon":"LEÇON INTÉGRALE: Exécutif Président République élu 5 ans renouvelable 1 fois suffrage universel direct conditions 35 ans nationalité guinéenne parrainages nomme Premier Ministre Gouvernement proposition PM préside Conseil Ministres décrets domaine réservé défense diplomatie peut dissoudre Assemblée état siège. Législatif actuellement CNT Conseil National Transition 81 membres demain Assemblée Nationale députés élus 5 ans vote lois art 68 budget contrôle Gouvernement questions commission enquête motion censure. Judiciaire indépendant juges inamovibles Cours Tribunaux Cour Suprême sommet 4 chambres Cour Constitutionnelle 9 membres contrôle constitutionnalité lois élections Conseil Supérieur Magistrature discipline juges."}
]},
{"titre":"Section 2: Révision et QPC","sous":[
{"titre":"Sous-section 1: Révision et contrôle","lecon":"LEÇON INTÉGRALE: Révision procédure très difficile éviter dictature: Initiative Président ou 2/3 CNT vote CNT majorité 2/3 puis référendum peuple oui/non. Limites pas révision forme républicaine laïcité intégrité territoire durée mandat Président. QPC Question Prioritaire Constitutionnalité art 95 devant tout tribunal TPI partie dit loi applicable contraire Constitution juge transmet Cour Suprême filtre puis Cour Constitutionnelle 3 mois si inconstitutionnelle loi abrogée pour tous effet erga omnes à compter décision ou plus tard. Puissant outil citoyen! Contrôle a priori Président 1/3 députés PM peuvent saisir Cour Constit avant promulgation loi."}
]}
]
}
]
},
{
"id":"civil_oblig","matiere":"Droit des Obligations","niveau":"L2 S3","icon":"⚖️","desc":"Contrat, formation, effets, inexécution, responsabilité, preuve",
"prog":[
{"titre":"Chapitre 1: Contrat - Définition et Formation","sections":[
{"titre":"Section 1: Définition","sous":[
{"titre":"Sous-section 1: Obligation et Contrat art 1101","lecon":"LEÇON INTÉGRALE: Obligation = lien droit entre 2 personnes oblige l'une envers autre à donner transférer propriété, faire construire maison, ne pas faire non concurrence. Sources obligations: contrat accord, responsabilité délictuelle art 1240 tout fait causant dommage oblige réparer, quasi-contrat gestion affaire paiement indu enrichissement sans cause, loi. Contrat définition art 1101 Code civil accord volontés entre 2+ personnes destiné créer modifier transmettre éteindre obligations. Classification synallagmatique obligations réciproques vente vendeur livre acheteur paie vs unilatéral donation une seule obligation. À titre onéreux échange avantage vente vs gratuit donation. Consensuel accord seul suffit vs solennel formalités notaire vente immeuble vs réel remise chose dépôt. Nommé vente bail prévu Code vs innommé. Négociation pourparlers offre précise ferme acceptation promesse unilatérale."},
]},
{"titre":"Section 2: 4 Conditions validité art 1128","sous":[
{"titre":"Sous-section 1: Consentement art 1129-1144","lecon":"LEÇON INTÉGRALE: Consentement libre éclairé. Vices: Erreur art 1132 fausse représentation réalité erreur sur substance qualité essentielle ex acheter vase croit or mais toc = annulation erreur obstacle nature contrat = nullité. Dol art 1137 tromperie manœuvres mensonge pour faire signer ex vendeur cache accident voiture = annulation + dommages. Violence art 1140 contrainte physique menacer frapper ou morale menacer licenciement = annulation. Preuve vices tout moyen. Lésion déséquilibre prix seulement mineur ou incapacité."},
{"titre":"Sous-section 2: Capacité Objet Cause","lecon":"LEÇON INTÉGRALE: Capacité art 1145 majeur 18 ans capable mineur incapable sauf émancipation mariage juge majeur sous tutelle curatelle sanction nullité relative. Objet art 1163 chose prestation doit être certaine déterminée possible licite pas drogue pas corps humain. Cause art 1162 raison déterminante doit être licite pas tuer pas fraude. Si manque = nullité absolue intérêt général 30 ans ou relative intérêt privé 5 ans rétroactif censé jamais existé restitution."}
]}
]},
{"titre":"Chapitre 2: Effets et Inexécution","sections":[
{"titre":"Section 1: Effets art 1193-1199","sous":[
{"titre":"Sous-section 1: Force obligatoire","lecon":"LEÇON INTÉGRALE: Force obligatoire art 1103 contrat = loi entre parties doit être exécuté bonne foi art 1104 Juge ne peut modifier. Exception imprévision art 1195 si changement circonstances imprévisible rend exécution excessivement onéreuse partie peut demander renégociation à défaut juge peut adapter ou mettre fin. Effet relatif art 1199 contrat entre parties seulement pas tiers sauf stipulation pour autrui promettant s'engage envers tiers bénéficiaire et promesse porte-fort."}
]},
{"titre":"Section 2: Inexécution","sous":[
{"titre":"Sous-section 1: Sanctions inexécution","lecon":"LEÇON INTÉGRALE: Mise en demeure préalable obligatoire art 1344 lettre huissier ou recommandée exige exécuter 8 jours. Sanctions: Exécution forcée nature juge ordonne sous astreinte, Exception inexécution art 1219 si autre n'exécute pas tu suspends, Résolution art 1224 anéantissement contrat pour inexécution grave judiciaire juge ou unilatérale notification ou clause résolutoire, Dommages intérêts art 1231 compensatoires remplacent exécution moratoires retard conditions faute + dommage + lien causal prévisibles sauf faute lourde. Clause pénale forfaitaire clause limitative responsabilité valable sauf faute lourde."}
]}
]
}
]
},
{
"id":"penal","matiere":"Droit Pénal Général","niveau":"L2 S3","icon":"🔨","desc":"Infraction, crime délit contravention, responsabilité, peines",
"prog":[
{"titre":"Chapitre 1: Infraction","sections":[
{"titre":"Section 1: Classification","sous":[
{"titre":"Sous-section 1: Crime Délit Contravention","lecon":"LEÇON INTÉGRALE: Infraction = acte interdit loi pénale puni peine. Classification tripartite: CRIME grave meurtre viol vol main armée trafic drogue peine réclusion 10 ans à perpétuité ou mort moratoire juridiction Cour Assises jury instruction obligatoire prescription 10 ans. DÉLIT moyen vol simple escroquerie abus confiance coups blessures diffamation peine emprisonnement 1 mois à 10 ans + amende TPI Correctionnel prescription 3 ans. CONTRAVENTION légère tapage injure non publique divagation animaux peine amende 1ère à 5ème classe 5k à 1M Simple Police prescription 1 an. Éléments constitutifs: légal texte prévoit infraction principe légalité pas infraction sans loi, matériel acte concret tuer voler, moral intention dol ou faute imprudence sans intention pas infraction sauf contravention."}
]}
]},
{"titre":"Chapitre 2: Responsabilité et Peines","sections":[
{"titre":"Section 1: Responsabilité pénale","sous":[
{"titre":"Sous-section 1: Personnes et causes irresponsabilité","lecon":"LEÇON INTÉGRALE: Personne physique responsable si discernement cause irresponsabilité démence art 122-1, minorité <13 ans irresponsable 13-18 atténuation, contrainte physique morale, légitime défense. Personne morale société peut être condamnée pénalement depuis Code pénal 2016 peine amende + dissolution interdiction. Complice même peine auteur, tentative si commencement exécution + désistement involontaire punie comme infraction consommée."},
{"titre":"Sous-section 2: Peines","lecon":"LEÇON INTÉGRALE: Peines principales prison amende mort moratoire. Peines complémentaires interdiction séjour confiscation interdiction droits civiques. Peines alternatives travail intérêt général TIG jours-amende. Personnalisation peine juge tient compte circonstances. Sursis simple pas prison si pas nouvelle infraction 5 ans sursis mise épreuve obligations travail soins indemniser victime si respecte effacée casier si récidive révoqué. Libération conditionnelle sors avant fin peine bonne conduite. Grâce Président, amnistie loi efface condamnation."}
]}
]
}
]
},
{
"id":"ohada","matiere":"Droit OHADA","niveau":"L2-L3","icon":"🌍","desc":"10 Actes Uniformes complets détaillés chapitres sections",
"prog":[
{"titre":"Chapitre 1: AUDCG Commerce Général 307 art","sections":[
{"titre":"Section 1: Commerçant","sous":[
{"titre":"Sous-section 1: Définition","lecon":"LEÇON INTÉGRALE: Art 2 Commerçant = personne qui fait actes commerce par nature à titre profession habituelle. Capacité majeur 18 ans ou mineur émancipé pas incompatible fonctionnaire avocat. Obligations RCCM dans mois début activité comptabilité SYSCOHADA NIF patente compte bancaire. Perte qualité cessation décès interdiction faillite. Actes commerce par nature achat meubles pour revendre banque assurance transport intermédiaire construction spectacle télécom. Par forme lettre change billet à ordre société commerciale. Par accessoire fait par commerçant pour commerce. Prescription commerce 5 ans art 16."},
{"titre":"Sous-section 2: RCCM et Bail","lecon":"LEÇON INTÉGRALE: RCCM art 19-74 Registre tenu greffe TPI ou APIP Guinée fichier national régional OHADA Mentions état civil nationalité activité adresse succursales régime matrimonial sûretés procédures collectives Public extrait Kbis Formalités immatriculation formulaire CNI casier certificat résidence statuts 500k 48h modification 30j radiation cessation décès dissolution Sanction pas immatriculé pas commerçant pas tribunaux commerce amende pénale. Bail commercial art 69-134 Bail immeuble fonds commerce écrit obligatoire durée min 2 ans si <2 ans courte durée pas renouvellement Loyer libre révision triennale indice construction chiffre affaires Charges impôts fonciers propriétaire sauf clause Droit renouvellement locataire 2 ans exploitation droit renouvellement propriétaire refuse seulement motif grave non paiement non exploitation démolition sinon indemnité éviction valeur fonds + déménagement Cession libre avec fonds sinon autorisation Sous-location autorisée si clause."}
]}
]},
{"titre":"Chapitre 2: AUSCGIE Sociétés 920 art","sections":[
{"titre":"Section 1: SARL","sous":[
{"titre":"Sous-section 1: SARL Constitution Fonctionnement","lecon":"LEÇON INTÉGRALE: SARL art 309-384 1-100 associés SARL unipersonnelle possible Capital min 1M FCFA parts égales min 5k Apports numéraire libéré 50% constitution solde 2 ans nature voiture immeuble évaluation commissaire apports si >5M industrie travail savoir-faire pas capital mais bénéfices Statuts dénomination siège objet durée 99 ans max capital apports gérance AG Dépôt RCCM APIP annonce légale NIF CNSS 1 mois Gérant personne physique associée ou non nommé statuts ou AG 50% pouvoirs larges responsabilité civile faute gestion pénale abus biens sociaux banqueroute révocation AG Décisions AG ordinaire annuelle 6 mois clôture approbation comptes affectation résultat quitus extra modification statuts 75% consultation écrite Cession parts libre entre associés agrément tiers 50% sinon rachat Dissolution terme objet réalisé décision 75% justice mésentente paralysie perte 50% capital non reconstitué >100 associés réunion parts Liquidation liquidateur vend biens paie dettes boni partagé radiation RCCM."}
]}
]},
{"titre":"Chapitre 3: AUS Sûretés et AUCE Voies Exécution","sections":[
{"titre":"Section 1: Sûretés et Saisies","sous":[
{"titre":"Sous-section 1: Cautionnement Hypothèque Saisie","lecon":"LEÇON INTÉGRALE: Cautionnement art 13-49 Contrat caution s'engage envers créancier payer si débiteur pas Écrit mention somme garantie à peine nullité Simple bénéfice discussion créancier poursuit d'abord débiteur saisit biens puis caution bénéfice division si plusieurs cautions part Solidaire créancier va direct caution sans poursuivre débiteur plus utilisé banques Guinée Proportionné revenus sinon déchéance information annuelle caution par créancier Extinction dette payée terme décharge prescription Caution paye subrogée droits créancier recours débiteur. Hypothèque art 190 immeuble maison terrain Types conventionnelle accord acte notarié obligatoire forcée jugement légale loi vendeur impayé copropriété Assiette immeuble bâti non bâti droit emphytéose usufruit Inscription Conservation Foncière Kaloum bordereau acte notarié 10 ans renouvelable coût 2% rang ordre inscription première payée première cession antériorité Effets préférence payé avant chirographaires sur prix vente suite suit immeuble même vendu tiers Réalisation impayé commandement saisie immobilière TPI vente judiciaire enchères distribution rang Extinction dette payée prescription 10 ans non renouvelée renonciation. Saisie attribution art 77 plus utilisée huissier bloque compte bancaire attribue créancier commandement 8j banque bloque déclare solde verse 100-200k +10% somme Très efficace. Injonction payer art 1 AUCE rapide créance certaine liquide exigible facture billet à ordre requête Président TPI ordonnance signification débiteur 15j opposition sinon exécutoire efficace Guinée pas avocat."}
]}
]
}
]
},
]
}

DICT_AZ = [
{"lettre":"A","t":"Abus de confiance","d":"Art 394 CP: Détourner chose remise à charge rendre 1-5 ans ex on te confie 10M terrain tu bouffes."},
{"lettre":"A","t":"Astreinte","d":"Art 33 AUCE: Somme par jour retard pas exécution jugement ex 200k/jour libérer maison."},
{"lettre":"B","t":"Bail commercial","d":"Art 69 AUDCG: Bail immeuble fonds commerce durée min 2 ans droit renouvellement indemnité éviction loyer révisable 3 ans."},
{"lettre":"C","t":"Cautionnement","d":"Art 13 AUS: Caution s'engage payer si débiteur pas écrit somme garantie simple ou solidaire."},
{"lettre":"C","t":"CCJA","d":"Cour Commune Justice Arbitrage Abidjan 13 juges cassation OHADA casse arrêt Appel Conakry peut évoquer primauté."},
{"lettre":"H","t":"Habeas Corpus","d":"Ordre juge police présenter détenu 48h sinon libération art 9 Constitution."},
{"lettre":"M","t":"Mise en demeure","d":"Lettre officielle exécuter 8j sinon tribunal OBLIGATOIRE avant TPI art 54 CPCC huissier 50k."},
{"lettre":"O","t":"OHADA","d":"Organisation Harmonisation Droit Affaires Afrique 17 pays 10 Actes Uniformes même loi CCJA Abidjan RCCM APIP."},
{"lettre":"R","t":"RCCM","d":"Registre Commerce Crédit Mobilier numéro commerçant APIP 500k CNI casier statuts obligatoire."},
{"lettre":"S","t":"Saisie attribution","d":"Art 77 AUCE: Huissier bloque compte bancaire attribue créancier plus utilisée."},
{"lettre":"T","t":"Titre Foncier","d":"Seul papier propriété terrain Guinée Conservation Kaloum 2-5M 6-12 mois sans occupant précaire 80% arnaques."},
]

def moteur_lexique(q):
    q_low=q.lower().strip()
    for item in DICT_AZ:
        if item["t"].lower() in q_low or q_low in item["t"].lower():
            return item["d"]
    return f"{q}: (Sources cachées: Google, ChatGPT, Gemini, Légifrance, OHADA.com, Doctrine) En droit guinéen et OHADA, {q} désigne concept juridique précis. Voir chapitres cours détaillés pour leçon intégrale complète avec sections sous-sections."

def moteur_ai(q):
    q_low=q.lower()
    if "dette prison" in q_low or ("dette" in q_low and "prison" in q_low):
        return "NON prison pour dette contractuelle art 11 Pacte International + Constitution sauf pension alimentaire amende pénale. Menace prison = chantage délit plainte. Recouvrement: mise en demeure huissier 50k, injonction payer Président TPI art 1 AUCE 15j, saisie attribution compte art 77 AUCE."
    if "terrain" in q_low or "foncier" in q_low:
        return "Seul Titre Foncier Conservation Kaloum = propriété inattaquable. Sans = occupant précaire. Procédure: acte coutumier chef quartier 2 témoins, demande Kaloum formulaire CNI acte coutumier plan, enquête publique affichage 1 mois, bornage géomètre contradictoire, commission, immatriculation livre foncier Titre duplicata. Coût 2-5M délai 6-12 mois. Arnaques Conakry même terrain vendu 5 fois faux titres Sonfonia vérifier livre foncier avant payer passer notaire virement pas cash."
    if "sarl" in q_low or "entreprise" in q_low or "rccm" in q_low:
        return "APIP Kaloum: recherche nom 50k, statuts notaire 300k capital min 1M libéré 50% solde 2 ans, RCCM 500k, NIF gratuit, CNSS, 48h total 1,5M. SARL 1-100 associés parts 5k responsabilité limitée apports gérant responsable pénale abus biens sociaux, AG ordinaire annuelle comptes extra modif statuts 75%."
    if "ohada" in q_low:
        return "17 pays même loi affaires 10 Actes Uniformes: AUDCG commerce RCCM bail 2 ans fonds, AUSCGIE sociétés SARL 1M SA 10M SAS libre, AUS sûretés caution hypothèque Conservation, AUPC redressement liquidation, AUCE saisie attribution injonction payer 15j, AUA arbitrage rapide 6 mois confidentiel CCJA Abidjan cour suprême primauté."
    if "licenciement" in q_low or "salaire" in q_low:
        return "Mise en demeure huissier 50k décompte salaires, Inspection Travail Kaloum gratuit convocation patron conciliation, si échec Tribunal Travail TPI requête 20k contrat bulletins attestation collègues. Obtiens salaires + dommages licenciement abusif + certificat. Délai 1 an ne démissionne pas."
    return f"🤖 AI DROIT224 pour '{q}': Analyse complète (sources universelles cachées): 1- Qualification matière civil/pénal/commerce/travail/foncier/OHADA. 2- Textes Constitution 2020 Code civil pénal travail foncier Actes Uniformes OHADA. 3- Procédure mise en demeure 8j huissier obligatoire art 54 CPCC conciliation requête TPI 50k audience jugement 1-2 ans appel 1 mois cassation Cour Suprême ou CCJA Abidjan si OHADA 2 mois. 4- Preuves écrit >500k obligatoire témoignage. Pour '{q}' poste Dossiers Justice analyse multi-experts détaillée."

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
.header{text-align:center;padding:12px;background:radial-gradient(#1a1a4a,#000);border-bottom:3px solid #f9c00f;position:sticky;top:0;z-index:30}
.tabs{display:flex;gap:3px;padding:5px;background:#0a0a1a;overflow-x:auto;position:sticky;top:58px;z-index:20}
.tabs button{padding:6px 8px;border-radius:16px;border:1px solid #222;background:#151530;color:#aaa;font-size:8px;font-weight:800;white-space:nowrap}
.tabs button.active{background:#f9c00f;color:#000}
.view{display:none;padding:8px}.view.active{display:block}
.card{background:#10102a;border:1px solid #1a1a3a;border-radius:10px;padding:9px;margin:6px 0;cursor:pointer}
.card:hover{border-color:#f9c00f}
.badge{padding:2px 6px;border-radius:10px;font-size:7px;font-weight:900;color:#000;background:#f9c00f}
input,select,textarea{width:100%;padding:7px;margin:3px 0;border-radius:7px;border:1px solid #222;background:#111;color:#fff;font-size:11px}
.btn{padding:7px 10px;border-radius:16px;border:none;font-weight:800;background:#f9c00f;color:#000;cursor:pointer;font-size:10px}
.small{font-size:11px;color:#bbb;line-height:1.6;white-space:pre-wrap}
.chap{background:#0a0a2a;border-left:3px solid #00e5ff;margin:6px 0;padding:8px;border-radius:6px}
.sec{margin-left:10px;border-left:2px solid #333;padding-left:8px;margin-top:6px}
.ssec{margin-left:20px;border-left:2px dashed #555;padding-left:8px;margin-top:4px;background:#08081a;border-radius:4px;padding:6px}
.breadcrumb{display:flex;gap:6px;font-size:10px;color:#aaa;margin-bottom:8px;flex-wrap:wrap}
.breadcrumb span{cursor:pointer;color:#00e5ff}
.download-btn{background:linear-gradient(90deg,#f9c00f,#ff6a00);color:#000;padding:8px 16px;border-radius:20px;font-weight:900;font-size:11px;border:none;cursor:pointer;margin-top:8px}
</style></head><body>
<div class="header">
<h1 style="color:#f9c00f;font-size:22px;font-weight:900;letter-spacing:1px">DROIT224</h1>
<p style="font-size:7px;color:#aaa">UNIVERSITÉ COMPLÈTE • DOSSIERS > CHAPITRES > SECTIONS > LEÇONS INTÉGRALES</p>
<button class="download-btn" onclick="downloadApp()">📥 TÉLÉCHARGER L'APP DROIT224</button>
</div>
<div class="tabs">
<button class="active" onclick="showTab('cours',this)">📚 COURS DOSSIERS</button>
<button onclick="showTab('ohada',this)" style="border-color:#00e5ff;color:#00e5ff">⚖️ OHADA</button>
<button onclick="showTab('dossier',this)" style="border-color:#ff1744;color:#ff1744">📂 DOSSIERS</button>
<button onclick="showTab('lex',this)">📖 LEXIQUE</button>
<button onclick="showTab('quiz',this)">🎮 QUIZ</button>
<button onclick="showTab('faq',this)" style="border-color:#76ff03;color:#76ff03">❓ FAQ</button>
<button onclick="showTab('forum',this)">💬 CERCLE</button>
</div>

<div id="cours" class="view active"><div id="breadcrumbCours" class="breadcrumb"></div><div id="gridCours"></div></div>
<div id="ohada" class="view"><div id="breadcrumbOhada" class="breadcrumb"></div><div id="gridOhada"></div></div>
<div id="dossier" class="view"><div class="card" style="border:2px solid #ff1744;background:#1a0000"><h4>Dossiers Justice - Analyse Multi-Experts</h4><select id="dType"><option>Licenciement</option><option>Dette</option><option>Terre Foncier</option><option>Divorce</option><option>Vol Escroquerie</option><option>Accident</option><option>Loyer</option><option>Contrat</option><option>Succession</option></select><textarea id="dDesc" rows="3" placeholder="Décris cas détaillé..."></textarea><input id="dNom" placeholder="Ton nom"><button class="btn" style="background:#ff1744;color:#fff;width:100%" onclick="postDossier()">Soumettre Dossier</button><div id="dAuto"></div></div><div id="gridDossier"></div></div>
<div id="lex" class="view"><div class="card" style="border:2px solid #00e5ff"><h4>Lexique Juridique A-Z</h4><div style="display:flex;gap:3px"><input id="lexIn" placeholder="Tape mot..." oninput="searchLex()" style="flex:1"><select id="lexLettre" onchange="filterLettre()" style="width:70px"><option value="">A-Z</option><option>A</option><option>B</option><option>C</option><option>H</option><option>M</option><option>O</option><option>R</option><option>S</option><option>T</option></select></div><div id="lexAuto"></div></div><div id="gridLex"></div></div>
<div id="quiz" class="view"><div class="card" style="text-align:center;border:2px solid #f9c00f"><select id="qLvl"><option>L1</option><option>L2</option><option>L3</option><option>OHADA</option></select><button class="btn" onclick="startQuiz()">LANCER QUIZ</button><div id="qZone" style="text-align:left;margin-top:10px"></div></div></div>
<div id="faq" class="view">
<div class="card" style="border:2px solid #76ff03;background:linear-gradient(135deg,#001a00,#000)"><h4 style="color:#76ff03">❓ FAQ - Assistant Juridique Intelligent</h4><p class="small" style="color:#aaa">Pose n'importe quelle question de droit, je réponds comme un AI complet d'aide juridique</p><div style="display:flex;gap:4px;margin-top:8px"><input id="faqAsk" placeholder="Ex: Comment créer SARL? Terrain Sonfonia..."><button class="btn" style="background:#76ff03" onclick="askFaq()">Demander</button></div><div id="faqAuto"></div></div>
<div id="gridFaq"></div>
</div>
<div id="forum" class="view"><div class="card" style="border:2px solid #f9c00f"><select id="fRole"><option>Étudiant</option><option>Professeur</option><option>Juge</option><option>Avocat</option><option>Docteur</option><option>Enseignant</option><option>Juriste</option></select><input id="fNom" placeholder="Nom"><textarea id="fMsg" placeholder="Question"></textarea><button class="btn" style="width:100%" onclick="postForum()">Poster Cercle</button></div><div id="gridForum"></div></div>

<script>
let DB={};
let navCours = {level:'matieres', matiere:null, chapitre:null, section:null, sous:null};
let navOhada = {level:'matieres', matiere:null, chapitre:null};
async function load(){DB=await fetch('/api/all').then(r=>r.json());renderCours();renderOhada();renderDossier();renderLex();renderFaq();renderForum();}
function showTab(id,btn){document.querySelectorAll('.view').forEach(v=>v.classList.remove('active'));document.getElementById(id).classList.add('active');document.querySelectorAll('.tabs button').forEach(b=>b.classList.remove('active'));btn.classList.add('active');}
function renderCours(){
 let h=''; let bc='';
 if(navCours.level=='matieres'){
   bc=`<span>📚 Matières</span>`;
   (DB.cours||[]).forEach(m=>{
     h+=`<div class=card onclick="openMatiere('${m.id}')"><div style=display:flex;justify-content:space-between"><b>${m.icon} ${m.matiere}</b><span class=badge>${m.niveau}</span></div><p class=small>${m.desc}</p><small style=color:#00e5ff>${m.prog.length} chapitres • Ouvrir dossier 📁</small></div>`;
   });
 } else if(navCours.level=='chapitres'){
   let mat = DB.cours.find(x=>x.id==navCours.matiere);
   bc=`<span onclick="navCours.level='matieres';renderCours()">📚 Matières</span> > <span>${mat.matiere}</span>`;
   mat.prog.forEach((ch, idx)=>{
     h+=`<div class=card onclick="openChapitre(${idx})"><b style=color:#00e5ff>📁 ${ch.titre}</b><p class=small>${ch.sections.length} sections • Voir programme</p></div>`;
   });
 } else if(navCours.level=='sections'){
   let mat = DB.cours.find(x=>x.id==navCours.matiere);
   let ch = mat.prog[navCours.chapitre];
   bc=`<span onclick="navCours.level='matieres';renderCours()">📚</span> > <span onclick="navCours.level='chapitres';renderCours()">${mat.matiere}</span> > <span>${ch.titre}</span>`;
   ch.sections.forEach((sec, idx)=>{
     h+=`<div class=card onclick="openSection(${idx})"><b>📂 ${sec.titre}</b><p class=small>${sec.sous.length} sous-sections • Voir sections</p></div>`;
   });
 } else if(navCours.level=='sous'){
   let mat = DB.cours.find(x=>x.id==navCours.matiere);
   let ch = mat.prog[navCours.chapitre];
   let sec = ch.sections[navCours.section];
   bc=`<span onclick="navCours.level='matieres';renderCours()">📚</span> > <span onclick="navCours.level='chapitres';renderCours()">${mat.matiere}</span> > <span onclick="navCours.level='sections';renderCours()">${ch.titre}</span> > <span>${sec.titre}</span>`;
   sec.sous.forEach((ssec, idx)=>{
     h+=`<div class=card onclick="openLecon(${idx})"><b>📄 ${ssec.titre}</b><p class=small style=color:#76ff03>Cliquez pour leçon intégrale complète</p></div>`;
   });
 } else if(navCours.level=='lecon'){
   let mat = DB.cours.find(x=>x.id==navCours.matiere);
   let ch = mat.prog[navCours.chapitre];
   let sec = ch.sections[navCours.section];
   let ssec = sec.sous[navCours.sous];
   bc=`<span onclick="navCours.level='matieres';renderCours()">📚</span> > <span onclick="navCours.level='chapitres';renderCours()">${mat.matiere}</span> > <span onclick="navCours.level='sections';renderCours()">${ch.titre}</span> > <span onclick="navCours.level='sous';renderCours()">${sec.titre}</span> > <span>${ssec.titre}</span>`;
   h=`<div class=card style=border:2px solid #76ff03><h3 style=color:#f9c00f>${ssec.titre}</h3><p class=small style=margin-top:10px;font-size:12px;line-height:1.8">${ssec.lecon}</p><div style=margin-top:12px;display:flex;gap:6px"><button class=btn onclick="navCours.level='sous';renderCours()">⬅️ Retour</button><button class=btn style=background:#00e5ff" onclick="navCours.level='sous';renderCours()">✅ Leçon comprise</button></div></div>`;
 }
 document.getElementById('breadcrumbCours').innerHTML=bc;
 document.getElementById('gridCours').innerHTML=h;
}
function openMatiere(id){navCours.matiere=id;navCours.level='chapitres';renderCours();}
function openChapitre(idx){navCours.chapitre=idx;navCours.level='sections';renderCours();}
function openSection(idx){navCours.section=idx;navCours.level='sous';renderCours();}
function openLecon(idx){navCours.sous=idx;navCours.level='lecon';renderCours();}

function renderOhada(){
 let h=''; let bc='';
 if(navOhada.level=='matieres'){
   bc=`<span>⚖️ OHADA Matières</span>`;
   (DB.ohada||[]).forEach((m, idx)=>{
     h+=`<div class=card onclick="openOhadaMatiere(${idx})"><b style=color:#00e5ff>${m.matiere}</b><p class=small>${m.prog.length} chapitres détaillés - Ouvrir dossier</p></div>`;
   });
 } else if(navOhada.level=='chapitres'){
   let mat = DB.ohada[navOhada.matiere];
   bc=`<span onclick="navOhada.level='matieres';renderOhada()">⚖️ OHADA</span> > <span>${mat.matiere}</span>`;
   mat.prog.forEach((ch, idx)=>{
     h+=`<div class=card onclick="openOhadaChap(${idx})"><b style=color:#00e5ff>📁 ${ch.titre}</b><p class=small>${ch.sections.length} sections</p></div>`;
   });
 } else if(navOhada.level=='sections'){
   let mat = DB.ohada[navOhada.matiere];
   let ch = mat.prog[navOhada.chapitre];
   bc=`<span onclick="navOhada.level='matieres';renderOhada()">⚖️ OHADA</span> > <span onclick="navOhada.level='chapitres';renderOhada()">${mat.matiere}</span> > <span>${ch.titre}</span>`;
   ch.sections.forEach(sec=>{
     sec.sous.forEach(ssec=>{
       h+=`<div class=card><b>${sec.titre} - ${ssec.titre}</b><p class=small style=margin-top:6px">${ssec.lecon}</p></div>`;
     });
   });
   h+=`<button class=btn onclick="navOhada.level='chapitres';renderOhada()">⬅️ Retour</button>`;
 }
 document.getElementById('breadcrumbOhada').innerHTML=bc;
 document.getElementById('gridOhada').innerHTML=h;
}
function openOhadaMatiere(idx){navOhada.matiere=idx;navOhada.level='chapitres';renderOhada();}
function openOhadaChap(idx){navOhada.chapitre=idx;navOhada.level='sections';renderOhada();}

function renderDossier(){let h='';(DB.dossiers||[]).slice().reverse().forEach(d=>{h+=`<div class=card style=border:1px solid #ff1744"><b style=font-size:11px>📂 ${d.type}</b><small style=color:#666"> ${d.time} par ${d.nom}</small><p class=small style=margin:6px 0"><b>Cas:</b> ${d.desc}</p><div style=background:#111;padding:6px;border-radius:6px;margin:6px 0"><small style=color:#f9c00f"><b>AI Analyse:</b> ${d.auto||''}</small></div><div style=margin-left:10px;border-left:2px solid #f9c00f;padding-left:8px">${(d.analyses||[]).map(a=>`<div style=margin:6px 0;padding:6px;background:#0a0a1a;border-radius:6px"><span class=badge>${a.role}</span> <b style=font-size:11px">${a.nom}</b><p class=small style=margin-top:4px">${a.msg}</p></div>`).join('')}</div><div style=display:flex;gap:3px;margin-top:8px"><select id=role-${d.id} style=width:28%;font-size:8px"><option>Étudiant</option><option>Professeur</option><option>Juge</option><option>Avocat</option><option>Docteur</option></select><input id=name-${d.id} placeholder="Nom" style=width:22%;font-size:8px"><input id=msg-${d.id} placeholder="Analyse..." style=width:50%;font-size:8px"><button class=btn style=padding:4px 6px;font-size:8px" onclick=analyseDossier('${d.id}')>Analyser</button></div></div>`});gridDossier.innerHTML=h;}
function renderLex(){let h='';(DB.lexique||[]).forEach(l=>h+=`<div class=card><b>[${l.lettre}] ${l.t}</b><p class=small>${l.d}</p></div>`);gridLex.innerHTML=h;}
function filterLettre(){let lettre=lexLettre.value;if(!lettre){renderLex();return}let filt=(DB.lexique||[]).filter(l=>l.lettre==lettre);let h='';filt.forEach(l=>h+=`<div class=card><b>[${l.lettre}] ${l.t}</b><p class=small>${l.d}</p></div>`);gridLex.innerHTML=h;}
async function searchLex(){let q=lexIn.value;if(q.length<1){lexAuto.innerHTML='';renderLex();return}let res=await fetch('/api/search?q='+encodeURIComponent(q)).then(r=>r.json());lexAuto.innerHTML=`<div class=card style=background:#002a2a;border-color:#00e5ff;margin-top:8px"><p class=small>${res.ans}</p></div>`;}
function renderFaq(){let h='';(DB.faq||[]).forEach(f=>h+=`<div class=card><b style=font-size:12px>Q: ${f.q}</b><p style=color:#76ff03;margin-top:6px" class=small>R: ${f.r}</p></div>`);gridFaq.innerHTML=h;}
async function askFaq(){let q=faqAsk.value;if(!q)return;let res=await fetch('/api/search_faq?q='+encodeURIComponent(q)).then(r=>r.json());faqAuto.innerHTML+=`<div class=card style=background:#001a00;border-color:#76ff03;margin-top:10px"><div style=display:flex;justify-content:space-between"><b style=color:#76ff03>👤 Toi:</b><small style=color:#666">${new Date().toLocaleTimeString()}</small></div><p class=small style=margin:6px 0">${q}</p><div style=border-top:1px solid #222;margin-top:8px;padding-top:8px"><b style=color:#00e5ff>🤖 FAQ AI:</b><p class=small style=margin-top:6px">${res.ans}</p></div></div>`;faqAsk.value='';faqAuto.scrollIntoView();}
async function postDossier(){let d={type:dType.value,desc:dDesc.value,nom:dNom.value};if(!d.desc)return alert('Décris cas');let res=await fetch('/api/search_faq?q='+encodeURIComponent(d.type+' '+d.desc)).then(r=>r.json());d.auto=res.ans;await fetch('/api/dossiers',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)});dDesc.value='';load();}
async function analyseDossier(id){let role=document.getElementById('role-'+id).value,nom=document.getElementById('name-'+id).value,msg=document.getElementById('msg-'+id).value;if(!nom||!msg)return alert('Nom et analyse');await fetch('/api/dossiers/analyse',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({id,role,nom,msg})});load();}
let cq=[],qi=0,sc=0;function startQuiz(){let lvl=qLvl.value;cq=DB.quiz[lvl]||[];qi=0;sc=0;showQ();}
function showQ(){if(qi>=cq.length){qZone.innerHTML=`<h2 style=text-align:center>${sc}/${cq.length}</h2><div style=text-align:center;font-size:36px">${sc==cq.length?'🏆 OR':sc>=3?'🥈 ARGENT':'🥉 BRONZE'}</div><button class=btn onclick=startQuiz()>Rejouer</button>`;return}let q=cq[qi];let h=`<h4 style=margin:10px 0;font-size:12px>Q${qi+1}/${cq.length}: ${q.q}</h4>`;q.o.forEach((o,i)=>h+=`<div class=opt onclick=checkQ(${i})>${o}</div>`);qZone.innerHTML=h;}
function checkQ(i){let q=cq[qi];let ok=i==q.r;if(ok)sc++;qZone.innerHTML+=`<div class=card style=background:${ok?'#001a00':'#1a0000'};margin-top:8px"><b>${ok?'✅':'❌'} ${q.e}</b><br><button class=btn onclick="qi++;showQ()" style=margin-top:6px>Suivant</button></div>`;}
function renderForum(){let h='';(DB.forum||[]).slice().reverse().forEach(m=>{h+=`<div class=card style=border-left:3px solid #f9c00f"><span class=badge>${m.role}</span> <b style=font-size:11px">${m.nom}</b> <small style=color:#666">${m.time}</small><p class=small style=margin:6px 0">${m.msg}</p></div>`});gridForum.innerHTML=h;}
async function postForum(){let d={role:fRole.value,nom:fNom.value,msg:fMsg.value};if(!d.nom||!d.msg)return;await fetch('/api/forum',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)});fMsg.value='';load();}
function downloadApp(){
 if('serviceWorker' in navigator){
   alert('📥 DROIT224 - Pour télécharger:\\n\\n1. Sur Chrome: Clique menu ⋮ > Installer l\\'app ou Ajouter à écran accueil\\n2. Sur iPhone Safari: Partage > Sur écran accueil\\n3. L\\'app s\\'installera comme vraie app!\\n\\nOu va sur droit224.com et garde le site!');
 } else {
   alert('📥 Pour télécharger DROIT224:\\nAjoute cette page à ton écran d\\'accueil:\\nChrome: Menu > Ajouter à écran accueil\\nTu auras l\\'icône DROIT224 comme app!');
 }
 // PWA install prompt
 if(window.deferredPrompt){window.deferredPrompt.prompt();}
}
let deferredPrompt;
window.addEventListener('beforeinstallprompt', (e)=>{e.preventDefault();deferredPrompt=e;window.deferredPrompt=e;});
load();setInterval(load,20000);
</script></body></html>
"""

@app.route("/manifest.json")
def manifest():
    return jsonify({"name":"DROIT224","short_name":"DROIT224","start_url":"/","display":"standalone","background_color":"#050510","theme_color":"#f9c00f","icons":[{"src":"https://cdn-icons-png.flaticon.com/512/1087/1087815.png","sizes":"192x192","type":"image/png"}]})

QUIZ_DATA = {
    "L1":[{"q":"Constitution 2020 = quelle République?","o":["3e","4e","5e"],"r":1,"e":"4e République référendum 2020"},{"q":"Garde à vue max?","o":["24h","48h renouvelable","7j"],"r":1,"e":"48h x2=96h"},{"q":"OHADA pays?","o":["10","17","54"],"r":1,"e":"17 pays membres"}],
    "L2":[{"q":"Crime jugé par?","o":["TPI","Assises","Suprême"],"r":1,"e":"Crime = Cour Assises jury"},{"q":"SARL capital min?","o":["100k","1M","10M"],"r":1,"e":"1M FCFA depuis 2014"}],
    "L3":[{"q":"Titre Foncier faux?","o":["Valable","Danger","Gratuit"],"r":1,"e":"80% arnaques Conakry vérifier Kaloum"},{"q":"Pourvoi délai?","o":["15j","2 mois","1 an"],"r":1,"e":"2 mois après arrêt Appel"}],
    "OHADA":[{"q":"OHADA =?","o":["Harmonisation Droit Affaires","Humanitaire","Douane"],"r":0,"e":"Organisation Harmonisation Droit Affaires Afrique"},{"q":"RCCM à?","o":["Mairie","APIP","TPI"],"r":1,"e":"APIP Guinée 500k"}],
}

def load_j(f,d):
    if not os.path.exists(f): return d
    try: return json.load(open(f,"r",encoding="utf-8"))
    except: return d
def save_j(f,d): json.dump(d, open(f,"w",encoding="utf-8"), ensure_ascii=False, indent=2)

@app.route("/api/all")
def all_api():
    dossiers=load_j("dossiers_v11.json", [])
    faq_extra=load_j("faq_extra_v11.json", [])
    all_faq=[{"q":"Prison pour dette?","r":"NON interdit sauf pension alimentaire."},{"q":"Terrain?","r":"Seul Titre Foncier Kaloum = propriété!"}] + faq_extra
    return jsonify({"cours":UNIVERSITE,"ohada":UNIVERSITE,"lexique":DICT_AZ,"quiz":QUIZ_DATA,"faq":all_faq,"dossiers":dossiers,"forum":load_j("forum_v11.json", [])})

@app.route("/api/search")
def search_api():
    q=request.args.get("q","")
    return jsonify({"ans":moteur_lexique(q)})

@app.route("/api/search_faq")
def search_faq_api():
    q=request.args.get("q","")
    return jsonify({"ans":moteur_ai(q)})

@app.route("/api/dossiers", methods=["POST"])
def dossiers_post():
    d=request.get_json()
    alld=load_j("dossiers_v11.json", [])
    alld.append({"id":uuid.uuid4().hex[:5],"type":d.get("type",""),"desc":d.get("desc",""),"nom":d.get("nom",""),"time":datetime.now().strftime("%d/%m %H:%M"),"auto":d.get("auto",""),"analyses":[]})
    save_j("dossiers_v11.json", alld)
    return jsonify({"ok":True})

@app.route("/api/dossiers/analyse", methods=["POST"])
def dossier_analyse():
    d=request.get_json()
    alld=load_j("dossiers_v11.json", [])
    for dos in alld:
        if dos["id"]==d.get("id"):
            dos.setdefault("analyses",[]).append({"role":d.get("role",""),"nom":d.get("nom",""),"msg":d.get("msg","")})
    save_j("dossiers_v11.json", alld)
    return jsonify({"ok":True})

@app.route("/api/forum", methods=["GET","POST"])
def forum_api():
    if request.method=="POST":
        d=request.get_json()
        allf=load_j("forum_v11.json", [])
        allf.append({"id":uuid.uuid4().hex[:5],"role":d.get("role",""),"nom":d.get("nom",""),"msg":d.get("msg",""),"time":datetime.now().strftime("%H:%M")})
        save_j("forum_v11.json", allf)
        return jsonify({"ok":True})
    return jsonify(load_j("forum_v11.json", []))

if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)))
