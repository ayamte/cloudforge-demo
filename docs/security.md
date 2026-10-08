# Sécurité de l’image de démonstration

## Contrôles réalisés

La CI exécute les tests, construit l’image Docker et analyse ses vulnérabilités connues avec Trivy.

Le scan produit un rapport JSON téléchargeable. Il est actuellement non bloquant : une CI verte ne signifie pas que l’image est sans vulnérabilité.

## Réduction des composants et des permissions

- pip est retiré après l’installation des dépendances.
- Les six vulnérabilités Python précédemment signalées ne sont plus détectées dans le rapport obtenu après cette modification.
- L’application s’exécute avec appuser (UID 10001), plutôt qu’avec root.

## Résultats Debian

Le rapport analysé contient 165 résultats :
44 HIGH, 58 MEDIUM, 61 LOW et 2 UNKNOWN.

Les 44 résultats HIGH correspondent à huit CVE distinctes.
Les fiches Debian consultées n’indiquent pas de correctif disponible pour ces cas dans Debian 13 stable.

Nous conservons Debian stable pour le laboratoire, sans mélanger ses paquets avec ceux d’une distribution instable.

## Analyse des conditions d’exploitation

Vérifications effectuées sur l’image locale :

- CVE-2026-16742 : systemd-homed est absent ; le service nécessaire au scénario décrit n’est pas présent.
- CVE-2026-9538 : le module Perl Archive::Tar est absent.
- CVE-2025-69720 : infocmp est présent, mais notre application ne l’appelle pas.
- CVE-2026-54369 : notre application ne réalise pas d’opérations privilégiées de modification des ACL.
- CVE-2026-76642, CVE-2026-78408, CVE-2026-78409 et CVE-2026-78410 : mount et nsenter sont présents ; notre application n’effectue pas les opérations privilégiées décrites dans les avis.

Ces observations ne prouvent pas l’absence générale de risque.
Les vérifications de présence devront aussi être confirmées sur l’image destinée au déploiement.

## Restrictions d’exécution prévues

La commande de lancement doit utiliser :

- --security-opt no-new-privileges:true
- --cap-drop ALL

Ces protections ne corrigent pas les paquets vulnérables.
Elles devront être vérifiées, puis reproduites dans Kubernetes.
Le conteneur ne doit pas être lancé en mode privilégié ni recevoir le socket Docker ou des accès sensibles à l’hôte.

## Suivi

Les vulnérabilités restent visibles dans le rapport Trivy.
Aucune exclusion générale n’est appliquée.

Cette décision est temporaire et limitée au laboratoire.
Elle devra être réévaluée avant exposition publique, lors d’un changement fonctionnel et lorsque des correctifs deviennent disponibles.