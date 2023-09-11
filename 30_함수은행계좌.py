# (1) 첫번째 방법 : 일반 함수 만들어서 실행
# 1. 계좌 개설
def open_account(name) :
    print(f"{name}님의 계좌가 개설 되었습니다.")
    return name   # 반환 값으로 이름을 전달
# 2. 입금 함수
def deposit(balance, input) : # 잔고와 입금액을 매개 변수로 전달 받음
    print(f"{input} 원이 입금 되었습니다. 잔액은 {balance + input} 원 입니다.")
    return balance + input
# 3. 출금 함수
def withdraw(balance, output) :
    if balance >= output :
        print(f"{output} 원이 출금 되었습니다. 잔액은 {balance - output} 원 입니다.")
        return balance - output
    else :
        print(f"출금이 실패 했습니다. 잔액은 {balance} 원 입니다.")
        return balance

balance = 0  # 외부에서 선언 했지만 매개 변수로 전달 하여 결과를 리턴 받음
name = open_account("우희")
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)
print(f"{name}의 잔액은 {balance} 원 입니다.")

# 두번째 방법 : balance를 전역변수 global을 이용하여 선언 (전역 변수 :  코드 전체 범위에서 사용 가능한 전역변수)
# 1. 계좌 개설
def open_account(name) :
    print(f"{name}님의 계좌가 개설 되었습니다.")
    return name   # 반환 값으로 이름을 전달

# 2. 입금 함수
def deposit(input) : # 잔고와 입금액을 매개 변수로 전달 받음
    global balance
    balance += input
    print(f"{input} 원이 입금 되었습니다. 잔액은 {balance} 원 입니다.")

# 3. 출금 함수
def withdraw(output) :
    global balance
    if balance >= output :
        balance -= output
        print(f"{output} 원이 출금 되었습니다. 잔액은 {balance} 원 입니다.")
    else :
        print(f"출금이 실패 했습니다. 잔액은 {balance} 원 입니다.")

balance = 0  # 외부에서 선언 했지만 매개 변수로 전달 하여 결과를 리턴 받음
name = open_account("우희")
deposit(2000)
withdraw(500)
print(f"{name}의 잔액은 {balance} 원 입니다.")