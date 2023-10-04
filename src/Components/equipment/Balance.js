import React from 'react';
import styles from './Balance.module.css';
const Balance = (props) => {
    const recentPrc = props.recentdata
    const fluctuation = props.fluctuationdata
    console.log(recentPrc)
    console.log(fluctuation)

    return (
        <div className={styles.wrapper}>
            <div className={styles.balanceSpan}>
                <span className={styles.recentPrc}>{recentPrc}</span>
                <span className={styles.fluctuation}>{fluctuation}%</span>
            </div>
            <div className={styles.balanceContainer}>
                <span className={styles.balancetext}>Balance</span>
                <div className={styles.hrsolid}></div>
            </div>
        </div>
    );
};

export default Balance; 