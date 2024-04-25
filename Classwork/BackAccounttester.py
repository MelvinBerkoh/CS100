import BankAccount


def main():
    # create the user instances for the Bank Account
    user1 = BankAccount.UserAccount(
        'Melvin', 'Berkoh', '123-11-1234', '1234567890', 'xyz@gmail.com')
    print(user1.getBankName())
    print(user1.bankName)
    print(user1.getBalance())


main()
