from datetime import date
from datetime import datetime

timezone = "+8:00" #Philippines timezone

txtSitemap = "sitemap.txt"
xmlSitenmap = "sitemap.xml"


arr = ""
arr += "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset\n\txmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\" \n\txmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\n\txsi:schemaLocation=\"http://www.sitemaps.org/schemas/sitemap/0.9\n\t\thttp://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd\">"

today = date.today()

with open(TxtSitemap) as f:
    lines = f.readlines()
    d = today.strftime("%Y-%m-%d")
    
    for line in lines:
    	res = "T" + datetime.now().strftime("%H:%M:%S")
    	res += "+08:00" #Philippines Timezone
    	
    	d += res
    	
    	if line[len(line) - 1] == "\n":
    		line = line[:-1]
    	
    	str = f"\n\t<url>\n\t\t<loc>{line}</loc>\n\t\t<lastmod>{d}</lastmod>\n\t</url>"
    	arr += str
    	
arr += "\n</urlset>"

fs = open(xmlSitenmap, "w+")
fs.write(arr)
fs.close()

print(arr)
