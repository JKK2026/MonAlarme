[app]
# (str) Title of your application
title = Mon Alarme

# (str) Package name
package.name = monalarme

# ... others lines ...
version = 0.1
# ou version = 1.0.0

git add buildozer.spec
git commit -m "Fix buildozer.spec: add version 0.1"
git push origin main  # ou ta branche

# ... ton code existant ...

# (str) Permet de preserver les données entre mises à jour
android.add_src = src

# (str) Icone de l'app (crée un dossier 'icones' avec tes icônes)
icon.filename = %(source.dir)s/icones/icône.png

# (str) Nom du fichier APK généré
p4a.branch = master

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,mp3

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET, WAKE_LOCK,SCHEDULE_EXACT_ALARM

# (int) Android API to use
android.api = 31

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 23b

# (bool) Use private storage for the app
android.private_storage = True

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
