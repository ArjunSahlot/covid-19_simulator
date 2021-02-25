import os
import sys
import zipfile
import urllib.request
from tkinter import Tk
from tkinter.filedialog import askdirectory
Tk().withdraw()

print("Choose installation location.")
dir = askdirectory()
tmp = os.path.join(dir, "tmp")
file = "covid-19_simulator-"
print("Installing...")
try:
    urllib.request.urlretrieve("https://github.com/ArjunSahlot/covid-19_simulator/archive/main.zip", tmp)
    file += "main"
except urllib.error.HTTPError:
    urllib.request.urlretrieve("https://github.com/ArjunSahlot/covid-19_simulator/archive/master.zip", tmp)
    file += "master"

print("Unzipping")
with zipfile.ZipFile(tmp, 'r') as zip:
    zip.extractall(dir)

print("Cleaning up")
<<<<<<< HEAD
final = os.path.join(dir, file.split("-")[0]
os.rename(os.path.join(dir, file), final))
=======
os.rename(os.path.join(dir, file), os.path.join(dir, file.split("-")[:2]))
>>>>>>> 717ccb8938514d8c35cd84684fbae9a09258f63d
os.remove(os.path.join(tmp))

with open(os.path.join(final, "requirements.txt"), "r") as f:
    packages = f.read().split("
")

if sys.platform == "windows":
    cmd = "pip install "
else:
    cmd = "pip3 install "

print("Installing packages")
for package in packages:
    if "n" in input(f"Install" + package + "? [y/n] ").lower():
        continue
    os.system(cmd.format(package))

print("Done!")
