#@Data Dasar Grabber by beta.uliansyah@pknstan.ac.id
import requests
from bs4 import BeautifulSoup
import json

data = []
data.append(['Daerah', 'Alokasi Dasar', 'Alokasi Afirmasi', 'Alokasi Formula', 'Total Alokasi', 'Jumlah Desa', 'Jumlah Penduduk', 'Jumlah Penduduk Miskin', 'Luas Wilayah', 'IKK'])

s = requests.Session()
r = s.get('http://www.djpk.kemenkeu.go.id/datadasar')
bsoup = BeautifulSoup(r.text, 'html.parser')

if r.status_code==200:
    token = bsoup.find("input", {"name":"_token"})['value']
    alldaerah = bsoup.find("select", {"name":"s_daerah"})
    for option in alldaerah.find_all("option"):
        #if option['value'] == '0103':
        #    break
        r = s.post('http://www.djpk.kemenkeu.go.id/datadasar/dashboard', 
                           data={'_token': token, 's_jenis': '03', 's_subjenis':'0000', 's_tahun': '2018', 's_daerah':option['value']})
        if r.status_code==200:
            bs = BeautifulSoup(r.text, 'html.parser')
            if "Maaf, Data belum tersedia!" in r.text:
                continue
            #print(r.text)
            token = bs.find("input", {"name":"_token"})['value']
            table = bs.find("table", attrs={"id":"example"})
            table_body = table.find('tbody')
            rows = table_body.find_all('tr')
            datarow = []
            for row in rows:
                cols = row.find_all('td')
                if len(cols)==0:
                    continue                    
                cols = [ele.text.strip() for ele in cols]
                datarow.append([ele for ele in cols if ele]) # Get rid of empty values
            ad = datarow[0][1].replace(".","").replace(",",".")
            aa = datarow[1][1].replace(".","").replace(",",".")
            af = datarow[2][1].replace(".","").replace(",",".")
            total = datarow[3][1].replace(".","").replace(",",".")
            jmldesa = datarow[4][1].replace(".","").replace(",",".")
            penduduk = datarow[5][1].replace(".","").replace(",",".")
            jpmiskin = datarow[6][1].replace(".","").replace(",",".")
            lwilayah = datarow[7][1].replace(".","").replace(",",".")
            ikk = datarow[8][1].replace(".","").replace(",",".")
            #dbhpajak = datarow[11][1].replace(".","").replace(",",".")
            #dbhsda = datarow[12][1].replace(".","").replace(",",".")
            #dauformula = datarow[13][1].replace(".","").replace(",",".")
            data.append([option.text.strip(), ad, aa, af, total, jmldesa, penduduk, jpmiskin, lwilayah, ikk])
jsondata = json.dumps(data, indent=None)
print(jsondata)
#print(datarow)
