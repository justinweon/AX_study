while True: #무한루프. 참인경우 계속 반복
    print("아무 메세지나 입력(q-종료)", end="")
    message = input()

    if message == "q":
        print("종료합니다")
        break #반복중단.

    print ("입력메세지:", message)

cmd에서 운영한 스크린샷 참조 