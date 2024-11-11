import subprocess
import os

#per esempio l'utente "TottiGL.jpg"
sFile = input("Inserisci il nome del file: ")

#["TottiGL", "jpg"]     sFileB64 è "TottiGL"
sFileB64 = os.path.splitext(sFile)[0]

#sFileB64 diventa "TottiGL.b64"
sFileB64 = sFileB64 + ".b64"

print(sFile)
print(sFileB64)

#crea il file   image1.jpeg
subprocess.run(["cp", sFile,"./image1.jpeg"])

#base64 -in image1.jpeg -o image2.b64
subprocess.run(["bash", "./comando.sh"])

#cp ./image2.b64 TottiGL.b64
subprocess.run(["cp", "./image2.b64",sFileB64])