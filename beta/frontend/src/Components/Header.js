import React from 'react';
import styles from './Header.module.css';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faMagnifyingGlass, faUser, faPowerOff } from "@fortawesome/free-solid-svg-icons"
import { Link } from 'react-router-dom'


const Header = () => {

    return (
        <div className={styles.wrapper}>
            <div className={styles.headerContainer}>
                <div className={`${styles.logo} ${styles.left}`}>
                    <Link to='http://ec2-43-200-73-25.ap-northeast-2.compute.amazonaws.com/'>
                        <div className={styles.logoImg} />
                    </Link>
                </div>

                <div className={`${styles.right} ${styles.icon}`}>
                    <Link to='http://ec2-43-200-73-25.ap-northeast-2.compute.amazonaws.com/search'> <FontAwesomeIcon className={`${styles.icon_spacing} ${styles.icons}`} icon={faMagnifyingGlass} /></Link>
                    <a href='http://ec2-13-124-209-114.ap-northeast-2.compute.amazonaws.com:3000/'>
                        <FontAwesomeIcon className={`${styles.icon_spacing} ${styles.icons}`} icon={faPowerOff} />
                    </a>
                    <Link to='http://ec2-13-124-209-114.ap-northeast-2.compute.amazonaws.com:3000/mypage'><FontAwesomeIcon className={`${styles.icon_spacing} ${styles.icons}`} icon={faUser} /></Link>
                </div>
            </div>
        </div>
    );
};

export default Header;
