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

## Api Urls

### URL

#### api/v1/users/<int:pk>/profile

    + GET
        1. 기능
            - 프로필
        2. 파라미터
            - pk
                - 회원가입시에 자동부여되는 Primary Key
                - GET request 한 유저가 운영자인 경우엔 모든 프로필 일람을 볼 수 있으며(pk 오름차순), 운영자가 아닐 경우엔 본인의 프로필만 볼 수 있다.
                - 운영자가 아닐 경우, pk에 아무리 다른 값을 넣더라도 본인의 프로필만 볼 수 있다.

#### api/v1/users/

    + POST
        1. 기능
            - 회원가입
        2. 파라미터
            + username
                + 회원명. 영어로만 가능. ID 성격임.
            + password
                + 비밀번호. Django의 password validate 기능에 따라 너무 쉬운 password 등은 불가능할 수 있음.
            + age
                + 10대,20대,30대,40대 중에 선택함. 이 외의 나이대의 유저는 없을 것으로 일단 생각하고 제작하므로 선택지가 없다.
            + gender
                + 남성, 여성, 그 외의 성별 중에 선택한다.

            + 그 외에 자신의 avatar 설정이 있을 수 있으나 이것은 서버 용량 관리 문제로 일단 보류.

---

### api/v1/shouts

####

    + GET
        1. 기능
            + 본인의 모든 Shout들을 가져옴.
            + Admin의 경우 모든 유저의 Shouts를 시계열순으로 봄.
        2. 파라미터
            + 없음

####

    + POST
        1. 기능
            + 신규 Shout
            + 글자수 140 ~ 200. 미정.
        2. 파라미터
            + text
                + 자유롭게 글씨를 넣는 것 뿐이다.
