class TeamMember:

    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def display(self):
        print("Team Member Name :", self.name)
        print("Team Member UID  :", self.uid)


class Worker:

    def __init__(self, pay, jobtitle):
        self.pay = pay
        self.jobtitle = jobtitle

    def display(self):
        print("Job Title :", self.jobtitle)
        print("Pay       :", self.pay)


class TeamLeader( Worker, TeamMember):

    def __init__(self, name, uid, pay, jobtitle, exp):

        self.exp = exp
        super().__init__(name, uid)
        super().__init__(pay, jobtitle)

    def display(self):
        super().display()
        super().display()

        print("Experience :", self.exp)


TL = TeamLeader("Prasanna",101,25000,"TESTNG Automation",5)
TL.display()