## OrderBook

class Task:
    id = 0
    def __init__(self,description,programmer,workload):
        Task.id += 1
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.id = Task.id
        self.finish = False
    def __str__(self):
        if self.finish ==False:
            return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} NOT FINISHED'
        else:
            return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} FINISHED'
    def is_finished(self):
        return self.finish
    def mark_finished(self):
        self.finish = True
    
class OrderBook:
    def __init__(self):
        self.tasks = [] 

    def add_order(self, description, programmer, workload):
        new_task = Task(description, programmer, workload)
        self.tasks.append(new_task)

    def all_orders(self):
        return self.tasks

    def programmers(self):
        unique_programmers = []
        for task in self.tasks:
            if task.programmer not in unique_programmers:
                unique_programmers.append(task.programmer)
        return unique_programmers

    def mark_finished(self,id):
        for new_task in self.tasks:
            if new_task.id == id:
                new_task.mark_finished()
                return
        raise ValueError
    def status_of_programmer(self, programmer: str):
        finished = 0
        not_finished = 0
        fin_summ = 0
        fin_not_summ = 0
        for task in self.tasks:
            if task.programmer == programmer:
                if task.finish == True:
                    finished += 1
                    fin_summ += task.workload
                else:
                    not_finished += 1
                    fin_not_summ += task.workload
        tuple = (finished,not_finished,fin_summ,fin_not_summ)
        return tuple
        

orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Adele", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)
orders.add_order("program the next facebook", "Eric", 1000)

orders.mark_finished(1)
orders.mark_finished(2)

status = orders.status_of_programmer("Adele")
print(status)
