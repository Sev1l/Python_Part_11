## List comprehensions
# Task 7 (Lottery numbers)


class LotteryNumbers:
    def __init__(self,week,const):
        self.week = week
        self.const = const

    def number_of_hits(self,number):
        return len([n for n in number if n in self.const])
    def hits_in_place(self,numbers):
        return [n  if n in self.const else -1 for n in numbers]
        

week5 = LotteryNumbers(5, [1,2,3,4,5,6,7])
my_numbers = [1,4,7,11,13,19,24]

print(week5.number_of_hits(my_numbers))

week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
my_numbers = [1,4,7,10,11,20,30]

print(week8.hits_in_place(my_numbers))
