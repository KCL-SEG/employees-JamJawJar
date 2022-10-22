"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Contract:
    def __init__(self):
        pass

    def get_contract_pay(self):
        return(0)

    def __str__(self):
        return("empty contract")

class SalaryContract(Contract):
    def __init__(self, monthlyWage):
        self.monthlyWage = monthlyWage

    def get_contract_pay(self):
        return(self.monthlyWage)

    def __str__(self):
        return(f"monthly salary of {self.monthlyWage}")

class HourlyContract(Contract):
    def __init__(self, hourlyWage, hoursWorked):
        self.hourlyWage = hourlyWage
        self.hoursWorked = hoursWorked

    def get_contract_pay(self):
        return(self.hourlyWage * self.hoursWorked)

    def __str__(self):
        return(f"contract of {self.hoursWorked} hours at {self.hourlyWage}/hour")


class Commission:
    def __init__(self):
        pass

    def get_commission_pay(self):
        return(0)

    def __str__(self):
        return("empty commission")


class BonusCommission(Commission):
    def __init__(self, bonusAmount):
        self.bonusAmount = bonusAmount

    def get_commission_pay(self):
        return(self.bonusAmount)

    def __str__(self):
        return(f"receives a bonus commission of {self.bonusAmount}")

class ContractCommission(Commission):
    def __init__(self, commissionPerContract, contractsLanded):
        self.commissionPerContract = commissionPerContract
        self.contractsLanded = contractsLanded

    def get_commission_pay(self):
        return(self.commissionPerContract * self.contractsLanded)

    def __str__(self):
        return(f"receives a commission for {self.contractsLanded} contract(s) at {self.commissionPerContract}/contract")





class Employee:
    def __init__(self, name, contract=Contract(), commission=Commission()):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        return(self.contract.get_contract_pay() + self.commission.get_commission_pay())

    def __str__(self):
        employeeString = f"{self.name} works on a {str(self.contract)}"

        if(str(self.commission) != "empty commission"):
            employeeString += f" and {str(self.commission)}"
        
        employeeString += f".  Their total pay is {self.get_pay()}."

        return(employeeString)



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', SalaryContract(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlyContract(25, 100))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', SalaryContract(3000), ContractCommission(200, 4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyContract(25, 150), ContractCommission(220, 3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', SalaryContract(2000), BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyContract(30, 120), BonusCommission(600))
