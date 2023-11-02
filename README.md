# forestcamp X cloudmate 인턴십 협업 프로젝트입니다



<br>
<p align="center">
<img width="400px" src="https://github.com/LeeMyungdeok/forestcamp/assets/115915362/1b353e95-3818-4f7b-a253-0f9b0679acc8">
<br>
<img src= "https://img.shields.io/badge/Javascript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white" />
<img src= "https://img.shields.io/badge/nodedotjs-339933?style=flat-square&logo=nodedotjs&logoColor=white" />
<img src= "https://img.shields.io/badge/mysql-4479A1?style=flat-square&logo=mysql&logoColor=white" />
<img src= "https://img.shields.io/badge/mongodb-47A248?style=flat-square&logo=mongodb&logoColor=white" />
<img src= "https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=white" />
<img src= "https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white" />
<img src= "https://img.shields.io/badge/react-61DAFB?style=flat-square&logo=react&logoColor=white" />
<br>
<img src= "https://img.shields.io/badge/amazonec2-FF9900?style=flat-square&logo=amazonec2&logoColor=white" />
<img src= "https://img.shields.io/badge/amazonsimpleemailservice-DD344C?style=flat-square&logo=amazonsimpleemailservice&logoColor=white" />
<img src= "https://img.shields.io/badge/docker-2496ED?style=flat-square&logo=docker&logoColor=white" />
<img src= "https://img.shields.io/badge/inux-FCC624?style=flat-square&logo=linux&logoColor=white" />
<br>
</p>

## 주제 선정 이유
코로나19 대유행 이후, 자연과 야외 활동에 대한 갈망이 증가함에 따라 캠핑장 예약에 대한 인기가 폭발적으로 증가하고 있습니다. 이러한 수요 증가로 인해 지역과 관계없이 캠핑장 예약이 엄청난 경쟁이 일어나고 있어, 예약을 얻기가 어려워진 상황입니다. 그러나 이러한 어려움 중에는 불법 캠핑장 예약 매크로 사이트로 인한 차별적인 문제도 불거져 나왔습니다.
우리의 목표는 이러한 어려움을 극복하고 캠핑을 즐기고자 하는 모든 이들에게 도움을 주기 위한 서비스를 제공하는 것입니다. 일반 정보를 갖고 있지 않은 사람들에게도 캠핑장 예약 정보를 쉽게 접할 수 있도록 하여, 자연과 캠핑의 아름다움을 누릴 수 있는 기회를 확대하는 것이 우리의 목표입니다. 이를 통해 사람들은 더 많은 야외 활동을 즐기며, 동시에 불법 예약과 차별을 줄이는데 도움이 되는 서비스를 제공하고자 합니다.

### development environment



## back-end 아키텍쳐 설계

<p align="center">
<img src='https://github.com/seonghtun/ForestCamp/assets/74886046/8edd99e9-d122-4c1a-8502-a4b379807b5f' width='500px' 
 height='300px'>
</p>

### 기능 동작
|                전체 화면             |                sign up               |
| :----------------------------------: | :----------------------------------: | 
| <img src='https://github.com/LeeMyungdeok/forestcamp/assets/115915362/e0d33021-77ed-43f4-bdf3-d72507daa963' width='400px' height='400px'> | <img src='https://github.com/LeeMyungdeok/forestcamp/assets/115915362/e7ae0496-4111-4ff8-9853-3bb2c9468325' width='400px' height='300px'>  |

|                return              |                rental               |
| :----------------------------------: | :----------------------------------: |
| <img src='https://github.com/LeeMyungdeok/forestcamp/assets/115915362/29467aa2-07ac-4fa5-be32-447cbd0f7abe' width='400px' height='300px'> | <img src='https://github.com/LeeMyungdeok/forestcamp/assets/115915362/90a81ef9-52b3-404b-8c24-9a329da9c126' width='400px' height='300px'> |


## 팀명: forestcamp

* [팀원](링크) - 이명덕, 이민섭, 윤성현, 김인철

## 담당 업무
- 캠핑장 데이터 수집
  - Selenium은 웹 브라우저를 자동화하고 제어할 수 있는 강력한 도구로, 웹 페이지를 렌더링하고 자바스크립트를 실행하여 동적으로 생성되는 콘텐츠를 수집하는 데 사용됩니다. 이를 통해 저희는 캠핑 용품 웹사이트에서 원하는 정보를 수집하고 분석할 수 있게 되었습니다.
    1. 동적 데이터를 가져온 후에는 원하는 정보를 추출하고 저장합니다. 이 과정에서 BeautifulSoup4와 같은 파싱 라이브러리를 사용하여 데이터를 정리하고 필요한 부분을 추출합니다.
    2. 필요한 모든 데이터를 수집하기 위해 페이지를 스크롤하거나 여러 페이지를 방문하는 등의 작업을 반복합니다.
    3. 수집한 데이터를 파일로 저장하거나 데이터베이스에 저장하여 나중에 분석 및 활용할 수 있도록 합니다.
  - 이런 방식으로 Selenium과 BeautifulSoup4를 조합하여 웹에서 동적 데이터를 수집하고 원하는 정보를 효과적으로 추출하는 데이터 수집 기능을 구현했습니다. 이를 통해 캠핑 용품 관련 정보를 자동으로 수집하고 분석하여 사용자에게 유용한 정보를 제공할 수 있게 되었습니다.
- python web framework인 Fast API를 활용하여 캠핑용품에 대한 데이터 조회와 각종 기능을 구현 했습니다.
  1. 캠핑장 찜하기, 알림 기능
  2. 캠핑장 검색 기능
  3. 캠핑장 상세 정보 조회 기능
  4. 캠핑장 카드모양 정보 조회
- mongodb 데이터 관리 
  - 크롤링한 데이터를 효율적으로 관리하고 활용하기 위해 NoSQL 데이터베이스를 선택하였으며, 이를 통해 유연성과 확장성을 확보하면서 터프한 데이터들을 효과적으로관리 하는 방식으로 관리했습니다. 
