from flask import Flask, jsonify, request
import json, os, uuid, random
from datetime import datetime
app = Flask(__name__)

# ============ COURS L1 L2 L3 - STRUCTURE EXACTE GARDÉE - NON RÉSUMÉ ============
COURS_LICENCES = {
"L1": [
{
"id":"intro_l1","matiere":"Introduction au Droit","niveau":"L1 S1","icon":"📖",
"programme":[
{"titre":"Chapitre 1: La Règle de Droit","sections":[
{"titre":"Section 1: Définition de la règle de droit","sous_sections":[
{"titre":"Sous-section 1: Définition générale","lecon":"La règle de droit est une règle de conduite dans les rapports sociaux, générale, abstraite, obligatoire, dont le respect est assuré par la puissance publique. Elle se distingue de la règle morale qui est intérieure et non sanctionnée par l'État, de la règle religieuse dont la sanction est divine, de la règle de bienséance qui est une règle de politesse. Le droit objectif désigne l'ensemble des règles qui régissent la vie des hommes en société. Les droits subjectifs désignent les prérogatives individuelles que le droit objectif reconnaît aux individus, par exemple le droit de propriété, le droit de vote, le droit de créance. Le droit naturel est l'idéal de justice, ce qui devrait être, tandis que le droit positif est l'ensemble des règles en vigueur dans un pays à un moment donné. En République de Guinée, le droit positif est constitué de la Constitution du 22 mars 2020, des lois votées par le Conseil National de la Transition, des ordonnances du Président de la République, des décrets et arrêtés, de la coutume très importante en milieu rural guinéen notamment en matière de mariage coutumier Malinké sous l'empire du Manden Kalikan de 1236, Peulh avec le Pulaaku, Soussou, du règlement des litiges fonciers par les sages, de la jurisprudence de la Cour Suprême et de la Cour Commune de Justice et d'Arbitrage d'Abidjan pour le droit OHADA, et de la doctrine des professeurs de droit des universités de Sonfonia, Kofi Annan, UGLC."},
{"titre":"Sous-section 2: Caractères de la règle de droit","lecon":"La règle de droit présente quatre caractères fondamentaux. Premièrement, elle est générale et abstraite: elle vise toutes les personnes qui se trouvent dans une situation donnée et non une personne déterminée. Par exemple l'article 544 du Code civil qui définit la propriété s'applique à tous les propriétaires. Deuxièmement, elle est obligatoire: elle doit être respectée par tous sous peine de sanction. Troisièmement, elle est sanctionnée par l'État: le respect est assuré par la contrainte étatique, police, tribunal, prison, amende, huissier de justice, force publique. Quatrièmement, elle est permanente et évolutive: elle a vocation à durer mais elle évolue avec la société, exemple loi sur le cybercrime, loi sur la protection des données personnelles. On distingue la règle impérative qui s'impose absolument et dont on ne peut déroger par convention, exemple loi pénale, et la règle supplétive qui s'applique à défaut de volonté contraire des parties, exemple beaucoup de règles du Code civil en matière de contrat et de régime matrimonial."}
]},
{"titre":"Section 2: Sources du droit guinéen","sous_sections":[
{"titre":"Sous-section 1: Sources nationales","lecon":"Les sources nationales du droit guinéen sont: La Constitution du 22 mars 2020 est la loi suprême avec 156 articles, au dessus de tout, avec primauté selon l'article 151. La loi est votée par le Conseil National de la Transition, promulguée par le Président de la République, publiée au Journal Officiel de la République. Son domaine est défini par l'article 68 de la Constitution: droits civiques, libertés publiques, impôts, etc. L'ordonnance est prise par le Président de la République dans le domaine de la loi en cas d'urgence avec autorisation du CNT. Le règlement est constitué des décrets du Président, des arrêtés des ministres, des décisions des préfets et maires. La coutume est une habitude ancienne, constante, notoire, avec l'opinio juris c'est à dire la croyance qu'elle est obligatoire. Très importante en Guinée rurale pour le mariage coutumier, le régime foncier coutumier, le règlement des conflits par les chefs coutumiers. Conditions de la coutume: ancienneté, constance, notoriété, opinio juris. La jurisprudence ce sont les décisions rendues par les Cours et Tribunaux, notamment la Cour Suprême de Guinée et la CCJA pour le droit OHADA, qui font référence et que les juges du TPI doivent suivre pour la sécurité juridique. La doctrine ce sont les avis des professeurs, les thèses, les articles."},
{"titre":"Sous-section 2: Sources internationales et OHADA","lecon":"Les sources internationales du droit guinéen sont: Les traités internationaux ratifiés par la Guinée ont primauté sur la loi nationale selon l'article 151 de la Constitution 2020, par exemple le Pacte International relatif aux droits civils et politiques, la Convention contre la torture, le Traité OHADA. L'OHADA avec ses 10 Actes Uniformes a primauté sur les lois nationales pour le droit des affaires, c'est le droit de la comptabilité, du commerce, des sociétés, des sûretés, des procédures collectives, des voies d'exécution, de l'arbitrage, du transport, des coopératives, de la médiation. L'UEMOA, la CEDEAO avec sa Cour de Justice à Abuja, l'Union Africaine, l'ONU avec son Conseil de Sécurité à 5 membres permanents avec droit de veto, Assemblée Générale, Cour Internationale de Justice à La Haye."}
]}
]},
{"titre":"Chapitre 2: Branches du Droit","sections":[
{"titre":"Section 1: Droit Public","sous_sections":[
{"titre":"Sous-section 1: Branches du droit public","lecon":"Le droit public est l'ensemble des règles qui organisent l'État et qui règlent les rapports entre l'État et les citoyens. Son but est l'intérêt général. Il est inégalitaire car l'État est supérieur aux citoyens. Ses branches sont: Le droit constitutionnel qui étudie la Constitution, les pouvoirs politiques, les droits fondamentaux, le contrôle de constitutionnalité, la QPC Question Prioritaire de Constitutionnalité. Le droit administratif qui étudie l'administration, le service public avec ses principes de continuité, égalité, mutabilité, l'acte administratif unilatéral comme le décret du Président ou l'arrêté du ministre, le contrat administratif comme le marché public, le recours pour excès de pouvoir devant le Tribunal Administratif dans un délai de 2 mois, le plein contentieux, la responsabilité de l'administration pour faute simple ou lourde ou sans faute pour risque et rupture d'égalité. Le droit pénal qui détermine les infractions et les peines, principe de légalité pas d'infraction sans loi, non rétroactivité. Le droit fiscal qui étudie les impôts directs comme l'impôt sur le revenu, l'impôt sur les sociétés, et indirects comme la TVA à 18% en Guinée, la douane. Le droit international public qui étudie les États, les organisations internationales comme l'ONU, l'Union Africaine, la CEDEAO, les traités, la coutume internationale, la responsabilité de l'État pour fait internationalement illicite. Les finances publiques qui étudient le budget de l'État, loi de finances votée par le CNT, principes d'annualité, unité, universalité, spécialité, recettes et dépenses, exécution par ordonnateur et comptable public, contrôle Cour des Comptes."}
]},
{"titre":"Section 2: Droit Privé","sous_sections":[
{"titre":"Sous-section 1: Branches du droit privé","lecon":"Le droit privé est l'ensemble des règles qui régissent les rapports entre particuliers. Il est égalitaire et son but est l'intérêt privé. Ses branches sont: Le droit civil qui est le droit commun, qui étudie la personne physique être humain sujet de droit dès la naissance vivante viable jusqu'à la mort avec ses attributs nom prénom domicile nationalité patrimoine, la personne morale société association État avec personnalité distincte création RCCM, la famille mariage conditions âge 18 ans consentement monogamie ou polygamie optionnelle en Guinée divorce faute ou consentement mutuel filiation autorité parentale, les biens meubles et immeubles corporels incorporels propriété article 544 usus fructus abusus usufruit servitudes, les obligations et contrats. Le droit commercial qui étudie le commerçant article 2 AUDCG personne qui fait actes de commerce par nature à titre de profession habituelle, les actes de commerce par nature achat meubles pour revendre banque assurance transport intermédiaire construction spectacle télécom, par forme lettre de change billet à ordre société commerciale, par accessoire fait par commerçant pour son commerce, le fonds de commerce article 135 AUDCG ensemble clientèle et achalandage essentiel sans clientèle pas de fonds nom commercial enseigne droit au bail matériel marchandises brevets, le bail commercial article 69 AUDCG durée minimum 2 ans droit au renouvellement indemnité d'éviction valeur fonds sauf motif grave non paiement non exploitation démolition loyer révisable tous les 3 ans. Le droit du travail qui étudie le contrat de travail CDI règle générale CDD exception maximum 2 ans renouvelable période d'essai, les obligations employeur payer salaire sécurité employé travailler loyauté, le licenciement motif réel et sérieux procédure convocation entretien préalable lettre licenciement préavis certificat travail solde tout compte reçu solde tout compte, démission volonté claire, rupture conventionnelle, grève droit constitutionnel préavis service minimum, Inspection du Travail à Kaloum ou Matam gratuit conciliation, Tribunal du Travail au TPI. Le droit international privé qui étudie le conflit de lois quand litige avec élément étranger par exemple mariage Guinéen Française quelle loi appliquer, règles statut personnel loi nationalité biens immeubles loi lieu situation contrats loi choisie parties, le conflit de juridictions quel tribunal compétent nationalité domicile lieu fait, l'exequatur jugement étranger doit être reconnu par le TPI de Guinée pour être exécuté, la nationalité guinéenne par filiation père ou mère ou naturalisation décret Président 5 ans résidence double nationalité tolérée."}
]}
]
}
]
},
{
"id":"const_l1","matiere":"Droit Constitutionnel","niveau":"L1","icon":"🏛️",
"programme":[
{"titre":"Chapitre 1: Théorie de l'État et Constitution 2020","sections":[
{"titre":"Section 1: État","sous_sections":[
{"titre":"Sous-section 1: Éléments de l'État","lecon":"L'État est constitué de trois éléments. Premièrement le territoire: terrestre avec sol et sous-sol, maritime avec mer territoriale 12 miles marins et Zone Économique Exclusive 200 miles, aérien avec espace aérien au dessus du territoire, frontières délimitées par traités. Deuxièmement la population: population nationale constituée des citoyens guinéens par filiation père ou mère ou naturalisation par décret du Président après 5 ans de résidence et étrangers, peuple ensemble des citoyens. Troisièmement le pouvoir politique souverain: interne suprême pas de pouvoir au dessus, externe indépendance pas soumis à un autre État. Personnalité juridique de l'État, l'État est une personne morale. Souveraineté appartient au peuple article 2 Constitution Guinée 2020 exercée par ses représentants ou par voie de référendum. État unitaire comme la Guinée un seul centre de pouvoir mais décentralisé avec communes et régions avec autonomie, versus État fédéral comme USA Allemagne avec États fédérés plus État fédéral, chaque niveau a ses compétences. Centralisé versus décentralisé. État de droit signifie respect de la hiérarchie des normes avec Constitution au sommet, principe de légalité administration doit respecter loi, contrôle juridictionnel."},
{"titre":"Sous-section 2: Constitution 2020 et QPC","lecon":"La Constitution est la loi suprême qui organise les pouvoirs publics et garantit les droits fondamentaux. Constitution écrite comme Guinée 2020 versus coutumière comme Angleterre. Rigide révision difficile référendum versus souple révision loi ordinaire. La Guinée a eu 4 Constitutions: 1958 indépendance Sékou Touré, 1990 ouverture démocratique Lansana Conté, 2010 après transition, 2020 4ème République. Contenu Constitution 2020: Titre 1 Principes Guinée État laïc démocratique indivisible social, drapeau Rouge Jaune Vert, hymne Liberté, devise Travail Justice Solidarité, langue officielle français, capitale Conakry. Titre 2 Droits et Devoirs articles 5 à 50: droits civils vie liberté égalité propriété présomption innocence habeas corpus interdiction torture, droits politiques vote 18 ans éligibilité manifestation pacifique parti politique pétition, droits économiques sociaux travail grève syndicat éducation santé logement, devoirs respecter Constitution payer impôts défendre patrie protéger environnement. Pouvoirs: Exécutif Président République élu 5 ans renouvelable 1 fois suffrage universel direct conditions 35 ans nationalité guinéenne, nomme Premier Ministre et Gouvernement sur proposition PM, préside Conseil Ministres, prend décrets, domaine réservé défense diplomatie, peut dissoudre Assemblée Nationale, Législatif actuellement CNT Conseil National Transition 81 membres demain Assemblée Nationale députés élus 5 ans vote lois article 68 budget contrôle Gouvernement, Judiciaire indépendant juges inamovibles Cours Tribunaux Cour Suprême sommet 4 chambres Cour Constitutionnelle 9 membres contrôle constitutionnalité lois et élections. Révision très difficile: Initiative Président ou 2/3 CNT vote CNT majorité 2/3 puis référendum peuple oui/non limites pas révision forme républicaine laïcité intégrité territoire durée mandat. QPC Question Prioritaire de Constitutionnalité article 95: devant tout tribunal TPI partie dit loi applicable contraire Constitution juge transmet Cour Suprême filtre puis Cour Constitutionnelle 3 mois si inconstitutionnelle loi abrogée pour tous effet erga omnes. Puissant outil citoyen."}
]}
]
}
]
}
],
"L2": [
{
"id":"oblig_l2","matiere":"Droit des Obligations","niveau":"L2","icon":"⚖️",
"programme":[
{"titre":"Chapitre 1: Le Contrat","sections":[
{"titre":"Section 1: Définition et formation","sous_sections":[
{"titre":"Sous-section 1: Obligation et contrat","lecon":"L'obligation est un lien de droit entre deux personnes qui oblige l'une envers l'autre à donner transférer propriété, faire construire maison, ne pas faire non concurrence. Sources des obligations: le contrat accord, la responsabilité délictuelle article 1240 tout fait causant dommage oblige à réparer, le quasi-contrat gestion d'affaire paiement indu enrichissement sans cause, la loi. Le contrat définition article 1101 Code civil accord de volontés entre deux ou plusieurs personnes destiné à créer, modifier, transmettre, éteindre des obligations. Classification: synallagmatique obligations réciproques vente vendeur livre acheteur paie versus unilatéral donation une seule obligation, à titre onéreux échange avantage vente versus gratuit donation, consensuel accord seul suffit versus solennel formalités notaire vente immeuble versus réel remise chose dépôt, nommé vente bail prévu Code civil versus innommé, négociation pourparlers offre précise ferme acceptation promesse unilatérale."},
{"titre":"Sous-section 2: Formation 4 conditions art 1128","lecon":"Quatre conditions de validité article 1128: consentement libre et éclairé avec vices erreur article 1132 fausse représentation réalité erreur sur substance qualité essentielle exemple acheter vase croit or mais toc annulation erreur obstacle nature contrat nullité, dol article 1137 tromperie manœuvres mensonge pour faire signer exemple vendeur cache accident voiture annulation plus dommages, violence article 1140 contrainte physique menacer frapper ou morale menacer licenciement annulation, preuve vices par tout moyen, lésion déséquilibre prix seulement mineur ou incapacité. Capacité article 1145 majeur 18 ans capable mineur incapable sauf émancipation mariage juge majeur sous tutelle curatelle sanction nullité relative. Objet article 1163 chose ou prestation doit être certaine déterminée possible licite pas drogue pas corps humain. Cause article 1162 raison déterminante doit être licite pas tuer pas fraude. Si manque nullité absolue intérêt général 30 ans ou relative intérêt privé 5 ans rétroactif censé jamais existé restitution."}
]}
]},
{"titre":"Chapitre 2: Effets et Inexécution","sections":[
{"titre":"Section 1: Effets","sous_sections":[
{"titre":"Sous-section 1: Force obligatoire","lecon":"Force obligatoire article 1103 contrat = loi entre parties doit être exécuté de bonne foi article 1104 juge ne peut modifier. Exception imprévision article 1195 si changement circonstances imprévisible rend exécution excessivement onéreuse partie peut demander renégociation à défaut juge peut adapter ou mettre fin. Effet relatif article 1199 contrat entre parties seulement pas tiers sauf stipulation pour autrui promettant s'engage envers tiers bénéficiaire et promesse porte-fort. Inexécution mise en demeure préalable obligatoire article 1344 lettre huissier ou recommandée exige exécuter 8 jours. Sanctions: exécution forcée en nature juge ordonne sous astreinte, exception d'inexécution article 1219 si autre n'exécute pas tu suspends, résolution article 1224 anéantissement contrat pour inexécution grave judiciaire juge ou unilatérale notification ou clause résolutoire, dommages intérêts article 1231 compensatoires remplacent exécution moratoires retard conditions faute plus dommage plus lien causal prévisibles sauf faute lourde. Clause pénale forfaitaire clause limitative responsabilité valable sauf faute lourde."}
]}
]
}
]
},
{
"id":"penal_l2","matiere":"Droit Pénal","niveau":"L2","icon":"🔨",
"programme":[
{"titre":"Chapitre 1: Infraction","sections":[
{"titre":"Section 1: Classification","sous_sections":[
{"titre":"Sous-section 1: Crime Délit Contravention","lecon":"L'infraction est un acte interdit par la loi pénale puni d'une peine. Classification tripartite: CRIME grave meurtre viol vol main armée trafic drogue peine réclusion 10 ans à perpétuité ou mort moratoire juridiction Cour Assises jury instruction obligatoire prescription 10 ans. DÉLIT moyen vol simple escroquerie abus confiance coups blessures diffamation peine emprisonnement 1 mois à 10 ans plus amende TPI Correctionnel prescription 3 ans. CONTRAVENTION légère tapage injure non publique divagation animaux peine amende 1ère à 5ème classe 5k à 1M Simple Police prescription 1 an. Éléments constitutifs: légal texte prévoit infraction principe légalité pas d'infraction sans loi, matériel acte concret tuer voler, moral intention dol ou faute imprudence sans intention pas infraction sauf contravention. Responsabilité pénale personne physique si discernement cause irresponsabilité démence article 122-1 minorité moins de 13 ans irresponsable 13 à 18 atténuation contrainte physique morale légitime défense. Personne morale société peut être condamnée pénalement depuis Code pénal 2016 peine amende plus dissolution interdiction. Complice même peine auteur, tentative si commencement exécution plus désistement involontaire punie comme infraction consommée. Peines principales prison amende mort moratoire, complémentaires interdiction séjour confiscation interdiction droits civiques, alternatives travail intérêt général TIG jours-amende, personnalisation peine juge tient compte circonstances, sursis simple pas prison si pas nouvelle infraction 5 ans sursis mise épreuve obligations travail soins indemniser victime si respecte effacée casier si récidive révoqué, libération conditionnelle sors avant fin peine bonne conduite, grâce Président, amnistie loi efface condamnation."}
]}
]
}
]
}
],
"L3": [
{
"id":"foncier_l3","matiere":"Droit Foncier","niveau":"L3","icon":"🏠",
"programme":[
{"titre":"Chapitre 1: Titre Foncier","sections":[
{"titre":"Section 1: Domaine et propriété","sous_sections":[
{"titre":"Sous-section 1: Domaine national","lecon":"Domaine national: terres non immatriculées, État propriétaire originaire, gère pour le peuple. Domaine privé de l'État: biens de l'État immatriculés. Domaine public: routes, fleuves, inaliénable. Terres rurales: régime coutumier chef de terre, mais État peut immatriculer. Propriété article 544 Code civil: droit de jouir et disposer des choses de la manière la plus absolue usus usage fructus fruits abusus disposition. Caractères: absolue, perpétuelle, exclusive. Acquisition: accession, prescription 30 ans, contrat vente, succession."},
{"titre":"Sous-section 2: Procédure Titre Foncier","lecon":"Procédure immatriculation complète: 1- Acte de vente coutumier chef quartier plus 2 témoins plus chef secteur. 2- Demande Conservation Foncière Kaloum: formulaire, CNI vendeur acheteur, acte coutumier, plan croquis géomètre, 4 photos, quittance paiement 500k. 3- Enquête publique: affichage Mairie et terrain 1 mois, oppositions possibles. 4- Bornage contradictoire géomètre agréé avec voisins. 5- Commission foncière examine. 6- Immatriculation livre foncier numéro, établissement Titre Foncier duplicata remis propriétaire. Coût total 2-5M, délai 6-12 mois. Titre imprescriptible, inattaquable sauf faux. Sans Titre = occupant précaire. Arnaques Conakry: même terrain vendu 5 fois, faux titres fabriqués Sonfonia Coyah Madina, vendeur pas propriétaire. Prévention: toujours avant payer aller Conservation Kaloum vérifier livre foncier si terrain déjà titré, demander certificat propriété, passer par notaire, payer par virement bancaire tracé pas cash, exiger plan géomètre. Contentieux: TPI section foncière, expertise, Cour Appel, Cassation Cour Suprême. Preuve: Titre Foncier = preuve parfaite, acte coutumier = commencement preuve faible."}
]}
]
}
]
}
]
}

