class TeamMember:
    def __int__(self, name, uid):
        self.name = name
        self.uid = uid
    
    def display(self):
        print(f"Team Member: {self.name}, UID: {self.uid}")


class Worker:
    def __int__(self, pay, jobtitle):
        self.pay = pay
        self.jobtitle = jobtitle 

    def display(self):
        print(f"Worker: {self.jobtitle}, Pay: {self.pay}")