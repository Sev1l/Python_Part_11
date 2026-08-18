## List comprehensions
# Task 7 (Lottery numbers)



class LotteryNumbers:
    def __init__(self, week, winning_numbers):
        self.week = week
        self.winning_numbers = winning_numbers

    def number_of_hits(self, player_numbers):
        return len([n for n in player_numbers if n in self.winning_numbers])

    def hits_in_place(self, player_numbers):
        return [n if i < len(self.winning_numbers) and n == self.winning_numbers[i] else -1
                for i, n in enumerate(player_numbers)]


week5 = LotteryNumbers(5, [1, 2, 3, 4, 5, 6, 7])
my_numbers = [1, 4, 7, 11, 13, 19, 24]
print(week5.number_of_hits(my_numbers))

week8 = LotteryNumbers(8, [1, 2, 3, 10, 20, 30, 33])
my_numbers = [1, 4, 7, 10, 11, 20, 30]
print(week8.hits_in_place(my_numbers))
