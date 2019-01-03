

withdraw_amt, account_bal = raw_input().split()

withdraw_amt = int(withdraw_amt)
init_account_bal=round(float(account_bal),2)

final_account_bal = init_account_bal

if (withdraw_amt % 5 == 0) and ((withdraw_amt+0.50) <= init_account_bal):
	final_account_bal = round(float(init_account_bal - withdraw_amt - 0.50), 2)

print final_account_bal
