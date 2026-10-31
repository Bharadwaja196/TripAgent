# from tools.tavily import tavilySearch
# res = tavilySearch(" places to watch out in hyderabad")
# print(res)
from tools.flight_tool import search_flights
res = search_flights("flights from india to japan")
print(res)