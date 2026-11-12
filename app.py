from flask import Flask, jsonify, request
import json, os, uuid, random
from datetime import datetime
app = Flask(__name__)

COURS_LICENCES = {
"L1": [
{"id":"intro_l1","matiere":"Introduction au Droit","niveau":"L1","icon":"📖","programme":[
{"titre":"Chapitre 1: La Règle de Droit","sections":[
{"titre":"Section 1: Définition","sous_sections":[
{"titre":"Sous-section 1: Définition générale","lecon":"La règle de droit est une règle de conduite dans les rapports sociaux, générale, abstraite, obligatoire, dont le respect est assuré par la puissance publique. Elle se distingue de la règle morale intérieure non sanctionnée par l'État, de la règle religieuse sanction divine, de la bienséance politesse. Droit objectif = ensemble règles qui régissent vie hommes en société. Droits subjectifs = prérogatives individus droit propriété vote créance. Droit naturel = idéal justice ce qui devrait être, Droit positif = règles en vigueur. En Guinée droit positif = Constitution 22 mars 2020 + lois CNT + ordonnances Président + décrets + coutume très importante mariage coutumier Malinké Manden Kalikan 1236, Peulh Pulaaku, Soussou, règlement litiges fonciers sages + jurisprudence Cour Suprême et CCJA Abidjan OHADA + doctrine professeurs Sonfonia Kofi Annan UGLC."},
{"titre":"Sous-section 2: Caractères","lecon":"Quatre caractères: 1- Générale et abstraite vise toutes personnes dans situation donnée pas personne déterminée. Ex art 544 Code civil propriété tous propriétaires. 2- Obligatoire doit être respectée sous peine sanction. 3- Sanctionnée par État contrainte police tribunal prison amende huissier force publique. 4- Permanente évolutive vocation durer mais évolue société ex cybercrime données personnelles. Règle impérative s'impose absolument pas déroger ex loi pénale, règle supplétive s'applique à défaut volonté contraire ex beaucoup règles Code civil contrat régime matrimonial."}
]},
{"titre":"Section 2: Sources","sous_sections":[
{"titre":"Sous-section 1: Sources nationales","lecon":"Sources nationales: Constitution 22 mars 2020 loi suprême 156 articles au dessus tout primauté art 151. Loi votée CNT promulguée Président publiée Journal Officiel domaine art 68 droits civiques libertés impôts. Ordonnance Président domaine loi urgence autorisation CNT. Règlement décrets Président arrêtés ministres décisions préfets maires. Coutume habitude ancienne constante notoire opinio juris croyance obligatoire très importante Guinée rurale mariage coutumier régime foncier coutumier règlement conflits chefs. Conditions coutume ancienneté constance notoriété opinio juris. Jurisprudence décisions Cours Tribunaux Cour Suprême CCJA OHADA font référence juges TPI doivent suivre sécurité juridique. Doctrine avis professeurs thèses articles."},
{"titre":"Sous-section 2: Sources internationales","lecon":"Traités internationaux ratifiés Guinée primauté sur loi nationale art 151 Constitution ex Pacte Droits Civils Convention torture Traité OHADA. OHADA 10 Actes Uniformes primauté lois nationales droit affaires comptabilité commerce sociétés sûretés procédures collectives voies exécution arbitrage transport coopératives médiation. UEMOA CEDEAO Cour Justice Abuja UA ONU Conseil Sécurité 5 permanents veto Assemblée Générale CIJ La Haye."}
]}
]},
{"titre":"Chapitre 2: Branches","sections":[
{"titre":"Section 1: Droit Public","sous_sections":[
{"titre":"Sous-section 1: Droit Public","lecon":"Droit public règles organisent État rapports État-citoyens but intérêt général inégalitaire État supérieur. Branches: Constitutionnel Constitution pouvoirs droits fondamentaux contrôle constitutionnalité QPC, Administratif administration service public principes continuité égalité mutabilité acte administratif unilatéral décret Président arrêté ministre contrat administratif marché public REP Recours Excès Pouvoir Tribunal Administratif 2 mois plein contentieux responsabilité administration faute simple lourde sans faute risque rupture égalité, Pénal infractions peines légalité pas infraction sans loi non rétroactivité, Fiscal impôts directs IR IS indirects TVA 18% Guinée douane, International Public États ONU traités responsabilité État fait illicite, Finances Publiques budget loi finances CNT annualité unité universalité spécialité recettes dépenses ordonnateur comptable public contrôle Cour des Comptes."}
]},
{"titre":"Section 2: Droit Privé","sous_sections":[
{"titre":"Sous-section 1: Droit Privé","lecon":"Droit privé règles entre particuliers égalitaire but intérêt privé. Branches: Civil droit commun personne physique être humain sujet droit naissance vivante viable jusqu'à mort attributs nom prénom domicile nationalité patrimoine personne morale société association État personnalité distincte création RCCM famille mariage conditions âge 18 ans consentement monogamie polygamie optionnelle Guinée divorce faute consentement mutuel filiation autorité parentale biens meubles immeubles corporels incorporels propriété art 544 usus fructus abusus usufruit servitudes obligations contrats. Commercial commerçant art 2 AUDCG fait actes commerce nature profession habituelle actes commerce nature achat meubles revendre banque assurance transport intermédiaire construction spectacle télécom forme lettre change billet ordre société commerciale accessoire fait commerçant pour commerce fonds commerce art 135 clientèle achalandage essentiel sans clientèle pas fonds nom enseigne droit bail matériel marchandises brevets bail commercial art 69 durée min 2 ans droit renouvellement indemnité éviction valeur fonds sauf motif grave non paiement non exploitation démolition loyer révisable 3 ans. Travail contrat travail CDI règle générale CDD exception max 2 ans renouvelable période essai obligations employeur payer salaire sécurité employé travailler loyauté licenciement motif réel sérieux convocation entretien préalable lettre licenciement préavis certificat solde reçu démission volonté claire rupture conventionnelle grève droit constitutionnel préavis service minimum Inspection Travail Kaloum Matam gratuit conciliation Tribunal Travail TPI. International Privé conflit lois litige élément étranger mariage Guinéen Française quelle loi statut personnel loi nationalité biens immeubles loi lieu situation contrats loi choisie parties conflit juridictions tribunal compétent nationalité domicile lieu fait exequatur jugement étranger reconnu TPI Guinée exécuter nationalité guinéenne filiation père mère naturalisation décret Président 5 ans résidence double tolérée."}
]}
]
}
]
},
{"id":"const_l1","matiere":"Droit Constitutionnel","niveau":"L1","icon":"🏛️","programme":[
{"titre":"Chapitre 1: État et Constitution 2020","sections":[
{"titre":"Section 1: État","sous_sections":[
{"titre":"Sous-section 1: Éléments État","lecon":"État 3 éléments: Territoire terrestre sol sous-sol maritime mer territoriale 12 miles ZEE 200 miles aérien espace aérien frontières traités. Population nationale citoyens guinéens filiation père mère naturalisation décret Président 5 ans résidence étrangers peuple ensemble citoyens. Pouvoir politique souverain interne suprême pas pouvoir au dessus externe indépendance pas soumis autre État. Personnalité juridique État personne morale. Souveraineté appartient peuple art 2 Constitution Guinée 2020 exercée représentants référendum. État unitaire Guinée un seul centre pouvoir décentralisé communes régions autonomie vs fédéral USA Allemagne États fédérés plus État fédéral compétences. Centralisé vs décentralisé. État droit respect hiérarchie normes Constitution sommet légalité administration doit respecter loi contrôle juridictionnel."},
{"titre":"Sous-section 2: Constitution 2020","lecon":"Constitution loi suprême organise pouvoirs garantit droits fondamentaux. Écrite Guinée 2020 vs coutumière Angleterre. Rigide révision difficile référendum vs souple loi ordinaire. Originaire crée nouvel ordre vs dérivée révise existante. Guinée 4 Constitutions 1958 Sékou Touré 1990 Lansana Conté 2010 transition 2020 4ème République. Contenu 2020: Titre 1 Principes Guinée État laïc démocratique indivisible social drapeau Rouge Jaune Vert hymne Liberté devise Travail Justice Solidarité langue française capitale Conakry. Titre 2 Droits Devoirs art 5-50 droits civils vie liberté égalité propriété présomption innocence habeas corpus interdiction torture politiques vote 18 ans éligibilité manifestation pacifique parti pétition économiques sociaux travail grève syndicat éducation santé logement devoirs respecter Constitution payer impôts défendre patrie protéger environnement. Pouvoirs Exécutif Président élu 5 ans renouvelable 1 fois suffrage universel direct conditions 35 ans nationalité guinéenne jouissance droits parrainages nomme PM Gouvernement proposition PM préside Conseil Ministres décrets domaine réservé défense diplomatie peut dissoudre Assemblée état siège urgence, Législatif CNT 81 membres demain Assemblée députés élus 5 ans vote lois art 68 budget contrôle Gouvernement questions commission enquête motion censure, Judiciaire indépendant juges inamovibles Cours Tribunaux Cour Suprême sommet 4 chambres judiciaire administrative constitutionnelle comptes Cour Constitutionnelle 9 membres contrôle constitutionnalité lois élections contentieux électoral CSM discipline juges."},
{"titre":"Sous-section 3: QPC Révision","lecon":"Révision très difficile éviter dictatures Initiative Président ou 2/3 CNT vote CNT majorité 2/3 puis référendum peuple oui non Limites pas révision forme républicaine laïcité intégrité territoire durée mandat nombre mandats. Contrôle constitutionnalité a priori avant promulgation loi Président 1/3 députés PM peuvent saisir Cour Constitutionnelle a posteriori voie exception QPC art 95 devant tout tribunal TPI partie procès dit loi applicable contraire Constitution juge transmet Cour Suprême filtre puis Cour Constitutionnelle 3 mois si inconstitutionnelle loi abrogée pour tous effet erga omnes compter décision ou date ultérieure fixée Cour Puissant outil citoyen protéger droits Exemple si loi presse contraire liberté expression Constitution avocat soulève QPC devant TPI TPI transmet Cour Constit déclare inconstitutionnelle loi disparaît JO."}
]}
]
}
]
}
],
"L2": [
{"id":"oblig_l2","matiere":"Droit des Obligations","niveau":"L2","icon":"⚖️","programme":[
{"titre":"Chapitre 1: Contrat","sections":[
{"titre":"Section 1: Définition","sous_sections":[
{"titre":"Sous-section 1: Obligation Contrat","lecon":"Obligation lien droit entre deux personnes oblige l'une envers autre à donner transférer propriété faire construire maison ne pas faire non concurrence Sources contrat accord responsabilité délictuelle art 1240 tout fait causant dommage oblige réparer quasi-contrat gestion affaire paiement indu enrichissement sans cause loi Contrat art 1101 accord volontés entre 2+ personnes destiné créer modifier transmettre éteindre obligations Classification synallagmatique obligations réciproques vente vendeur livre acheteur paie vs unilatéral donation une seule obligation onéreux échange avantage vente vs gratuit donation consensuel accord seul suffit vs solennel formalités notaire vente immeuble vs réel remise chose dépôt nommé vente bail prévu Code vs innommé négociation pourparlers offre précise ferme acceptation promesse unilatérale."},
{"titre":"Sous-section 2: Formation 4 conditions","lecon":"4 conditions validité art 1128 consentement libre éclairé vices erreur art 1132 fausse représentation réalité erreur substance qualité essentielle ex acheter vase croit or mais toc annulation erreur obstacle nature contrat nullité dol art 1137 tromperie manœuvres mensonge faire signer ex vendeur cache accident voiture annulation plus dommages violence art 1140 contrainte physique menacer frapper morale menacer licenciement annulation preuve vices tout moyen lésion déséquilibre prix seulement mineur incapacité Capacité art 1145 majeur 18 ans capable mineur incapable sauf émancipation mariage juge majeur tutelle curatelle sanction nullité relative Objet art 1163 chose prestation doit être certaine déterminée possible licite pas drogue pas corps humain Cause art 1162 raison déterminante doit être licite pas tuer pas fraude Si manque nullité absolue intérêt général 30 ans relative intérêt privé 5 ans rétroactif censé jamais existé restitution."}
]}
]},
{"titre":"Chapitre 2: Effets","sections":[
{"titre":"Section 1: Effets Inexécution","sous_sections":[
{"titre":"Sous-section 1: Force obligatoire","lecon":"Force obligatoire art 1103 contrat = loi entre parties doit être exécuté bonne foi art 1104 juge ne peut modifier Exception imprévision art 1195 changement circonstances imprévisible rend exécution excessivement onéreuse partie peut demander renégociation défaut juge peut adapter mettre fin Effet relatif art 1199 contrat entre parties seulement pas tiers sauf stipulation pour autrui promettant s'engage envers tiers bénéficiaire promesse porte-fort Inexécution mise en demeure préalable obligatoire art 1344 lettre huissier recommandée exige exécuter 8 jours Sanctions exécution forcée nature juge ordonne sous astreinte exception inexécution art 1219 si autre n'exécute pas tu suspends résolution art 1224 anéantissement contrat inexécution grave judiciaire juge unilatérale notification clause résolutoire dommages intérêts art 1231 compensatoires remplacent exécution moratoires retard conditions faute plus dommage plus lien causal prévisibles sauf faute lourde Clause pénale forfaitaire clause limitative responsabilité valable sauf faute lourde."}
]}
]
}
]
},
{"id":"penal_l2","matiere":"Droit Pénal","niveau":"L2","icon":"🔨","programme":[
{"titre":"Chapitre 1: Infraction","sections":[
{"titre":"Section 1: Classification","sous_sections":[
{"titre":"Sous-section 1: Crime Délit Contravention","lecon":"Infraction acte interdit loi pénale puni peine Classification tripartite CRIME grave meurtre viol vol main armée trafic drogue peine réclusion 10 ans à perpétuité mort moratoire juridiction Cour Assises jury instruction obligatoire prescription 10 ans DÉLIT moyen vol simple escroquerie abus confiance coups blessures diffamation peine emprisonnement 1 mois à 10 ans plus amende TPI Correctionnel prescription 3 ans CONTRAVENTION légère tapage injure non publique divagation animaux peine amende 1ère à 5ème classe 5k à 1M Simple Police prescription 1 an Éléments légal texte prévoit infraction principe légalité pas infraction sans loi matériel acte concret tuer voler moral intention dol faute imprudence sans intention pas infraction sauf contravention Responsabilité personne physique si discernement cause irresponsabilité démence art 122-1 minorité moins 13 ans irresponsable 13 à 18 atténuation contrainte physique morale légitime défense Personne morale société condamnée pénalement depuis Code pénal 2016 peine amende plus dissolution interdiction Complice même peine auteur tentative si commencement exécution plus désistement involontaire punie comme infraction consommée Peines principales prison amende mort moratoire complémentaires interdiction séjour confiscation interdiction droits civiques alternatives TIG jours-amende personnalisation peine juge tient compte circonstances sursis simple pas prison si pas nouvelle infraction 5 ans sursis mise épreuve obligations travail soins indemniser victime si respecte effacée casier si récidive révoqué libération conditionnelle sors avant fin peine bonne conduite grâce Président amnistie loi efface condamnation."}
]}
]
}
]
}
],
"L3": [
{"id":"foncier_l3","matiere":"Droit Foncier","niveau":"L3","icon":"🏠","programme":[
{"titre":"Chapitre 1: Titre Foncier","sections":[
{"titre":"Section 1: Domaine Propriété","sous_sections":[
{"titre":"Sous-section 1: Domaine national","lecon":"Domaine national terres non immatriculées État propriétaire originaire gère pour peuple Domaine privé État biens État immatriculés Domaine public routes fleuves inaliénable Terres rurales régime coutumier chef terre mais État peut immatriculer Propriété art 544 Code civil droit jouir disposer choses manière plus absolue usus usage fructus fruits abusus disposition Caractères absolue perpétuelle exclusive Acquisition accession prescription 30 ans contrat vente succession."},
{"titre":"Sous-section 2: Procédure Titre","lecon":"Procédure immatriculation complète: 1- Acte vente coutumier chef quartier plus 2 témoins plus chef secteur. 2- Demande Conservation Foncière Kaloum formulaire CNI vendeur acheteur acte coutumier plan croquis géomètre 4 photos quittance paiement 500k. 3- Enquête publique affichage Mairie terrain 1 mois oppositions possibles. 4- Bornage contradictoire géomètre agréé avec voisins. 5- Commission foncière examine. 6- Immatriculation livre foncier numéro établissement Titre Foncier duplicata remis propriétaire. Coût total 2-5M délai 6-12 mois Titre imprescriptible inattaquable sauf faux Sans Titre = occupant précaire Arnaques Conakry même terrain vendu 5 fois faux titres Sonfonia Coyah Madina vendeur pas propriétaire Prévention toujours avant payer aller Conservation Kaloum vérifier livre foncier si terrain déjà titré demander certificat propriété passer notaire payer virement bancaire tracé pas cash exiger plan géomètre Contentieux TPI section foncière expertise Cour Appel Cassation Cour Suprême Preuve Titre Foncier = preuve parfaite acte coutumier = commencement preuve faible."}
]}
]
}
]
}
]
}

