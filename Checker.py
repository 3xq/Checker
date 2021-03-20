from validate_email import validate_email
from threading import Thread
from requests import get

CommonWords = get('http://www.mit.edu/~ecprice/wordlist.10000').text
ThreeDigitNumberPatterns = ['123','456','789','111','222','333','444','555','666','777','888','999','000']
ThreeCharacterPatterns = ['aaa','bbb','ccc','ddd','eee','fff','ggg','hhh','iii','jjj','kkk','lll','mmm','nnn','ooo','ppp','qqq','rrr','sss','ttt','uuu','vvv','www','xxx','yyy','zzz','asd','bad','cat','lol','dog','god','the','too']

Emails = ['shaw.ca', 'charter.net', 'mchsi.com']

def align(Str):
    return ' '+str(Str)+str(' '*int(60-len(Str)))+' |'

def toBool(Value):
    if Value == 'True':
        return True
    elif Value == 'False':
        return False
    elif Value == 'None':
        return 'NO RTRN'

def alignBool(Bool):
    return '| '+str(Bool)+str(' '*int(7-len(str(Bool))))+' |'

def align2(Str,Sp):
    return ' '+str(Str)+str(' '*int(Sp-len(str(Str))))+' |'

def alignScores(Username,Score):
	 return '|'+align2(Score,3)+align2(Username,35)

def RateUser(Username):
	#Check if 3 char:
	if len(Username) == 3:
		if Username.isnumeric() == True:
			if Username in ThreeDigitNumberPatterns:
				return alignScores(Username,81)
			else:
				return alignScores(Username,72)
		elif '_' in Username:
			Gsub = Username.replace('_','')
			if Gsub.isnumeric():
				return alignScores(Username,89)
		elif Username in ThreeCharacterPatterns:
			return alignScores(Username,84)
	elif len(Username) > 20:
		if '[' in Username:
			return alignScores(Username,94)
		else:
			return alignScores(Username,90)
	elif ' ' in Username:
		if len(Username) > 8:
			return alignScores(Username,95)
		else:
			return alignScores(Username,97)
	elif Username.lower() in CommonWords:
		return alignScores(Username,79)
	else:
		return alignScores(Username,59)

open("account.txt", "w").write(get('https://raw.githubusercontent.com/3xq/database_leaks/main/roblox_50k').text)
file = open('account.txt', 'r', encoding='windows-1252').read().strip().split('\n')
open('emailz.txt','x')

def Check(line):
	if ':' in line:
		Strip = line.strip()
		Strip = Strip.split(':')
		Username = Strip[len(Strip)-3]
		Email = Strip[len(Strip)-1]
		Split = Email.split('@')
		Domain = Split[len(Split)-1]
		if Domain.lower() in Emails:
			if len(Email) < 99:
				Valid = validate_email(Email,verify=True)
				OUTPUT=str(RateUser(Username))+alignBool(toBool(str(Valid)))+align(Email)
				if 'None' not in OUTPUT:
					print(OUTPUT.replace('||','|'))
					emailz = open('emailz.txt', 'a')
					emailz.write(OUTPUT.replace('||','|')+'\n')

def StripNone(txt):
	lines = open(txt,'r',encoding='windows-1252').readlines()
	open(txt,'w').write('')
	file = open(txt,'a')
	for line in lines:
		if line.strip("\n") != "None":
			file.write(line)

for line in file:
    Thread(target=Check, args=[line]).start()

StripNone('emailz.txt')
