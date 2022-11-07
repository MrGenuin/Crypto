from sre_compile import isstring
import pyfiglet as fig
import termcolor as color
import math as mt
import fractions as fra
import random as ran
from re import I
import numpy as np

def iden ():
     print(color.colored("-------------------------------------------------------------------------------------\n",'blue',attrs=['blink']))  
     print(color.colored("Welcom To CRYPTOZIZ, a tool that Provides many classical Cryptography Techniques    |",'yellow',attrs=['blink']))
     print(color.colored("This Tool was created By Eng: 'Aziz Abdulaziz Ahmed Al-Qwati'                       |",'yellow',attrs=['blink']))
     print(color.colored("As Final Requirments for Cryptography Subject at Alrazi University/Yemen 2022/10/22 |",'yellow',attrs=['blink']))
     print(color.colored("\n-----------------------------------------------------------------------------------\n",'blue',attrs=['blink']))
     return

 
def LetterToNumber(letter):
    alpha,i=[],97
    while i!=123:
       alpha.append(i)
       i=i+1
    letter=letter.lower()
    return(alpha.index(ord(letter)))


def NumberToLetter(number):
    alpha,i=[],97
    while i!=123:
       alpha.append(chr(i).upper())
       i=i+1
    return(alpha[number%26])

#OR
""" alpha="ABCDEFGHIGKLMNOPQRSTUVWXYZ"
numbers=dict(zip(alpha,range(len(alpha))))
letters=dict(zip(range(len(alpha)),alpha)) """


def go_on():
    print(color.colored("--------------------------------------------------------------",'blue',attrs=['bold']))
    print(color.colored("---------------- Press Any Key To Continue--------------------",'blue',attrs=['bold']))
    print(color.colored("--------------------------------------------------------------",'blue',attrs=['bold']))
    input();
    return

def MultiplicativeCipherKey(key,for_rev_key):
    KeyToEnc=[]
    KeyToDec=[]
    for i in range(0,26):
        for j in range(0,26):
            if (i*j)%26==1:
                KeyToEnc.append(i)
                KeyToDec.append(j)
                if i==key:
                    rev_key=j 
    if for_rev_key!='':
        return rev_key
    if KeyToEnc.count(key)!=0 or KeyToDec.count(key)!=0: 
       return True
    else:
       return False

def caeser_encrypt(plain_text,key):
   cipher_text="";
   for i in range(len(plain_text)):
          plain_text=plain_text.upper()
          if(plain_text[i]==" "):
                cipher_text+=""
          else:
                cipher_text=cipher_text+NumberToLetter(LetterToNumber(plain_text[i])+key)
   return cipher_text                
                
def caeser_decrypt(cipher_text,key):
    plain_text =""  
    for i in range(len(cipher_text)):
        cipher_text=cipher_text.upper()
        if(cipher_text[i]==" "):
            plain_text+=" "
        else:
            plain_text=plain_text+NumberToLetter(LetterToNumber(cipher_text[i])-key)
    return plain_text
        
                
def Multiplicative_cipher_encrypt(plain_text,key):
    cipher_text=""
    for i in range(len(plain_text)):
        plain_text=plain_text.upper()
        if plain_text[i]==" ":
            cipher_text+=" "
        else:
            cipher_text=cipher_text+NumberToLetter(LetterToNumber(plain_text[i])*key)
    return cipher_text
            
        
def Multiplicative_cipher_decrypt(cipher_text,key):
    plain_text=""
    for i in range(len(cipher_text)):
        cipher_text=cipher_text.upper()
        if cipher_text[i]==" ":
            plain_text+=" "
        else:
            plain_text=plain_text+NumberToLetter(LetterToNumber(cipher_text[i])*key)
    return plain_text


def Affine_cipher_encrypt(plain_text,key1,key2):
    cipher_text=""
    for i in range(len(plain_text)):
        plain_text=plain_text.upper()
        if plain_text[i]==" ":
            cipher_text+=" "
        else:
            cipher_text=cipher_text+NumberToLetter(LetterToNumber(plain_text[i])*key1+key2)
    return cipher_text

def Affine_cipher_decrypt(cipher_text,key1,key2):
    plain_text=""
    for i in range(len(cipher_text)):
        cipher_text=cipher_text.upper()
        if cipher_text[i]==" ":
            plain_text+=" "
        else:                  
            plain_text=plain_text+NumberToLetter((LetterToNumber(cipher_text[i])+(26-key2))*key1)
    return plain_text


