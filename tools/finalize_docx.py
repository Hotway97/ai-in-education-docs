import os
import sys
import zipfile

path = sys.argv[1]
tmp = path + ".tmp"

with zipfile.ZipFile(path, "r") as source:
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as target:
        for item in source.infolist():
            data = source.read(item.filename)
            if item.filename == "word/settings.xml":
                text = data.decode("utf-8")
                if "<w:updateFields" not in text:
                    text = text.replace("</w:settings>", '<w:updateFields w:val="true"/></w:settings>')
                data = text.encode("utf-8")
            target.writestr(item, data)

os.replace(tmp, path)
print("DOCX finalized:", path)
