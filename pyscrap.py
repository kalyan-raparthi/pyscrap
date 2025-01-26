'''
PYSCRAP MAIN SCRIPT 
AUTHOUR: 
1. KALYAN RAPARTHI / [ qb ], kalyan.raparthi@hotmail.com, GitHub: kalyan-raparthi
'''

import http.client

url = "kalyan-raparthi.github.io"
con = http.client.HTTPSConnection(url)
con.request('GET', '/')

response  = con.getresponse()
print(response.read().decode('utf-8'))

con.close()

