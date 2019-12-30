#@Data Dasar Grabber by beta.uliansyah@pknstan.ac.id
import requests
from bs4 import BeautifulSoup
import json

data = []
data.append(['Daerah', 'Belanja Pegawai', 'Penduduk', 'Luas Daratan', 'Luas Lautan', 'Total Luas Wilayah', 'IKK', 'IPM', 'PDRB per kapita', 'PAD', 'DBH Pajak', 'DBH SDA', 'Alokasi DAU'])

s = requests.Session()
r = s.get('http://www.djpk.kemenkeu.go.id/datadasar')
bsoup = BeautifulSoup(r.text, 'html.parser')

if r.status_code==200:
    token = bsoup.find("input", {"name":"_token"})['value']
    alldaerah = bsoup.find("select", {"name":"s_daerah"})
    for option in alldaerah.find_all("option"):
        #if option['value'] == '0102':
        #    break
        r = s.post('http://www.djpk.kemenkeu.go.id/datadasar/dashboard', 
                           data={'_token': token, 's_jenis': '01', 's_subjenis':'0000', 's_tahun': '2018', 's_daerah':option['value']})
        if r.status_code==200:
            bs = BeautifulSoup(r.text, 'html.parser')
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
            bpegawai = datarow[0][1].replace(".","").replace(",",".")
            penduduk = datarow[1][1].replace(".","").replace(",",".")
            ldaratan = datarow[3][1].replace(".","").replace(",",".")
            llautan = datarow[4][1].replace(".","").replace(",",".") if datarow[4][1] != 'km2' else '0'
            ltotal = datarow[5][1].replace(".","").replace(",",".")
            ikk = datarow[6][1].replace(".","").replace(",",".")
            ipm = datarow[7][1].replace(".","").replace(",",".")
            pdrbpercap = datarow[8][1].replace(".","").replace(",",".")
            pad = datarow[9][1].replace(".","").replace(",",".")
            dbhpajak = datarow[10][1].replace(".","").replace(",",".")
            dbhsda = datarow[11][1].replace(".","").replace(",",".")
            dauformula = datarow[12][1].replace(".","").replace(",",".")
            data.append([option.text, bpegawai, penduduk, ldaratan, llautan, ltotal, ikk, ipm, pdrbpercap, pad, dbhpajak, dbhsda, dauformula])
jsondata = json.dumps(data, indent=None)
print(jsondata)
#print(datarow)