def AutoKey_cipher_encrypt(plain_text,key):
    cipher_text=" "
    plain_text=plain_text.upper()
    plain_text=plain_text.replace(" ","")
    cipher_text=cipher_text+NumberToLetter(LetterToNumber(plain_text[0])+key)
    for i in range(1,len(plain_text)):
        if plain_text[i]==" ":
            cipher_text=cipher_text+" "
        else:
            cipher_text=cipher_text+NumberToLetter(LetterToNumber(plain_text[i])+LetterToNumber(plain_text[i-1]))
    return cipher_text


def AutoKey_cipher_decrypt(cipher_text,key):
    plain_text=""
    cipher_text=cipher_text.upper()
    plain_text=plain_text+NumberToLetter(LetterToNumber(cipher_text[0])-key)
    for i in range(1,len(cipher_text)):
        plain_text=plain_text+NumberToLetter(LetterToNumber(cipher_text[i])-LetterToNumber(plain_text[i-1]))
    return plain_text


def get_plaintext(plain_text):
    n=0
    if len(plain_text)%2!=0:
        n=1
    for i in range(0,len(plain_text)-n,2):
        if(plain_text[i]==plain_text[i+1]):
            plain_text=plain_text[:i+1]+'x'+plain_text[i+1:]
    if(len(plain_text))%2!=0:
        plain_text=plain_text+"x"
    return plain_text

def key():
    key=[['p','z','g','b','q'],
         ['d','l','h','m','e'],
         ['y','x','k','w','t'],
         ['v','c','f','i','n'],
         ['o','a','r','s','u']]
    return key

def Plaiyfair_cipher_encrypt(text):
    message = get_plaintext(text)
    k = key()
    message.replace("j","i")
    cipher=''
    for m in range(0, len(message)- 1, 2):
        for i in range(5):
            for j in range(5):
                if message[m] == k[i][j]:
                    i1=i
                    j1=j
                if message[m+1] == k[i][j]:
                    i2=i
                    j2=j
        if i1==i2:
            if j1 != 4:
                cipher=cipher+k[i1][j1+1]
            else:
                cipher=cipher+k[i1][0]
            if j2!=4:
                cipher=cipher+k[i2][j2+1]
            else:
                cipher=cipher+k[i2][0]
        if j1==j2:
            if i1 != 4:
                cipher=cipher+k[i1+1][j1]
            else:
                cipher=cipher+k[0][j1]
            if i2!=4:
                cipher=cipher+k[i2+1][j2]
            else:
                cipher=cipher+k[0][j2]
        if i1 != i2 and j1 != j2:
            cipher=cipher+k[i1][j2]
            cipher=cipher+k[i2][j1]
    return cipher

def Plaiyfair_cipher_decrypt(text):
    message = text
    k = key()
    plain=''
    for m in range(0, len(message)- 1, 2):
        for i in range(5):
            for j in range(5):
                if message[m] == k[i][j]:
                    i1=i
                    j1=j
                if message[m+1] == k[i][j]:
                    i2=i
                    j2=j
        if i1==i2:
            if j1 != 0:
                plain=plain+k[i1][j1-1]
            else:
                plain=plain+k[i1][4]
            if j2!=0:
                lain=plain+k[i2][j2-1]
            else:
                plain=plain+k[i2][4]
        if j1==j2:
            if i1 != 0:
                plain=plain+k[i1-1][j1]
            else:
                plain=plain+k[4][j1]
            if i2!=0:
                plain=plain+k[i2-1][j2]
            else:
                plain=plain+k[4][j2]
        if i1 != i2 and j1 != j2:
            plain=plain+k[i1][j2]
            plain=plain+k[i2][j1]
    return plain





def Return_valid_Vigenere_key(plain_text,key):
    new_key=""
    n=0
    if(len(plain_text)==len(key)):
        new_key=key
    else:
       for i in range(len(plain_text)):
            if n>=len(key):
                n=0
            new_key=new_key+key[n]
            n=n+1
    return(new_key)
    
def Vigenere_cipher_encrypt(plain_text, key): 
    encrypt_text = []
    plain_text=plain_text.replace(" ","")
    for i in range(len(plain_text)): 
        x = (ord(plain_text[i]) +ord(key[i])) % 26
        x += ord('A') 
        encrypt_text.append(chr(x)) 
    return("" . join(encrypt_text)) 

