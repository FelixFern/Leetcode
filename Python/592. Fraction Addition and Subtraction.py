class Solution:
    def fractionAddition(self, expression: str) -> str:
        parsed = []
        def gcd(a, b): 
            if(a == 0):
                return b
            return gcd(b % a, a)

        fillDenominator = False
        numerator = ""
        denominator = ""
        for idx, i in enumerate(expression):
            if(i == "+" or (i == "-" and idx != 0)):
                parsed.append([int(numerator), int(denominator)])
                fillDenominator = False
                numerator = i + ""
                denominator = ""
            elif(i == "/"):
                fillDenominator = True
            elif(fillDenominator):
                denominator += i
            else:
                numerator += i
        parsed.append([int(numerator), int(denominator)])

        res = [0, 0]
        for idx, val in enumerate(parsed):
            if(idx == 0):
                res = val
            else:
                product = val[1] * res[1] 
                res = [res[1] * val[0] + val[1] * res[0], product]

        if(res[0] == 0):
            return "0/1"
        else:
            _gcd = abs(gcd(res[0], res[1]))
            print(res)

            return str(res[0] // _gcd) + "/" + str(res[1] // _gcd)
