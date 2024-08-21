import os,sys,time,random

def logo():
    print('\033[1;36m   ⊰᯽⊱─╌⊰❊⊱╌──┈⊰᯽⊱𝐗𝐘𝐋𝐎𝐍⊰᯽⊱┈──╌⊰❊⊱╌─⊰᯽⊱')
    print('\033[1;36m    ＵＳＥＲ - ＡＧＥＮＴ - ＭＡＫＥＲ')
    print('\033[1;36m   ⊰᯽⊱─╌⊰❊⊱╌──┈⊰᯽⊱𝐗𝐘𝐋𝐎𝐍⊰᯽⊱┈──╌⊰❊⊱╌─⊰᯽⊱')

def lxx():
    print('\033[1;36m   ⊰᯽⊱─╌⊰❊⊱╌──┈⊰᯽⊱ ⊰᯽⊱┈──╌⊰❊⊱╌─⊰᯽⊱')
def lnx():
    print('\n'+'\033[1;31m┃😈┃\033[47m\033[1;46m   𝗧𝗛𝗘 𝐀𝐁𝐃𝐔𝐋𝐋𝐇𝐀    ➤   𝐗𝐘𝐋𝐎𝐍   \033[40m\033[00m\x1b[1;91m┃😈┃\n')
    
def main():
    os.system('clear')
    logo();os.system('xdg-open https://t.me/Abdullha_404')
    try:limit = int(input('\n\033[1;32m 𝐄𝐍𝐓𝐄𝐑 𝐋𝐈𝐌𝐈𝐓 : '))
    except ValueError:
        lxx()
        print(' Use Limit Only Number\'s ! ')
        time.sleep(2.5)
        main()
    for x in range(limit):
        user_agents = []
        colour = random.choice(['\033[91m','\033[92m','\033[93m','\033[94m','\033[95m','\033[96m'])
        user_agent = f"[FBAN/FB4A;FBAV/"+str(random.randint(199,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(99,199))+";FBBV/"+str(random.randint(111111111,999999999))+";FBDM/{density="+str(random.randint(2,3))+"."+str(random.randint(2,5))+",width=1080,height="+str(random.randint(1400,1499))+"};FBLC/"+str(random.choice(["cs_CZ","en_GB","en_US","lt_LT","pl_PL","id_ID","ru_RU","pt_PT","he_IL","hi_IN","nl_NL"," it_IT","en_IN","es_ES","en_PK"]))+";FBRV/"+str(random.randint(111111111,999999999))+";FBCR/"+str(random.choice(["Tele2You","Telenor","FASTWEB","Banglalink","Sprint","Jazz","Vodafone IN","Vi India","Tele2 LT","Jio 4G","EE","Oi","MtelBG","AT&amp;amp-T","Ufone","Azercell"]))+";FBMF/Xiaomi;FBBD/"+str(random.choice(["xiaomi","Xiaomi","Redmi"]))+";FBPN/com.facebook.katana;FBDV/"+str(random.choice(["M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2003J15SC","MI MAX 2","AT&amp;amp-T","Redmi Note 4", "Redmi 4X","Redmi Note 8 Pro","Redmi Note 5","Redmi Note 8T","Redmi 6A","Redmi 7A","MI PLAY","MI 8 Lite","Mi 9T","Mi A2 Lite"," Mi 9", "M2101K7AG"]))+";FBSV/"+str(random.randint(9,12))+";FBOP/1;FBCA/arm64-v8a:;]"
        lnx();print(colour+user_agent)
        open('/sdcard/XYLON-UA.txt', 'a').write(''+user_agent+'\n\n')
    lnx()
    print(f'\n{colour}</>{colour} 𝐀𝐋𝐋 𝐔𝐒 𝐒𝐀𝐕𝐄𝐃 IN{colour} - {colour}XYLON-UA.txt')
    lxx()
    lj=input(f'{colour}</> 𝐑𝐔𝐍 𝐀𝐆𝐀𝐈𝐍 ? [Y/n] : ')
    if lj in ('y','Y'):
        main()
    elif lj in ('n','N'):
        lxx()
        sys.exit(f'{colour}</> 𝐓𝐇𝐀𝐍𝐊 𝐅𝐎𝐑 𝐗𝐘𝐋𝐎𝐍 𝐓𝐎𝐎𝐋 ')
    else:
        lxx()
        sys.exit()
        
main()

