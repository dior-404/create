import os, sys, re, requests, bs4, time, random, json, string
from bs4 import BeautifulSoup
from datetime import datetime
try:
    import requests
except ImportError:
    os.system('pip install requests > /dev/null')
try:
    import bs4
except ImportError:
    print ('\n [×] Modul Bs4 Not installed!...\n')
    os.system('pip install bs4')
def convert(cok):
    __for = 'datr=' + cok['datr'] + ';' + ('sb=' + cok['sb']) + ';' + ('fr=' + cok['fr']) + ';' + ('c_user=' + cok['c_user']) + ';' + ('xs=' + cok['xs'])
    return __for
def inbox(session):
    time.sleep(1)
    ses = requests.Session()
    __ = str(time.time()).replace('.', '')[:13]
    data = ses.get(f"https://10minutemail.net/address.api.php?sessionid={session}&_={str(__)}").json()
    if len(data["mail_list"]) !=1:
        address = data["mail_list"][0]["subject"]
        session = address.replace('FB-', '').replace('is your Facebook confirmation code', '')
        return session
ugen = []
for xd in range(10000):
	rr = random.randint
	andro_version = str(random.randint(4,13))
	fbav = str(random.randint(50,367))+'.'+str(random.randint(0,2))+'.0.'+str(random.randint(1,20))+'.'+str(random.randint(50,300))
	fbcr = str(random.choice(['TELKOMSEL','AXIS','Indosat','XL','3SinyalKuatHemat','Tsel-PakaiMasker','XL Axiata']))
	density = str(random.choice(['1.2','1.0','2.0','2.25','3.0','3.25']))
	height = str(random.randint(333,4444))
	width = str(random.randint(344,4444))
	andro_mini = str(random.randint(3,9))+'.'+str(random.randint(0,2))+'.'+str(random.randint(0,2))
	usertrel = str(random.randint(1111,3333))
	fblc = random.choice(['en_GB','en_US','es_MX','th_TH','pl_PL'])
	fbpn = random.choice(['com.facebook.katana','com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.mlite','MessengerLite'])
	fban = random.choice(['Katana-Android','Adsmanager-Android','Facebook.lite-Android','Orca-Android','Facebook.mlite-Android','MessengerLite'])
	asu = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
	build = (str(random.choice(asu))+str(random.choice(asu))+str(random.randint(1,9))+str(random.choice(asu))+'.'+str(random.randint(111111,333333))+'.'+'00'+str(random.randint(1,9)))
	redmi = str(random.randint(1,30))
	a = random.randrange(30,200)
	b = random.randrange(1000,5000)
	c = random.randrange(10,150)
	andro = random.choice(['2','3','4','4.0.4','4.1.1','4.1.2','4.2.2','5','5.0','5.0.2','5.1.1','6','6.0','6.0.1','7','7.0','8','8.0.0','8.1','9','10','11','12','13'])
	chr = f'{a}.0.{b}.{c}'
	chrome = random.choice(['87.0.4280.101','106.0.5249.126','55.0.2883.91','79.0.3945.116','92.0.4515.159','96.0.4664.45','92.0.4515.131','91.0.4472.101','91.0.4472.120','90.0.4430.91','51.0.2704.91','78.0.3904.108','107.0.5304.54','112.0.5615.48','73.0.3683.90','85.0.4183.127','85.0.4183.101','83.0.4103.106','85.0.4183.101','83.0.4103.106','74.0.3729.157','80.0.3987.162','80.0.3987.149','78.0.3904.108','112.0.0.0','113.0.5672.162','108.0.0.0','88.0.4324.141','92.0.4515.159','104.0.5112.97','61.0.3163.98','114.0.0.0','72.0.3626.76','37.0.0.0','47.0.2526.100','42.0.2311.111','69.0.3497.100'])
	fbap = random.choice(['414.0.0.30.113','414.0.0.30.113','354.0.0.8.108','354.0.0.8.108','405.0.0.16.112','414.0.0.30.113','414.0.0.30.113','413.0.0.30.104','414.0.0.30.113','408.1.0.16.113','363.0.0.30.112'])
	fbbv = str(random.randint(111111111,999999999))
	s = random.choice(['SamsungBrowser/96.4','SamsungBrowser/19.0','SamsungBrowser/9.2','SamsungBrowser/3.0','SamsungBrowser/3.1','SamsungBrowser/3.2','SamsungBrowser/3.3','SamsungBrowser/3.4','SamsungBrowser/3.5','SamsungBrowser/3.6','SamsungBrowser/3.7','SamsungBrowser/3.8','SamsungBrowser/3.9','SamsungBrowser/4.0','SamsungBrowser/2.0','SamsungBrowser/2.1','SamsungBrowser/2.2','SamsungBrowser/2.3','SamsungBrowser/2.4','SamsungBrowser/2.5','SamsungBrowser/2.6','SamsungBrowser/2.7','SamsungBrowser/2.8','SamsungBrowser/2.9','SamsungBrowser/1.0','SamsungBrowser/1.1','SamsungBrowser/1.2','SamsungBrowser/5.0','SamsungBrowser/5.1','SamsungBrowser/5.2','SamsungBrowser/5.3','SamsungBrowser/5.4','SamsungBrowser/5.5','SamsungBrowser/5.6','SamsungBrowser/5.7','SamsungBrowser/5.8','SamsungBrowser/5.9','SamsungBrowser/6.0','SamsungBrowser/6.1','SamsungBrowser/19.0','SamsungBrowser/20.0','SamsungBrowser/21.0','SamsungBrowser/18.0','SamsungBrowser/17.0','SamsungBrowser/16.0','SamsungBrowser/15.0'])
	t = random.choice(['Build/JZO54K)','Build/LMY47V)','Build/LMY48B)','Build/LRX22C)','Build/LRX21V) ','Build/LRX22G)','Build/LRX21T)','Build/GINGERBREAD)','Build/JDQ39)','Build/KOT49H)','Build/KTU84P)','Build/LMY47X)','Build/LRX22G)'])
	mini = random.choice(['2','3','4','4.0.4','4.1.1','4.1.2','4.2.2','5','5.0','5.0.2','5.1.1','6','6.0','6.0.1','7','7.0','8','8.0.0','8.1','4.3','5.0','7.0','7.0.1','8.1.0','6.0.1;','10','11','12','13'])
	merk = random.choice(['SM-G850F','SM-G850FQ','SM-G850Y','SM-G850M','SM-G850T','SM-G850A','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','SM-J415GN','SM-J415N','SAMSUNG SM-T530','SAMSUNG SM-T530','SAMSUNG SM-T805','SAMSUNG-SM-G530AZ','SAMSUNG SM-G925K','SAMSUNG SM-G925L','SAMSUNG SM-G925T','SAMSUNG-SM-T337A','SAMSUNG SM-J110F','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','SM-G850S','SM-G850L','SM-G850K','SM-E025F','SM-J415F','SM-J415FN','SM-J415G','SAMSUNG-SM-G890A','SAMSUNG SM-T355Y','SAMSUNG SM-T817T','SAMSUNG SM-G925F','SAMSUNG SM-G928F','SAMSUNG SM-W2021)','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','SAMSUNG SM-G996B)','GT-S7500L','GT-S7500T'])
	a1 = str(random.randint(40,599))
	a2 = str(random.randint(10,99))
	a3 = str(random.randint(10,99))
	ins = f'{a1}.0.0.{a2}.{a3}'
	b4 = str(random.randint(10,99))
	b5 = str(random.randint(10,99))
	yan = f'{b4}.{b5}.0'
	c6 = str(random.randint(1,9))
	c7 = str(random.randint(1,9))
	c8 = str(random.randint(1,9))
	c9 = str(random.randint(100,999))
	qua = f'{c6}.{c7}.{c8}.{c9}'
	d10 = str(random.randint(10,99))
	d11 = str(random.randint(10000,99999))
	ed = f'{d10}.{d11}'
	bahasa = random.choice(["en","fr","ru","tr","id","pt","es","en-GB"])
	ua1 = f"Mozilla/5.0 (Linux; U; Androidy Build/NMF26X; wv).{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Chrome/.{str(rr(4, 20))}.{str(rr(420, 490))} Version/4.0"
	ua2 = f"Mozilla/5.0 (Linux; U; Android 9; SM-N950F Build/PPR1.180610.011; wv).{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Chrome/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/4.0"
	ua3 = f"Opera/9.80 (iPhone; Opera Mini/16.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua4 = f"Opera/9.80 (Android; Opera Mini/11.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	ua5 = f"Opera/9.80 (Windows Mobile; Opera Mini/5.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	uaku3 = random.choice([ua1,ua2,ua3,ua4,ua5])
	ugen.append(uaku3)
logo4 = """
\x1b[1;91m
\x1b[1;92m
\x1b[1;96m
\x1b[1;92m         {|} {|}  {|} {|}{|}{|} {|}{|}{|}
\x1b[1;97m         {|} {|}  {|}    {|}       {|}
\x1b[1;93m         {|} {|}  {|}    {|}       {|}
\x1b[1;96m         {|} {|}  {|}    {|}       {|}
\x1b[1;94m     {|}{|}   {|}{|}     {|}       {|}
\x1b[1;93m
\x1b[1;92m         Jutt Badshah Brand~
\x1b[1;91m-----------------------------------------------
\x1b[1;97m> Author : Jutt Badshah
\x1b[1;97m> Github : https://github.com/SHOOTER-MAKER
\x1b[1;97m> Facebok: Jutt Badshah
\x1b[1;97m> Version: auto create facebook
\x1b[0;97m-----------------------------------------------"""
boy = ['Ali Khan', 'Rustam Khan', 'Faisal Khan', 'Afzal Khan', 'Haider Khan', 'Suleman Khan', 'Nadeem Khan', 'Nazeer Malik', 'Nazeer Jutt', 'Nazeer Rehmani', 'Safdar Malik', 'Intzar Khan', 'Saleem Malik', 'Abdullah Malik', 'Naseer Jutt', 'Muzammil Malik', 'Fiaz Ahmad', 'Asghar Ali', 'Shabeer Ahmad', 'Irfan Ali', 'Ahmad Gujjar']
girl = ['Sajida Malik', 'Ayesha Khan', 'Nabeela Malik', 'Kinza Fatima', 'Arooj Khan', 'Muskan Khan', 'Ayesha Malik', 'Safina Malik', 'Nida Ali', 'Rimsha Ali']
ok = []
cp = []
def menu():
    os.system('clear')
    print (logo4)
    print ('            Auto create tool')
    print (47*'-')
    print ('[1]auto creat')
    print ('[2]join Facebok group')
    print ('[3] join whatsapp group')
    print (47*'-')
    sel = input('Select: ')
    if sel in['1', '01']:
        create().start()
    elif sel in ['2', '02']:
        os.system('xdg-open https://www.facebook.com/groups/262660289344669/?ref=share_group_link')
        menu()
    elif sel in ['3', '03']:
        os.system('xdg-open https://chat.whatsapp.com/C4EokyLxEaZGBlyJ99M3pA')
        menu()
    else:
        print ('select valid option')
        time.sleep(3)
        menu()
class create:

    def __init__(self):
        self.loop = 0
        self.gender = []

    def start(self):
        os.system('clear')
        print (logo4)
        print ('[1] Boys name ids')
        print ('[2] girls name ids')
        print (47*'-')
        gen = input('select: ')
        print (47*'-')
        if gen in ['1', '01']:
            self.gender.append('boy')
        elif gen in ['2', '02']:
            self.gender.append('girl')
        else:
            self.gender.append('boy')
        print ('Example 1000, 2000, 5000, 10000')
        lim = int(input('limit: '))
        os.system('clear')
        print (logo4)
        agent = random.choice(ugen)
        headers = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': agent,
            'viewport-width': '980',
        }
        headers1 = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': agent,
        }
        OO = '\033[0;97m'
        for x in range(lim):
            self.loop += 1
            sys.stdout.write(f'\r {OO}[Creat-fb] {OO}{self.loop}/{str(lim)} OK:{len(ok)} - CP:{len(cp)}{OO} '),
            sys.stdout.flush()
            if 'boy' in self.gender:
                name = random.choice(boy).split(' ')
                sex = '2'
            elif 'girl' in self.gender:
                name = random.choice(girl).split(' ')
                sex = '1'
            try:
                ses = requests.Session()
                buildses = user = "".join(random.SystemRandom().choice("qwertyuiopasdfghjklzxcvbnm0987654321") for i in range(26))
                create = ses.get(f"https://10minutemail.net/address.api.php?new=1&sessionid={buildses}&_={int(datetime.now().timestamp() * 1000)}").json()
                mail = {"mail": create["permalink"]["mail"], "session": create["session_id"]}
                email = mail['mail']
                session = mail['session']
            except KeyError:
                pass
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass
            passw = name[0]+name[1]+str(random.randint(111,999))
            try:
                self.ses = requests.Session()
                a = self.ses.get('https://m.facebook.com/reg?_fb_noscript', headers=headers)
                loger = re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1)
                ref = BeautifulSoup(a.text, 'html.parser').find('form', {'action': True, "id":"mobile-reg-form", "method":"post"})
                bl = ['lsd', 'jazoest', 'cpp', 'reg_instance', 'submission_request']
                bz = ['reg_impression_id', 'ns']
                self.data = {}
                for v in ref('input'):
                    if v.get('name') in bl:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({'helper': ''})
                for v in ref('input'):
                    if v.get('name') in bz:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({
                    "zero_header_af_client": "",
                    "app_id": "103",
                    "logger_id": re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1),
                    "field_names[0]": "firstname",
                    "firstname": name[0],
                    "lastname": name[1],
                    "field_names[1]": "birthday_wrapper",
                    "birthday_day": str(random.randint(1,28)),
                    "birthday_month": str(random.randint(1,12)),
                    "birthday_year": str(random.randint(1992,2004)),
                    "age_step_input": "",
                    "did_use_age": "",
                    "field_names[2]": "reg_email__",
                    "reg_email__": email,
                    "field_names[3]": "sex",
                    "sex": sex,
                    "preferred_pronoun": "",
                    "custom_gender": "",
                    "field_names[]": "reg_passwd__",
                    "reg_passwd__": passw,
                    "submit": "Sign Up",
                    "name_suggest_elig": "false",
                    "was_shown_name_suggestions": "false",
                    "did_use_suggested_name": "false",
                    "use_custom_gender": "",
                    "guid": "",
                    "pre_form_step": "",
                })
                gett = self.ses.post('https://m.facebook.com'+ref['action'], headers=headers1, data=self.data)
                getts = self.ses.get('https://m.facebook.com/login/save-device/?login_source=account_creation&logger_id='+loger+'&app_id=103', headers=headers1)
                data1 = {}
                data2 = {}
                data3 = {}
                cok = self.ses.cookies.get_dict()
                if 'checkpoint' in getts.url:
                    cp.append(email+passw)
                    print ('\r\033[1;33m[CP] '+cok['c_user']+' | '+passw+'\033[0;97m     ')
                dbl = ['fb_dtsg', 'jazoest', 'flow', 'next', 'nux_source']
                for x in BeautifulSoup(getts.text, 'html.parser').find_all('form', {'method': 'post'}):
                    if '/login/device-based/update-nonce/' in str(x):
                        for v in x('input'):
                            if v.get('name') in dbl:
                                try:
                                    data1.update({v.get('name'):v.get('value')})
                                except:
                                    pass
                        data1.update({'submit': 'OK'})
                        po = self.ses.post('https://m.facebook.com'+x.get('action'), headers=headers1, data=data1)
                        for x in BeautifulSoup(po.text, 'html.parser').find_all('form', {'method': 'post'}):
                            if 'confirmation_event_location=cliff' in str(x):
                                for v in x('input'):
                                    if v.get('name') in dbl:
                                        try:
                                            data2.update({v.get('name'):v.get('value')})
                                        except:
                                            pass
                                code = inbox(session)
                                data2.update({'c': code, 'submit': 'Confirm'})
                                rex = self.ses.post('https://m.facebook.com'+x.get('action'), headers=headers1, data=data2)
                                if 'checkpoint' in rex.url:
                                    cok = self.ses.cookies.get_dict()
                                    cp.append(email+passw)
                                    print ('\r\033[1;33m[CP] '+cok['c_user']+' | '+passw+'\033[0;97m     ')
                                else:
                                    coki = (";").join([ "%s=%s" % (key, value) for key, value in self.ses.cookies.get_dict().items() ])
                                    cok = self.ses.cookies.get_dict()
                                    print ('\r\033[1;32m[OK] '+cok['c_user']+' | '+passw+' | '+coki+'\033[0;97m     ')
                                    ok.append(email+passw)
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass
        print ('process has been completed')
        print (47*'-')
        print ('\033[1;32mTotal ids > Ok/' +str(len(ok)) + ' CP/' + str(len(cp)))
        print (47*'-')
        input('back')
        menu()
menu()
