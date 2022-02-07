# API Security
In diesem Techtalk werden API Sicherheitslücken betrachtet und gehackt. 


## Juice Shop 
Der Juice Shop enthält viele Schwachstellen und es werden verschiedene Aufgaben gestellt. Den passenden Hack zu finden ist Teil des Spiels. Der Maintainer ist das OWASP Konsortium.
Die App kann einfach als Docker Container gestartet werden:

     $ docker run --rm -p 3000:3000 bkimminich/juice-shop

For some tasks the Zed Attack Proxy (ZAP) can be usefull:

     $ docker pull owasp/zap2docker-stable


## Registrierung
Über die `Netzwerk-Analyse` in der Entwickler-Console wird der POST-Request abgefangen

Über die das VSCode Plugin `REST Client` können modifizierte Requests gesendet und Responses empfangen werden.

## Attacks
Attacken die ich im TechTalk zeigen möchte

## Broken User Authentication
- Füge einen Benutzer mit  `users/promote-to-admin.http` hinzu, der das `role` Attribut setzt
- Schaue den Warenkorb eines anderen Users an (Session Storage bid neu setzen)
- Poste ein Review im Namen eines anderen Users `put-review.http`

## Input Validierung
- Im Warenkorb eine negative Menge hinzufügen mit `basketitems/add-negative-quantity.http`
- Füge jemand anderem ein Item im Warenkorb hinzu mit `basketitems/add-to-another-persons-basket.http`
  Benutzt HTTP Parameter Pollution (HPP)

## Ein 0 Sterne Feedback abgeben
- Umgehe die Inputvalidierung im Frontend und löse das Captcha mit `feedbacks/post-feedback.http`

## SQL Injection
- Die Suche ist anfällig für XSS:
    <iframe src="javascript:alert(`xss`)">

Die Schwachstelle lässt sich auch für eine SQL-Injection ausnutzen
- Welche Database-Engine verwendet wird, lässt sich mit `query/find-database-engine.http` ermitteln. Es wird ein Fehler provoziert, welcher diese Info preisgibt.

- Zeige mir alle Benutzer und Passwörter an mittels `query/union-sql-injection.http`

## Brute Force
- Setze ein neues Passwort über das Password-Zurücksetzen-Formulars für ein fremdes Konto mit `scripts/brute-force-pass-reset.py`