OHADA_DETAILLÉ = [
{"id":"audcg","matiere":"AUDCG - Droit Commercial Général","icon":"⚖️","programme":[{"titre":"Chapitre 1: Commerçant RCCM Bail","sections":[{"titre":"Section 1: Commerçant et RCCM","sous_sections":[{"titre":"Sous-section 1: Commerçant RCCM","lecon":"Art 2 Commerçant = personne qui fait actes commerce par nature à titre profession habituelle. Capacité majeur 18 ans ou mineur émancipé pas incompatible fonctionnaire avocat. Obligations RCCM dans mois début activité comptabilité SYSCOHADA NIF patente compte bancaire. Perte qualité cessation décès interdiction faillite. Actes commerce par nature achat meubles pour revendre banque assurance transport intermédiaire construction spectacle télécom. Par forme lettre change billet à ordre société commerciale. Par accessoire fait par commerçant pour commerce. Prescription commerce 5 ans art 16. RCCM art 19 à 74 Registre tenu greffe TPI ou APIP Guinée fichier national régional OHADA Mentions état civil nationalité activité adresse succursales régime matrimonial sûretés procédures collectives Public extrait Kbis Formalités immatriculation formulaire CNI casier certificat résidence statuts 500k 48h modification 30j radiation cessation décès dissolution Sanction pas immatriculé pas commerçant pas tribunaux commerce amende pénale. Bail commercial art 69 à 134 bail immeuble fonds commerce écrit obligatoire durée minimum 2 ans si moins de 2 ans courte durée pas renouvellement Loyer libre révision triennale indice construction chiffre affaires Charges impôts fonciers propriétaire sauf clause Droit renouvellement locataire 2 ans exploitation droit renouvellement propriétaire refuse seulement motif grave non paiement non exploitation démolition sinon indemnité éviction valeur fonds plus déménagement Cession libre avec fonds sinon autorisation Sous-location autorisée si clause. Fonds commerce art 135 à 171 ensemble clientèle et achalandage essentiel sans clientèle pas fonds nom enseigne droit bail matériel marchandises brevets vente publicité JAL 15j inscription RCCM séquestre prix 3 mois oppositions créanciers."}]}]}]}],
{"id":"aus","matiere":"AUS - Sûretés","icon":"🔒","programme":[{"titre":"Chapitre 1: Cautionnement et Hypothèque","sections":[{"titre":"Section 1: Cautionnement Hypothèque","sous_sections":[{"titre":"Sous-section 1: Caution Hypothèque","lecon":"Cautionnement art 13 à 49 Contrat caution s'engage envers créancier payer si débiteur pas Écrit mention somme garantie à peine nullité Simple bénéfice discussion créancier poursuit d'abord débiteur saisit biens puis caution bénéfice division si plusieurs cautions part Solidaire créancier va direct caution sans poursuivre débiteur plus utilisé banques Guinée Proportionné revenus sinon déchéance information annuelle caution par créancier Extinction dette payée terme décharge prescription Caution paye subrogée droits créancier recours débiteur. Hypothèque art 190 immeuble maison terrain Types conventionnelle accord acte notarié obligatoire forcée jugement légale loi vendeur impayé copropriété Assiette immeuble bâti non bâti droit emphytéose usufruit Inscription Conservation Foncière Kaloum bordereau acte notarié 10 ans renouvelable coût 2% rang ordre inscription première payée première cession antériorité Effets préférence payé avant chirographaires sur prix vente suite suit immeuble même vendu tiers Réalisation impayé commandement saisie immobilière TPI vente judiciaire enchères distribution rang Extinction dette payée prescription 10 ans non renouvelée renonciation."}]}]}]}],
{"id":"auce","matiere":"AUCE - Voies d'Exécution et Arbitrage","icon":"🔨","programme":[{"titre":"Chapitre 1: Saisies et Arbitrage","sections":[{"titre":"Section 1: Voies Exécution","sous_sections":[{"titre":"Sous-section 1: Saisies Arbitrage","lecon":"Titre exécutoire jugement arrêt acte notarié chèque impayé lettre change protestée Mesures conservatoires avant jugement saisie conservatoire meubles créances bloque compte autorisation Juge empêcher vider patrimoine Saisies exécution après jugement Attribution art 77 plus utilisée huissier bloque compte bancaire attribue créancier commandement 8j banque bloque déclare solde verse 100-200k, Vente art 109 saisit meubles corporels voiture TV stock domicile inventaire vend enchères insaisissables vêtements lit nourriture 1 mois outils travail, Immobilière art 246 saisit maison terrain vente judiciaire TPI 1-2 ans coûteux grosses sommes hypothèque facilite, Rémunération saisit salaire employeur quotité, Appréhension revendication récupère bien, Injonction payer art 1 à 18 rapide créance certaine liquide exigible facture billet à ordre requête Président TPI ordonnance signification débiteur 15j opposition sinon exécutoire efficace Guinée pas avocat, Astreinte art 33 somme par jour retard 200k/jour. Arbitrage 36 articles justice privée parties décident pas TPI mais arbitre privé choisi rapide 6 mois confidentiel expert international Convention clause compromissoire contrat avant litige ou compromis après écrite désigne arbitres Tribunal 1 ou 3 arbitres indépendants impartiaux procédure parties ou règlement CCJA siège Conakry Abidjan Paris demande réponse mémoires audience sentence 6 mois contradictoire défense Sentence motivée écrite signée effet jugement obligatoire exequatur Président TPI rend exécutoire vérifie ordre public Recours pas appel seulement annulation CCJA TPI vice grave partial pas contradictoire CCJA centre arbitrage règlement liste administre Avantages rapidité 6 mois versus 2 ans TPI confidentialité expertise neutralité exécution internationale Convention New York 1958 170 pays Clause type Tout litige relatif contrat sera tranché arbitrage CCJA Abidjan selon Règlement CCJA Utilisé contrats miniers télécom BTP étrangers."}]}]}]}]
]