OHADA_DATA = [
{"id":"audcg","matiere":"AUDCG - Droit Commercial Général","icon":"⚖️","programme":[
{"titre":"Chapitre 1: Commerçant RCCM Bail","sections":[
{"titre":"Section 1: Commerçant RCCM","sous_sections":[
{"titre":"Sous-section 1: Commerçant","lecon":"Art 2 Commerçant = personne qui fait actes commerce par nature à titre profession habituelle Capacité majeur 18 ans mineur émancipé pas incompatible fonctionnaire avocat Obligations RCCM dans mois début activité comptabilité SYSCOHADA NIF patente compte bancaire Perte qualité cessation décès interdiction faillite Actes commerce nature achat meubles revendre banque assurance transport intermédiaire construction spectacle télécom Forme lettre change billet ordre société commerciale Accessoire fait commerçant pour commerce Prescription commerce 5 ans art 16 RCCM art 19-74 Registre tenu greffe TPI APIP Guinée fichier national régional OHADA Mentions état civil nationalité activité adresse succursales régime matrimonial sûretés procédures collectives Public extrait Kbis Formalités immatriculation formulaire CNI casier certificat résidence statuts 500k 48h modification 30j radiation cessation décès dissolution Sanction pas immatriculé pas commerçant pas tribunaux commerce amende pénale Bail commercial art 69-134 bail immeuble fonds commerce écrit obligatoire durée min 2 ans si moins 2 ans courte durée pas renouvellement Loyer libre révision triennale indice construction chiffre affaires Charges impôts fonciers propriétaire sauf clause Droit renouvellement locataire 2 ans exploitation droit renouvellement propriétaire refuse seulement motif grave non paiement non exploitation démolition sinon indemnité éviction valeur fonds plus déménagement Cession libre avec fonds sinon autorisation Sous-location autorisée si clause Fonds commerce art 135-171 ensemble clientèle achalandage essentiel sans clientèle pas fonds nom enseigne droit bail matériel marchandises brevets vente publicité JAL 15j inscription RCCM séquestre prix 3 mois oppositions créanciers."}
]}
]
}
]
},
{"id":"aus","matiere":"AUS - Sûretés","icon":"🔒","programme":[
{"titre":"Chapitre 1: Caution Hypothèque","sections":[
{"titre":"Section 1: Caution Hypothèque","sous_sections":[
{"titre":"Sous-section 1: Caution Hypothèque","lecon":"Cautionnement art 13-49 Contrat caution s'engage envers créancier payer si débiteur pas Écrit mention somme garantie peine nullité Simple bénéfice discussion créancier poursuit d'abord débiteur saisit biens puis caution bénéfice division si plusieurs cautions part Solidaire créancier va direct caution sans poursuivre débiteur plus utilisé banques Guinée Proportionné revenus sinon déchéance information annuelle caution créancier Extinction dette payée terme décharge prescription Caution paye subrogée droits créancier recours débiteur Hypothèque art 190 immeuble maison terrain Types conventionnelle accord acte notarié obligatoire forcée jugement légale loi vendeur impayé copropriété Assiette immeuble bâti non bâti droit emphytéose usufruit Inscription Conservation Foncière Kaloum bordereau acte notarié 10 ans renouvelable coût 2% rang ordre inscription première payée première cession antériorité Effets préférence payé avant chirographaires sur prix vente suite suit immeuble même vendu tiers Réalisation impayé commandement saisie immobilière TPI vente judiciaire enchères distribution rang Extinction dette payée prescription 10 ans non renouvelée renonciation."}
]}
]
}
]
},
{"id":"auce","matiere":"AUCE - Voies Exécution Arbitrage","icon":"🔨","programme":[
{"titre":"Chapitre 1: Saisies Arbitrage","sections":[
{"titre":"Section 1: Voies Exécution","sous_sections":[
{"titre":"Sous-section 1: Saisies Arbitrage","lecon":"Titre exécutoire jugement arrêt acte notarié chèque impayé lettre change protestée Mesures conservatoires avant jugement saisie conservatoire meubles créances bloque compte autorisation Juge empêcher vider patrimoine Saisies exécution après jugement Attribution art 77 plus utilisée huissier bloque compte bancaire attribue créancier commandement 8j banque bloque déclare solde verse 100-200k Vente art 109 saisit meubles corporels voiture TV stock domicile inventaire vend enchères insaisissables vêtements lit nourriture 1 mois outils travail Immobilière art 246 saisit maison terrain vente judiciaire TPI 1-2 ans coûteux grosses sommes hypothèque facilite Rémunération saisit salaire employeur quotité Appréhension revendication récupère bien Injonction payer art 1-18 rapide créance certaine liquide exigible facture billet ordre requête Président TPI ordonnance signification débiteur 15j opposition sinon exécutoire efficace Guinée pas avocat Astreinte art 33 somme par jour retard 200k/jour Arbitrage 36 articles justice privée parties décident pas TPI mais arbitre privé choisi rapide 6 mois confidentiel expert international Convention clause compromissoire contrat avant litige compromis après écrite désigne arbitres Tribunal 1 ou 3 arbitres indépendants impartiaux procédure parties règlement CCJA siège Conakry Abidjan Paris demande réponse mémoires audience sentence 6 mois contradictoire défense Sentence motivée écrite signée effet jugement obligatoire exequatur Président TPI rend exécutoire vérifie ordre public Recours pas appel seulement annulation CCJA TPI vice grave partial pas contradictoire CCJA centre arbitrage règlement liste administre Avantages rapidité 6 mois vs 2 ans TPI confidentialité expertise neutralité exécution internationale Convention New York 1958 170 pays Clause type Tout litige relatif contrat sera tranché arbitrage CCJA Abidjan selon Règlement CCJA Utilisé contrats miniers télécom BTP étrangers."}
]}
]
}
]
}
]

