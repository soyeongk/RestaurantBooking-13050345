from communication import SmsSender

class TestableSmsSender(SmsSender):
    def __init__(self):
        super().__init__()
        self.sms_sender = False

    def send(self, schedule):
        print("테스트용 SmsSender에서 send 메서드 실행")
        self._send_called = True

    @property
    def send_called(self) -> bool:
        return self._send_called
