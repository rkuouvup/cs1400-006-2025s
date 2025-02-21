import argparse

def cal_bal(deposit, irate, month):
    c_balance = deposit
    m_balance = []
    monthly_irate = irate / 12 / 100
    for i in range(month):
        c_balance = c_balance + c_balance * monthly_irate
        m_balance.append(c_balance)
    return m_balance

#def print_monthly_bal(lst):

def main():
    parser = argparse.ArgumentParser(description="Calculate balance based on the deposit and interest rate")
    parser.add_argument("deposit", metavar = "d",
                        type=float, help="the initial deposit")
    parser.add_argument("irate", metavar="i",
                        type=float, help="annual interest rate in percentage")
    args = parser.parse_args()
    #print(args.deposit)
    #print(args.irate)

    # simulation
    monthly_bal = cal_bal(args.deposit, args.irate, 12)

    # print data
    #print_monthly_bal(monthly_bal)
    print(monthly_bal)


if __name__ == "__main__":
    main()