class Paperboy:

    def __init__(self, new_name):
        self.name = new_name
        self.experience = 0
        self.earnings = 0
        self.delivery_quota = 50
    
    def __str__(self):
        return f"Name: {self.name}, experience: {self.experience}, earning: {self.earnings}. quota: {self.delivery_quota}"
    
    def quota(self):
        return self.delivery_quota
    
    def deliver(self, start_address, end_address):
        total_deliveries = abs(end_address - start_address) + 1
        self.experience += total_deliveries
        if total_deliveries > self.delivery_quota:
            self.earnings += self.delivery_quota * 0.25
            self.earnings += (total_deliveries - self.delivery_quota)* 0.5
        else:
            self.earnings += total_deliveries*0.25
            self.earnings -= 2
        self.delivery_quota += round(self.experience/2)

    def report(self):
        return f"My name is {self.name}, I've delivered {self.experience} and i've earned ${self.earnings} so far!"


# Using the testing code given in the assignment page.
tommy = Paperboy("Tommy")

print(tommy.quota()) #  50
print(tommy.deliver(101, 160)) # 17.5
print(tommy.earnings) # 17.5
print(tommy.report()) # "I'm Tommy, I've delivered 60 papers and I've earned $17.5 so far!"

print(tommy.quota()) # 80
print(tommy.deliver(1, 75)) # 16.75
print(tommy.earnings) # 34.25
print(tommy.report()) # "I'm Tommy, I've been delivered 135 papers and I've earned $34.25 so far!"