def Vigenere_cipher_decrypt(cipher_text,key):
    cipher_text=cipher_text.upper()
    key=key.upper()
    plain_text=""
    for i in range(len(cipher_text)):
        plain_text+=NumberToLetter(LetterToNumber(cipher_text[i])-LetterToNumber(key[i]))
    return plain_text

   
   
   
def Return_hill_key_as_array(key,block) :
    n=0
    new_key=np.zeros((block,block),dtype=np.int32)
    for i in range(block):
        for j in range(block):
            new_key[i][j] =LetterToNumber(key[n])
            n+=1
    return new_key

def Return_valid_Hill_plain(text,el) :
    while True:   
          if len(text)!=(el*el):
               text+=""
          else:
              break
    return text

def check_valid_string_input(text):
    valid =True
    for i in range(len(text)):
        if ord(text[i])<97 or ord(text[i])>122:
            valid= False
            break
    return valid

def get_valid_hill_plain_text(text,block):
    text=text.lower().replace(" ","")
    if len(text)<block:
        print("Shorter text than size of block ,Try again")
    elif len(text)==block*block:
        el=block
    elif len(text) <block*block:
        el=int((len(text)/block)+1)
        text=Return_valid_Hill_plain(text,el)
    elif len(text)>block*block:
        if len(text)%block==0:
            el=len(text)/block
        else:
            el=int((len(text)/block)+1)
    plain=[[0]*el for i in range(block)]
    n=0
    for i in range(block):
        for j in range(el):
            if n>=len(text): break
            plain[i][j]=LetterToNumber(text[n])
            n+=1
    return plain

def check_hill_decrypr_text(cipher,block):
    if len(cipher)==block*block:
        el=block
    elif len(cipher) <block*block:
        print("Invalid Cipher text")
        return
    elif len(cipher)>block*block:
        if len(cipher)%block==0:
            el=len(cipher)/block
        else:
            el=int((len(cipher)/block)+1)
    return int(el)
    
def Return_hill_decrypt_as_array(cipher,block,le) :
    n=0
    new_cipher=np.zeros((block,le),dtype=np.int32)
    for i in range(block):
        for j in range(le):
            new_cipher[i][j] =LetterToNumber(cipher[n])
            n+=1
    return new_cipher    

def return_matrix_inverse(key):
    try:
        det=np.linalg.det(key)
        cof=np.linalg.inv(key).T *det
        adj=np.transpose(cof)
        inve=adj/det
        return inve
    except Exception as ex:
        print("Matrix has no inverse value")

def generate_hill_key(block):
    while True:
        try:       
            collect=[[0]*block for i in range (block)]
            for i in range(block):
                for j in range(block):
                    collect[i][j]=ran.randint(2,6)
            inverse=return_matrix_inverse(collect)
            if (np.identity(block)==inverse).all and np.linalg.det(inverse) !=0:
                    return collect
                    break
        except ValueError as ex:
            print("Searching for Proper Matrix for encryption...")
            
def hill_cipher_encrypt(key,text,block):
    cipher=""
    cipher_text=np.dot(key,text)%26
    for i in range(block):
        for j in range(len(cipher_text[0])):
            cipher+=NumberToLetter(cipher_text[i][j])
    return cipher
  



def Rail_Fence_Cipher_Encrypt(plain_text):
    plain_text =plain_text.replace(" ","")
    plain_text1=""
    plain_text2=""
    for i in range(len(plain_text)):
        if i %2==0:
           plain_text1+=plain_text[i]+"  "
        if i %2!=0:
            plain_text2+=" "+plain_text[i]+" "
    print("\t"+plain_text1)
    print("\t"+plain_text2)
    cipher_text=plain_text1+plain_text2           
    return cipher_text.upper() 

def Rail_Fence_Cipher_Decrypt(cipher_text): 
    half_of_cpiher=int(len(cipher_text)/2)
    plain_text=""
    if len(cipher_text)%2!=0:
        cipher_text1=cipher_text[:half_of_cpiher+1]
        cipher_text2=cipher_text[half_of_cpiher+1:]
        for i in range (len(cipher_text2)):
            plain_text+=cipher_text1[i]+cipher_text2[i]
        return plain_text+cipher_text1[len(cipher_text1)-1]
    else:
        cipher_text1=cipher_text[:half_of_cpiher]
        cipher_text2=cipher_text[half_of_cpiher:]
    for i in range (len(cipher_text2)):
        plain_text+=cipher_text1[i]+cipher_text2[i]
    return plain_text







