# API Security
In diesem Techtalk werden API Sicherheitslücken betrachtet und gehackt. 


## Juice Shop 
Der Juice Shop enthält viele Schwachstellen und es werden verschiedene Aufgaben gestellt. Den passenden Hack zu finden ist Teil des Spiels. Der Maintainer ist das OWASP Konsortium.
Die App kann einfach als Docker Container gestartet werden:

     $ docker run --rm -p 3000:3000 bkimminich/juice-shop


## Registrierung
Über die `Netzwerk-Analyse` in der Entwickler-Console wird der POST-Request abgefangen

Über die das VSCode Plugin `REST Client` können modifizierte Requests gesendet und Responses empfangen werden.

