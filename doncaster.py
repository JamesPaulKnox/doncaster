########################################################################

# ~ Copyright 2019, James P. Knox

# ~ Permission is hereby granted, free of charge, to any person
# ~ obtaining a copy of this software and associated documentation files
# ~ (the "Software"), to deal in the Software without restriction,
# ~ including without limitation the rights to use, copy, modify, merge,
# ~ publish, distribute, sublicense, and/or sell copies of the Software,
# ~ and to permit persons to whom the Software is furnished to do so,
# ~ subject to the following conditions:

# ~ The above copyright notice and this permission notice shall be
# ~ included in all copies or substantial portions of the Software.

# ~ THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# ~ EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
# ~ MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# ~ IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
# ~ CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
# ~ TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
# ~ SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

########################################################################

import json
import requests
import copy
import os

base_url = "https://api.iextrading.com/"
version = "1.0/"
scope = "5y"

app_dir = "/run/media/james/MediaB/projects/doncaster_2/"

########################################################################

def get_json_path(symbol):
# This function will find the path a
# json file should be in, given a symbol

	path = app_dir + "chart/" + symbol + ".json"
	
	return path
	
########################################################################

def get_json_symbol(path):
# This function will find the symbol of
# a saved json file, given a path

	symbol = os.path.basename(path).split(".")[0]
	
	return symbol 
	
########################################################################

def get_json(symbol):
# This function will make a local
# copy of the IEX chart JSON file	
	
	url = base_url + version + "/stock/" + symbol + "/chart/" + scope
	
	r = copy.copy(requests.get(url))
	
	if r.status_code == 404: # If symbol doesn't exist, skip
		return
	
	f = open(get_json_path(symbol), "wb+")
	
	f.write(r.content)
	f.close()
	
########################################################################	
	
def read_json(symbol):
# This function will read the local copy
# of the IEX chart JSON file, given a file name.


	return json.load(open(get_json_path(symbol)))

########################################################################

