"""
클래스 메소드 : 클래스 변수를 사용하기 위한 함수.
클래스 메소드는 첫 번째 인자로 클래스를 넘겨 받는 cls가 필요하며 이를 이용해 클래스 변수에 접근
"""


class Person:
    count = 0  # 클래스 변수

    def __init__(self):
        Person.count += 1  # 인스턴스가 만들어질 때
        # 클래스 속성 count에 1을 더함

    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))  # cls로 클래스 속성에 접근


james = Person()
maria = Person()

Person.print_count()  # 2명 생성되었습니다.

