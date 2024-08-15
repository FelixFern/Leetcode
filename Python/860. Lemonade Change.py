class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = {}
        for i in bills:
            if i == 5:
                money[5] = money.get(5, 0) + 1
            elif i == 10:
                if (money.get(5, 0) > 0):
                    money[5] = money.get(5, 0) - 1
                    money[10] = money.get(10, 0) + 1
                else:
                    return False
            elif i == 20:
                if ((money.get(5, 0) > 0 and money.get(10, 0) > 0)):
                    money[5] = money.get(5, 0) - 1
                    money[10] = money.get(10, 0) - 1
                    money[20] = money.get(20, 0) + 1
                elif (money.get(5, 0) > 2):
                    money[5] = money.get(5, 0) - 3
                    money[20] = money.get(20, 0) + 1
                else:
                    return False
        return True
