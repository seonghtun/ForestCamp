import React from "react";
import styles from "./Login.module.css";
import Naver from "./images/naver.png";
import Google from "./images/google.png";
import Kakao from "./images/kakao.png";

const iconStyle = {
  width: "30px",
  height: "30px",
};

const Login = () => {
  const onLogin = (provider) => {
    const baseUrl = "http://43.200.73.25:3000";
    const authURLs = {
      naver: baseUrl + "/auth/naver",
      google: baseUrl + "/auth/google",
      kakao: baseUrl + "/auth/kakao",
    };

    window.location.href = authURLs[provider];
  };

  return (
    <div className={styles.login_div}>
      <button onClick={() => onLogin("naver")}>
        <img src={Naver} alt="Naver" style={iconStyle} /> Continue with NAVER
      </button>
      <button onClick={() => onLogin("google")}>
        <img src={Google} alt="Google" style={iconStyle} /> Continue with Google
      </button>
      <button onClick={() => onLogin("kakao")}>
        <img src={Kakao} alt="Kakao" style={iconStyle} /> Continue with Kakao
      </button>
    </div>
  );
};

export default Login;
