import requests
from bs4 import BeautifulSoup
import re

rq = requests.get("https://10minutemail.net/")
bp = BeautifulSoup(rq.text, "html.parser")
eles = bp.select('input')
print(eles)

rg = re.compile(r'value="(.*?)"')
check_rg = rg.search(str(eles))
if check_rg:
    kq_rg = check_rg.group(1)
    print(kq_rg)
