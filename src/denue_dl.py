from bs4 import BeautifulSoup
import zipfile
import os
import io
import requests

cwd = os.path.dirname(os.getcwd())
data_dir = os.path.join(cwd, 'data')
denue_dir = os.path.join(data_dir, 'denue')
with open(os.path.join(denue_dir, 'DescargaMasivaOD.xml'),'r') as infile:
    files = infile.read()

cwd = os.path.dirname(os.getcwd())
data_dir = os.path.join(cwd, 'data')
denue_dir = os.path.join(data_dir, 'denue')

with open(os.path.join(denue_dir, 'DescargaMasivaOD.xml'),'r') as infile:
    files = infile.read()

parsed = BeautifulSoup(files, "xml")
urls = [x.text for x in parsed.find_all('Archivo')]
files_dl = [x for x in urls if ((len(x.split('_'))==4) or ('2015' in x)) & ('csv' in x)]
files_subset = [x for x in files_dl if ('2015' not in x) and any(y in x for y in ['22','51'])]
files_subset

data = requests.get(urls[0])

def get_denue_data(url):
    print(f'working on {url}')

    #Download
    dl = requests.get(url)

    #Parse
    zf = zipfile.ZipFile(io.BytesIO(dl.content))

    if '2015' in url: #If it is a 2015 file
        zf.extractall(os.path.join(denue_dir,'inegi_2015'))
    else:
        zf.extractall(os.path.join(denue_dir,'inegi_2018'))
    print(f'{url} done')

[get_denue_data(x) for x in files_subset]
dl = requests.get(files_subset[0])
zf = zipfile.ZipFile(io.BytesIO(dl.content))
for f in zf.filelist:
    print(f.filename)
