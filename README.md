# donkey_ears_api

아무에게도 할 수 없는 말을 아무에게도 보여주지 않고 외칠 수 있는 앱의 API. by Django Rest Framework

---

## Apps

- User

  - User의 설명
    - 말 그대로 User.
    - 유저 회원가입(username, password, 나이대(10대~40대), 성별 필요.) 가능
    - 유저 로그인 가능.

- Shout

  - Shout(샤우트)의 설명

    - 이 앱의 핵심.
    - '임금님 귀는 당나귀 귀' 동화처럼, 어딘가에 외치고는 싶은데 메모장에 쓰긴 그렇고 인터넷에는 말하고 싶고, 하지만 남이 보기에는 좀 그런 내용이라도 자유롭게 외칠 수 있음.
    - Twitter의 Tweet과 비슷함.

  - Shout의 기능 설명.
    - Admin(운영자)는 모든 유저의 Shout를 볼 수 있다.
    - Admin이 아닌 회원의 경우, 자기 자신이 했던 Shout만 오로지 볼 수 있다.
    - 한 회원은 자기 자신의 Shout만 볼 수 있으며 남의 Shout는 볼 수 없다.
    - 하고 싶은 말을 마음껏 할 수 있으나 (글자수 제한 140~200, 미정) 사진은 올릴 수 없다.

---

## Api Document

### 아래의 문서를 참고 바랍니다.

https://documenter.getpostman.com/view/12230851/TW71jmLg
