import React, { useEffect, useState } from "react";
import axios from "axios";

function MyPage() {
  const [userData, setUserData] = useState(null);

  // API 호출을 위한 기본 URL
  const baseURL = "http://43.200.73.25:3000";

  useEffect(() => {
    fetchMyPage();
  }, []);

  const fetchMyPage = async () => {
    try {
      const response = await axios.get("http://43.200.73.25:3000/mypage", {
        withCredentials: true, // 쿠키 포함
      });
      const { displayName, email } = response.data;

      // 상태 업데이트
      setUserData({ displayName, email });

      console.log("User info:", displayName, email);
    } catch (error) {
      console.error("An error occurred:", error);
      // 에러 핸들링
    }
  };

  // 컴포넌트 마운트 될 때 호출
  useEffect(() => {
    fetchMyPage();
  }, []);

  const handleLogout = async () => {
    try {
      // 로그아웃 버튼 클릭 시 로그아웃 URL로 이동
      window.location.href = "http://43.200.73.25:3000/logout";
    } catch (error) {
      console.error("Logout failed:", error);
    }
  };

  // 즐겨찾기나 알림을 추가/삭제하는 함수
  const handleFavorOrNoti = async (category, type, action, num) => {
    try {
      // userData에서 userId를 가져옵니다.
      const userId = userData?.userId;

      const url = `${baseURL}/${category}/${type}`;

      const payload = { userid: userId, [`${category}num`]: num };

      // axios 요청시 쿠키를 포함
      if (action === "add") {
        await axios.post(url, payload, { withCredentials: true });
      } else if (action === "delete") {
        await axios.delete(url, { data: payload, withCredentials: true });
      } else if (action === "get") {
        const result = await axios.get(url + `?${category}num=${num}`, {
          withCredentials: true,
        });
        alert(result);
      }

      alert(`Successfully ${action}ed to ${type}`);
    } catch (error) {
      console.error(`An error occurred while ${action}ing to ${type}:`, error);
    }
  };

  return (
    <div>
      <h1>Welcome to MyPage</h1>
      <p>Display Name: {userData?.displayName}</p>
      <p>Email: {userData?.email}</p>
      <button onClick={handleLogout}>Logout</button>
      <button onClick={() => handleFavorOrNoti("camp", "favor", "add", 1)}>
        Add to Camp Favor
      </button>
      <button onClick={() => handleFavorOrNoti("camp", "favor", "delete", 1)}>
        Remove from Camp Favor
      </button>
      <button onClick={() => handleFavorOrNoti("camp", "noti", "add", 1)}>
        Add to Camp Notification
      </button>
      <button onClick={() => handleFavorOrNoti("camp", "noti", "delete", 1)}>
        Remove from Camp Notification
      </button>
      <button onClick={() => handleFavorOrNoti("equipment", "favor", "add", 1)}>
        Add to Equipment Favor
      </button>
      <button
        onClick={() => handleFavorOrNoti("equipment", "favor", "delete", 1)}
      >
        Remove from Equipment Favor
      </button>
      <button onClick={() => handleFavorOrNoti("equipment", "noti", "add", 1)}>
        Add to Equipment Notification
      </button>
      <button
        onClick={() => handleFavorOrNoti("equipment", "noti", "delete", 1)}
      >
        Remove from Equipment Notification
      </button>
    </div>
  );
}

export default MyPage;
