"""
정적 메소드
클래스나 인스턴스(객체)와는 무관하게 독립적으로 동작하는 함수를 만들고 싶을 때 이용함.
함수를 정의할 때 인자로 self를 사용하지 않는다.
정적 메서드 안에서는 인스턴스 메서드나 인스턴스 변수에 접근 할 수 없습니다.
"""

class Car :
    isinstance_count = 0     # 여기에 있으면 클래스 변수 = 클래스 소속 변수

    # 초기화 함수
    def __init__(self, size, model):   # 여기에 있으면 인스턴스 변수
        self.size = size   # 인스턴스 변수 생성 및 초기화
        self.model = model
        Car.isinstance_count = Car.isinstance_count + 1 # 클래스 변수 이용
        print(f"자동차 객체 생성 수 : {Car.isinstance_count}")

    def move(self, speed):
        self.speed = speed
        print(f"자동차 {self.size} & {self.model}가 시속 {self.speed}로 달립니다.")

    @staticmethod
    def check_type(code):
        if(code >= 10): print("전기차 입니다.")
        elif(code >= 20): print("가솔린차 입니다.")
        elif(code >= 30): print("디젤차 입니다.")
        else: print("분류 코드가 없습니다.")

car1 = Car("소형", "모닝")
car2 = Car("중형", "쏘나타")

car1.move(90)
Car.check_type(11)
car2.move(70)
