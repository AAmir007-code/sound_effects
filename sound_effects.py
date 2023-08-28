
from playsound import playsound

data = input('Enter one of these: `dog`,`car`,`horror`: ').lower()
try:
    playsound(data+'.wav')
except:
    print('Error')



