import os
import urllib
import mechanicalsoup
from time import sleep


def download(url_dir, path, data_type):
	"""
	Download image data from given url index.html.

	Args:
		url_dir (dict): Index url which hosts multiple image download urls. 
		path 	 (str): Path dedicated for saving the images.

	"""

    #Make a Browser (think of this as chrome or firefox etc)
	br = mechanicalsoup.StatefulBrowser()

	for url in url_dir.keys():
	    # Open your site
	    br.open(url_dir[url])

	    f = open("source.html", "w")
	    #f.write(br.response().read()) #can be helpful for debugging maybe

	    ext = ".tiff" if data_type == 'images' else ".tif"
	    file_types = [ext] # you will need to do some kind of pattern matching on your files
	    url_images = []
	    for l in br.links(): # you can also iterate through br.forms() to print forms on the page!
	        for t in file_types:
	            if str(t) in str(l): # check if this link has the file extension we want (you may choose to use reg expressions or something)
	                url_img = str(l).split('"')[1]
	                url_images.append(url_img)
	                
	                image_name = url_img.split('/')[-1]
	                urllib.request.urlretrieve(url_img, f'../data/buildings_set/{data_type}/{url}/{image_name}')

	print("Finished.")


if __name__ == '__main__':
	# Initialisation
	path = '/Users/Orchestrator/Documents/Ambition/Projects/AngelHackLondon/data/buildings_set'

	urls = {'train': 'https://www.cs.toronto.edu/~vmnih/data/mass_buildings/train/sat/index.html', 
	        'valid': 'https://www.cs.toronto.edu/~vmnih/data/mass_buildings/valid/sat/index.html', 
	        'test':  'https://www.cs.toronto.edu/~vmnih/data/mass_buildings/test/sat/index.html'}

	ground = {
			#'train': 'https://www.cs.toronto.edu/~vmnih/data/mass_buildings/train/map/index.html',
			'valid':   'https://www.cs.toronto.edu/~vmnih/data/mass_buildings/valid/map/index.html',
			'test': 'https://www.cs.toronto.edu/~vmnih/data/mass_buildings/test/map/index.html'}

	print('Downloading data...')
	#download(urls, path, 'images')
	download(ground, path, 'labels')