from xeger import Xeger
import sys
import re
import configparser
from custom_syntax import custom_syntax
from tools import debug

config = configparser.ConfigParser()
config.read('anonex.conf')
xeger = Xeger(limit=10**6)


if '--help' in sys.argv or '-h' in sys.argv:
    with open('man.txt','r') as file:
        print(file.read())
    sys.exit()



with open(config.get('DEFAULT', 'file'),'r') as file:
    raw = file.read()
res = raw
debug("file wrote")

matches = re.findall(config.get('DEFAULT', 'inex'), raw)
if (l:=len(matches)) == 0:
    print("Oops, nothing match to your input regex (inex)")
else:
    debug(f"found {l} matches")


for match in matches:
    x = xeger.xeger(config.get('DEFAULT', 'outex'))
    res = res.replace(match,x)
    res = custom_syntax(res)

debug("result :\n")
print(res)

