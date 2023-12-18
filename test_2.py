import zipfile
import re

archive = zipfile.ZipFile("/Users/valeriiamoiseeva/Downloads/Conference presentation_final.pptx", "r")
ms_data = archive.read("docProps/app.xml")
archive.close()
app_xml = ms_data.decode("utf-8")

regex = r"<(Pages|Slides)>(\d)</(Pages|Slides)>"

matches = re.findall(regex, app_xml, re.MULTILINE)
match = matches[0] if matches[0:] else [0, 0]
page_count = match[1]

print(page_count)
