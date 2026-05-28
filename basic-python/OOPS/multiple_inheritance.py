class TeamMember:

    def __init__(self, name, uid):
        self.name = name
        self.uid = uid


class Worker:

    def __init__(self, pay, jobtitle):
        self.pay = pay
        self.jobtitle = jobtitle


class TeamLeader(TeamMember, Worker):

    def __init__(self, name, uid, pay, jobtitle, exp):

        self.exp = exp

        TeamMember.__init__(self, name, uid)
        Worker.__init__(self, pay, jobtitle)

        print(
            "Name: {}, UID: {}, Pay: {}, Job Title: {}, Experience: {}".format(
                self.name,
                self.uid,
                self.pay,
                self.jobtitle,
                self.exp
            )
        )


# Object Creation
TL = TeamLeader(
    "Prasanna",
    1001,
    25000,
    "Automation Tester",
    5
)