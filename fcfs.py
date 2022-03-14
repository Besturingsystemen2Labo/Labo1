from xml.dom import minidom
imnport numpy as np

file = minidom.parse('processen10000.xml')

models = file.getElementsByTagName('arrivaltime')

print(models[0].childNodes[0].data)



def FCFS(input):
        