def Shift_Cipher1():
    while True:
         try:
            plain_text=input("Enter Plain Text To Encrypt: ")
            key=int(input("Enter Key: "))
            if(key>25 or key <0):
                print("Invalid Key, Try key between 1:25")
            else:
                print("The Cipher Text is: ", caeser_encrypt(plain_text,key))
                break
         except ValueError as ex:
             print("Invalid Input,Try insert String data")
    return

def Shift_Cipher2():
    while True:
         try:
            cipher_text=input("Enter Cipher Text To Decrypt: ")
            key=int(input("Enter Key: "))
            if(key>25 or key <0):
                print("Invalid Key, Try key between 1:25")
            else:           
                print("The Plain Text is: ", caeser_decrypt(cipher_text,key))
                break
         except ValueError as ex:
             print("Invalid Input,Try insert String data")
    return





def Multiplicative_cipher1():
    while True:
        try:
            plain_text=input("Enter Plain Text To Encrypt: ")
            key=int(input("Enter Key: "))
            if MultiplicativeCipherKey(key,''):
                print("The Cipher Text is: ", Multiplicative_cipher_encrypt(plain_text,key))
                break
            else:
                print(color.colored("Key Has No Reverse Value",'yellow'))
        # or(as general) // except Exception as ex:
        except ValueError as ex:
            print("Invalid Input, Try insert valid data")
    return

def Multiplicative_cipher2():
    while True:
        try:
            cipher_text=input("Enter Cipher Text To Decrypt: ")
            key=int(input("Enter Key: "))
            if MultiplicativeCipherKey(key,''):
                key=MultiplicativeCipherKey(key," Aziz")
                print("The Plain Text is: ",Multiplicative_cipher_decrypt(cipher_text,key))
                break
            else:
                print(color.colored("Multiplicative Key Has No Reverse Value",'yellow'))
        except ValueError as ex:
            print("Invalid Value, Try Agin: ")
      
    return





def Affine_cipher1():
    while True:
        try:
            plain_text=input("Enter Plain Text To Encrypt: ")
            key1=int(input("Enter Multiplicative Encrypt Key: "))            
            key2=int(input("Enter Additive Encrypt Key: "))          
            if MultiplicativeCipherKey(key1,'') and key2 >=0 and key2<=25:
                print("The Cipher Text is: ", Affine_cipher_encrypt(plain_text,key1,key2))
                break
            else:
                print(color.colored("Multiplicative Key Has No Reverse Value OR Invalid additive key, Try again",'yellow'))
        # or(as general) // except Exception as ex:
        except ValueError as ex:
            print("Invalid Input, Try insert valid data")
    return

def Affine_cipher2():
    while True:
        try:
            cipher_text=input("Enter cipher Text To Deccrypt: ")
            key1=int(input("Enter Multiplicative Decrypt Key: "))            
            key2=int(input("Enter Additive Decrypt Key: "))
            if MultiplicativeCipherKey(key2,'') and key2 >=0 and key2<=25:
                key1=MultiplicativeCipherKey(key1,"Aziz")
                print("The Plain Text is: ", Affine_cipher_decrypt(cipher_text,key1,key2))
                break
            else:
                print(color.colored("Multiplicative Key Has No Reverse Value OR Invalid additive key, Try again",'yellow'))
        # or(as general) // except Exception as ex:
        except ValueError as ex:
            print("Invalid Input, Try again")
    return






def AutoKey_cipher1():
    while True:
        try:
            plain_text=input("Enter cipher Text To Encrypt: ")
            key=int(input("Enter Encrypt Key: "))
            if key >=0 and key <=25:
                print("The Cipher Text is: ", AutoKey_cipher_encrypt(plain_text,key))
                break
            else:
                print("Invalid Key, Try insert key between 1:25")
        # or(as general) // except Exception as ex:
        except ValueError as ex:
            print("Invalid Input, Try again")
    return

def AutoKey_cipher2():
    while True:
        try:
            cipher_text=input("Enter cipher Text To Decrypt: ")
            key=int(input("Enter Decrypt Key: "))
            if key >=0 and key <=25:
                print("The Plain Text is: ", AutoKey_cipher_decrypt(cipher_text,key))
                break
            else:
                print("Invalid Key, Try insert key between 1:25")
        # or(as general) // except Exception as ex:
        except ValueError as ex:
            print("Invalid Input, Try Again")
    return






