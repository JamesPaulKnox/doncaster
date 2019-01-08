### MAIN IDEA

* This is [going to be] a probably-terrible security market program.
* For the requested set of securities (individual stocks? ETFs? DOW? Etc.), it will pull the 30, 60, and 100 day moving averages.
* For each item, it will compare the averages.
** If the 30 day is the highest AND 100 day is the lowest, it signifies a long-term upward motion of price (BUY)
** If the 60 day is above the 30 day, it signifies an intermediary-term downward motion of price (SELL)
* At this time, it is only planned to support long positions.
* *Don't use this program to actually trade. It's a thought experiment.*


### CONSIDER THIS

* Maybe I should calculate the MAs using VWAP?
* It would be pretty easy to support a simulation of profit/loss using the method on an individual stock over the past 5 years - IF I PLAN IT EARLY
** Probably want to use the /stock/####/chart/time part of the API.
** Actually, now that I think of it. Why not pull the whole past year's info and calculate a historical return using the method?
** That might make a decent filter, too. Only display stocks that have a positive return using the method, AND display % that it worked and didn't.
** If I ever want to make a 5 yr simulation, it'd be a matter of changing a couple variables and commenting a couple of lines out.

### MOVING AVERAGE

* This program will calculate both the exponential and simple moving averages.
* It will find the average return & % that it worked for each, independently.
* Comparing what happens to return using EMA vs SMA, it will calculate it's decision based on the better-performing MA.
** Sometimes, the EMA detects hiccups, causing a false-alarm sell.
** However, the EMA can also signal true-alarm sells faster.
** By comparing the performance of the two, I hope it will mitigate false-alarms and maximize early warnings.

#### EXPONENTIAL MOVING AVERAGE FORMULA

Current EMA = (Current Price x alpha) + (Previous EMA x (1 - alpha))
alpha = (2 / (1 + n))

* NOTE: For the initial value of previous EMA, use SMA.
* Also, because alpha is a constant for *every* EMA of the same period,
* I shouldn't calculate it for every single EMA calculation.
* It would be smarter to calculate it at run, and store the numbers.

### STORING BUY/SELL

I'd like to use a dictionary. If the key is "BUY" or "SELL", that'll
run into problems really fast. The key needs to be unique. I also considered
setting the VWAP price as the key and the BUY/SELL as the value. Which would work
fine, as long as two days never have the same VWAP. I don't want to take 
that risk.I'm thinking instead, create a list of "BUY", "SELL", or "NO CHANGE" strings
in the same order as the VWAP list. Only on the first day of an upward
or downward trend will the list state BUY or SELL.


There's something wrong with my for statements right now. I need to logically
think about the range in which I iterate through


I think I fixed the for statement. But something is wrong. Try running it.

I think I fixed fixed it.

The values for EMA and SMA are slightly off. Usually within a dollar. I think that's
a reasonable error for a thought experiment.
