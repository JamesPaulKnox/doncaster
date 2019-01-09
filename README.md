# doncaster

## What is this?
It's for the stock market. You _really_ shouldn't use this program to actually make trades, it's an exercise in programming and a financial thought experiment. In a nutshell, you tell it 5 things: a ticker symbol, a period of time, and 3 numbers that it'll use to find moving averages with (in order from shortest to longest). In return, the program will run a simulation of trades and return useful information. Most notably, whether it thinks yesterday was a good day to buy or sell (and why).

## How does it work?
1. Given the above attributes, it'll request from IEX the daily VWAPs for your specified period of time.
2. It will calculate the simple moving averages and the exponential moving averages - for the lengths you specified.
3. It will simulate the buying and selling of 1 share for SMA and EMA separately, leaving a dollar amount that would have been gained using the strategy.
4. While simulating, it will judge if a trade was a good or bad. If it sold higher than what it was bought for, it considers that trade a good one (success). Vice versa.
5. When finished, it will calculate the average daily price appreciation rate as follows (( money in / money out ) / days held )
6. To judge how effective the strategy was overall, it will multiply the average daily price appreciation rate by its success rate.
* In other words, it tries to factor in how reliable the strategy is when predicting the future. If the strategy only worked 50% of the time in the past, then it'll cut the estimated future appreciation rate in half. This is useful if comparing how stocks perform on this strategy.
* For example, using SMA a stock has historically appreciated by 0.05% daily during the time the simulation held it, but it made good trades 100% of the time. However, using EMA the same stock appreciated by 0.08% daily but only made good trades 50% of the time. Using SMA, it appreciated less, but the program was right all the time. Using EMA, it appreciated more, but the program was only right half the time. It therfore estimates that SMA will continue to average 0.05% but EMA will average 0.04% ( = 0.08 * 50%). Signifying that using the SMA will likely perform better than EMA in the future using this strategy.
* Yes, I am aware that the calculation mentioned in #5 does consider how often it was right - indirectly.
7. The calculation in #6 is performed separately for SMA and EMA. This is used by the program to decide which method was overall "better."
8. The program will then output "BUY" "SELL" or "HOLD" for the most recent day, taking that decision from either the EMA method or SMA method - whichever was better performing according to #6.
* Note that "HOLD" doesn't mean hold in the traditional sense. "BUY" means that there is upward motion, "SELL" means there is downward motion, *but* "HOLD" means that there has been no directional change during that day. Buy/Sell responses only occur on inflection points. The remainder are notated as hold.
9. The program returns a dictionary of nearly every value it used during the calculation.

## But why?
It was fun and I wanted to. It was a good exercise of critical thinking.

To elaborate, I read about doing something extremely similar in a book last summer. It's titled "Lucky and Good: Risk, Decisions & Bets for Investors, Traders & Entrepreneurs" by John Sherriff, former Enron Europe CEO. Using his method of trading based on the alignment of the 30, 60, and 100 day moving average, he demonstrated how someone could have predicted the rise and fall of Enron's price - and profited. The book wasn't all about that, though, but that bit has been bugging for me to test out on today's markets since I read it. I do recommend the read - the book is all about applying probability in everyday situations to maximize returns.

(If you know of any good books that are remotely about Enron, please let me know! It's my favorite company to read about. Fascinating case study, in my opinion.)

## Disclaimer
Please do not use this program's output as trading advice. It was a thought experiment, and it'd be reckless to execute real-world trades with it. I am not qualified to give trading advice, so you shouldn't trust my code with your money. Simply said, don't sue me. What you choose to do with this program is on you. **Under NO circumstances should you consider this program's output as actual trading advice. This program is not intended for real-world financial activities. It is a hypothetical exercise in programming and thought.**

## IEX API Attribution
Data provided for free by IEX. View IEX’s Terms of Use.

* IEX: https://iextrading.com/developer/
* IEX Terms of Use: https://iextrading.com/api-exhibit-a/

## License

Copyright 2019, James P. Knox

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.**
