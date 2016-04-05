from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
import re
def home(request):
  return render(request, 'matrix/homepage.html')


def getarray(request):
	myList = request.GET['list']
	newList = re.findall(r'[^,;\s]+',myList)
	print newList
	newList = [int(i) for i in newList]
	myBellArray = RiordanBellArrayGeneratorWithSum(newList)

	df = pd.DataFrame(myBellArray)
	html = df.to_html(index = False , header = False, col_space=200).replace('border="1"','border="0"')
	print html
	return HttpResponse(html)

def RiordanBellArrayGeneratorWithSum(myArray):
    size = len(myArray)
    myFinalArray = np.zeros((size, size), dtype=np.int)
    b = np.zeros(size, dtype = np.int)
    myFinalArray[0] = myArray
    c = myArray
    for a in xrange(1,size):
        b = np.zeros(size, dtype = np.int)
        for x in xrange(size-a):
            for y in xrange(size):
                for z in xrange(len(c)):
                    if y + z == x:
                        b[x+a] += myArray[y] * c[z]
        myFinalArray[a] = b
        c=b[a:]

    
    myFinalArray =  np.transpose(myFinalArray)

    rowSums = myFinalArray.sum(axis=1)
    rowSums.shape = (size,1)
    return myFinalArray

