
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
# ~ This file was a little experiment I did. I thought I'd upload it
# ~ just to show off a potential application of the program. Given a sector
# ~ (Or set it to None for the whole market) it will gather a list of
# ~ symbols belonging to it, do the analysis for each of them, and output
# ~ some of the results in a CSV. Feel free to play around with it.
########################################################################

from doncaster_main import *
import pyiex_misc, copy

print("Generating list of symbols")

count = 0

sector = None

# Set sector to None for whole market.

symbols = copy.copy(pyiex_misc.listSymbols(sector))

print("Generated.")

with open('csvfile.csv','w') as file:
	for i in symbols:
		
		count = count + 1
		
		print("Starting {} out of {}".format(count, len(symbols)))
		
		try:
		
			output = copy.copy(main(i,"5y",30,60,100))
			
			line = i + "," \
			+ str(output["est_yield"]) + "," \
			+ str(output["decision"]) + "," \
			+ str(output["recent"]) + "," \
			+ str(output["date_recent"]) + "," \
			+ str(output["sma_success_rate"]) + "," \
			+ str(output["ema_success_rate"]) + "\n" \
			
			file.write(line)

		except ZeroDivisionError:
			print("Can't divide by zero! Skipping.")