def Play_fair_cipher1():
    while True:
        try:
            plain_text=input("Enter plain Text To Encrypt: ")
            print("The matrix used in Encryption is: \t\t")
            print("\t\t",color.colored(key(),'yellow'))
            print("The Cipher Text is: ", Plaiyfair_cipher_encrypt(plain_text))
            break
        # or(as general) // except Exception as ex:
        except ValueError as ex:
            print("Invalid Input, Insert valid Data")
    return

def Play_fair_cipher2():
    while True:
        try:
            cipher_text=input("Enter cipher Text To Decrypt: ")
            print("The plain Text is: ", Plaiyfair_cipher_decrypt(cipher_text))
            break
        # or(as general) // except Exception as ex:
        except ValueError as ex:
            print("Invalid Input, Try again")   
    return






def Vigenere_cipher1():
    while True:
        try:
            valid=True
            plain_text=input("Enter cipher Text To Encrypt: ")
            plain_text=plain_text.replace(" ","")
            key=input("Enter String Encrypt Key: ")
            key=key.lower()
            key=key.replace(" ","")
            for i in range(len(key)):
                if ord(key[i])<97 or ord(key[i])>122:
                    valid=False
            if valid:
                new_key=Return_valid_Vigenere_key(plain_text,key)
                print("The Cipher Text is: ", Vigenere_cipher_encrypt(plain_text.upper(),new_key.upper()))
                break 
            else:
                print("Only string data type is allowed as key, try again")                                
        # or(as general) // except Exception as ex:
        except ValueError as ex:
            print("Invalid input, insert string data only\n") 
    return

def Vigenere_cipher2():
    while True:
        try:
            valid=True
            cipher_text=input("Enter cipher Text To Decrypt: ")
            key=input("Enter Decrypt string Key: ")
            key=key.lower()
            key=key.replace(" ","")
            for i in range(len(key)):
                if ord(key[i])<97 or ord(key[i])>122:
                    valid=False
            if valid:
                new_key=Return_valid_Vigenere_key(cipher_text,key)
                print("The Plain Text is: ", Vigenere_cipher_decrypt(cipher_text,new_key))
                break
            else:
                print("Only string data type is allowed as key, try again")
        # or(as general) // except Exception as ex:
        except ValueError as ex:
            print("Invalid Input, Try again")
    return




def Hill_cipher1():
    while True:
        try:         
            block=int(input("Enter square size of block: "))
            text=input("Enter Plain text: ")
            text=text.replace(" ","")
            if not check_valid_string_input(text):
               print(color.colored("Only string data type is allowed, try again",'yellow'))
            else:     
                text=get_valid_hill_plain_text(text,block)
                key=generate_hill_key(block)
                key_as_string=""
                for i in range(block):
                    for j in range(block):
                        key_as_string+=NumberToLetter(key[i][j])
                print(color.colored("The implemented matrix key is:  ",'yellow'),color.colored(key,'yellow'))
                print(color.colored("The matrix key as String is  :  ",'yellow'),color.colored(key_as_string,'yellow'))
                print(color.colored("Cipher Text is               :  ",'yellow'),color.colored(hill_cipher_encrypt(key,text,block),'yellow'))
                break
        except ValueError as ex:
            print(color.colored("Invalid String Data input, please try again",'yellow')    )



def Hill_cipher2():
    while True:
        try:
            block=int(input("Enter square size of block: "))
            cipher=input("Enter Cipher text: ")
            key=input("Enter Decryptive String key: ")
            cipher=cipher.replace(" ","").lower()
            key=key.replace(" ","").lower()
        
            if (not check_valid_string_input(cipher)) or (not check_valid_string_input(key)):
                print(color.colored("Only string data type is allowed, try again",'yellow'))
            else:
                le=check_hill_decrypr_text(cipher,block)
                inv_key=return_matrix_inverse(Return_hill_key_as_array(key,block))
                cipher=Return_hill_decrypt_as_array(cipher,block,le)
                dot=np.dot(inv_key,cipher)
                plain_text=""
                for i in range(len(dot)):
                    for j in range(len(dot[0])):
                        plain_text+=NumberToLetter(int(dot[i][j]))
                print(color.colored("The inverse of matrix key is:\n",'yellow'),color.colored(inv_key,'yellow'))
                print(color.colored("Plain Text is               :  ",'yellow'),color.colored(plain_text,'yellow'))
                break  
        except ValueError as ex:
            print(color.colored("Invalid String Data input, please try again",'yellow'))



