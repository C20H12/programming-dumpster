abbs = {
"CU" : "see you",
":-)" : "I'm happy",
":-(" : "I'm unhappy",
";-)" : "wink",
":-P" : "stick out my tongue",
"(~.~)" : "sleepy",
"TA" : "totally awesome",
"CCC" : "Canadian Computing Competition",
"CUZ" : "because",
"TY" : "thank-you",
"YW" : "you're welcome",
"TTYL" : "talk to you later"
}

output = ""
while True:
	letters = input()
	
	if letters == "TTYL":
		output += abbs[letters]
		print(output)
		break
	
	try:
		output += abbs[letters] + '\n'
	except KeyError:
		output += letters + '\n'
	
	
"""
CCC
:-)
SQL
TTYL
"""