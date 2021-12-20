# The main class for the application

from PIL import Image
import logging
import glob
import PIL.Image

class chitr():

	version = 0.1
	supported_extensions = ['jpg' , 'jpeg', 'png' , 'gif', 'bmp' , 'raw']

	def __init__(self):
		logging.debug("Initializing the python image class")
		



	
	def scanPath(self):
		image_list = []
		for filename in glob.glob('Chitr/images/*'):
			image_details = dict()
			im=Image.open(filename)
			image_details['image'] = im
			image_details['exif'] = self.getImageExif(im)
			image_list.append(image_details)			
		logging.debug(image_list)
		return image_list

	def getImageExif(self,pilImage):
		#This function is created so that the exif data can be modified according to later requirements
		return pilImage._getexif()






