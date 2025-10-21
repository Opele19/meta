lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII, llllllllllllIll = print, range, bool, open, len

from requests import Session as IlIIIlIllllllI, RequestException as lIlIlllIIlIllI
from random import randint as llIlIIIIIIIlII, choice as IlIlIIIllIlIll
from bs4 import BeautifulSoup as IlIIlIIllIIlII

def IIllIlIlIIIllIllII():
    lIIlllllIIlIlIlIll = 'https://whatmyuseragent.com'
    lIlIlIIlIlIIIIllll = ['xi/xiaomi', 'if/infinix', 'tb/tecno-mobile', 'sa/samsung', 'op/oppo']
    lllllllllllllll('sedang create user agent')

    def llIllllIlIlIIIIIll(lIIlllllIIIIlllIIl, IlllllIllllIIlIlII):
        llIIIllIIlIlIlllll = f'{lIIlllllIIlIlIlIll}/brand/{IlllllIllllIIlIlII}'
        try:
            lIIIlllIllIlIlllIl = lIIlllllIIIIlllIIl.get(llIIIllIIlIlIlllll)
            lIIIlllIllIlIlllIl.raise_for_status()
        except lIlIlllIIlIllI as IIIllIlIIlIlIlIllI:
            lllllllllllllll('Gagal mengakses halaman:', IIIllIlIIlIlIlIllI)
            return None
        lllIlllllIIIlllllI = IlIIlIIllIIlII(lIIIlllIllIlIlllIl.text, 'html.parser')
        IIIlIIllIIIlllllll = []
        IlllIlIlIIIIlllIlI = []
        for IllllllIIlllIlIllI in lllIlllllIIIlllllI.find_all('a'):
            llIIIlIIIlIIIllIII = IllllllIIlllIlIllI.get('href', '')
            if '/device/' in llIIIlIIIlIIIllIII:
                IlllIIIlIIlllIIlIl = IllllllIIlllIlIllI.get_text(strip=lllllllllllllIl(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))
                if IlllIIIlIIlllIIlIl and IlllIIIlIIlllIIlIl not in IIIlIIllIIIlllllll:
                    IIIlIIllIIIlllllll.append(IlllIIIlIIlllIIlIl)
                    IlllIlIlIIIIlllIlI.append(llIIIlIIIlIIIllIII)
        if not IIIlIIllIIIlllllll:
            lllllllllllllll('Tidak ditemukan daftar device pada halaman tersebut untuk brand', IlllllIllllIIlIlII)
            return None
        lIIIIlIIIIIlIIIlll = llIlIIIIIIIlII(0, llllllllllllIll(IIIlIIllIIIlllllll) - 1)
        llIllIlIIIIlIllIII = lIIlllllIIlIlIlIll + IlllIlIlIIIIlllIlI[lIIIIlIIIIIlIIIlll]
        try:
            lIlIlIIIIlIIlllllI = lIIlllllIIIIlllIIl.get(llIllIlIIIIlIllIII)
            lIlIlIIIIlIIlllllI.raise_for_status()
        except lIlIlllIIlIllI as IIIllIlIIlIlIlIllI:
            lllllllllllllll('Gagal mengakses halaman device:', IIIllIlIIlIlIlIllI)
            return None
        IlIIlIlIllIIlllIlI = IlIIlIIllIIlII(lIlIlIIIIlIIlllllI.text, 'html.parser')
        lllllIIIllIIIIIllI = [llIlIIlIlllIllllIl.get_text(strip=lllllllllllllIl(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1)) for llIlIIlIlllIllllIl in IlIIlIlIllIIlllIlI.find_all('td', class_='useragent')]
        if lllllIIIllIIIIIllI:
            return IlIlIIIllIlIll(lllllIIIllIIIIIllI)
        else:
            lllllllllllllll('Tidak ditemukan user agent pada halaman device tersebut.')
            return None
    IlIlIIllllllIIIIII = []
    with IlIIIlIllllllI() as lIIlllllIIIIlllIIl:
        for IlIIlIIIlIIIlllIII in llllllllllllllI(5):
            IlllllIllllIIlIlII = IlIlIIIllIlIll(lIlIlIIlIlIIIIllll)
            IlllIIlIIlllIIIIIl = llIllllIlIlIIIIIll(lIIlllllIIIIlllIIl, IlllllIllllIIlIlII)
            if IlllIIlIIlllIIIIIl:
                lllllllllllllll(IlllIIlIIlllIIIIIl)
                IlIlIIllllllIIIIII.append(IlllIIlIIlllIIIIIl)
            else:
                IIllIlllIlIllIIIIl = 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36'
                lllllllllllllll(IIllIlllIlIllIIIIl)
                IlIlIIllllllIIIIII.append(IIllIlllIlIllIIIIl)
    with lllllllllllllII('user.txt', 'w', encoding='utf-8') as IIllIlllIlIIIIIIlI:
        for IlllIIlIIlllIIIIIl in IlIlIIllllllIIIIII:
            IIllIlllIlIIIIIIlI.write(IlllIIlIIlllIIIIIl + '\n')