DICT_AZ = [
{"lettre":"A","t":"Abus de confiance","d":"Art 394 CP: Détourner chose remise à charge rendre 1-5 ans ex on te confie 10M terrain tu bouffes."},
{"lettre":"A","t":"Astreinte","d":"Art 33 AUCE: Somme par jour retard pas exécution jugement ex 200k/jour libérer maison."},
{"lettre":"B","t":"Bail commercial","d":"Art 69 AUDCG: Bail immeuble fonds commerce durée min 2 ans droit renouvellement indemnité éviction loyer révisable 3 ans."},
{"lettre":"C","t":"Cautionnement","d":"Art 13 AUS: Caution s'engage payer si débiteur pas écrit somme garantie simple ou solidaire."},
{"lettre":"C","t":"CCJA","d":"Cour Commune Justice Arbitrage Abidjan 13 juges cassation OHADA casse arrêt Appel Conakry peut évoquer primauté."},
{"lettre":"D","t":"Dol","d":"Art 1137 Code civil: Tromperie manœuvres mensonge pour faire signer contrat annulation plus dommages."},
{"lettre":"E","t":"Escroquerie","d":"Art 394 CP: Tromperie remise volontaire chose par ruse mensonge manœuvre 1-5 ans différence vol sans accord."},
{"lettre":"F","t":"Fonds de commerce","d":"Art 135 AUDCG: Ensemble clientèle nom enseigne droit bail matériel marchandises vente publicité JAL 15j séquestre 3 mois."},
{"lettre":"G","t":"Garde à vue","d":"Police retient suspect 48h renouvelable 96h max droits avocat 1ère heure médecin famille silence nullité si dépassement."},
{"lettre":"H","t":"Habeas Corpus","d":"Ordre juge police présenter détenu 48h sinon libération art 9 Constitution."},
{"lettre":"H","t":"Hypothèque","d":"Art 190 AUS: Sûreté immeuble maison terrain notariée inscrite Conservation Kaloum 10 ans renouvelable rang première payée première."},
{"lettre":"I","t":"Injonction de payer","d":"Art 1 AUCE: Procédure rapide facture impayée requête Président TPI ordonnance signification 15j opposition sinon exécutoire pas avocat."},
{"lettre":"J","t":"Juge","d":"Magistrat qui tranche litiges au nom du peuple guinéen. Juge TPI Première Instance juge civil pénal commerce travail foncier. Juge instruction enquête crime. Juge Cour Appel. Juge Cour Suprême cassation. Juge CCJA Abidjan OHADA. Indépendant inamovible, statue selon loi et conscience, impartial. Nomination CSM Conseil Supérieur Magistrature. Différence Procureur: Procureur accuse, Juge tranche."},
{"lettre":"M","t":"Mise en demeure","d":"Lettre officielle exécuter 8j sinon tribunal OBLIGATOIRE avant TPI art 54 CPCC huissier 50k recommandée."},
{"lettre":"N","t":"Nullité","d":"Sanction acte ne respectant conditions absolue intérêt général 30 ans relative intérêt privé 5 ans rétroactif censé jamais existé."},
{"lettre":"O","t":"OHADA","d":"Organisation Harmonisation Droit Affaires Afrique 17 pays 10 Actes Uniformes même loi CCJA Abidjan RCCM APIP SARL 1M."},
{"lettre":"P","t":"Prescription","d":"Délai agir pénal crime 10 ans délit 3 ans contravention 1 an civil contrat 5 ans terrain 30 ans commerce 5 ans."},
{"lettre":"Q","t":"QPC","d":"Question Prioritaire Constitutionnalité devant tout tribunal dis loi contraire Constitution transmission Cour Constit abrogation."},
{"lettre":"R","t":"RCCM","d":"Registre Commerce Crédit Mobilier numéro commerçant APIP 500k CNI casier statuts obligatoire."},
{"lettre":"S","t":"SARL","d":"Société Responsabilité Limitée 1-100 associés capital min 1M parts 5k responsabilité limitée gérant responsable pénale RCCM APIP."},
{"lettre":"S","t":"Saisie attribution","d":"Art 77 AUCE: Huissier bloque compte bancaire attribue créancier plus utilisée commandement 8j banque bloque 100-200k."},
{"lettre":"T","t":"Titre Foncier","d":"Seul papier propriété terrain Guinée Conservation Kaloum après enquête bornage sans occupant précaire 80% arnaques vérifier 2-5M."},
{"lettre":"V","t":"Viol","d":"Art 321 CP Guinée: Acte sexuel sans consentement par violence contrainte menace surprise. Peine 5-10 ans réclusion criminelle. Sur mineur moins 18 ans aggravé 10-20 ans. Sur mineur moins 13 ans réclusion à perpétuité. Procédure plainte Procureur ou Commissariat, certificat médical CHU 24h, enquête OPJ, TPI Cour Assises. Victime peut se constituer partie civile dommages intérêts. Pas de prescription courte viol mineur 20 ans."},
{"lettre":"V","t":"Vente","d":"Contrat transfert propriété moyennant prix obligations vendeur délivrance garantie éviction vices cachés acheteur payer prix art 1582."},
]

