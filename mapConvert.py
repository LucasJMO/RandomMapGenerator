import os
#TODO: find some non awful way of doing this
def mapToPDF(fileName):
	fileEPS = fileName + ".eps"
	filePDF = fileName + ".pdf"
	os.system('ps2pdf '+fileEPS+' '+filePDF)

#mapToPDF('t')