import BankAccount


def main():
    # create the user instances for the Bank Account
    user1 = BankAccount.UserAccount(
        'Melvin', 'Berkoh', '123-11-1234', '1234567890', 'xyz@gmail.com')
    # whenever initializing a class, you need to pass all of the  the required parameters
    user2 = BankAccount.UserAccount(
        'John', 'Doe', '123-11-1234', '1234567890',)
    # create the account instances for the Bank Account
    user3 = BankAccount.Account('Jane', 'Doe', '123-11-1234', '1234567890', )
    print(user2.getBankName())
    print(user1.getBankName())
    print(user1.bankName)
    print(user1.getBalance())


main()