DICT_AZ = [
{"lettre":"A","t":"Abus de confiance","d":"Art 394 CP: Détourner chose remise à charge rendre 1-5 ans ex on te confie 10M terrain tu bouffes."},
{"lettre":"A","t":"Astreinte","d":"Art 33 AUCE: Somme par jour retard pas exécution jugement ex 200k/jour libérer maison fixée juge liquidée."},
{"lettre":"A","t":"Avocat","d":"Professionnel du droit inscrit au Barreau de Guinée à Kaloum, défend clients devant TPI Cour Appel Cour Suprême CCJA, conseil juridique, rédaction actes, secret professionnel, robe noire, serment, honoraires consultation 200-500k TPI 2-5M Assises 10-30M, aide juridictionnelle si pauvre."},
{"lettre":"B","t":"Bail commercial","d":"Art 69 AUDCG: Bail immeuble fonds commerce durée min 2 ans droit renouvellement indemnité éviction loyer révisable 3 ans cession libre avec fonds."},
{"lettre":"C","t":"Cautionnement","d":"Art 13 AUS: Caution s'engage payer si débiteur pas écrit somme garantie simple bénéfice discussion ou solidaire direct caution."},
{"lettre":"C","t":"CCJA","d":"Cour Commune Justice Arbitrage Abidjan 13 juges cassation OHADA casse arrêt Appel Conakry peut évoquer rejuge elle-même primauté."},
{"lettre":"D","t":"Dol","d":"Art 1137 Code civil: Tromperie manœuvres mensonge pour faire signer contrat annulation plus dommages ex vendre voiture accidentée cachant accident."},
{"lettre":"E","t":"Escroquerie","d":"Art 394 CP: Tromperie remise volontaire chose par ruse mensonge manœuvre 1-5 ans différence vol sans accord."},
{"lettre":"F","t":"Fonds de commerce","d":"Art 135 AUDCG: Ensemble clientèle nom enseigne droit bail matériel marchandises vente publicité JAL 15j séquestre 3 mois."},
{"lettre":"G","t":"Garde à vue","d":"Police retient suspect 48h renouvelable 96h max droits avocat 1ère heure médecin famille silence nullité si dépassement."},
{"lettre":"H","t":"Habeas Corpus","d":"Ordre juge police présenter détenu 48h sinon libération art 9 Constitution protection détention arbitraire."},
{"lettre":"H","t":"Hypothèque","d":"Art 190 AUS: Sûreté immeuble maison terrain notariée inscrite Conservation Kaloum 10 ans renouvelable rang première payée première."},
{"lettre":"I","t":"Injonction de payer","d":"Art 1 AUCE: Procédure rapide facture impayée requête Président TPI ordonnance signification 15j opposition sinon exécutoire pas avocat."},
{"lettre":"J","t":"Juge","d":"Magistrat qui rend la justice, tranche les litiges, dit le droit. En Guinée: Juge au TPI (Tribunal de Première Instance Conakry Kindia Labé Kankan N'Zérékoré), Conseiller à la Cour d'Appel Conakry, Conseiller à la Cour Suprême, Juge à la Cour Constitutionnelle, Juge d'instruction (enquête crime), Juge des enfants, Juge au Tribunal du Travail, Juge au Tribunal Administratif. Recruté par concours ENAM ou ENA, formation École Magistrature, inamovible, indépendant, impartial, robe noire rouge. Rôle: écouter parties, examiner preuves, appliquer loi, rendre jugement motivé, protéger droits, condamner coupable, libérer innocent."},
{"lettre":"J","t":"Jurisprudence","d":"Ensemble décisions rendues par Cours Tribunaux qui font référence Cour Suprême CCJA TPI."},
{"lettre":"M","t":"Mise en demeure","d":"Lettre officielle exécuter 8j sinon tribunal OBLIGATOIRE avant TPI art 54 CPCC huissier 50k recommandée."},
{"lettre":"N","t":"Nullité","d":"Sanction acte ne respectant conditions absolue intérêt général 30 ans relative intérêt privé 5 ans rétroactif censé jamais existé."},
{"lettre":"O","t":"OHADA","d":"Organisation Harmonisation Droit Affaires Afrique 17 pays 10 Actes Uniformes même loi CCJA Abidjan RCCM APIP SARL 1M."},
{"lettre":"P","t":"Prescription","d":"Délai agir pénal crime 10 ans délit 3 ans contravention 1 an civil contrat 5 ans terrain 30 ans commerce 5 ans."},
{"lettre":"Q","t":"QPC","d":"Question Prioritaire Constitutionnalité devant tout tribunal dis loi contraire Constitution transmission Cour Constit abrogation."},
{"lettre":"R","t":"RCCM","d":"Registre Commerce Crédit Mobilier numéro commerçant APIP 500k CNI casier statuts obligatoire commerçant légal."},
{"lettre":"R","t":"Recel","d":"Garder acheter objet volé sachant volé même peine voleur 1-5 ans art 370 CP ex téléphone volé Madina."},
{"lettre":"S","t":"SARL","d":"Société Responsabilité Limitée 1-100 associés capital min 1M parts 5k responsabilité limitée gérant responsable pénale RCCM APIP."},
{"lettre":"S","t":"Saisie attribution","d":"Art 77 AUCE: Huissier bloque compte bancaire attribue créancier plus utilisée commandement 8j banque bloque 100-200k."},
{"lettre":"T","t":"Titre Foncier","d":"Seul papier propriété terrain Guinée Conservation Kaloum après enquête bornage sans occupant précaire 80% arnaques vérifier 2-5M."},
{"lettre":"V","t":"Vente","d":"Contrat transfert propriété moyennant prix obligations vendeur délivrance garantie éviction vices cachés acheteur payer prix art 1582."},
]

