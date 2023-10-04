import React, { useState, useEffect } from "react"
import { useParams, Link, createBrowserRouter } from 'react-router-dom';
import Img from './Image'
import Information from './information'
import Calendar from './Calendar';
import styles from './CampDetailPage.module.css';
import FacilityIcons from "./FacilityIcons";
import NaverReviewSample from "./NaverReviewSample";
import Paper from '@mui/material/Paper';
import LikeButton from './LikeButton'
import NotOpenCalendar from './NotOpenCalendar'
import Button from '@mui/material/Button';
import axios from "axios";
import NotificationButton from "./NotificationButton";

export default function DetailPage() {
    let { campId } = useParams("");
    const [camping, setCamping] = useState(false)
    const [lets, setLets] = useState("")
    // const [like, setLike] = useState(false)
    const [noti, setNoti] = useState(false)
    console.log(campId)
    // const [userData, setUserData] = useState(null);
    const url = `/v1/search/blog.json?query=${camping.name}&display=3`
    // console 
    // const handleFavorOrNoti = async (category, type, action, num) => {
    //     // API 호출을 위한 기본 URL
    //     const baseURL = "http://13.125.151.237:3000"; // 서버의 실제 주소로 변경해야 할 수 있습니다.


    //     try {
    //         // userData에서 userId를 가져옵니다.
    //         const userId = userData?.userId;

    //         // 예: http://13.124.209.114:3000/add/campfavor
    //         const userUrl = `${baseURL}/${category}/${type}`;

    //         const payload = { userid: userId, [`${category}num`]: num };

    //         // axios 요청시 쿠키를 포함
    //         if (action === "add") {
    //             await axios.post(userUrl, payload, { withCredentials: true });
    //         } else if (action === "delete") {
    //             await axios.delete(userUrl, { data: payload, withCredentials: true });
    //         } else if (action === "get") {
    //             const result = await axios.get(userUrl + `?${category}num=${num}`, { withCredentials: true });
    //             alert(result)
    //         }

    //         alert(`Successfully ${action}ed to ${type}`);
    //     } catch (error) {
    //         console.error(`An error occurred while ${action}ing to ${type}:`, error);
    //     }
    // };


    // loginCheck();


    // useEffect(() => {
    //     const handleBeforeUnload = (event) => {
    //         // Perform actions before the component unloads
    //         event.preventDefault();
    //         event.returnValue = false;
    //     };
    //     window.addEventListener('beforeunload', handleBeforeUnload);
    //     window.addEventListener('popstate', handlePopstate);

    //     return () => {
    //         window.removeEventListener('beforeunload', handleBeforeUnload);
    //         window.removeEventListener('popstate', handlePopstate);
    //     };
    // }, []);

    useEffect(() => {
        fetchMyPage();
    }, []);

    const fetchMyPage = async () => {
        try {
            console.log(campId)
            const response = await axios.get(`http://43.200.73.25:3000/camp/favor/`, {
                withCredentials: true,
                params: {
                    campnum: campId
                }
            });
            const { rows } = response.data;
            console.log(rows)
            // 상태 업데이트
            setLets(rows);
            console.log(rows)
        } catch (error) {
            console.error("An error occurred:", error);
            // 에러 핸들링
        }
    };




    useEffect(() => {
        fetch(`http://13.209.180.103:3000/camp/row/${campId}`, {
            headers: {
                Accept: "application/json",
                mode: 'no-cors',
            },
            method: "GET"
        }).then(res => res.json())
            .then(res => {
                console.log(1, res.ok);
                console.log(2, res);
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
                        <div className={styles.inline}>
                            <LikeButton className={styles.inline_in} lets={lets} campId={campId} />
                            <NotificationButton className={styles.inline_in} noti={noti} campName={camping.name} onClick={setNoti} />
                        </div>

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

// onClick = { setLike }