#@Data Dasar Grabber by beta.uliansyah@pknstan.ac.id
import requests
from bs4 import BeautifulSoup
import json

data = []
data.append(['Daerah', 'Jumlah Kelurahan', 'Kategori Pelayanan Dasar Publik', 'Alokasi DAU Tambahan'])

s = requests.Session()
r = s.get('http://www.djpk.kemenkeu.go.id/datadasar')
bsoup = BeautifulSoup(r.text, 'html.parser')

if r.status_code==200:
    token = bsoup.find("input", {"name":"_token"})['value']
    alldaerah = bsoup.find("select", {"name":"s_daerah"})
    for option in alldaerah.find_all("option"):
        #if option['value'] == '0108':
        #    break
        r = s.post('http://www.djpk.kemenkeu.go.id/datadasar/dashboard', 
                           data={'_token': token, 's_jenis': '01', 's_subjenis':'2', 's_tahun': '2019', 's_daerah':option['value']})
        if r.status_code==200:
            #print(r.text)
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
            jmlkelurahan = datarow[0][1].replace(".","").replace(",",".") if datarow[0][1] != 'kelurahan' else '0'
            pelayananpublik = datarow[1][1]
            dautambahan = datarow[2][1].replace(".","").replace(",",".") if datarow[2][1] != 'Rupiah' else '0'
            data.append([option.text.strip(), jmlkelurahan, pelayananpublik, dautambahan])
jsondata = json.dumps(data, indent=None)
print(jsondata)
#print(datarow)