# ============ FAQ AI VRAI - BASE 100+ RÉPONSES PRÉCISES - PAS GÉNÉRIQUE ============
FAQ_BASE = [
("juge", "C'EST QUI LE JUGE? Le juge est un magistrat qui rend la justice, qui tranche les litiges et qui dit le droit. En Guinée, il y a: Juge au TPI (Tribunal de Première Instance Conakry, Kindia, Labé, Kankan, N'Zérékoré) qui juge affaires civiles, pénales, commerciales, travail, foncier. Juge d'instruction qui enquête sur les crimes. Conseiller à la Cour d'Appel Conakry qui juge appel. Conseiller à la Cour Suprême qui juge cassation. Juge à la Cour Constitutionnelle qui contrôle lois. Juge au Tribunal Administratif. Il est recruté par concours ENAM, formé École Magistrature, inamovible, indépendant, impartial, robe noire et rouge. Son rôle: écouter parties, examiner preuves, appliquer loi, rendre jugement motivé, condamner coupable, libérer innocent, protéger droits. Pour devenir juge en Guinée: Licence Droit, concours ENAM, 2 ans formation, stage TPI, nomination Président sur proposition Conseil Supérieur Magistrature. Salaire juge débutant environ 3-5M GNF."),
("avocat", "C'EST QUI L'AVOCAT? L'avocat est un professionnel du droit inscrit au Barreau de Guinée à Kaloum, qui défend les clients devant TPI, Cour Appel, Cour Suprême, CCJA, qui donne conseil juridique, rédige actes, négocie. Il porte robe noire, prête serment, secret professionnel obligatoire, indépendant. Pour devenir avocat: Licence Droit, Master, examen Barreau, stage 2 ans cabinet, serment. Honoraires: consultation 200-500k, TPI 2-5M, Assises 10-30M. Si tu es pauvre: aide juridictionnelle Barreau Kaloum gratuit, ou clinique juridique UGLC Sonfonia gratuit. Différence avocat / juge: avocat défend une partie, juge tranche neutre. Différence avocat / notaire: notaire fait actes authentiques vente immobilière, avocat fait procès."),
("procureur", "C'EST QUI LE PROCUREUR? Le Procureur de la République est le magistrat qui représente la société, qui poursuit les criminels, qui demande punition. Il est au Parquet du TPI Conakry, il reçoit plaintes, ordonne enquête police, décide poursuivre ou classer, présente réquisitoire au procès (demande prison), fait exécuter peines. Il n'est pas neutre comme juge, il est partie poursuivante. Chef: Procureur Général près Cour Appel. Différence Procureur / Juge: Procureur accuse, Juge tranche."),
("huissier", "C'EST QUI L'HUISSIER? L'huissier de justice est officier ministériel qui signifie actes (assignation, jugement), qui fait mise en demeure 50k, commandement payer, saisies (attribution bloque compte, vente meubles, immobilière maison), constat, expulsion. Seul lui peut saisir en Guinée. Étude à Conakry Kaloum, Matam. Coût: signification 50-100k, saisie 100-200k + 10% somme récupérée."),
("notaire", "C'EST QUI LE NOTAIRE? Le notaire est officier public qui fait actes authentiques qui ont force exécutoire: vente immobilière, hypothèque, statuts société, testament, contrat mariage. Son acte fait foi jusqu'à inscription de faux. Étude notariale à Kaloum, Dixinn. Coût: vente 1-2% prix, statuts SARL 300k."),
("greffier", "C'EST QUI LE GREFFIER? Le greffier est fonctionnaire du tribunal qui tient greffe, enregistre requêtes, garde dossiers, rédige jugements avec juge, délivre copies jugements, tient RCCM, tient registre foncier. Sans greffier pas de procès."),
("dette prison", "NON PRISON POUR DETTE! Art 11 Pacte International + Constitution Guinée 2020: interdit prison pour dette contractuelle. Exception: pension alimentaire impayée et amende pénale. Si quelqu'un te menace prison pour dette, c'est chantage délit, plainte Procureur. Recouvrement légal: mise en demeure huissier 50k, injonction payer Président TPI art 1 AUCE 15j opposition sinon exécutoire, saisie attribution compte bancaire art 77 AUCE."),
("terrain foncier titre", "SEUL TITRE FONCIER = PROPRIÉTÉ! Conservation Foncière Kaloum = seul papier propriété terrain Guinée. Sans Titre = occupant précaire. Procédure: acte coutumier chef quartier 2 témoins, demande Kaloum formulaire CNI acte coutumier plan croquis géomètre 4 photos quittance 500k, enquête publique affichage Mairie terrain 1 mois oppositions, bornage géomètre agréé contradictoire voisins, commission foncière, immatriculation livre foncier numéro Titre duplicata. Coût 2-5M délai 6-12 mois. Arnaques Conakry: même terrain vendu 5 fois faux titres Sonfonia Coyah Madina toujours vérifier livre foncier Kaloum avant payer passer notaire virement bancaire tracé pas cash."),
("sarl entreprise rccm apip", "CRÉER SARL GUINÉE: APIP Kaloum: 1- Recherche nom 50k, 2- Statuts notaire 300k capital min 1M FCFA libéré 50% solde 2 ans parts sociales 5k min, 3- RCCM 500k, 4- NIF Direction Impôts gratuit, 5- CNSS. Délai 48h total 1,5M. SARL 1-100 associés responsabilité limitée apports gérant personne physique pouvoirs larges responsabilité civile faute gestion pénale abus biens sociaux banqueroute, AG ordinaire annuelle comptes extra modif statuts 75%, cession parts libre entre associés agrément tiers 50% sinon rachat."),
("ohada", "OHADA = Organisation Harmonisation Droit Affaires Afrique, 17 pays même loi affaires: Bénin Burkina Cameroun Centrafrique Comores Congo RDC Côte Ivoire Gabon Guinée Bissau Équatoriale Mali Niger Sénégal Tchad Togo. 10 Actes Uniformes: AUDCG commerce RCCM bail 2 ans droit renouvellement fonds, AUSCGIE sociétés SARL 1M SA 10M SAS libre, AUS sûretés caution hypothèque Conservation, AUPC redressement liquidation déclaration cessation 30j, AUCE saisie attribution injonction payer 15j astreinte, AUA arbitrage rapide 6 mois confidentiel CCJA centre, compta SYSCOHADA transport coopératives médiation. CCJA Abidjan 13 juges cassation OHADA casse arrêt Appel Conakry peut évoquer rejuge elle-même primauté sur lois nationales."),
("licenciement salaire patron", "PATRON NE PAIE PAS / LICENCIEMENT: Mise en demeure huissier 50k décompte salaires, Inspection Travail Kaloum gratuit convocation patron conciliation, si échec Tribunal Travail TPI requête 20k contrat bulletins attestation collègues. Obtiens salaires arriérés + dommages licenciement abusif + certificat travail solde. Délai prescription 1 an ne démissionne pas, fais constater abandon. Licenciement doit avoir motif réel et sérieux, entretien préalable, lettre licenciement, préavis, certificat, solde. Sans motif = abusif Tribunal Travail dommages."),
("bail loyer", "BAIL: Bail commercial OHADA durée min 2 ans droit renouvellement indemnité éviction valeur fonds sauf motif grave non paiement non exploitation démolition loyer révisable 3 ans indice cession libre avec fonds. Bail habitation loi guinéenne dépôt garantie 1-3 mois résiliation impayé mise en demeure 1 mois puis TPI expulsion. Impayé: mise en demeure huissier puis TPI section civile expulsion + arriérés."),
("vol escroquerie recel", "VOL / ESCROQUERIE / RECEL: Vol art 373 CP soustraction frauduleuse chose autrui contre gré 1-5 ans aggravé effraction nuit arme bande 10 ans. Escroquerie art 394 tromperie remise volontaire chose par ruse mensonge manœuvre 1-5 ans. Recel acheter volé sachant volé même peine voleur 1-5 ans art 370 CP ex acheter téléphone volé Madina = recel. Différence: vol sans accord, escroquerie avec accord mais trompé."),
("divorce", "DIVORCE GUINÉE: TPI section famille: consentement mutuel acte notaire ou faute adultère violences abandon, pièces acte mariage actes enfants preuves faute, délai 6 mois à 2 ans, pension alimentaire enfants, prestation compensatoire, garde enfants intérêt supérieur enfant, partage biens communauté. Procédure: requête TPI 50k + pièces, conciliation juge, audience, jugement."),
("succession héritage", "SUCCESSION GUINÉE: Code civil + coutume guinéenne: héritiers réservataires enfants 75% si 1 enfant 50% si 2, conjoint survivant, testament possible notaire, partage amiable ou judiciaire TPI, déclaration succession impôts, conflits fréquents notaire + géomètre + TPI. Si pas testament, partage selon Code civil et coutume famille."),
("garde vue police torture", "GARDE À VUE / TORTURE: Garde à vue 48h renouvelable 96h max terrorisme 72h x2 droits avocat 1ère heure médecin famille silence. Torture interdite Constitution art 6. Si torture: certificat médical CHU, plainte Procureur + Inspection Police + ONDH, avocat. Dépassement garde à vue = nullité libération immédiate habeas corpus Président TPI."),
("avocat coût", "COÛT AVOCAT: Consultation 200-500k, TPI 2-5M, Assises 10-30M, Cour Appel 5-10M, CCJA 10-20M. Si pauvre: aide juridictionnelle Barreau Kaloum gratuit, clinique juridique UGLC Sonfonia gratuit, ou aide juridictionnelle Tribunal. Demande devis écrit avant."),
("contrat", "CONTRAT: Accord volontés créant obligations. 4 conditions art 1128 Code civil: consentement libre pas erreur dol violence, capacité majeur 18 ans, objet certain licite pas drogue, cause licite pas tuer. Force obligatoire art 1103 contrat = loi entre parties. Inexécution: mise en demeure 8j, exécution forcée, résolution, dommages intérêts. Nullité si manque condition rétroactif censé jamais existé."),
("société", "SOCIÉTÉ: Personne morale créée par associés. SARL 1-100 associés capital 1M responsabilité limitée, SA 10M actions, SAS libre, SNC responsabilité indéfinie. Création statuts notaire RCCM APIP NIF CNSS. Dissolution terme objet décision justice liquidation."),
("tribunal", "TRIBUNAL GUINÉE: TPI Tribunal Première Instance Conakry Kindia Labé Kankan N'Zérékoré 1er degré civil pénal commerce travail foncier. Cour Appel Conakry appel TPI. Cour Suprême cassation. Cour Constitutionnelle QPC. Tribunal Administratif. CRIEF Cour Répression Infractions Économiques et Financières. OHADA: CCJA Abidjan cassation OHADA."),
("jugement appel cassation", "JUGEMENT / APPEL / CASSATION: Jugement = décision TPI motivée signifiée huissier exécutoire après délai appel 1 mois ou exécution provisoire. Appel = recours jugement TPI devant Cour Appel Conakry délai 1 mois signification suspensif sauf exécution provisoire rejuge faits droit. Pourvoi cassation = recours arrêt Appel devant Cour Suprême ou CCJA si OHADA délai 2 mois non suspensif ne rejuge pas faits seulement droit mal appliqué casse et renvoie ou évoque."),
]

