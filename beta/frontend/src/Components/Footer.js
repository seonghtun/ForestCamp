import React, { useEffect, useState } from 'react';
import styles from './Footer.module.css';

const Footer = () => {
    const [showFooter, setShowFooter] = useState(false);

    useEffect(() => {
        const handleScroll = () => {
            const isBottom = window.innerHeight + window.scrollY >= document.documentElement.scrollHeight;
            setShowFooter(isBottom);
        };

        window.addEventListener('scroll', handleScroll);
        return () => {
            window.removeEventListener('scroll', handleScroll);
        };
    }, []);



    return (
        <div className={`${styles.wrapper} ${showFooter ? styles.visible : ""}`}>
            <div className={styles.footerContainer}>
                <div className={styles.flexContainer}>
                    <div className={`${styles.flexItemLogo}`}>
                        <div className={styles.imgwrap} />
                    </div>
                    <div className={`${styles.flexItem} ${styles.rightLine}`}>
                        <h3>ForestCamp X CloudMate</h3>
                        <span>해당 사이트는 Kibwa 기업멤버십SW 캠프</span><br />
                        <span>파이널 프로젝트로 제작되었습니다</span><br />
                        <h5>팀원 소개</h5>
                        <span>김인철:Laby8239@gmail.com</span><br />
                        <span>이명덕:audejr21345@gmail.com</span><br />
                        <span>이민섭:lyll4192@gmail.com </span><br />
                        <span>윤성현:ysh970718@gmail.com</span><br />
                    </div>
                    <div className={styles.flexItem}>
                        <h1>대충 내용 </h1>
                        <span>
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                        </span>
                    </div>
                </div>
                <div className={`${styles.flexItem} ${styles.foot}`}>
                    ⓒ 2023 - 2023 Privacy - Team
                </div>
            </div>
        </div>
    );
};

export default Footer;
