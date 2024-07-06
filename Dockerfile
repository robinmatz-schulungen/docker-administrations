# Bestimme das Basis Image für unser eigenes Image
# Da das Image "python" auf hub.docker.com gehostet wird,
# muss die Registry (registry-1.docker.io bzw. docker.io) nicht angegeben werden
FROM python:3.12-slim

# Setzt das Arbeitsverzeichnis, das für alle weiteren Befehle gilt
WORKDIR /app

# Kopiert alle Dateien aus dem Hostverzeichnis in das Containerverzeichnis
COPY . .

# Python-spezifischer Befehl, um die Dependencies, die in der Datei
# requirements.txt gelistet sind, zu installieren
RUN python3 -m pip install -r requirements.txt

# Sagt dem Container, dass der Port 5000 nach außen freigegeben wird
EXPOSE 5000

# Legt den Startbefehl des Containers fest.
# Syntax CMD [ "executable", ["parameter1"], ["parameter2"], ...]
CMD [ "flask", "--app", "app", "run", "--host", "0.0.0.0" ]
