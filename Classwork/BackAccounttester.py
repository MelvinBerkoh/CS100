import BankAccount


def main():
    # create the user instances for the Bank Account
    user1 = BankAccount.UserAccount(
        'Melvin', 'Berkoh', '123-11-1234', '1234567890', 'xyz@gmail.com')
    # whenever initializing a class, you need to pass all of the  the required parameters
    # user2 = BankAccount.UserAccount(
    #     'John', 'Doe', '123-11-1234', '1234567890',)
    # create the account instances for the Bank Account
    # whenever initializing a class, you need to pass all of the  the required parameters
    user3 = BankAccount.Account(
        'Jane', 'Doe', '123-11-1234', '1234567890', 'dus@gmail.com')
    # print(user2.getBankName())
    print(user1.getBankName())
    print(user1.bankName)
    # so when a user is created by the parent if the child has a method built it the parent class cannot access it?? tested below.
    # print(user1.getBalance())
    print(user3.getBalance())
    print(user3.getName())


main()
