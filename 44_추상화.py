"""
추상화
1. 부모 클래스에서 선언한 메소드에 대해서 반드시 상속 받은 클래스에서 기능을 구현 해야 하는 특성
2. 추상 메서드가 포함된 부모 클래스는 객체로 만들 수 없고 단지 상속을 주기 위해서 존재

- 키워드 -
- 객체 : 클래스라는 설계도를 이용해 물건을 만들어 내는 것을 의미 합니다.
- 클래스 : 객체를 생성하기 위해 만들어진 설계도라고 생각 할 수 있습니다. 멤버와 함수로 구성되어 있습니다.
- 인스턴스 : 클래스를 기반으로 객체를 생성하는 과정을 의미 합니다.
- 생성자: 객체가 생성될 때 자동으로 호출되며 주로 초기값을 가지고 있습니다.
- 추상화 : 객체화되지 않고 상속을 주기 위해서만 존재하는 클래스를 의미 합니다.
- 매소드 : 클래스 내부의 함수를 의미 합니다.
"""
from abc import *
class NetworkAdapter(metaclass=ABCMeta) : # 추상 클래스 선언  metaclass=ABCMeta
    @abstractmethod
    def connect(self): pass  # 구현할 내용이 없는 경우 pass 키워드를 사용

class WiFi(NetworkAdapter) :
    def __init__(self, company):  # __init__ : 생성자 만들기
        self.company = company

    def connect(self):  # 부모에게서 상속 받은 추상 메서드를 구현함 (반드시 구현해줘야 함)
        print(f"{self.company} Wi-Fi에 연결 했습니다.")


class FiveG(NetworkAdapter) :
    def __init__(self, company):  # __init__ : 생성자 만들기
        self.company = company

    def connect(self):  # 부모에게서 상속 받은 추상 메서드를 구현함 (반드시 구현해줘야 함)
        print(f"{self.company} 5G에 연결 했습니다.")


net = input("연결할 네트워크를 선택 : [1] WiFi  [2] 5G : ")
if net == "1" :
    adapter = WiFi("KT Megapass")
    adapter.connect()
elif net == "2" :
    adapter = FiveG("LG U+")
    adapter.connect()
else: print("연결할 네트워크가 없습니다.")