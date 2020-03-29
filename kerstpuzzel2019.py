opdracht = 'cdzadrbgqhiuhmfdmzghdqnmcdqzyhimz`kkdl``kzldszb`dr`qzudqbhiedqc.cdz`msvnnqcdmzjtmzid,zudqbhiedqczldszcdydkecdzrkdtsdkz`krzcdzadrbgqhiuhmf,zhmzcdzvnnqcyndjdqzuhmcdm.zcdzkdssdqrzchdznudqakhiudmzfdudmzcdzdhmcnocq`bgs'
invoer3 = 'xgtnkejvblcrcpubmgkagtbowvuwjkvq'
invoer4 = 'dinruwlqjcydqcghcqlhwcehvwddqghcqddpcydqcghcedqgcydqcmdqcnhlbhu'
invoer5 = 'tivlhdiizh`aikphswvqvohdmzl'
invoer6 = 'bxwtnim`jpbialq`nnoimrbijjwimnitxwrwp' 
invoer7 = 'rsmsnqosfoenpsroqvgnrsnqosfoe-fozor'
invoer8 = 'ibbeaoo`nioanyhafgfqvwzrsenrsnybbawau'
invoer9 = 'iorsenioanybawaunrhaqoanioanoeozhsa'
invoer10 = 'dhgbgdkbcdtougtxyyetuwamtougtxyt`kbcsytcu`yk'
invoer11 = 'jnmhmfzi`mzy`bgsyv``qcznnjzadjdmcz`krz‘i`mzynmcdqz____’'
invoer12 = '`clhq``kzlhbghdkzcdzqtxsdqzhrzhmzcdydzl``mczfdanqdm'

def versleutel(invoer, ROT):
    for letter in invoer:
        nummer = ord(letter) - 96
        geroteerdNummer = (nummer + ROT) % 27
        geroteerdKarakter = chr(geroteerdNummer + 96)
        print(geroteerdKarakter, end='')

versleutel('maart', -1)
print()

for ROT in range(1, 26):
    print(ROT, end=': ')
    versleutel(opdracht, ROT)
    print('')