# ===== QUIZ 30 QUESTIONS PAR LICENCE =====
QUIZ_BANK = {
"L1": [
{"q":"Constitution 2020 = quelle République?","o":["3e","4e","5e"],"r":1,"e":"4e République référendum 2020"},
{"q":"Garde à vue max en Guinée?","o":["24h","48h renouvelable 96h","7 jours"],"r":1,"e":"48h renouvelable 1 fois = 96h"},
{"q":"OHADA combien de pays?","o":["10","17","54"],"r":1,"e":"17 pays membres"},
{"q":"Sans mise en demeure, TPI?","o":["Irrecevable","OK","Amende"],"r":0,"e":"Mise en demeure obligatoire art 54 CPCC"},
{"q":"Règle de droit caractère?","o":["Morale","Obligatoire sanctionnée État","Facultative"],"r":1,"e":"Obligatoire sanctionnée police tribunal"},
{"q":"Constitution au dessus de quoi?","o":["Toutes lois","Rien","Coutume seulement"],"r":0,"e":"Constitution loi suprême art 151"},
{"q":"Droit Public but?","o":["Intérêt privé","Intérêt général","Profit"],"r":1,"e":"Droit public intérêt général"},
{"q":"Droit Privé exemple?","o":["Constitutionnel","Civil","Fiscal"],"r":1,"e":"Civil = droit privé"},
{"q":"Source droit guinéen?","o":["Coutume","Rêve","Hasard"],"r":0,"e":"Coutume très importante Guinée rurale"},
{"q":"QPC c'est quoi?","o":["Question Prioritaire Constitutionnalité","Quiz","Police"],"r":0,"e":"QPC devant tout tribunal loi contraire Constitution"},
{"q":"Président Guinée mandat?","o":["4 ans","5 ans renouvelable 1 fois","À vie"],"r":1,"e":"5 ans renouvelable 1 fois Constitution 2020"},
{"q":"Habeas Corpus?","o":["Présenter détenu 48h sinon libération","Payer","Voter"],"r":0,"e":"Ordre juge police présenter détenu 48h"},
{"q":"Séparation pouvoirs auteur?","o":["Montesquieu","Rousseau","Voltaire"],"r":0,"e":"Montesquieu 1748 Esprit des Lois"},
{"q":"Droit civil étudie?","o":["Personne famille biens obligations","Armée","ONU"],"r":0,"e":"Personne famille biens obligations contrats"},
{"q":"Coutume conditions?","o":["Ancienneté constance opinio juris","Nouveauté","Richesse"],"r":0,"e":"Ancienneté constance notoriété opinio juris"},
],
"L2": [
{"q":"Crime jugé par?","o":["TPI","Cour Assises","Simple Police"],"r":1,"e":"Crime = Cour Assises jury"},
{"q":"SARL capital min OHADA?","o":["100k","1M","10M"],"r":1,"e":"1M FCFA"},
{"q":"Délit prescription?","o":["1 an","3 ans","10 ans"],"r":1,"e":"Délit 3 ans, crime 10 ans"},
{"q":"Contrat 4 conditions?","o":["Consentement capacité objet cause","Argent seul","Hasard"],"r":0,"e":"Consentement capacité objet cause art 1128"},
{"q":"Dol c'est quoi?","o":["Tromperie pour faire signer","Cadeau","Vérité"],"r":0,"e":"Dol tromperie manœuvres mensonge annulation"},
{"q":"Force obligatoire contrat?","o":["Contrat = loi entre parties","On peut ne pas respecter","Juge change"],"r":0,"e":"Art 1103 contrat = loi entre parties"},
{"q":"Vol art?","o":["373 CP","1 CP","999 CP"],"r":0,"e":"Vol art 373 CP soustraction frauduleuse"},
{"q":"Escroquerie différence vol?","o":["Vol sans accord, escroquerie avec accord trompé","Même chose","Pas de différence"],"r":0,"e":"Vol sans accord, escroquerie tu donnes car trompé"},
{"q":"Sursis?","o":["Pas prison si pas récidive 5 ans","Prison direct","Amende"],"r":0,"e":"Sursis pas prison si pas récidive 5 ans"},
{"q":"Responsabilité civile conditions?","o":["Faute dommage lien causal","Richesse","Chance"],"r":0,"e":"Faute + dommage + lien causal"},
{"q":"Preuve civile >500k?","o":["Écrit obligatoire","Parole suffit","Rien"],"r":0,"e":"Au dessus 500k écrit obligatoire"},
{"q":"Nullité relative délai?","o":["5 ans","30 ans","1 jour"],"r":0,"e":"Nullité relative 5 ans, absolue 30 ans"},
{"q":"Mise en demeure délai?","o":["8 jours","1 an","0"],"r":0,"e":"Mise en demeure 8 jours huissier"},
{"q":"Abus confiance?","o":["Détourner chose confiée","Donner","Vendre légal"],"r":0,"e":"Détourner chose remise à charge rendre art 394"},
{"q":"Tentative punie?","o":["Oui comme infraction consommée","Non","Parfois"],"r":0,"e":"Tentative commencement exécution + désistement involontaire = punie"},
],
"L3": [
{"q":"Titre Foncier où?","o":["Mairie","Conservation Kaloum","APIP"],"r":1,"e":"Conservation Foncière Kaloum"},
{"q":"Titre Foncier coût?","o":["Gratuit","2-5M","100M"],"r":1,"e":"2-5M délai 6-12 mois"},
{"q":"Sans Titre Foncier tu es?","o":["Propriétaire","Occupant précaire","Riche"],"r":1,"e":"Sans Titre = occupant précaire"},
{"q":"Pourvoi délai?","o":["15j","2 mois","1 an"],"r":1,"e":"2 mois après arrêt Appel"},
{"q":"SA capital min?","o":["1M","10M","100k"],"r":1,"e":"SA 10M, 100M si appel épargne"},
{"q":"Hypothèque où inscrite?","o":["Mairie","Conservation Kaloum","APIP"],"r":1,"e":"Conservation Foncière Kaloum 10 ans renouvelable"},
{"q":"Saisie attribution bloque quoi?","o":["Compte bancaire","Maison","Voiture"],"r":0,"e":"Bloque compte bancaire attribue créancier art 77 AUCE"},
{"q":"Injonction payer délai opposition?","o":["15 jours","1 an","0"],"r":0,"e":"Débiteur 15j opposition sinon exécutoire"},
{"q":"SARL gérant responsable?","o":["Civile et pénale abus biens sociaux","Jamais","Seulement civile"],"r":0,"e":"Gérant responsable civile faute gestion pénale abus biens sociaux"},
{"q":"Prescription terrain?","o":["5 ans","30 ans","1 an"],"r":1,"e":"Prescription acquisitive terrain 30 ans"},
{"q":"CCJA où?","o":["Conakry","Abidjan","Dakar"],"r":1,"e":"CCJA Abidjan"},
{"q":"CCJA peut faire quoi?","o":["Casser et évoquer rejuge elle-même","Rien","Conseiller"],"r":0,"e":"CCJA casse et peut évoquer rejuge elle-même"},
{"q":"Arbitrage durée?","o":["6 mois","5 ans","10 ans"],"r":0,"e":"Arbitrage rapide 6 mois vs 2 ans TPI"},
{"q":"Bail commercial durée min?","o":["1 an","2 ans","10 ans"],"r":1,"e":"Bail commercial OHADA durée min 2 ans"},
{"q":"Fonds commerce essentiel?","o":["Clientèle","Voiture","Maison"],"r":0,"e":"Clientèle essentielle sans clientèle pas fonds"},
],
"OHADA": [
{"q":"OHADA =?","o":["Harmonisation Droit Affaires","Humanitaire","Douane"],"r":0,"e":"Organisation Harmonisation Droit Affaires Afrique"},
{"q":"RCCM à?","o":["Mairie","APIP","TPI"],"r":1,"e":"APIP Guinée 500k"},
{"q":"AUDCG =?","o":["Commerce","Sociétés","Sûretés"],"r":0,"e":"AUDCG Droit Commercial Général"},
{"q":"AUSCGIE =?","o":["Sociétés","Exécution","Arbitrage"],"r":0,"e":"AUSCGIE Sociétés et GIE"},
{"q":"AUS =?","o":["Sûretés","Commerce","Pénal"],"r":0,"e":"AUS Sûretés caution hypothèque gage"},
{"q":"AUCE =?","o":["Voies Exécution","Sociétés","Transport"],"r":0,"e":"AUCE Voies Exécution saisie injonction payer"},
{"q":"AUA =?","o":["Arbitrage","Transport","Comptabilité"],"r":0,"e":"AUA Arbitrage justice privée"},
{"q":"AUPC =?","o":["Procédures Collectives","Commerce","Pénal"],"r":0,"e":"AUPC Entreprise difficulté redressement liquidation"},
{"q":"SARL associés?","o":["1-100","1-10","0"],"r":0,"e":"SARL 1-100 associés"},
{"q":"SA capital?","o":["1M","10M","100k"],"r":1,"e":"SA 10M"},
{"q":"Hypothèque rang?","o":["Première inscrite payée première","Dernière","Hasard"],"r":0,"e":"Rang ordre inscription première payée première"},
{"q":"Caution solidaire?","o":["Créancier va direct caution","Poursuit d'abord débiteur","Jamais paie"],"r":0,"e":"Solidaire direct caution sans poursuivre débiteur"},
{"q":"Saisie attribution art?","o":["77 AUCE","1 AUCE","999"],"r":0,"e":"Saisie attribution art 77 AUCE"},
{"q":"Injonction payer art?","o":["1 AUCE","77 AUCE","190 AUS"],"r":0,"e":"Injonction payer art 1 AUCE"},
{"q":"OHADA primauté?","o":["Oui sur lois nationales affaires","Non","Parfois"],"r":0,"e":"OHADA primauté sur lois nationales affaires"},
]
}

