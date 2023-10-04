import React from "react";
import styles from "./Header.module.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faMagnifyingGlass,
  faUser,
  faPowerOff,
} from "@fortawesome/free-solid-svg-icons";
import { Link } from "react-router-dom";

function isTokenPresent() {
  return document.cookie
    .split(";")
    .some((item) => item.trim().startsWith("auth_token="));
}

const Header = () => {
  const hasToken = isTokenPresent();

  return (
    <div className={styles.wrapper}>
      <div className={styles.headerContainer}>
        <div className={`${styles.logo} ${styles.left}`}>
          <Link to="/">
            <div className={styles.logoImg} />
          </Link>
          {" "}
        </div>

        <div className={`${styles.right} ${styles.icon}`}>
          <Link to="/search">
            <FontAwesomeIcon
              className={`${styles.icon_spacing} ${styles.icons}`}
              icon={faMagnifyingGlass}
            />
          </Link>
          <a href={hasToken ? "http://43.200.73.25:3000/logout" : "/login"}>
            <FontAwesomeIcon
              className={`${styles.icon_spacing} ${styles.icons}`}
              icon={faPowerOff}
            />
          </a>
          <Link to={hasToken ? "http://43.200.73.25:3000/mypage" : "/login"}>
            <FontAwesomeIcon
              className={`${styles.icon_spacing} ${styles.icons}`}
              icon={faUser}
            />
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Header;