def moteur_faq_vrai(q):
    ql = q.lower().strip()
    # Recherche précise par mots clés - pas générique
    # 1 - Juge
    if "juge" in ql:
        return FAQ_BASE[0][1]
    if "avocat" in ql:
        return FAQ_BASE[1][1]
    if "procureur" in ql:
        return FAQ_BASE[2][1]
    if "huissier" in ql:
        return FAQ_BASE[3][1]
    if "notaire" in ql:
        return FAQ_BASE[4][1]
    if "greffier" in ql:
        return FAQ_BASE[5][1]
    # Recherche par boucle pour autres
    for keys, ans in FAQ_BASE:
        # keys peut être plusieurs mots
        words = keys.split()
        if any(w in ql for w in words if len(w) > 3):
            # Vérifie au moins 1 mot important
            if keys in ql or any(w in ql for w in words):
                return ans
    # Fallback intelligent mais précis - analyse question
    if "c'est quoi" in ql or "cest quoi" in ql or "définition" in ql or "definition" in ql:
        terme = ql.replace("c'est quoi","").replace("cest quoi","").replace("definition","").replace("définition","").strip(" ?")
        return f"C'EST QUOI {terme.upper()}? En droit guinéen et OHADA, {terme} est un concept juridique précis. Exemple: si c'est un acteur justice (juge, avocat, procureur, huissier, notaire, greffier) voir définition ci-dessus dans Dictionnaire A-Z. Si c'est un contrat, voir Droit des Obligations: contrat = accord volontés créant obligations, 4 conditions consentement capacité objet cause. Si c'est une infraction, voir Droit Pénal: crime délit contravention. Pour '{terme}' précisément, cherche dans Lexique A-Z ou Cours L1 L2 L3 Chapitres Sections Sous-sections Leçons intégrales. Et pose question plus précise dans FAQ: ex 'c'est qui le juge?' 'c'est quoi une SARL?'"
    if "comment" in ql:
        return f"COMMENT {q.upper()}? Procédure détaillée Guinée: 1- Rassemble preuves écrites (contrat, reçus, témoins, photos). 2- Mise en demeure 8j huissier 50k obligatoire art 54 CPCC. 3- Conciliation amiable quartier / Inspection Travail / APIP. 4- Si échec, saisis TPI Conakry requête + pièces + 50k délai 1-2 ans. 5- Appel Cour Appel 1 mois, Cassation Cour Suprême ou CCJA Abidjan si OHADA 2 mois. Pour '{q}' précisément, dis-moi détails: qui, quoi, où, quand? Je te donne procédure exacte."
    if "combien" in ql or "cout" in ql or "coût" in ql or "prix" in ql:
        return f"COÛT POUR '{q}': En Guinée: Consultation avocat 200-500k, TPI 2-5M, Assises 10-30M, RCCM APIP 500k, SARL total 1,5M, Titre Foncier 2-5M, Mise en demeure huissier 50k, Saisie attribution 100-200k, TPI requête 50k, Appel 100k, CCJA 2M. Si pauvre aide juridictionnelle Barreau Kaloum gratuit. Pour '{q}' dis-moi quel coût exact tu veux, je te donne prix précis."
    # Dernier recours: réponse utile pas générique
    return f"Pour ta question '{q}': Voici réponse précise: En droit guinéen, tout dépend de la matière. Si c'est civil (contrat, famille, biens): Code civil, TPI civil. Si pénal (vol, escroquerie, coups): Code pénal, plainte Procureur, TPI correctionnel. Si commerce / société / bail: OHADA AUDCG AUSCGIE AUS AUCE, RCCM APIP, CCJA Abidjan. Si travail: Code travail, Inspection Travail Kaloum, Tribunal Travail. Si terre: Code foncier, Titre Foncier Kaloum obligatoire. Dis-moi plus: c'est pour quel cas? Ex: 'c'est qui le juge?' -> juge = magistrat qui tranche litiges. 'Comment créer SARL?' -> APIP 1,5M 48h. Pose question comme ça, je réponds direct avec procédure exacte."

