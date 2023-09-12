"""
오버라이딩 : 부모 클래스를 상속받아 동일한 매소드에 대해 재정의해 사용하는 것
오버로딩 : 파이썬은 오버로딩이 없다. (필요 없음)
1. 매개변수의 타입이 따로 정해져있지 않았기 때문에 > 데이터형이 따로 정해져 있지 않아 아무 변수(숫자, 글자 등)를 넣어도 동작 가능.
2. 디폴트 매개변수 문법이 있음.
"""
# 오버로딩 없는 이유 예시
# def sum(num1, num2, num3=100) :
#     return num1 + num2 + num3
#
# print(sum(100, 200))
# print(sum(100, 200, 300))
#print(sum("korea","seoul","busan"))
"""
출력
400  매개변수가 2개만 있어도 자동으로 계산되서 출력 된다. 
600
"""

# 상속
class ProtoTV:
    def __init__(self, isOn, channel, volume):
        self.isOn = isOn
        self.channel = channel
        self.volume = volume
    def set_on(self, isOn):
        self.isOn = isOn
    def set_channel(self, cnl):
        if 0 < cnl < 1000 :
            self.channel = cnl
            print(f"채널을 {cnl}로 변경 하였습니다.")
        else :
            print(f"채널 설정 범위가 아닙니다.")
    def set_volume(self, vol):
        self.volume = vol
    def get_on(self):
        return self.isOn
    def get_channel(self):
        return self.channel
    def get_volume(self):
        return self.volume

class TV(ProtoTV) : # ProtoTV로 부터 상속을 받음
    def set_channel(self, cnl):   # 부모가 가진 메소드를 상속 받아 재정의함 > 오버라이딩
        if 0 < cnl < 2000:
            self.channel = cnl
            print(f"채널을 {cnl}로 변경 하였습니다.")
        else:
            print(f"채널 설정 범위가 아닙니다.")

lg_tv = TV(False,10,10)