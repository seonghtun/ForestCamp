import React from "react"
import styles from './Image.module.css'
import Paper from '@mui/material/Paper';
const Img = (props) => {
    return (
        <div className={styles.img_wrapper}>
            <img className={styles.size} src={props.imgSrc} alt='img입니다' />
        </div>
    );
}

export default Img