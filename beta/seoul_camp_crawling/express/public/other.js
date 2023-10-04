function campInfo(url) {
    const xhr = new XMLHttpRequest();
    const method = "GET";
    console.log(url)
    xhr.open(method, url);

    // xhr.open(method, 'http://54.180.186.96:3000/camp/resource/난지');
    // xhr.setRequestHeader('Access-Control-Allow-Origin', 'http://54.180.186.96:8000')
    xhr.send();

    xhr.onreadystatechange = function () {
        if (xhr.readyState !== 4) return;

        if (xhr.status === 200) {
            console.log(xhr.responseText);
            const img = document.getElementById('image');
            const info = document.getElementById('use-info');
            const res = JSON.parse(xhr.response);
            console.log(res.data)

            document.title = document.title + ` > ${res.data.name}`
            img['src'] = res.data.img_url
            info.innerHTML = res.data.information_use
            console.log(new Date(res.data.use_term[0]))
            buildCalendar(new Date(res.data.use_term[0]))
            wish(res.data)
        } else {
            console.log("HTTP error", xhr.status, xhr.statusText);
        }
    };
}

function userInfo() {
    const xhr = new XMLHttpRequest();
    const method = "GET";
    const url = "#";
    xhr.open(method, url);
    xhr.send();

    xhr.onreadystatechange = function () {
        if (xhr.readyState !== 4) return;

        if (xhr.status === 200) {
            console.log(xhr.response);
            const res = JSON.parse(xhr.response);
            res.data.data.img_url
            element.innerHTML = res.data.information_use
        } else {
            console.log("HTTP error", xhr.status, xhr.statusText);
        }
    };
}

function buildCalendar(useDate) {
    let today = new Date();     // 페이지를 로드한 날짜를 저장
    today.setHours(0, 0, 0, 0)

    let firstDate = new Date(useDate.getFullYear(), useDate.getMonth(), 1);     // 이번달 1일
    let lastDate = new Date(useDate.getFullYear(), useDate.getMonth() + 1, 0);  // 이번달 마지막날
    let tbody_Calendar = document.querySelector(".Calendar > tbody");

    document.getElementById("calYear").innerText = useDate.getFullYear();             // 연도 숫자 갱신
    document.getElementById("calMonth").innerText = leftPad(useDate.getMonth() + 1);  // 월 숫자 갱신

    while (tbody_Calendar.rows.length > 0) {                        // 이전 출력결과가 남아있는 경우 초기화
        tbody_Calendar.deleteRow(tbody_Calendar.rows.length - 1);
    }

    let nowRow = tbody_Calendar.insertRow();        // 첫번째 행 추가           
    for (let j = 0; j < firstDate.getDay(); j++) {  // 이번달 1일의 요일만큼
        let nowColumn = nowRow.insertCell();        // 열 추가
    }
    //const day1 = birthday.getDay();
    // Sunday - Saturday : 0 - 6

    for (let nowDay = firstDate; nowDay <= lastDate; nowDay.setDate(nowDay.getDate() + 1)) {   // day는 날짜를 저장하는 변수, 이번달 마지막날까지 증가시키며 반복  

        let nowColumn = nowRow.insertCell();        // 새 열을 추가하고
        nowColumn.innerText = leftPad(nowDay.getDate());      // 추가한 열에 날짜 입력

        if (nowDay.getDay() == 0) {                 // 일요일인 경우 글자색 빨강으로
            nowColumn.style.color = "#DC143C";
        }
        if (nowDay.getDay() == 6) {                 // 토요일인 경우 글자색 파랑으로 하고
            nowColumn.style.color = "#0000CD";
            nowRow = tbody_Calendar.insertRow();    // 새로운 행 추가
        }

        if (nowDay < today) {                       // 지난날인 경우
            nowColumn.className = "pastDay";
        }
        else if (nowDay.getFullYear() == today.getFullYear() && nowDay.getMonth() == today.getMonth() && nowDay.getDate() == today.getDate()) { // 오늘인 경우           
            nowColumn.className = "today";
            nowColumn.onclick = function () { choiceDate(this); }
        }
        else {                                      // 미래인 경우
            nowColumn.className = "futureDay";
            nowColumn.onclick = function () { choiceDate(this); }
        }
    }
}

// 날짜 선택
function choiceDate(nowColumn) {
    if (document.getElementsByClassName("choiceDay")[0]) {                              // 기존에 선택한 날짜가 있으면
        document.getElementsByClassName("choiceDay")[0].classList.remove("choiceDay");  // 해당 날짜의 "choiceDay" class 제거
    }
    nowColumn.classList.add("choiceDay");           // 선택된 날짜에 "choiceDay" class 추가
}



// 이전달 버튼 클릭
// function prevCalendar(useDate) {
//     useDate = new Date(useDate.getFullYear(), useDate.getMonth() - 1, useDate.getDate());   // 현재 달을 1 감소
//     buildCalendar();    // 달력 다시 생성
// }
// 다음달 버튼 클릭
// function nextCalendar(useDate) {
//     useDate = new Date(useDate.getFullYear(), useDate.getMonth() + 1, useDate.getDate());   // 현재 달을 1 증가
//     buildCalendar();    // 달력 다시 생성
// }

// input값이 한자리 숫자인 경우 앞에 '0' 붙혀주는 함수

function ratingReview() {

}

function imgDraw(imgUrl) {
    const element = document.getElementById("image");
    element.setAttribute('src', imgUrl)
}

function addList(list, key, value, url) {

    // 2. 추가할 li element 생성
    // 2-1. 추가할 li element 생성
    const li = document.createElement("li");
    // 2-2. li에 id 속성 추가 
    li.setAttribute('id', key);

    let textNode
    if (url) {
        const aTag = document.createElement('a');
        textNode = document.createTextNode(value)
        aTag.setAttribute('id', 'reservation');
        aTag['href'] = url;
        aTag.appendChild(textNode);
        li.appendChild(aTag)
    } else {
        // 2-3. li에 text node 추가 
        textNode = document.createTextNode(value);
        li.appendChild(textNode);
    }
    // 3. 생성된 li를 ul에 추가
    list.appendChild(li);
}


function wish(data) {
    const list = document.querySelector('div.alternating-colors > ul')
    addList(list, 'use_term', data['use_term'].join('~'));
    addList(list, 'receipt_term', data['receipt_term'].join('~'));
    addList(list, 'phone', data['phone']);
    if (data['is_tent']) addList(list, 'is_tent', "텐트 제공");
    else addList(list, 'is_tent', "텐트 미제공");
    addList(list, 'camp_url', '예약페이지로 이동', data['camp_url']);
}

// function () { }