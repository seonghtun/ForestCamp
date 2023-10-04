import React, { useState, useEffect } from "react"
import { useParams } from 'react-router-dom';
import Img from './Image'
import Information from './information'
import Calendar from './Calendar';
import styles from './DetailPage.module.css';
import FacilityIcons from "./FacilityIcons";
import NaverReviewSample from "./NaverReviewSample";
import Paper from '@mui/material/Paper';
import LikeButton from './like'
import NotOpenCalendar from './NotOpenCalendar'
import Button from '@mui/material/Button';

// function List(props) {
//   return (
//     <ul>
//       <li>이용기간 : {props.data.use_term}</li>
//       <li>접수기간 : {props.data.receipt_term}</li>
//       <li>문의전화 : {props.data.phone}</li>
//       <li>텐트 : {props.data.is_tent ? "텐트 제공" : "텐트 미제공"}</li>
//       <li><a href={props.data.camp_url}>예약페이지로 이동</a></li>
//     </ul>
//   )
// }

export default function DetailPage() {
    let { campId } = useParams();
    const [camping, setCamping] = useState([])
    const url = `/v1/search/blog.json?query=${camping.name}&display=3`

    useEffect(() => {
        fetch(`http://54.180.186.96:3000/camp/row/${campId}`, {
            headers: {
                Accept: "application/json",
                mode: 'no-cors',
            },
            method: "GET"
        }).then(res => res.json())
            .then(res => {
                console.log(1, res.ok);
                // console.log(2, res.data);
                setCamping(res.data);
            })
    }, []);

    return (
        <div className={`${styles.main}`}>

            <Paper>
                <div className={styles.container}>
                    <div className={styles.item}>
                        <h1 className={styles.name}>{camping.name}</h1>
                    </div>
                    <div className={styles.item}>
                        <Img imgSrc={camping.img_url} />
                        <FacilityIcons isTent={camping.is_tent} className={styles.inline} />
                        <LikeButton className={styles.inline} />
                    </div>
                    {camping.name !== undefined ? (
                        <div className={styles.item}>
                            <NaverReviewSample url={url} name={camping.name} />
                        </div>) :
                        (<div></div>)
                    }

                    {/* // <List camping={camping} /> */}
                    <div className={styles.item}>
                        <Calendar date={
                            camping.use_term ?
                                camping.use_term[0].split('.') : ""}
                            able={camping.able_date} state={camping.reservation_state} />
                    </div>
                    <div className={styles.item}>
                        <NotOpenCalendar date={
                            camping.use_term ?
                                camping.use_term[0].split('.') : ""} />
                    </div>
                </div>
            </Paper>
            <div className={styles.fixed_btn}>
                <Button variant="contained" onClick={() => { window.open(camping.camp_url, '_blank') }} color="success">
                    예약 페이지
                </Button>
            </div>
            <div className={styles.info}>
                <Information info={camping.information_use} src={camping.part_plan} />
            </div>
        </div>
    )
}