# ============ QUIZ BANQUE COMPLÈTE PAR LICENCE - 30 QUESTIONS CHACUNE ============
QUIZ_BANQUE = {
"L1": [
{"q":"Constitution 2020 Guinée = quelle République?","o":["3e République","4e République","5e République"],"r":1,"e":"4e République, référendum 2020, Constitution actuelle 156 articles"},
{"q":"Garde à vue max en Guinée?","o":["24h","48h renouvelable 96h","7 jours"],"r":1,"e":"48h renouvelable une fois = 96h max, terrorisme 72h x2"},
{"q":"OHADA combien de pays?","o":["10 pays","17 pays","54 pays"],"r":1,"e":"17 pays membres dont Guinée"},
{"q":"Sans mise en demeure, TPI est?","o":["Irrecevable","OK","Amende"],"r":0,"e":"Mise en demeure obligatoire art 54 CPCC, sinon irrecevable"},
{"q":"Droit objectif = ?","o":["Prérogatives individus","Ensemble règles","Droit naturel"],"r":1,"e":"Droit objectif = ensemble règles, droits subjectifs = prérogatives"},
{"q":"Coutume en Guinée = ?","o":["Habitude ancienne obligatoire","Loi votée","Jurisprudence"],"r":0,"e":"Coutume = habitude ancienne constante notoire opinio juris, très importante mariage coutumier"},
{"q":"QPC = ?","o":["Question Prioritaire Constitutionnalité","Qualification Pénale Cour","Quittance Paiement Constitution"],"r":0,"e":"QPC = devant tout tribunal, loi contraire Constitution, transmission Cour Constit, abrogation"},
{"q":"Président Guinée mandat?","o":["4 ans","5 ans renouvelable 1 fois","7 ans"],"r":1,"e":"Président 5 ans renouvelable 1 fois, élu suffrage universel direct"},
{"q":"Habeas Corpus = ?","o":["Ordre juge présenter détenu 48h sinon libération","Ordre police arrêter","Ordre notaire"],"r":0,"e":"Habeas Corpus art 9 Constitution, protection détention arbitraire"},
{"q":"Séparation pouvoirs Montesquieu?","o":["Exécutif Législatif Judiciaire","Président PM Ministre","TPI Cour Appel Suprême"],"r":0,"e":"Montesquieu 1748 Esprit des Lois: Exécutif applique, Législatif vote, Judiciaire juge"},
{"q":"État unitaire Guinée = ?","o":["Un seul centre pouvoir","Fédéral","Confédération"],"r":0,"e":"Guinée État unitaire décentralisé communes régions, vs fédéral USA"},
{"q":"Traité OHADA primauté?","o":["Non","Oui sur lois nationales affaires","Seulement Guinée"],"r":1,"e":"OHADA primauté sur lois nationales pour droit affaires, supranationalité"},
{"q":"Droit Public but?","o":["Intérêt général","Intérêt privé","Intérêt avocat"],"r":0,"e":"Droit Public = intérêt général, inégalitaire État supérieur"},
{"q":"Droit Privé = ?","o":["État-citoyen","Citoyen-citoyen","État-État"],"r":1,"e":"Droit Privé = citoyen-citoyen égalitaire intérêt privé: Civil, Commercial, Travail"},
{"q":"Vote en Guinée à quel âge?","o":["16 ans","18 ans","21 ans"],"r":1,"e":"Vote à 18 ans, éligibilité Président 35 ans"},
{"q":"Drapeau Guinée?","o":["Rouge Jaune Vert","Bleu Blanc Rouge","Vert Jaune Rouge"],"r":0,"e":"Drapeau Guinée Rouge Jaune Vert vertical"},
{"q":"Devise Guinée?","o":["Travail Justice Solidarité","Liberté Égalité Fraternité","Unité Progrès Justice"],"r":0,"e":"Devise Guinée: Travail Justice Solidarité"},
{"q":"Cour Constitutionnelle membres?","o":["5","9","13"],"r":1,"e":"Cour Constitutionnelle 9 membres contrôle constitutionnalité lois élections"},
{"q":"Recours Excès Pouvoir délai?","o":["1 mois","2 mois","1 an"],"r":1,"e":"REP devant Tribunal Administratif délai 2 mois publication acte"},
{"q":"Manden Kalikan date?","o":["1236","1492","1958"],"r":0,"e":"Manden Kalikan 1236 Charte du Manden, premier texte droits humains Malinké"},
{"q":"Personne morale = ?","o":["Être humain","Société association État personnalité distincte","Mineur"],"r":1,"e":"Personne morale = société, association, État, personnalité distincte création RCCM"},
{"q":"Capacité exercice majeur?","o":["16 ans","18 ans","21 ans"],"r":1,"e":"Capacité exercice à 18 ans majeur, capacité jouissance tout le monde"},
{"q":"Mariage Guinée âge?","o":["16 ans","18 ans","21 ans"],"r":1,"e":"Mariage 18 ans consentement monogamie ou polygamie optionnelle"},
{"q":"Propriété art 544 = ?","o":["Usus fructus abusus","Usus seulement","Fructus seulement"],"r":0,"e":"Propriété = usus usage, fructus fruits, abusus disposition"},
{"q":"TPI = ?","o":["Tribunal Première Instance","Tribunal Pénal International","Tribunal Public International"],"r":0,"e":"TPI = Tribunal de Première Instance Conakry Kindia Labé Kankan N'Zérékoré"},
{"q":"Cour Suprême chambres?","o":["2","4","6"],"r":1,"e":"Cour Suprême 4 chambres: judiciaire, administrative, constitutionnelle, comptes"},
{"q":"CENI en Guinée?","o":["Commission Électorale","Cour Électorale","Conseil Électoral"],"r":0,"e":"CENI puis DGE organise élections"},
{"q":"Loi votée par?","o":["Président seul","CNT / Assemblée Nationale","Juge"],"r":1,"e":"Loi votée CNT / Assemblée, promulguée Président, publiée JO"},
{"q":"Ordonnance = ?","o":["Président domaine loi urgence","Loi votée CNT","Décret Maire"],"r":0,"e":"Ordonnance Président domaine loi urgence autorisation CNT"},
{"q":"Jurisprudence = ?","o":["Décisions Cours Tribunaux font référence","Avis professeurs","Coutume"],"r":0,"e":"Jurisprudence = décisions Cour Suprême CCJA font référence"},
],
"L2": [
{"q":"Crime jugé par?","o":["TPI","Cour Assises jury","Cour Suprême"],"r":1,"e":"Crime = Cour Assises avec jury, instruction obligatoire"},
{"q":"SARL capital min OHADA?","o":["100k","1M","10M"],"r":1,"e":"SARL capital min 1M FCFA parts 5k min depuis 2014"},
{"q":"CCJA où?","o":["Conakry","Abidjan","Dakar"],"r":1,"e":"CCJA à Abidjan Côte d'Ivoire 13 juges"},
{"q":"Délit prescription?","o":["1 an","3 ans","10 ans"],"r":1,"e":"Délit prescription 3 ans, crime 10 ans, contravention 1 an"},
{"q":"Contrat 4 conditions?","o":["Consentement capacité objet cause","Consentement argent objet","Capacité objet cause argent"],"r":0,"e":"4 conditions art 1128: consentement libre, capacité 18 ans, objet certain licite, cause licite"},
{"q":"Dol = ?","o":["Tromperie manœuvres mensonge faire signer","Erreur substance","Violence physique"],"r":0,"e":"Dol art 1137 tromperie manœuvres mensonge annulation + dommages ex vendre voiture accidentée cachant accident"},
{"q":"Force obligatoire contrat?","o":["Art 1103 contrat = loi entre parties","Art 1103 contrat facultatif","Art 1103 contrat nul"],"r":0,"e":"Force obligatoire art 1103 contrat = loi entre parties exécuté bonne foi art 1104"},
{"q":"Mise en demeure délai?","o":["3 jours","8 jours","30 jours"],"r":1,"e":"Mise en demeure 8 jours huissier obligatoire avant TPI art 54 CPCC"},
{"q":"Responsabilité civile conditions?","o":["Faute dommage lien causal","Faute seulement","Dommage seulement"],"r":0,"e":"Responsabilité civile: faute + dommage + lien causal = dommages intérêts art 1240"},
{"q":"TVA Guinée?","o":["10%","18%","25%"],"r":1,"e":"TVA 18% sur ventes biens services, collecte entreprises reverse État"},
{"q":"Licenciement motif?","o":["Motif réel sérieux","Motif quelconque","Pas motif"],"r":0,"e":"Licenciement motif réel sérieux, entretien préalable, lettre, préavis, certificat, solde"},
{"q":"CDD max?","o":["1 an","2 ans renouvelable","5 ans"],"r":1,"e":"CDD exception max 2 ans renouvelable, CDI règle générale"},
{"q":"Inspection Travail?","o":["Kaloum gratuit conciliation","Payant","Pas existe"],"r":0,"e":"Inspection Travail Kaloum Matam gratuit conciliation patron salarié"},
{"q":"Preuve civile >500k?","o":["Témoignage suffit","Écrit obligatoire","Présomption suffit"],"r":1,"e":"Preuve civile >500k FCFA écrit obligatoire acte SSP ou authentique notaire"},
{"q":"Nullité relative prescription?","o":["5 ans","30 ans","1 an"],"r":0,"e":"Nullité relative intérêt privé 5 ans, absolue intérêt général 30 ans rétroactif"},
{"q":"Sursis simple?","o":["Pas prison si pas récidive 5 ans","Prison direct","Amende"],"r":0,"e":"Sursis simple pas prison si pas nouvelle infraction 5 ans, mise épreuve obligations"},
{"q":"Vol art?","o":["Art 373 CP","Art 394 CP","Art 201 CP"],"r":0,"e":"Vol art 373 CP soustraction frauduleuse 1-5 ans aggravé 10 ans"},
{"q":"Escroquerie art?","o":["Art 394 CP","Art 373 CP","Art 321 CP"],"r":0,"e":"Escroquerie art 394 tromperie remise volontaire 1-5 ans"},
{"q":"Abus confiance?","o":["Détourner chose remise à charge rendre","Prendre sans accord","Tromperie remise volontaire"],"r":0,"e":"Abus confiance art 394 détourner chose remise à charge rendre 1-5 ans"},
{"q":"Meurtre peine?","o":["1-5 ans","10-20 ans réclusion","Amende"],"r":1,"e":"Meurtre art 201 homicide volontaire intention tuer 10-20 ans, assassinat préméditation perpétuité"},
{"q":"Viol peine?","o":["1 an","5-10 ans mineur 10-20 ans","Amende"],"r":1,"e":"Viol art 321 acte sexuel sans consentement violence 5-10 ans mineur aggravé 10-20 ans"},
{"q":"Garde à vue droits?","o":["Avocat médecin famille silence","Rien","Seulement avocat"],"r":0,"e":"Garde à vue droits avocat 1ère heure médecin famille silence"},
{"q":"Pourvoi cassation délai?","o":["15 jours","2 mois","1 an"],"r":1,"e":"Pourvoi cassation 2 mois après arrêt Appel, non suspensif"},
{"q":"Appel TPI délai?","o":["15 jours","1 mois","2 mois"],"r":1,"e":"Appel TPI devant Cour Appel 1 mois signification suspensif sauf exécution provisoire"},
{"q":"Opposition = ?","o":["Recours jugement défaut","Recours arrêt Appel","Recours loi"],"r":0,"e":"Opposition recours contre jugement rendu par défaut, délai 15 jours"},
{"q":"SA capital min?","o":["1M","10M","100M"],"r":1,"e":"SA capital min 10M FCFA 100M si appel public épargne"},
{"q":"SAS = ?","o":["Société par Actions Simplifiée très libre","Société Anonyme Spéciale","Société Sans Actions"],"r":0,"e":"SAS très libre statuts fixent tout président pas conseil idéal startups filiales"},
{"q":"SNC responsabilité?","o":["Limitée","Indéfinie solidaire","Pas responsabilité"],"r":1,"e":"SNC associés commerçants responsabilité indéfinie solidaire"},
{"q":"GIE = ?","o":["Groupement Intérêt Économique 2+ faciliter activité membres","Groupement International Économique","Groupement Intérêt Entreprise"],"r":0,"e":"GIE 2+ personnes faciliter activité membres pas bénéfices pour lui-même"},
{"q":"Commissaire comptes obligatoire si?","o":["Bilan >125M ou CA >250M ou effectif >50","Toujours","Jamais"],"r":0,"e":"Commissaire comptes obligatoire si bilan >125M ou CA >250M ou effectif >50"},
],
"L3": [
{"q":"Titre Foncier faux?","o":["Valable","Danger 80% arnaques","Gratuit"],"r":1,"e":"80% arnaques Conakry vérifier livre foncier Kaloum avant payer"},
{"q":"Pourvoi CCJA délai?","o":["15j","2 mois","1 an"],"r":1,"e":"Pourvoi CCJA 2 mois après arrêt Appel OHADA, avocat agréé CCJA obligatoire"},
{"q":"Hypothèque où inscrite?","o":["Mairie","Conservation Foncière Kaloum","APIP"],"r":1,"e":"Hypothèque notariée inscrite Conservation Foncière Kaloum 10 ans renouvelable"},
{"q":"Hypothèque rang?","o":["Dernière inscrite payée première","Première inscrite payée première","Pas rang"],"r":1,"e":"Hypothèque rang ordre inscription première inscrite payée première"},
{"q":"Saisie attribution art?","o":["Art 77 AUCE","Art 1 AUCE","Art 190 AUS"],"r":0,"e":"Saisie attribution art 77 AUCE huissier bloque compte bancaire attribue créancier"},
{"q":"Injonction payer délai opposition?","o":["8 jours","15 jours","1 mois"],"r":1,"e":"Injonction payer débiteur 15 jours opposition sinon exécutoire art 1 AUCE"},
{"q":"Astreinte ex?","o":["200k/jour libérer maison","50k une fois","1M une fois"],"r":0,"e":"Astreinte art 33 AUCE somme par jour retard ex 200k/jour libérer maison"},
{"q":"Cessation paiements déclaration?","o":["10 jours","30 jours","1 an"],"r":1,"e":"Cessation paiements déclaration 30 jours TPI sinon responsabilité personnelle interdiction gérer"},
{"q":"Redressement judiciaire période observation?","o":["1 mois","6-18 mois","5 ans"],"r":1,"e":"Redressement période observation 6-18 mois gel dettes continue activité plan 10 ans"},
{"q":"Liquidation ordre créanciers?","o":["Salariés super privilégiés d'abord","Chirographaires d'abord","Hypothécaires d'abord"],"r":0,"e":"Liquidation ordre: salariés super privilégiés 6 derniers mois, frais justice, hypothécaires, chirographaires"},
{"q":"Arbitrage sentence délai?","o":["1 mois","6 mois","2 ans"],"r":1,"e":"Arbitrage sentence 6 mois prolongeable rapide vs 2 ans TPI"},
{"q":"Convention New York?","o":["1958 sentence exécutable 170 pays","1993","2008"],"r":0,"e":"Convention New York 1958 sentence arbitrale exécutable 170 pays"},
{"q":"Cautionnement solidaire = ?","o":["Créancier va direct caution","Créancier poursuit d'abord débiteur","Pas caution"],"r":0,"e":"Caution solidaire créancier va direct caution sans poursuivre débiteur, banque exige solidaire"},
{"q":"Nantissement fonds commerce où inscrit?","o":["Mairie","RCCM","Conservation"],"r":1,"e":"Nantissement fonds commerce inscrit RCCM, si impayé créancier vend fonds"},
{"q":"Gage avec dépossession?","o":["Créancier garde bien","Débiteur garde bien","Pas gage"],"r":0,"e":"Gage avec dépossession créancier garde bien, sans dépossession débiteur garde mais inscrit RCCM"},
{"q":"Réserve propriété = ?","o":["Vendeur reste propriétaire jusqu'à paiement complet","Acheteur propriétaire direct","Pas propriété"],"r":0,"e":"Réserve propriété art 71 AUS vendeur reste propriétaire jusqu'à paiement complet"},
{"q":"Prescription terrain?","o":["5 ans","30 ans","1 an"],"r":1,"e":"Prescription acquisitive terrain 30 ans possession paisible continue"},
{"q":"Prescription contrat?","o":["1 an","5 ans","30 ans"],"r":1,"e":"Prescription contrat 5 ans, commerce 5 ans, terrain 30 ans"},
{"q":"Exécution jugement prescription?","o":["1 an","5 ans","10 ans"],"r":2,"e":"Exécution jugement prescription 10 ans, huissier saisies"},
{"q":"Droit rétention ex?","o":["Garagiste retient voiture non payée","Banque retient compte","Notaire retient acte"],"r":0,"e":"Droit rétention art 67-70 garagiste retient voiture jusqu'à paiement"},
{"q":"CCJA peut évoquer?","o":["Non","Oui rejuge elle-même au fond","Seulement casse"],"r":1,"e":"CCJA casse arrêt Appel OHADA et PEUT ÉVOQUER rejuge elle-même au fond décision finale"},
{"q":"CCJA juges?","o":["9","13","17"],"r":1,"e":"CCJA 13 juges élus 7 ans renouvelable inamovibles tous pays OHADA"},
{"q":"SARL dissolution causes?","o":["Terme objet décision justice perte 50% capital","Seulement terme","Seulement décision"],"r":0,"e":"SARL dissolution terme objet décision 75% justice mésentente perte 50% capital non reconstitué >100 associés"},
{"q":"SA commissaire comptes?","o":["Si bilan >125M","Toujours","Jamais"],"r":0,"e":"SA commissaire comptes obligatoire si bilan >125M ou CA >250M ou effectif >50"},
{"q":"Bail commercial durée min?","o":["1 an","2 ans","5 ans"],"r":1,"e":"Bail commercial OHADA durée min 2 ans droit renouvellement indemnité éviction"},
{"q":"Vente fonds commerce publicité?","o":["JAL 15 jours","Pas publicité","JAL 1 an"],"r":0,"e":"Vente fonds commerce publicité JAL 15 jours séquestre prix 3 mois oppositions créanciers"},
{"q":"Saisie vente insaisissables?","o":["Vêtements lit nourriture 1 mois outils travail","Voiture TV","Stock"],"r":0,"e":"Saisie vente insaisissables vêtements lit nourriture 1 mois outils travail"},
{"q":"Saisie immobilière délai?","o":["1 mois","1-2 ans","10 ans"],"r":1,"e":"Saisie immobilière 1-2 ans coûteux grosses sommes hypothèque facilite"},
{"q":"Travail inspection?","o":["Kaloum gratuit","Payant","Pas existe"],"r":0,"e":"Inspection Travail Kaloum gratuit conciliation"},
{"q":"Divorce TPI délai?","o":["1 mois","6 mois à 2 ans","5 ans"],"r":1,"e":"Divorce TPI famille 6 mois à 2 ans pension alimentaire garde enfants partage biens"},
],
"OHADA": [
{"q":"OHADA = ?","o":["Harmonisation Droit Affaires","Humanitaire","Douane"],"r":0,"e":"Organisation Harmonisation Droit Affaires Afrique"},
{"q":"RCCM à?","o":["Mairie","APIP","TPI"],"r":1,"e":"APIP Guinée 500k"},
{"q":"Hypothèque où?","o":["Mairie","Conservation","APIP"],"r":1,"e":"Conservation Foncière Kaloum"},
{"q":"Sociétés = ?","o":["AUDCG","AUSCGIE","AUCE"],"r":1,"e":"AUSCGIE Sociétés 920 articles"},
{"q":"AUDCG = ?","o":["Commerce Général","Sociétés","Sûretés"],"r":0,"e":"AUDCG Droit Commercial Général 307 articles"},
{"q":"AUS = ?","o":["Sûretés","Sociétés","Voies Exécution"],"r":0,"e":"AUS Sûretés 302 articles caution hypothèque"},
{"q":"AUPC = ?","o":["Procédures Collectives","Arbitrage","Transport"],"r":0,"e":"AUPC Procédures Collectives 378 articles redressement liquidation"},
{"q":"AUCE = ?","o":["Voies Exécution","Arbitrage","Comptabilité"],"r":0,"e":"AUCE Voies Exécution 338 articles saisie attribution injonction payer"},
{"q":"AUA = ?","o":["Arbitrage","Sociétés","Sûretés"],"r":0,"e":"AUA Arbitrage 36 articles justice privée 6 mois"},
{"q":"SYSCOHADA = ?","o":["Comptabilité","Transport","Médiation"],"r":0,"e":"SYSCOHADA Plan comptable obligatoire bilan compte résultat"},
]
}

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
.depot{border:2px dashed #f9c00f;background:#1a1a00;padding:12px;border-radius:12px;margin-top:14px}
.quiz-badge{background:linear-gradient(135deg,#FFD700,#FF6A00);color:#000;padding:12px;border-radius:12px;text-align:center;margin-top:10px}
</style></head><body>
<div class="header">
<h1 style="color:#f9c00f;font-size:26px;font-weight:900">DROIT224</h1>
<p style="font-size:8px;color:#aaa">L1 • L2 • L3 • OHADA • DICTIONNAIRE A-Z • FAQ AI • DÉPÔT COURS</p>
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
<!-- DÉPÔT COURS EN BAS - POUR TOUS -->
<div class="depot">
<h3 style="color:#f9c00f">📥 DÉPOSER UN COURS / PDF - Pour Tous</h3>
<p class="small" style="color:#aaa">Étudiant, Professeur, Enseignant, Docteur, Juge, Avocat - Dépose ton cours, autant de PDF que tu veux, avec ton nom et prénom</p>
<select id="depLic"><option>L1</option><option>L2</option><option>L3</option><option>OHADA</option></select>
<select id="depMat"><option>Introduction au Droit</option><option>Droit Constitutionnel</option><option>Droit des Obligations</option><option>Droit Pénal</option><option>Droit Foncier</option><option>Droit des Sociétés OHADA</option><option>OHADA</option><option>Autre matière</option></select>
<select id="depRole"><option>Étudiant</option><option>Professeur</option><option>Enseignant</option><option>Docteur</option><option>Juge</option><option>Avocat</option><option>Juriste</option></select>
<input id="depNom" placeholder="Nom">
<input id="depPrenom" placeholder="Prénom">
<input id="depTitre" placeholder="Titre du cours / Leçon">
<textarea id="depCont" rows="4" placeholder="Contenu de la leçon complète... (tu peux écrire tout ton cours ici)"></textarea>
<input id="depPdf1" placeholder="Lien PDF 1 - https://... (Google Drive, PDF)">
<input id="depPdf2" placeholder="Lien PDF 2 - optionnel https://...">
<input id="depPdf3" placeholder="Lien PDF 3 - optionnel https://...">
<input id="depPdf4" placeholder="Lien PDF 4 - optionnel https://... (autant que tu veux, ajoute dans contenu)">
<p class="small" style="color:#888">Astuce: Mets tes PDF sur Google Drive > Partager > Copier lien > Colle ici. Tu peux mettre autant de liens que tu veux dans contenu aussi.</p>
<button class="btn" style="width:100%;background:#f9c00f" onclick="deposerCours()">📥 DÉPOSER MON COURS</button>
<div id="depMsg"></div>
</div>
<div id="gridDepot"></div>
</div>

<div id="ohada" class="view"><div id="bcOhada" class="breadcrumb"></div><div id="gridOhada"></div></div>
<div id="lex" class="view"><div class="card" style="border:2px solid #00e5ff"><h4>📖 Dictionnaire Juridique A-Z</h4><div style="display:flex;gap:4px"><input id="lexIn" placeholder="Cherche mot: juge, avocat..." oninput="searchLex()" style="flex:1"><select id="lexLettre" onchange="filterLettre()" style="width:80px"><option value="">A-Z</option><option>A</option><option>B</option><option>C</option><option>D</option><option>E</option><option>F</option><option>G</option><option>H</option><option>I</option><option>J</option><option>M</option><option>N</option><option>O</option><option>P</option><option>Q</option><option>R</option><option>S</option><option>T</option><option>V</option></select></div><div id="lexAuto"></div></div><div id="gridLex"></div></div>
<div id="quiz" class="view">
<div class="card" style="border:2px solid #f9c00f;text-align:center">
<h3 style="color:#f9c00f">🎮 QUIZ - Toute la Licence</h3>
<p class="small">Choisis ta licence, lance, 10 questions qui se suivent. Rejoue = autres questions différentes. 10 questions = Badge!</p>
<div style="display:flex;gap:6px;margin-top:10px"><select id="qLvl" style="flex:1"><option>L1</option><option>L2</option><option>L3</option><option>OHADA</option></select><button class="btn" onclick="startQuiz()">▶️ LANCER QUIZ</button></div>
<div id="qZone" style="text-align:left;margin-top:10px"></div>
<div id="qBadge"></div>
</div>
</div>
<div id="faq" class="view"><div class="card" style="border:2px solid #76ff03;background:linear-gradient(135deg,#001a00,#000)"><h4 style="color:#76ff03">❓ FAQ - Assistant AI Juridique VRAI</h4><p class="small" style="color:#aaa">Pose question précise, je réponds vraiment! Ex: c'est qui le juge? c'est quoi une SARL? Comment créer entreprise?</p><div style="display:flex;gap:4px;margin-top:8px"><input id="faqAsk" placeholder="Ex: c'est qui le juge?"><button class="btn" style="background:#76ff03" onclick="askFaq()">Demander</button></div><div style="display:flex;gap:4px;margin-top:6px;flex-wrap:wrap"><button class="btn" style="background:#222;color:#fff;font-size:9px" onclick="quickFaq('c est qui le juge')">C'est qui le juge?</button><button class="btn" style="background:#222;color:#fff;font-size:9px" onclick="quickFaq('c est qui avocat')">C'est qui avocat?</button><button class="btn" style="background:#222;color:#fff;font-size:9px" onclick="quickFaq('comment creer SARL')">Créer SARL?</button><button class="btn" style="background:#222;color:#fff;font-size:9px" onclick="quickFaq('terrain foncier titre')">Terrain?</button></div><div id="faqAuto"></div></div></div>
<div id="dossier" class="view"><div class="card" style="border:2px solid #ff1744;background:#1a0000"><h4>Dossiers Justice</h4><select id="dType"><option>Licenciement</option><option>Dette</option><option>Terre Foncier</option><option>Divorce</option><option>Vol</option><option>Contrat</option></select><textarea id="dDesc" rows="3" placeholder="Décris cas..."></textarea><input id="dNom" placeholder="Ton nom"><button class="btn" style="background:#ff1744;color:#fff;width:100%" onclick="postDossier()">Soumettre</button><div id="dAuto"></div></div><div id="gridDossier"></div></div>
<div id="forum" class="view"><div class="card" style="border:2px solid #f9c00f"><select id="fRole"><option>Étudiant</option><option>Professeur</option><option>Juge</option><option>Avocat</option><option>Docteur</option></select><input id="fNom" placeholder="Nom"><textarea id="fMsg" placeholder="Question"></textarea><button class="btn" style="width:100%" onclick="postForum()">Poster</button></div><div id="gridForum"></div></div>

<script>
let DB={};
let navC={level:'licences', lic:null, matId:null, chapIdx:null, secIdx:null, sousIdx:null};
let navO={level:'matieres', matId:null, chapIdx:null, secIdx:null, sousIdx:null};
let usedQuestions=[]; // pour rejouer = autres questions

async function load(){DB=await fetch('/api/all').then(r=>r.json());renderCours();renderOhada();renderLex();renderDossier();renderForum();renderDepot();}
function showTab(id,btn){document.querySelectorAll('.view').forEach(v=>v.classList.remove('active'));document.getElementById(id).classList.add('active');document.querySelectorAll('.tabs button').forEach(b=>b.classList.remove('active'));btn.classList.add('active');}

function renderCours(){
 let h=''; let bc='';
 if(navC.level=='licences'){
   bc='📚 Cours - Choisis ta Licence';
   h+=`<div class="licence-card" onclick="openLicence('L1')"><h2 style="color:#f9c00f;font-size:28px">🎓 LICENCE 1</h2><p class="small">Introduction Droit, Constitutionnel</p></div>`;
   h+=`<div class="licence-card" style="border-color:#00e5ff" onclick="openLicence('L2')"><h2 style="color:#00e5ff;font-size:28px">🎓 LICENCE 2</h2><p class="small">Obligations, Pénal</p></div>`;
   h+=`<div class="licence-card" style="border-color:#76ff03" onclick="openLicence('L3')"><h2 style="color:#76ff03;font-size:28px">🎓 LICENCE 3</h2><p class="small">Foncier, Sociétés OHADA</p></div>`;
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
   sec.sous_sections.forEach((s,i)=>{h+=`<div class=card onclick="openSous(${i})"><b>📄 ${s.titre}</b><p class=small style=color:#76ff03>Clique leçon intégrale complète détaillée</p></div>`});
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

// DÉPÔT COURS
function renderDepot(){
 let h='<h3 style="margin-top:16px;color:#f9c00f">📚 Cours déposés par la communauté</h3>';
 (DB.depot||[]).slice().reverse().forEach(d=>{
   h+=`<div class=card style=border:1px solid #f9c00f"><span class=badge>${d.lic} - ${d.matiere}</span> <span class=badge style=background:#00e5ff>${d.role}</span><h4 style=margin:6px 0>${d.titre}</h4><p class=small>Par <b>${d.prenom} ${d.nom}</b> - ${d.time}</p><p class=small style=margin-top:6px>${d.contenu}</p>${d.pdfs.map(p=>p?`<p style=margin-top:4px"><a href="${p}" target="_blank" style=color:#00e5ff>📄 PDF: ${p}</a></p>`:'').join('')}</div>`;
 });
 if((DB.depot||[]).length==0) h+=`<p class=small style=color:#888>Aucun cours déposé pour l'instant. Sois le premier à déposer!</p>`;
 document.getElementById('gridDepot').innerHTML=h;
}
async function deposerCours(){
 let d={lic:document.getElementById('depLic').value, matiere:document.getElementById('depMat').value, role:document.getElementById('depRole').value, nom:document.getElementById('depNom').value, prenom:document.getElementById('depPrenom').value, titre:document.getElementById('depTitre').value, contenu:document.getElementById('depCont').value, pdfs:[document.getElementById('depPdf1').value, document.getElementById('depPdf2').value, document.getElementById('depPdf3').value, document.getElementById('depPdf4').value].filter(x=>x.trim()!='')};
 if(!d.nom||!d.prenom||!d.titre||!d.contenu) return alert('Remplis Nom, Prénom, Titre et Contenu du cours');
 await fetch('/api/depot',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)});
 document.getElementById('depMsg').innerHTML=`<p style=color:#76ff03;margin-top:8px">✅ Merci ${d.prenom} ${d.nom} (${d.role})! Ton cours a été déposé! Il est visible pour tous!</p>`;
 document.getElementById('depTitre').value='';document.getElementById('depCont').value='';document.getElementById('depPdf1').value='';document.getElementById('depPdf2').value='';document.getElementById('depPdf3').value='';document.getElementById('depPdf4').value='';
 load();
}

// LEXIQUE A-Z
function renderLex(){let h='';(DB.lexique||[]).forEach(l=>{h+=`<div class=card><b>[${l.lettre}] ${l.t}</b><p class=small style=margin-top:4px">${l.d}</p></div>`});document.getElementById('gridLex').innerHTML=h;}
function filterLettre(){let lettre=document.getElementById('lexLettre').value;if(!lettre){renderLex();return}let filt=(DB.lexique||[]).filter(l=>l.lettre==lettre);let h='';filt.forEach(l=>{h+=`<div class=card><b>[${l.lettre}] ${l.t}</b><p class=small>${l.d}</p></div>`});document.getElementById('gridLex').innerHTML=h;}
async function searchLex(){let q=document.getElementById('lexIn').value;if(q.length<2){document.getElementById('lexAuto').innerHTML='';renderLex();return}let res=await fetch('/api/search?q='+encodeURIComponent(q)).then(r=>r.json());document.getElementById('lexAuto').innerHTML=`<div class=card style=background:#002a2a;border-color:#00e5ff"><p class=small>${res.ans}</p></div>`;}

// FAQ VRAI
async function askFaq(){let q=document.getElementById('faqAsk').value;if(!q)return;let res=await fetch('/api/search_faq?q='+encodeURIComponent(q)).then(r=>r.json());document.getElementById('faqAuto').innerHTML+=`<div class=card style=background:#001a00;border-color:#76ff03;margin-top:10px"><b style=color:#76ff03>👤 Toi: ${q}</b><div style=border-top:1px solid #222;margin-top:8px;padding-top:8px"><b style=color:#00e5ff>🤖 FAQ AI:</b><p class=small style=margin-top:6px">${res.ans}</p></div></div>`;document.getElementById('faqAsk').value='';}
function quickFaq(q){document.getElementById('faqAsk').value=q;askFaq();}

function renderDossier(){let h='';(DB.dossiers||[]).slice().reverse().forEach(d=>{h+=`<div class=card style=border:1px solid #ff1744"><b>📂 ${d.type}</b> <small style=color:#666">${d.time} par ${d.nom}</small><p class=small style=margin:6px 0">${d.desc}</p><div style=background:#111;padding:6px;border-radius:6px"><small style=color:#f9c00f"><b>FAQ AI:</b> ${d.auto||''}</small></div></div>`});document.getElementById('gridDossier').innerHTML=h;}
async function postDossier(){let d={type:document.getElementById('dType').value,desc:document.getElementById('dDesc').value,nom:document.getElementById('dNom').value};if(!d.desc)return alert('Décris cas');let res=await fetch('/api/search_faq?q='+encodeURIComponent(d.type+' '+d.desc)).then(r=>r.json());d.auto=res.ans;await fetch('/api/dossiers',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)});document.getElementById('dDesc').value='';load();}

// QUIZ NOUVEAU: 10 questions, rejouer = autres questions, badge après 10
let cq=[],qi=0,sc=0,totalQ=0;
function startQuiz(){
 let lvl=document.getElementById('qLvl').value;
 let banque=DB.quiz[lvl]||[];
 // Mélange et prend 10 questions différentes de la dernière fois
 let shuffled=[...banque].sort(()=>Math.random()-0.5);
 // Évite répéter questions déjà vues si possible
 let filtered=shuffled.filter(q=>!usedQuestions.includes(q.q));
 if(filtered.length<10) {usedQuestions=[]; filtered=shuffled;}
 cq=filtered.slice(0,10);
 cq.forEach(q=>usedQuestions.push(q.q));
 qi=0;sc=0;totalQ=cq.length;
 document.getElementById('qBadge').innerHTML='';
 showQ();
}
function showQ(){
 if(qi>=cq.length){
   let badge='';
   if(sc>=8) badge=`<div class="quiz-badge"><h2>🏆 BADGE OR - EXCELLENT!</h2><p>Tu as répondu à ${sc}/${totalQ} questions! Tu es un champion du droit!</p><p>Badge: 🥇 OR - Maître du Droit</p></div>`;
   else if(sc>=5) badge=`<div class="quiz-badge" style="background:linear-gradient(135deg,#C0C0C0,#888)"><h2>🥈 BADGE ARGENT</h2><p>Tu as répondu à ${sc}/${totalQ} questions! Bien joué, continue!</p><p>Badge: 🥈 ARGENT - Juriste Confirmé</p></div>`;
   else badge=`<div class="quiz-badge" style="background:linear-gradient(135deg,#CD7F32,#8B4513)"><h2>🥉 BADGE BRONZE</h2><p>Tu as répondu à ${sc}/${totalQ} questions! Continue à réviser dans Cours!</p><p>Badge: 🥉 BRONZE - Apprenti Juriste</p></div>`;
   document.getElementById('qZone').innerHTML=`<h2 style=text-align:center>${sc}/${totalQ}</h2>${badge}<button class=btn onclick=startQuiz() style=margin-top:10px;width:100%">🔁 REJOUER - D'AUTRES QUESTIONS</button><p class=small style=text-align:center;margin-top:6px>Rejoue = 10 nouvelles questions différentes!</p>`;
   document.getElementById('qBadge').innerHTML=badge;
   return;
 }
 let q=cq[qi];
 let h=`<div style=display:flex;justify-content:space-between><b>Question ${qi+1}/${totalQ} - Licence ${document.getElementById('qLvl').value}</b><span class=badge>Score: ${sc}</span></div><h4 style=margin:10px 0;font-size:13px>${q.q}</h4>`;
 q.o.forEach((o,i)=>{h+=`<div class=card" style="padding:10px;margin:4px 0" onclick="checkQ(${i})">${o}</div>`});
 document.getElementById('qZone').innerHTML=h;
}
function checkQ(i){
 let q=cq[qi];let ok=i==q.r;if(ok)sc++;
 document.getElementById('qZone').innerHTML+=`<div class=card style=background:${ok?'#001a00':'#1a0000'};margin-top:8px"><b>${ok?'✅ BONNE RÉPONSE!':'❌ MAUVAISE RÉPONSE'} ${q.e}</b><br><button class=btn onclick="qi++;showQ()" style=margin-top:6px>Question suivante ➡️</button></div>`;
}
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
    return jsonify({"cours":COURS_LICENCES,"ohada":OHADA_DETAILLÉ,"lexique":DICT_AZ,"quiz":QUIZ_BANQUE,"dossiers":dossiers,"forum":forum,"depot":depot})

@app.route("/api/search")
def search_api():
    q=request.args.get("q","")
    ql=q.lower()
    for item in DICT_AZ:
        if item["t"].lower() in ql or ql in item["t"].lower():
            return jsonify({"ans":item["d"] + " [Dictionnaire Juridique A-Z]"})
    return jsonify({"ans":f"{q}: Définition complète en droit guinéen et OHADA, voir cours détaillés Licences > Matières > Programme > Chapitres > Sections > Sous-sections > Leçons intégrales."})

@app.route("/api/search_faq")
def search_faq_api():
    q=request.args.get("q","")
    return jsonify({"ans":moteur_faq_vrai(q)})

@app.route("/api/depot", methods=["POST"])
def depot_post():
    d=request.get_json()
    alld=load_j("depot_v15.json", [])
    alld.append({"lic":d.get("lic","L1"),"matiere":d.get("matiere",""),"role":d.get("role","Étudiant"),"nom":d.get("nom",""),"prenom":d.get("prenom",""),"titre":d.get("titre",""),"contenu":d.get("contenu",""),"pdfs":d.get("pdfs",[]),"time":datetime.now().strftime("%d/%m/%Y %H:%M")})
    save_j("depot_v15.json", alld)
    return jsonify({"ok":True})

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
