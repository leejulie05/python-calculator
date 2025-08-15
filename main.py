#main.py

from calc import FourCal

print("==Fourcal 콘솔계산기==")
print("끝내려면 q입력!")

while True:

    try:
        num1=input("첫번째 숫자를 입력하세요")
        if num1.lower() =='q' : break

        num1=float(num1)
        
        num2=input("두번째 숫자를 입력하세요")
        if num2.lower()=='q' : break
        num2=float(num2)
        
        op=input("연산기호('+ - * /): ")
        if op.lower()=='q':break
        while True:
            
            a=FourCal(num1,num2)

            try:
                if op=='+':
                    print(a.add())
                    break
                elif op=='-':
                    print(a.sub())
                    break
                elif op=='*':
                    print(a.mul())
                    break
                elif op=='/':
                    print(a.div())
                    break
                
                else:
                    print("지원하지 않는 연산입니다.")
                    break
            except ZeroDivisionError as e:
                num2=input(f"{e} 두번째 숫자를 다시 입력하세요")
                isbreak=False
                if num2.lower()=='q' :
                    isbreak=True
                    break
                try:
                    num2=float(num2)
                except ValueError as e:
                    print(f"{e}숫자를 입력해주세요.")
                    continue
                
        if isbreak :break
    except ValueError as e:
            print(f"숫자를 입력하세요. {e}")
 
