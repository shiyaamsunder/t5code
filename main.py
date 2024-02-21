import glob
import os

dataset_path = ".\\Training\\*"


files = glob.glob(dataset_path)
key_files = glob.glob(dataset_path + ".key")
text_files = glob.glob(dataset_path + ".txt")



keycontent = ""


db = []

for keyfile, textfile in list(zip(key_files, text_files)):
    dbdict = {}
    with open(keyfile, encoding="utf-8") as file:
        topic = os.path.basename(keyfile).split("-")[0]
        dbdict["topic"] = topic
        dbdict["keywords"] = file.read().replace("\'", "'").replace("\\", "").replace("\n", " ")
        with open(textfile, encoding="utf-8") as text:
            dbdict["sentences"] = text.read().replace("\'", "'").replace("\\", "").replace("\n", " ")
        db.append(dbdict)
        

print(db)