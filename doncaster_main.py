from pyiex_config import *
import copy, pyiex_company

# Symbol is the symbol you'd like to calculate for
# Scope is the time period to simulate trading. Must be at least 6m
# ( scope > 100 trading days ), read up on acceptable values on the IEX
# API documentation, under "chart"

def sma(vwap_list, n):
	
	vwaps = copy.copy(vwap_list)
	
	if len(vwaps) >= n:
		while len(vwaps) > n:
			vwaps.remove(vwaps[0])
		return (sum(vwaps) / len(vwaps))
		
def ema(vwap_list, n, yesterday):

	vwaps = copy.copy(vwap_list)

	if len(vwaps) >= n:
		while len(vwaps) > n:
			vwaps.remove(vwaps[0])
		try:
			return ((vwaps[-1] - yesterday) * (2 / (n + 1)) + yesterday)
		except:
			return ((vwaps[-1] - sma(vwaps, n - 1)) * (2 / (n + 1)) + sma(vwaps, n - 1))

def decide(ma_a, ma_b, ma_c):
	
	if ma_a > ma_b > ma_c:
		return "BUY"
	
	else:
		return "SELL"


def main(symbol, scope, a=20, b=50, c=100):

	print("Checking if \"{}\" is a valid symbol".format(symbol.upper()))

	try:
		print("Fetching historical data for {}".format(pyiex_company.companyName(symbol)))
	except:
		exit

	resp_str = requests.get(base_url + version + "/stock/" + symbol + "/chart/" + scope).json()

	for i in resp_str:		
		try:
			vwap_list.append(i["vwap"])
			date_list.append([int(i["date"].replace("-", ""))])
			
			sma_a.append(sma(vwap_list, a))
			sma_b.append(sma(vwap_list, b))
			sma_c.append(sma(vwap_list, c))

			ema_a.append(ema(vwap_list, a, ema_a[-1]))
			ema_b.append(ema(vwap_list, b, ema_b[-1]))
			ema_c.append(ema(vwap_list, c, ema_c[-1]))
		
		except:
			
			vwap_list = [resp_str[0]["vwap"]]
			date_list = [int(resp_str[0]["date"].replace("-", ""))]
			
			sma_a = [sma(vwap_list, a)]
			sma_b = [sma(vwap_list, b)]
			sma_c = [sma(vwap_list, c)]
			
			ema_a = [ema(vwap_list, a, sma_a[-1])]
			ema_b = [ema(vwap_list, b, sma_b[-1])]
			ema_c = [ema(vwap_list, c, sma_c[-1])]
		
	for i in range(0, max(sma_a.count(None),sma_a.count(None),sma_b.count(None),sma_c.count(None),ema_b.count(None),ema_c.count(None))):
		sma_a.remove(sma_a[0])
		sma_b.remove(sma_b[0])
		sma_c.remove(sma_c[0])

		ema_a.remove(ema_a[0])
		ema_b.remove(ema_b[0])
		ema_c.remove(ema_c[0])
		
		vwap_list.remove(vwap_list[0])
		date_list.remove(date_list[0])
		
	
	
	for i in range(0, len(sma_a)):
		try:
			
			if decide(sma_a[i-1], sma_b[i-1], sma_c[i-1]) == decide(sma_a[i], sma_b[i], sma_c[i]):
				sma_decision.append("HOLD")
			else:
				sma_decision.append(decide(sma_a[i], sma_b[i], sma_c[i]))
			
			if decide(ema_a[i - 1], ema_b[i - 1], ema_c[i - 1]) == decide(ema_a[i], ema_b[i], ema_c[i]):
				ema_decision.append("HOLD")
			else:
				ema_decision.append(decide(ema_a[i], ema_b[i], ema_c[i]))

		except:
		
			if "SELL" == decide(sma_a[i], sma_b[i], sma_c[i]):
				sma_decision = ["HOLD"]
			else:
				sma_decision = [decide(sma_a[i], sma_b[i], sma_c[i])]
			
			if "SELL" == decide(ema_a[i], ema_b[i], ema_c[i]):
				ema_decision = ["HOLD"]
			else:
				ema_decision = [decide(ema_a[i], ema_b[i], ema_c[i])]

	sma_cash = 0
	sma_days = 0
	sma_success = 0
	sma_failure = 0
	sma_recent = "NONE"
	ema_cash = 0
	ema_days = 0
	ema_success = 0
	ema_failure = 0
	ema_recent = "NONE"
	
	sma_cost = 0
	ema_cost = 0
	
	sma_total_days = 0
	ema_total_days = 0


	for i in range(0, len(date_list)):
		if sma_decision[i] == "BUY":
			sma_cash = sma_cash - vwap_list[i]
			sma_recent = "BUY"
			sma_date_recent = date_list[i]
			sma_cost = sma_cost + vwap_list[i]			

		if sma_decision[i] == "SELL":
			
			if sma_cash < (sma_cash + vwap_list[i]):
				sma_success = sma_success + 1
			
			else:
				sma_failure = sma_failure + 1
			
			sma_cash = sma_cash + vwap_list[i]
			sma_recent = "SELL"
			sma_date_recent = date_list[i]
			sma_total_days = sma_days + sma_total_days
			sma_days = 0
	
			
		if sma_decision[i] == "HOLD":
			if sma_recent == "BUY":
				sma_days = sma_days + 1
	
	if sma_recent == "BUY":
		sma_cash = sma_cash + vwap_list[i]

	sma_cash = round(sma_cash, 4)


	for i in range(0, len(date_list)):
		if ema_decision[i] == "BUY":
			ema_cash = ema_cash - vwap_list[i]
			ema_recent = "BUY"
			ema_date_recent = date_list[i]
			ema_cost = ema_cost + vwap_list[i]
		
		if ema_decision[i] == "SELL":
			
			if ema_cash < (ema_cash + vwap_list[i]):
				ema_success = ema_success + 1
			
			else:
				ema_failure = ema_failure + 1
				
			ema_cash = ema_cash + vwap_list[i]
			ema_recent = "SELL"
			ema_date_recent = date_list[i]
			ema_total_days = ema_days + ema_total_days
			ema_days = 0
			
		if ema_decision[i] == "HOLD":
			if ema_recent == "BUY":
				ema_days = ema_days + 1
	
	if ema_recent == "BUY":
		ema_cash = ema_cash + vwap_list[i]
		
	ema_cash = round(ema_cash, 4)
	
	ema_success_rate = (ema_success / (ema_success + ema_failure))
	ema_avg_return = (ema_cash / ema_cost)
	ema_yield = (ema_avg_return / ema_total_days)
	
	sma_success_rate = (sma_success / (sma_success + sma_failure))
	sma_avg_return = (sma_cash / sma_cost)
	sma_yield = (sma_avg_return / sma_total_days)
	
	sma_est_yield = sma_success_rate * sma_yield
	ema_est_yield = ema_success_rate * ema_yield
	
	# Est Yields and Yields are quoted PER DAY of holding the stock. In other words,
	# it can be viewed as being the DAILY avg. volume weighted price appreciation of the
	# stock during the time it is held.
	
	# All percentages are quoted as a decimal ( 0.75 for 75% )

	if ema_est_yield > sma_est_yield:
		est_yield = ema_est_yield
		decision = ema_decision[-1]
		recent = ema_recent
		date_recent = ema_date_recent
	
	else:
		est_yield = sma_est_yield
		decision = sma_decision[-1]
		recent = sma_recent
		date_recent = sma_date_recent

	disclaimer = "Under NO circumstances should you consider this \
		program's output as actual trading advice. This program is not \
		intended for real-world financial activities - but instead a \
		hypothetical exercise in programming."

	data = { \
		"est_yield": est_yield, \
		"decision": decision, \
		"recent": recent, \
		"date_recent": date_recent, \
		"sma_decision": sma_decision, \
		"ema_decision": ema_decision, \
		"sma_cash": sma_cash, \
		"ema_cash": ema_cash, \
		"sma_total_days": sma_total_days, \
		"ema_total_days": ema_total_days, \
		"sma_success": sma_success, \
		"ema_success": ema_success, \
		"sma_failure": sma_failure, \
		"ema_failure": ema_failure, \
		"sma_success_rate": sma_success_rate, \
		"ema_success_rate": ema_success_rate, \
		"sma_avg_return": sma_avg_return, \
		"ema_avg_return": ema_avg_return, \
		"sma_yield": sma_yield, \
		"ema_yield": ema_yield, \
		"sma_est_yield": sma_est_yield, \
		"ema_est_yield": ema_est_yield, \
		"vwap_list": vwap_list, \
		"date_list": date_list, \
		"disclaimer": disclaimer \
		}
	
	return data