def moteur_faq_vrai(q):
    ql=q.lower().strip()
    # ===== REPONSES SPECIFIQUES - PAS GENERIQUE =====
    if "juge" in ql:
        return "LE JUGE c'est le magistrat qui tranche les litiges au nom du peuple guinéen. Il est indépendant et inamovible. Il existe: Juge au TPI Première Instance (Conakry, Kindia, Labé, Kankan, N'Zérékoré) qui juge civil, pénal, commerce, travail, foncier. Juge d'instruction qui enquête sur les crimes. Juge à la Cour d'Appel Conakry qui rejuge appel. Juge à la Cour Suprême qui casse les arrêts mal jugés. Juge à la CCJA Abidjan pour OHADA. Différence avec Procureur: Procureur accuse (il demande prison), Juge tranche (il décide prison ou pas). Juge statue selon loi et conscience, impartial. Nomination par Conseil Supérieur Magistrature. Pour devenir juge: Master Droit + ENAM + concours magistrature."
    if "viol" in ql or "viole" in ql:
        return "PRISON POUR VIOL en Guinée: Art 321 Code pénal. Viol = acte sexuel sans consentement par violence, contrainte, menace, surprise. Peine: 5 à 10 ans réclusion criminelle. Si victime mineure moins 18 ans: 10 à 20 ans. Si victime moins 13 ans: réclusion à perpétuité. Procédure: Victime porte plainte Commissariat ou Procureur TPI, certificat médical CHU dans 24h très important, enquête OPJ, Cour Assises juge. Victime peut se constituer partie civile pour dommages intérêts. Prescription: 20 ans si mineur. Si tu es accusé à tort: avocat, preuves alibi, témoins. Si tu es victime: ne te lave pas, garde vêtements, va CHU, porte plainte vite, association aide."
    if "prison" in ql and "dette" in ql:
        return "NON! Pas de prison pour dette contractuelle! Art 11 Pacte International + Constitution Guinée. Tu as emprunté 10M tu ne paies pas = pas prison, c'est civil. Exception: pension alimentaire non payée = prison, amende pénale non payée = prison. Si quelqu'un te menace prison pour dette = chantage délit, porte plainte. Recouvrement légal: mise en demeure huissier 50k, injonction payer Président TPI 15 jours, saisie attribution compte bancaire art 77 AUCE."
    if "terrain" in ql or "foncier" in ql or "titre" in ql:
        return "TERRAIN - Titre Foncier: Seul Titre Foncier Conservation Kaloum = propriété inattaquable. Sans = occupant précaire. Procédure: 1- Acte coutumier chef quartier 2 témoins, 2- Demande Kaloum formulaire CNI acte coutumier plan, 3- Enquête publique affichage 1 mois, 4- Bornage géomètre contradictoire voisins, 5- Commission, 6- Immatriculation livre foncier Titre duplicata. Coût 2-5M délai 6-12 mois. Arnaques Conakry: même terrain vendu 5 fois, faux titres Sonfonia Coyah Madina. Toujours vérifier livre foncier Kaloum avant payer, passer notaire, virement pas cash."
    if "sarl" in ql or "entreprise" in ql or "rccm" in ql or "créer" in ql:
        return "CRÉER SARL Guinée: APIP Kaloum: 1- Recherche nom 50k, 2- Statuts notaire 300k capital min 1M FCFA libéré 50% solde 2 ans parts 5k min, 3- RCCM 500k, 4- NIF gratuit, 5- CNSS. Délai 48h total 1,5M. SARL 1-100 associés responsabilité limitée apports, gérant personne physique pouvoirs larges responsabilité civile faute gestion pénale abus biens sociaux, AG ordinaire annuelle comptes extra modif statuts 75%, cession parts libre entre associés agrément tiers 50%."
    if "ohada" in ql:
        return "OHADA: 17 pays même loi affaires. 10 Actes Uniformes: AUDCG commerce RCCM bail 2 ans droit renouvellement fonds, AUSCGIE sociétés SARL 1M SA 10M SAS libre, AUS sûretés caution hypothèque Conservation, AUPC redressement liquidation déclaration cessation 30 jours, AUCE saisie attribution injonction payer 15 jours astreinte, AUA arbitrage rapide 6 mois confidentiel CCJA centre, compta SYSCOHADA, transport, coopératives, médiation. CCJA Abidjan 13 juges cassation OHADA casse arrêt Appel Conakry peut évoquer rejuge elle-même primauté sur lois nationales."
    if "licenciement" in ql or "salaire" in ql or "patron" in ql:
        return "PATRON NE PAIE PAS / LICENCIEMENT: 1- Mise en demeure huissier 50k décompte salaires. 2- Inspection Travail Kaloum gratuit convocation patron conciliation. 3- Si échec Tribunal Travail TPI requête 20k contrat bulletins attestation collègues. Tu obtiens salaires arriérés + dommages licenciement abusif + certificat. Délai prescription 1 an. Ne démissionne pas! Licenciement doit avoir motif réel sérieux, entretien préalable, lettre, préavis, certificat, solde. Sans motif = abusif Tribunal Travail dommages."
    if "vol" in ql:
        return "VOL: Art 373 CP soustraction frauduleuse chose autrui contre gré. Peine 1-5 ans. Aggravé effraction nuit arme bande organisée 10 ans. Différence Escroquerie: vol sans accord tu arraches, escroquerie avec accord mais trompé tu donnes car faux. Recel: acheter volé sachant volé même peine voleur 1-5 ans art 370 CP ex téléphone volé Madina. Procédure: plainte Commissariat ou Procureur, enquête OPJ, TPI Correctionnel."
    if "escroquerie" in ql:
        return "ESCROQUERIE: Art 394 CP tromperie remise volontaire chose par ruse mensonge manœuvre. Ex faux iPhone, faux terrain, faux marabout. Peine 1-5 ans + remboursement. Preuves: messages WhatsApp, reçus, témoins. Plainte Procureur ou Commissariat. Différence vol: vol sans accord, escroquerie tu donnes car trompé."
    if "divorce" in ql:
        return "DIVORCE Guinée: TPI section famille. 2 types: Consentement mutuel acte notaire rapide, ou Faute adultère violences abandon. Pièces: acte mariage, actes enfants, preuves faute. Délai 6 mois à 2 ans. Pension alimentaire enfants, prestation compensatoire, garde enfants intérêt supérieur enfant, partage biens communauté. Avocat conseillé."
    if "succession" in ql or "héritage" in ql:
        return "SUCCESSION / HÉRITAGE Guinée: Code civil + coutume. Héritiers réservataires: enfants 75% si 1 enfant 50% si 2, conjoint survivant. Testament possible notaire. Partage amiable ou judiciaire TPI. Déclaration succession impôts. Conflits fréquents notaire + géomètre + TPI. Garde acte décès, livret famille."
    if "avocat" in ql:
        return "AVOCAT Guinée: Consultation 200-500k, TPI 2-5M, Assises 10-30M. Si pauvre aide juridictionnelle Barreau Kaloum gratuit ou clinique juridique UGLC Sonfonia. Avocat défend, conseille, rédige contrats. Différence avocat / juge / procureur: Avocat défend client, Procureur accuse, Juge tranche. Pour trouver avocat: Barreau Guinée Kaloum liste."
    if "garde" in ql and "vue" in ql or "police" in ql:
        return "GARDE À VUE / POLICE: Police retient suspect commissariat enquête 48h renouvelable 96h max. Terrorisme 72h x2. Droits: avocat 1ère heure, médecin, famille, silence. Dépassement = nullité libération. Torture interdite Constitution art 6. Si torture: certificat médical CHU, plainte Procureur + Inspection Police, ONDH, avocat. Habeas Corpus: ordre juge police présenter détenu 48h sinon libération."
    if "bail" in ql or "loyer" in ql:
        return "BAIL / LOYER: Bail commercial OHADA durée min 2 ans droit renouvellement indemnité éviction valeur fonds sauf motif grave non paiement non exploitation démolition loyer révisable 3 ans indice cession avec fonds libre. Bail habitation loi guinéenne dépôt garantie 1-3 mois résiliation impayé mise en demeure 1 mois puis TPI expulsion. Impayé: mise en demeure puis TPI, pas couper électricité illégal."
    if "contrat" in ql:
        return "CONTRAT: Accord volontés créant obligations. 4 conditions art 1128: consentement libre (pas erreur dol violence), capacité 18 ans, objet certain licite (pas drogue), cause licite (pas tuer). Force obligatoire art 1103 contrat = loi entre parties. Inexécution = mise en demeure 8j, exécution forcée, résolution, dommages intérêts. Nullité si manque condition."
    if "mariage" in ql:
        return "MARIAGE Guinée: Conditions âge 18 ans consentement libre monogamie ou polygamie optionnelle si choix au mariage, pas lien parenté. Cérémonie: coutumier chef quartier + civil Mairie + religieux. Effets: devoirs fidélité secours assistance, régime biens communauté sauf contrat. Divorce faute ou consentement mutuel TPI famille."
    # Fallback intelligent mais spécifique à question
    return f"Pour ta question '{q}': Voici analyse droit guinéen et OHADA: Cette question relève du droit {'pénal' if any(x in ql for x in ['vol','viol','prison','meurtre']) else 'civil' if any(x in ql for x in ['contrat','famille','divorce']) else 'commercial OHADA' if any(x in ql for x in ['société','commerce','bail']) else 'général'}. Textes: Constitution 2020, Code civil, Code pénal, Code travail, Actes Uniformes OHADA. Procédure: 1- Mise en demeure 8j huissier obligatoire art 54 CPCC, 2- Conciliation quartier / Inspection Travail / APIP, 3- Requête TPI 50k + pièces, 4- Audience jugement 1-2 ans, 5- Appel Cour Appel 1 mois, 6- Cassation Cour Suprême ou CCJA Abidjan si OHADA 2 mois. Preuves: écrit >500k obligatoire, témoignage. Poste dans Dossiers Justice pour analyse multi-experts détaillée. Si tu veux plus précis, repose question avec détails ex: 'prison pour vol téléphone?'"

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
.tabs{display:flex;gap:4px;padding:6px;background:#0a0a1a;overflow-x:auto;position:sticky;top:100px;z-index:20}
.tabs button{padding:7px 10px;border-radius:18px;border:1px solid #222;background:#151530;color:#aaa;font-size:9px;font-weight:800;white-space:nowrap}
.tabs button.active{background:#f9c00f;color:#000}
.view{display:none;padding:10px}.view.active{display:block}
.card{background:#10102a;border:1px solid #1a1a3a;border-radius:12px;padding:12px;margin:8px 0;cursor:pointer}
.card:hover{border-color:#f9c00f}
.badge{padding:3px 8px;border-radius:12px;font-size:8px;font-weight:900;color:#000;background:#f9c00f}
input,select,textarea{width:100%;padding:8px;margin:4px 0;border-radius:8px;border:1px solid #222;background:#111;color:#fff;font-size:12px}
.btn{padding:8px 12px;border-radius:18px;border:none;font-weight:800;background:#f9c00f;color:#000;cursor:pointer;font-size:11px}
.small{font-size:12px;color:#ddd;line-height:1.7;white-space:pre-wrap}
.breadcrumb{font-size:11px;color:#aaa;margin-bottom:10px}
.breadcrumb span{color:#00e5ff;cursor:pointer}
.download-btn{background:linear-gradient(90deg,#f9c00f,#ff6a00);color:#000;padding:10px 18px;border-radius:25px;font-weight:900;font-size:12px;border:none;cursor:pointer;margin-top:10px}
.lecon{background:#0a1a0a;border:2px solid #76ff03;padding:14px;border-radius:10px;margin-top:10px}
.licence-card{background:linear-gradient(135deg,#1a1a4a,#0a0a2a);border:2px solid #f9c00f;padding:18px;border-radius:16px;margin:10px 0;text-align:center;cursor:pointer}
.depot{border:2px dashed #f9c00f;background:#1a1a00;padding:14px;border-radius:12px;margin-top:16px}
</style></head><body>
<div class="header">
<h1 style="color:#f9c00f;font-size:26px;font-weight:900">DROIT224</h1>
<p style="font-size:8px;color:#aaa">L1 • L2 • L3 • OHADA • DICTIONNAIRE A-Z • FAQ AI</p>
<button class="download-btn" onclick="downloadApp()">📥 TÉLÉCHARGER L'APP DROIT224</button>
</div>
<div class="tabs">
<button class="active" onclick="showTab('cours',this)">📚 COURS L1 L2 L3</button>
<button onclick="showTab('ohada',this)" style="border-color:#00e5ff;color:#00e5ff">⚖️ OHADA</button>
<button onclick="showTab('lex',this)">📖 DICTIONNAIRE A-Z</button>
<button onclick="showTab('quiz',this)">🎮 QUIZ</button>
<button onclick="showTab('faq',this)" style="border-color:#76ff03;color:#76ff03">❓ FAQ</button>
<button onclick="showTab('dossier',this)" style="border-color:#ff1744">📂 DOSSIERS</button>
<button onclick="showTab('forum',this)">💬 CERCLE</button>
</div>

<div id="cours" class="view active"><div id="bcCours" class="breadcrumb"></div><div id="gridCours"></div>
<!-- DEPOT COURS TOUJOURS VISIBLE EN BAS DES COURS -->
<div class="depot">
<h3 style="color:#f9c00f">➕ DÉPÔT DE COURS - Étudiant / Professeur / Enseignant / Docteur / Juge / Avocat</h3>
<p class="small" style="color:#aaa">Dépose ton cours PDF ou leçon, quantité illimitée, avec ton nom et prénom. Il apparaîtra pour tous!</p>
<input id="depNom" placeholder="Nom et Prénom * ex: Mamadou Diallo">
<input id="depPrenom" placeholder="Prénom (si séparé)">
<select id="depRole"><option>Étudiant</option><option>Professeur</option><option>Enseignant</option><option>Docteur</option><option>Juge</option><option>Avocat</option><option>Juriste</option></select>
<select id="depLic"><option>L1</option><option>L2</option><option>L3</option><option>OHADA</option></select>
<input id="depMat" placeholder="Matière * ex: Droit Constitutionnel">
<input id="depTitre" placeholder="Titre du cours * ex: Chapitre 1 Constitution">
<textarea id="depCont" rows="4" placeholder="Contenu leçon complet... ou colle ton cours ici"></textarea>
<input id="depPdf" placeholder="Lien PDF (optionnel) https://... ou drive / pdf">
<button class="btn" style="width:100%;padding:12px;font-size:12px" onclick="deposerCours()">📥 DÉPOSER MON COURS</button>
<div id="depMsg"></div>
</div>
<div id="gridDepot"></div>
</div>

<div id="ohada" class="view"><div id="bcOhada" class="breadcrumb"></div><div id="gridOhada"></div></div>
<div id="lex" class="view"><div class="card" style="border:2px solid #00e5ff"><h4>📖 Dictionnaire Juridique A-Z</h4><div style="display:flex;gap:4px"><input id="lexIn" placeholder="Cherche mot..." oninput="searchLex()" style="flex:1"><select id="lexLettre" onchange="filterLettre()" style="width:80px"><option value="">A-Z</option><option>A</option><option>B</option><option>C</option><option>D</option><option>E</option><option>F</option><option>G</option><option>H</option><option>I</option><option>J</option><option>M</option><option>N</option><option>O</option><option>P</option><option>Q</option><option>R</option><option>S</option><option>T</option><option>V</option></select></div><div id="lexAuto"></div></div><div id="gridLex"></div></div>
<div id="quiz" class="view">
<div class="card" style="text-align:center;border:2px solid #f9c00f">
<h3>🎮 QUIZ - Toute la Licence</h3>
<p class="small">Choisis ta licence, 10 questions aléatoires, Rejouer = nouvelles questions! 10/10 = Badge OR!</p>
<select id="qLvl"><option>L1</option><option>L2</option><option>L3</option><option>OHADA</option></select>
<button class="btn" onclick="startQuiz()">🚀 LANCER QUIZ 10 QUESTIONS</button>
<div id="qZone" style="text-align:left;margin-top:10px"></div>
<div id="qBadge"></div>
</div>
</div>
<div id="faq" class="view"><div class="card" style="border:2px solid #76ff03;background:linear-gradient(135deg,#001a00,#000)"><h4 style="color:#76ff03">❓ FAQ - Assistant AI Juridique</h4><p class="small" style="color:#aaa">Pose n'importe quelle question de droit. Ex: c'est qui le juge? prison pour viol? terrain? Je réponds précisément, pas générique!</p><div style="display:flex;gap:4px;margin-top:8px"><input id="faqAsk" placeholder="Ex: c'est qui le juge? prison pour viol?"><button class="btn" style="background:#76ff03" onclick="askFaq()">Demander</button></div><div id="faqAuto"></div></div><div style="display:flex;gap:4px;flex-wrap:wrap;margin-top:8px"><button class="btn" style="background:#222;color:#fff" onclick="askQuick('c est qui le juge')">C'est qui le juge?</button><button class="btn" style="background:#222;color:#fff" onclick="askQuick('prison pour viol')">Prison pour viol?</button><button class="btn" style="background:#222;color:#fff" onclick="askQuick('prison pour dette')">Prison dette?</button><button class="btn" style="background:#222;color:#fff" onclick="askQuick('terrain Sonfonia')">Terrain?</button></div></div>
<div id="dossier" class="view"><div class="card" style="border:2px solid #ff1744;background:#1a0000"><h4>Dossiers Justice</h4><select id="dType"><option>Licenciement</option><option>Dette</option><option>Terre Foncier</option><option>Divorce</option><option>Vol</option><option>Contrat</option></select><textarea id="dDesc" rows="3" placeholder="Décris cas..."></textarea><input id="dNom" placeholder="Ton nom"><button class="btn" style="background:#ff1744;color:#fff;width:100%" onclick="postDossier()">Soumettre</button><div id="dAuto"></div></div><div id="gridDossier"></div></div>
<div id="forum" class="view"><div class="card" style="border:2px solid #f9c00f"><select id="fRole"><option>Étudiant</option><option>Professeur</option><option>Juge</option><option>Avocat</option><option>Docteur</option></select><input id="fNom" placeholder="Nom"><textarea id="fMsg" placeholder="Question"></textarea><button class="btn" style="width:100%" onclick="postForum()">Poster</button></div><div id="gridForum"></div></div>

<script>
let DB={};
let navC={level:'licences', lic:null, matId:null, chapIdx:null, secIdx:null, sousIdx:null};
let navO={level:'matieres', matId:null, chapIdx:null, secIdx:null, sousIdx:null};

async function load(){DB=await fetch('/api/all').then(r=>r.json());renderCours();renderOhada();renderLex();renderDossier();renderForum();renderDepot();}
function showTab(id,btn){document.querySelectorAll('.view').forEach(v=>v.classList.remove('active'));document.getElementById(id).classList.add('active');document.querySelectorAll('.tabs button').forEach(b=>b.classList.remove('active'));btn.classList.add('active');}

function renderCours(){
 let h=''; let bc='';
 if(navC.level=='licences'){
   bc='📚 Cours - Choisis ta Licence';
   h+=`<div class="licence-card" onclick="openLicence('L1')"><h2 style="color:#f9c00f;font-size:28px">🎓 LICENCE 1</h2><p class="small">Introduction Droit, Constitutionnel - Clique pour voir matières</p></div>`;
   h+=`<div class="licence-card" style="border-color:#00e5ff" onclick="openLicence('L2')"><h2 style="color:#00e5ff;font-size:28px">🎓 LICENCE 2</h2><p class="small">Obligations, Pénal - Clique pour voir matières</p></div>`;
   h+=`<div class="licence-card" style="border-color:#76ff03" onclick="openLicence('L3')"><h2 style="color:#76ff03;font-size:28px">🎓 LICENCE 3</h2><p class="small">Foncier, Sociétés OHADA - Clique pour voir matières</p></div>`;
 } else if(navC.level=='matieres'){
   let list=DB.cours[navC.lic]||[];
   bc=`<span onclick="goLicences()">📚 Licences</span> > ${navC.lic}`;
   list.forEach(m=>{h+=`<div class=card onclick="openMatiere('${m.id}')"><b>${m.icon} ${m.matiere}</b> <span class=badge>${m.niveau}</span><p class=small style=margin-top:6px>${m.programme.length} chapitres - Ouvrir dossier 📁</p></div>`});
   h+=`<button class=btn onclick="goLicences()">⬅️ Retour Licences</button>`;
 } else if(navC.level=='chapitres'){
   let mat=(DB.cours[navC.lic]||[]).find(x=>x.id==navC.matId);
   bc=`<span onclick="goLicences()">📚</span> > <span onclick="goMatieres()">${navC.lic}</span> > ${mat.matiere} - Programme`;
   mat.programme.forEach((ch,i)=>{h+=`<div class=card onclick="openChap(${i})"><b style=color:#00e5ff>📁 ${ch.titre}</b><p class=small>${ch.sections.length} sections</p></div>`});
   h+=`<button class=btn onclick="goMatieres()">⬅️ Retour Matières</button>`;
 } else if(navC.level=='sections'){
   let mat=(DB.cours[navC.lic]||[]).find(x=>x.id==navC.matId);
   let ch=mat.programme[navC.chapIdx];
   bc=`<span onclick="goLicences()">📚</span> > <span onclick="goMatieres()">${navC.lic}</span> > <span onclick="goChapitres()">${mat.matiere}</span> > ${ch.titre}`;
   ch.sections.forEach((sec,i)=>{h+=`<div class=card onclick="openSec(${i})"><b>📂 ${sec.titre}</b><p class=small>${sec.sous_sections.length} sous-sections</p></div>`});
   h+=`<button class=btn onclick="goChapitres()">⬅️ Retour Chapitres</button>`;
 } else if(navC.level=='sous'){
   let mat=(DB.cours[navC.lic]||[]).find(x=>x.id==navC.matId);
   let ch=mat.programme[navC.chapIdx];
   let sec=ch.sections[navC.secIdx];
   bc=`<span onclick="goLicences()">📚</span> > <span onclick="goMatieres()">${navC.lic}</span> > <span onclick="goChapitres()">${mat.matiere}</span> > <span onclick="goSections()">${ch.titre}</span> > ${sec.titre}`;
   sec.sous_sections.forEach((s,i)=>{h+=`<div class=card onclick="openSous(${i})"><b>📄 ${s.titre}</b><p class=small style=color:#76ff03>Clique pour leçon intégrale complète détaillée</p></div>`});
   h+=`<button class=btn onclick="goSections()">⬅️ Retour Sections</button>`;
 } else if(navC.level=='lecon'){
   let mat=(DB.cours[navC.lic]||[]).find(x=>x.id==navC.matId);
   let ch=mat.programme[navC.chapIdx];
   let sec=ch.sections[navC.secIdx];
   let ssec=sec.sous_sections[navC.sousIdx];
   bc=`<span onclick="goLicences()">📚</span> > <span onclick="goMatieres()">${navC.lic}</span> > <span onclick="goChapitres()">${mat.matiere}</span> > <span onclick="goSections()">${ch.titre}</span> > <span onclick="goSous()">${sec.titre}</span> > ${ssec.titre}`;
   h=`<div class=card style=border:2px solid #76ff03"><h3 style=color:#f9c00f>${ssec.titre}</h3><div class="lecon"><p class=small>${ssec.lecon}</p></div><div style=margin-top:12px;display:flex;gap:6px"><button class=btn onclick="goSous()">⬅️ Retour Sous-sections</button><button class=btn style=background:#00e5ff" onclick="goSous()">✅ Leçon comprise</button></div></div>`;
 }
 document.getElementById('bcCours').innerHTML=bc;
 document.getElementById('gridCours').innerHTML=h;
}
function openLicence(lic){navC.lic=lic;navC.level='matieres';renderCours();}
function openMatiere(id){navC.matId=id;navC.level='chapitres';renderCours();}
function openChap(i){navC.chapIdx=i;navC.level='sections';renderCours();}
function openSec(i){navC.secIdx=i;navC.level='sous';renderCours();}
function openSous(i){navC.sousIdx=i;navC.level='lecon';renderCours();}
function goLicences(){navC.level='licences';renderCours();}
function goMatieres(){navC.level='matieres';renderCours();}
function goChapitres(){navC.level='chapitres';renderCours();}
function goSections(){navC.level='sections';renderCours();}
function goSous(){navC.level='sous';renderCours();}

function renderOhada(){
 let h=''; let bc='';
 if(navO.level=='matieres'){
   bc='⚖️ OHADA - Choisis Acte Uniforme';
   (DB.ohada||[]).forEach(m=>{h+=`<div class=card onclick="openOhadaMat('${m.id}')"><b style=color:#00e5ff>${m.icon} ${m.matiere}</b><p class=small>${m.programme.length} chapitres - Ouvrir dossier 📁</p></div>`});
 } else if(navO.level=='chapitres'){
   let mat=(DB.ohada||[]).find(x=>x.id==navO.matId);
   bc=`<span onclick="goOhadaMat()">⚖️ OHADA</span> > ${mat.matiere} - Programme`;
   mat.programme.forEach((ch,i)=>{h+=`<div class=card onclick="openOhadaChap(${i})"><b style=color:#00e5ff>📁 ${ch.titre}</b><p class=small>${ch.sections.length} sections</p></div>`});
   h+=`<button class=btn onclick="goOhadaMat()">⬅️ Retour OHADA</button>`;
 } else if(navO.level=='sections'){
   let mat=(DB.ohada||[]).find(x=>x.id==navO.matId);
   let ch=mat.programme[navO.chapIdx];
   bc=`<span onclick="goOhadaMat()">⚖️</span> > <span onclick="goOhadaChapitres()">${mat.matiere}</span> > ${ch.titre}`;
   ch.sections.forEach((sec,i)=>{h+=`<div class=card onclick="openOhadaSec(${i})"><b>📂 ${sec.titre}</b><p class=small>${sec.sous_sections.length} sous-sections</p></div>`});
   h+=`<button class=btn onclick="goOhadaChapitres()">⬅️ Retour Chapitres</button>`;
 } else if(navO.level=='sous'){
   let mat=(DB.ohada||[]).find(x=>x.id==navO.matId);
   let ch=mat.programme[navO.chapIdx];
   let sec=ch.sections[navO.secIdx];
   bc=`<span onclick="goOhadaMat()">⚖️</span> > <span onclick="goOhadaChapitres()">${mat.matiere}</span> > <span onclick="goOhadaSections()">${ch.titre}</span> > ${sec.titre}`;
   sec.sous_sections.forEach((s,i)=>{h+=`<div class=card onclick="openOhadaSous(${i})"><b>📄 ${s.titre}</b><p class=small style=color:#76ff03>Clique leçon intégrale</p></div>`});
   h+=`<button class=btn onclick="goOhadaSections()">⬅️ Retour Sections</button>`;
 } else if(navO.level=='lecon'){
   let mat=(DB.ohada||[]).find(x=>x.id==navO.matId);
   let ch=mat.programme[navO.chapIdx];
   let sec=ch.sections[navO.secIdx];
   let ssec=sec.sous_sections[navO.sousIdx];
   bc=`<span onclick="goOhadaMat()">⚖️</span> > <span onclick="goOhadaChapitres()">${mat.matiere}</span> > <span onclick="goOhadaSections()">${ch.titre}</span> > <span onclick="goOhadaSous()">${sec.titre}</span> > ${ssec.titre}`;
   h=`<div class=card style=border:2px solid #76ff03"><h3 style=color:#f9c00f>${ssec.titre}</h3><div class="lecon"><p class=small>${ssec.lecon}</p></div><button class=btn style=margin-top:10px" onclick="goOhadaSous()">⬅️ Retour</button></div>`;
 }
 document.getElementById('bcOhada').innerHTML=bc;
 document.getElementById('gridOhada').innerHTML=h;
}
function openOhadaMat(id){navO.matId=id;navO.level='chapitres';renderOhada();}
function openOhadaChap(i){navO.chapIdx=i;navO.level='sections';renderOhada();}
function openOhadaSec(i){navO.secIdx=i;navO.level='sous';renderOhada();}
function openOhadaSous(i){navO.sousIdx=i;navO.level='lecon';renderOhada();}
function goOhadaMat(){navO.level='matieres';renderOhada();}
function goOhadaChapitres(){navO.level='chapitres';renderOhada();}
function goOhadaSections(){navO.level='sections';renderOhada();}
function goOhadaSous(){navO.level='sous';renderOhada();}

function renderLex(){let h='';(DB.lexique||[]).forEach(l=>{h+=`<div class=card><b>[${l.lettre}] ${l.t}</b><p class=small style=margin-top:4px">${l.d}</p></div>`});document.getElementById('gridLex').innerHTML=h;}
function filterLettre(){let lettre=document.getElementById('lexLettre').value;if(!lettre){renderLex();return}let filt=(DB.lexique||[]).filter(l=>l.lettre==lettre);let h='';filt.forEach(l=>{h+=`<div class=card><b>[${l.lettre}] ${l.t}</b><p class=small>${l.d}</p></div>`});document.getElementById('gridLex').innerHTML=h;}
async function searchLex(){let q=document.getElementById('lexIn').value;if(q.length<2){document.getElementById('lexAuto').innerHTML='';renderLex();return}let res=await fetch('/api/search?q='+encodeURIComponent(q)).then(r=>r.json());document.getElementById('lexAuto').innerHTML=`<div class=card style=background:#002a2a;border-color:#00e5ff"><p class=small>${res.ans}</p></div>`;}

// ===== DEPOT COURS =====
async function deposerCours(){
 let d={nom:document.getElementById('depNom').value, prenom:document.getElementById('depPrenom').value, role:document.getElementById('depRole').value, lic:document.getElementById('depLic').value, mat:document.getElementById('depMat').value, titre:document.getElementById('depTitre').value, contenu:document.getElementById('depCont').value, pdf:document.getElementById('depPdf').value};
 if(!d.nom||!d.mat||!d.titre){alert('Remplis Nom, Matière, Titre');return}
 let res=await fetch('/api/depot',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)});
 document.getElementById('depMsg').innerHTML=`<div class=card style=background:#001a00;border-color:#76ff03;margin-top:8px"><b style=color:#76ff03>✅ Cours déposé! Merci ${d.nom} (${d.role}) - Il est visible pour tous en bas!</b></div>`;
 document.getElementById('depTitre').value='';document.getElementById('depCont').value='';document.getElementById('depPdf').value='';
 load();
}
function renderDepot(){
 let h='';(DB.depot||[]).slice().reverse().forEach(d=>{
   h+=`<div class=card style=border:2px solid #f9c00f"><b>📄 ${d.titre}</b> <span class=badge>${d.lic} - ${d.mat}</span><p class=small style=margin-top:6px">${d.contenu||''}</p>${d.pdf?`<p style=margin-top:6px"><a href="${d.pdf}" target="_blank" style=color:#00e5ff>📄 OUVRIR PDF: ${d.pdf}</a></p>`:''}<small style=color:#00e5ff>Déposé par ${d.nom} ${d.prenom||''} (${d.role}) - ${d.time}</small></div>`;
 });
 document.getElementById('gridDepot').innerHTML = h ? `<h3 style="margin-top:16px;color:#f9c00f">📚 Cours déposés par la communauté (${(DB.depot||[]).length}) - Quantité illimitée</h3>`+h : '';
}

// ===== QUIZ CORRIGÉ: 10 QUESTIONS ALÉATOIRES, BADGE =====
let cq=[],qi=0,sc=0;
function startQuiz(){
 let lvl=document.getElementById('qLvl').value;
 let bank=[...(DB.quiz[lvl]||[])];
 // Mélange aléatoire
 for(let i=bank.length-1;i>0;i--){let j=Math.floor(Math.random()*(i+1));[bank[i],bank[j]]=[bank[j],bank[i]];}
 cq=bank.slice(0,10); // 10 questions
 qi=0;sc=0;
 document.getElementById('qBadge').innerHTML='';
 showQ();
}
function showQ(){
 if(qi>=cq.length){
   let badge = sc==10 ? '🏆 BADGE OR - EXCELLENT! Tu es Maître Droit224!' : sc>=7 ? '🥈 BADGE ARGENT - Très bien!' : sc>=5 ? '🥉 BADGE BRONZE - Continue!' : '📚 Encore un effort!';
   document.getElementById('qZone').innerHTML=`<div style=text-align:center><h2 style=font-size:28px>${sc}/10</h2><div style=font-size:32px;margin:10px 0">${badge}</div><button class=btn onclick=startQuiz() style=padding:12px 20px;font-size:13px>🔄 REJOUER - Nouvelles questions!</button><p class=small style=margin-top:8px>Rejouer = 10 nouvelles questions aléatoires différentes!</p></div>`;
   return
 }
 let q=cq[qi];
 let h=`<div style=display:flex;justify-content:space-between><b>Question ${qi+1}/10</b><span class=badge>Score: ${sc}</span></div><h4 style=margin:10px 0;font-size:13px>${q.q}</h4>`;
 q.o.forEach((o,i)=>{h+=`<div class=card style="padding:10px;margin:4px 0" onclick="checkQ(${i})">${o}</div>`});
 document.getElementById('qZone').innerHTML=h;
}
function checkQ(i){
 let q=cq[qi];let ok=i==q.r;if(ok)sc++;
 document.getElementById('qZone').innerHTML+=`<div class=card style=background:${ok?'#001a00':'#1a0000'};margin-top:8px"><b>${ok?'✅ BONNE RÉPONSE!':'❌ MAUVAISE RÉPONSE'} ${q.e}</b><br><button class=btn onclick="qi++;showQ()" style=margin-top:6px>Question suivante ➡️</button></div>`;
}

// ===== FAQ VRAI AI =====
async function askFaq(){
 let q=document.getElementById('faqAsk').value;
 if(!q)return alert('Écris ta question');
 document.getElementById('faqAuto').innerHTML+=`<div class=card style=background:#111;border-color:#76ff03"><b style=color:#76ff03>⏳ Recherche en cours...</b></div>`;
 let res=await fetch('/api/search_faq?q='+encodeURIComponent(q)).then(r=>r.json());
 // Enlève loading
 let cards=document.getElementById('faqAuto').querySelectorAll('.card');
 if(cards.length) cards[cards.length-1].remove();
 document.getElementById('faqAuto').innerHTML+=`<div class=card style=background:#001a00;border-color:#76ff03;margin-top:10px"><b style=color:#76ff03>👤 Toi: ${q}</b><div style=border-top:1px solid #222;margin-top:8px;padding-top:8px"><b style=color:#00e5ff>🤖 FAQ AI:</b><p class=small style=margin-top:6px">${res.ans}</p></div></div>`;
 document.getElementById('faqAsk').value='';
 document.getElementById('faqAuto').scrollIntoView();
}
function askQuick(q){document.getElementById('faqAsk').value=q;askFaq();}

function renderDossier(){let h='';(DB.dossiers||[]).slice().reverse().forEach(d=>{h+=`<div class=card style=border:1px solid #ff1744"><b>📂 ${d.type}</b> <small style=color:#666">${d.time} par ${d.nom}</small><p class=small style=margin:6px 0">${d.desc}</p><div style=background:#111;padding:6px;border-radius:6px"><small style=color:#f9c00f"><b>FAQ AI:</b> ${d.auto||''}</small></div></div>`});document.getElementById('gridDossier').innerHTML=h;}
async function postDossier(){let d={type:document.getElementById('dType').value,desc:document.getElementById('dDesc').value,nom:document.getElementById('dNom').value};if(!d.desc)return alert('Décris cas');let res=await fetch('/api/search_faq?q='+encodeURIComponent(d.type+' '+d.desc)).then(r=>r.json());d.auto=res.ans;await fetch('/api/dossiers',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)});document.getElementById('dDesc').value='';load();}
function renderForum(){let h='';(DB.forum||[]).slice().reverse().forEach(m=>{h+=`<div class=card style=border-left:3px solid #f9c00f"><span class=badge>${m.role}</span> <b style=font-size:11px">${m.nom}</b> <small style=color:#666">${m.time}</small><p class=small style=margin:6px 0">${m.msg}</p></div>`});document.getElementById('gridForum').innerHTML=h;}
async function postForum(){let d={role:document.getElementById('fRole').value,nom:document.getElementById('fNom').value,msg:document.getElementById('fMsg').value};if(!d.nom||!d.msg)return alert('Nom et message');await fetch('/api/forum',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)});document.getElementById('fMsg').value='';load();}
function downloadApp(){alert('📥 TÉLÉCHARGER DROIT224:\\n\\n1. Chrome Android: Menu ⋮ > Installer application ou Ajouter à écran accueil\\n2. iPhone: Partage (carré flèche) > Sur écran accueil > Ajouter\\n3. Tu auras icône DROIT224 comme vraie app! PWA - Pas besoin Play Store!');if(window.deferredPrompt){window.deferredPrompt.prompt();}}
let deferredPrompt;window.addEventListener('beforeinstallprompt',(e)=>{e.preventDefault();deferredPrompt=e;window.deferredPrompt=e;});
load();
</script></body></html>
"""

@app.route("/manifest.json")
def manifest():
    return jsonify({"name":"DROIT224","short_name":"DROIT224","start_url":"/","display":"standalone","background_color":"#050510","theme_color":"#f9c00f","icons":[{"src":"https://cdn-icons-png.flaticon.com/512/1087/1087815.png","sizes":"192x192","type":"image/png"}]})

@app.route("/api/all")
def all_api():
    dossiers=load_j("dossiers_v15.json", [])
    forum=load_j("forum_v15.json", [])
    depot=load_j("depot_v15.json", [])
    return jsonify({"cours":COURS_LICENCES,"ohada":OHADA_DATA,"lexique":DICT_AZ,"quiz":QUIZ_BANK,"dossiers":dossiers,"forum":forum,"depot":depot})

@app.route("/api/search")
def search_api():
    q=request.args.get("q","")
    ql=q.lower()
    for item in DICT_AZ:
        if item["t"].lower() in ql or ql in item["t"].lower():
            return jsonify({"ans":item["d"]})
    return jsonify({"ans":f"{q}: Définition complète en droit guinéen et OHADA, voir cours détaillés."})

@app.route("/api/search_faq")
def search_faq_api():
    q=request.args.get("q","")
    return jsonify({"ans":moteur_faq_vrai(q)})

@app.route("/api/depot", methods=["POST"])
def depot_post():
    d=request.get_json()
    alld=load_j("depot_v15.json", [])
    alld.append({"id":uuid.uuid4().hex[:5],"nom":d.get("nom",""),"prenom":d.get("prenom",""),"role":d.get("role",""),"lic":d.get("lic",""),"mat":d.get("mat",""),"titre":d.get("titre",""),"contenu":d.get("contenu",""),"pdf":d.get("pdf",""),"time":datetime.now().strftime("%d/%m %H:%M")})
    save_j("depot_v15.json", alld)
    return jsonify({"ok":True,"total":len(alld)})

@app.route("/api/dossiers", methods=["POST"])
def dossiers_post():
    d=request.get_json()
    alld=load_j("dossiers_v15.json", [])
    alld.append({"id":uuid.uuid4().hex[:5],"type":d.get("type",""),"desc":d.get("desc",""),"nom":d.get("nom",""),"time":datetime.now().strftime("%d/%m %H:%M"),"auto":d.get("auto","")})
    save_j("dossiers_v15.json", alld)
    return jsonify({"ok":True})

@app.route("/api/forum", methods=["GET","POST"])
def forum_api():
    if request.method=="POST":
        d=request.get_json()
        allf=load_j("forum_v15.json", [])
        allf.append({"id":uuid.uuid4().hex[:5],"role":d.get("role",""),"nom":d.get("nom",""),"msg":d.get("msg",""),"time":datetime.now().strftime("%H:%M")})
        save_j("forum_v15.json", allf)
        return jsonify({"ok":True})
    return jsonify(load_j("forum_v15.json", []))

if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)))
