##
#   18.03.08
#   20152262    Hong Geun Ji
#
#   Implemnetation of absolute

user_input = int(input("임의의 정수를 입력하시오 :"))
num_type = "양수"

if user_input < 0:
    user_input = -user_input
    num_type = "음수"
elif user_input == 0:
    num_type = "0"

print("입력하신 수는", num_type,"이고 절댓값은",user_input,"입니다.")
