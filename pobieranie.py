from urllib.request import Request, urlopen
from io import BytesIO
from zipfile import ZipFile
import datetime

def download_and_unzip(url, extract_to='.'):
    http_response = urlopen(url)
    zipfile = ZipFile(BytesIO(http_response.read()))
    zipfile.extractall(path=extract_to)

def main():
    today = datetime.date.today()
    year = today.year
    adres = 'https://www.cftc.gov/files/dea/history/fut_fin_xls_{}.zip'.format(year)
    url = Request(adres, headers={'User-Agent': 'Mozilla/5.0'})
    path = "E:\\AppData\\money\\COT\\"
    download_and_unzip(url, path)

if __name__ == '__main__':
    main()