def rail_fence1():
    while True:
        try:
            plain_text=input("Enter Text To Encrypt: ")
            print("The Cipher Text is: ",Rail_Fence_Cipher_Encrypt(plain_text).replace(" ",""))
            break
        except ValueError as ex:
            print("Invalid Input, Try again")
    return 

def rail_fence2():
     while True:
        try:
            cipher_text=input("Enter cipher Text To Decrypt: ")
            print("The Plain Text is: ",Rail_Fence_Cipher_Decrypt(cipher_text))
            break
        except ValueError as ex:
            print("Invalid Input, Try again")
     return

      
def start():
    print(color.colored("                            [ Choose an operation ]",'blue',attrs=['bold']))
    print(color.colored("------------------------------------------------------------------------------------",'yellow',attrs=['bold']))
    print(color.colored("[ 1  ]- Encrypt Shift Cipher.                                                       |",'green',attrs=['bold']))
    print(color.colored("[ 2  ]- Decrypt Shift Cipher.                                                       |",'green',attrs=['bold']))
    print(color.colored("[ 3  ]- Encrypt Multiplicative Cipher.                                              |",'green',attrs=['bold']))
    print(color.colored("[ 4  ]- Decrypt Multiplicative Cipher.                                              |",'green',attrs=['bold']))
    print(color.colored("[ 5  ]- Encrypt Affine Cipher.                                                      |",'green',attrs=['bold']))
    print(color.colored("[ 6  ]- Decrypt Affine Cipher.                                                      |",'green',attrs=['bold']))
    print(color.colored("[ 7  ]- Encrypt Auto-Key Cipher.                                                    |",'green',attrs=['bold']))
    print(color.colored("[ 8  ]- Decrypt Auto-Key Cipher.                                                    |",'green',attrs=['bold']))
    print(color.colored("[ 9  ]- Encrypt Play-Fair Cipher.                                                   |",'green',attrs=['bold']))
    print(color.colored("[ 10 ]- Decrypt Play-Fair Cipher.                                                   |",'green',attrs=['bold']))
    print(color.colored("[ 11 ]- Encrypt Vigenere Cipher.                                                    |",'green',attrs=['bold']))
    print(color.colored("[ 12 ]- Decrypt Vigenere Cipher.                                                    |",'green',attrs=['bold']))
    print(color.colored("[ 13 ]- Encrypt Hill Cipher.                                                        |",'green',attrs=['bold']))
    print(color.colored("[ 14 ]- Decrypt Hill Cipher.                                                        |",'green',attrs=['bold']))
    print(color.colored("[ 15 ]- Encrypt Rail-Fence Cipher                                                   |",'green',attrs=['bold']))
    print(color.colored("[ 16 ]- Decrypt Rail-Fence Cipher                                                   |",'green',attrs=['bold']))
    print(color.colored("------------------------------------------------------------------------------------",'yellow',attrs=['bold']))  
    begin()
      
      
def begin():       
    while True:
        try:
            
            op=int(input(color.colored("Operation: ",'cyan',attrs=['bold']))   )         
            if op==1:
                Shift_Cipher1()
                go_on()
                start()     
            elif op==2:
                Shift_Cipher2()
                go_on()
                start()          
            elif op==3:     
                Multiplicative_cipher1()
                go_on()
                start()                
            elif op==4:
                Multiplicative_cipher2()
                go_on()
                start()                  
            elif op==5:
                Affine_cipher1()
                go_on()
                start()                
            elif op==6:
                Affine_cipher2()
                go_on()
                start()                
            elif op==7:
                AutoKey_cipher1()
                go_on()
                start()               
            elif op==8:
                AutoKey_cipher2()
                go_on()
                start()                 
            elif op==9:
                Play_fair_cipher1()
                go_on()
                start()                
            elif op==10:
                Play_fair_cipher2()
                go_on()
                start()              
            elif op==11:
                Vigenere_cipher1()
                go_on()
                start()              
            elif op==12:
                Vigenere_cipher2()
                go_on()
                start()              
            elif op==13:
                Hill_cipher1()
                go_on()
                start()             
            elif op==14:
                Hill_cipher2()
                go_on()
                start()
            elif op==15:
                rail_fence1()
                go_on()
                start()
            elif op==16:
                rail_fence2()
                go_on()
                start()              
            else:
                print(quit())     
            break               
        except ValueError as ex:
            print("Invalid Input, Try Again And Enter Valid Data: ")


if __name__=="__main__":
    result =fig.figlet_format("\nCryptoZez",font="larry3d")
    print(color.colored(result,'yellow'))
    iden()
    start()
    