# programmers-campus-auto-video-finish
프로그래머스 캠퍼스 강의 동영상을 자동으로 이수해주는 프로그램입니다.

> [!WARNING]
> 이 프로젝트는 교육용 목적으로 개발되었습니다.</br>
> 프로젝트 사용에 대한 모든 책임은 사용자 본인에게 있으며, 사용 중 발생하는 모든 문제에 대해서는 책임지지 않습니다. 

## 사용법
기본적으로 `Python 3.x`가 설치가 필요합니다.

### 1. 해당 리포지토리를 불러옵니다.
```
git clone https://github.com/simnple/programmers-campus-auto-video-finish
cd programmers-campus-auto-video-finish
```

### 2. `.env` 파일의 내용물을 수정합니다.
```
PROGRAMMERS_ID = -1
COOKIE = ""
```
여기서 `PROGRAMMERS_ID`는 프로그래머스 캠퍼스 아이디, `COOKIE`는 `.programmers.co.kr`의 쿠키의 평문 형태입니다.

#### 2-1. 프로그래머스 캠퍼스 아이디가 뭔지 모르겠어요.
프로그래머스 캠퍼스 대시보드로 이동할 경우에 다음과 같은 링크를 확인하실 수 있습니다.
```
https://campus.programmers.co.kr/app/courses/{캠퍼스 아이디}/dashboard
```
`/courses/`와 `/dashboard` 사이에 있는 숫자가 캠퍼스 아이디입니다.

#### 2-2. 쿠키가 뭔지 모르겠어요.

1. 자신의 프로그래머스 캠퍼스 대시보드 사이트에 접속합니다.
2. `F12`를 눌러 개발자 도구를 엽니다.
3. `Network(네트워크)` 탭에 들어갑니다.
4. `Clear Network log` 버튼을 누릅니다.
5. 페이지를 새로고침합니다. (`F5`)
6. 개발자 도구에 뜬 요소들 중 `dashboard`를 찾고 클릭합니다. (보통 맨 위 요소)
7. `Headers -> Request Headers -> Cookie` 가 필요한 쿠키입니다.

### 3. 파일을 실행합니다.
```
python3 main.py
```
