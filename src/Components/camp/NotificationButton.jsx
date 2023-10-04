import React, { useState } from "react"
import axios from 'axios'
import { Cookies } from 'react-cookie';

// import styles from './like.module.css';

// const NotiCountHandler = (toggle, count, onClick) => {

//     if (toggle) {
//         onClick(count + 1)
//     } else {
//         onClick(count - 1)
//     }
// }


function NotificationButton({ className, noti, onClick, campName }) {
    const cookies = new Cookies();
    const [notiCount, setNotiCount] = useState(0);

    async function toggleNoti() {
        onClick(!noti)
        console.log(noti)
        if (noti == true) {
            const response = await axios.delete(
                `http://13.209.180.103:3000/camp/sns_sub`,
                {
                    data: {
                        email: "yyh718@naver.com",
                        camp_name: campName
                    }
                });

            // 상태 업데이트
        } else {
            const response = await axios.post(
                `http://13.209.180.103:3000/camp/sns_sub`,
                {
                    email: "yyh718@naver.com",
                    camp_name: campName
                }
            );

        }
    }

    return (

        <div onClick={toggleNoti} className={className}>
            {noti ? (
                <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 32 32"><path fill="#000000" d="M28.707 19.293L26 16.586V13a10.014 10.014 0 0 0-9-9.95V1h-2v2.05A10.014 10.014 0 0 0 6 13v3.586l-2.707 2.707A1 1 0 0 0 3 20v3a1 1 0 0 0 1 1h7v1a5 5 0 0 0 10 0v-1h7a1 1 0 0 0 1-1v-3a1 1 0 0 0-.293-.707ZM19 25a3 3 0 0 1-6 0v-1h6Z"></path></svg>

            ) : (
                <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 32 32"><path fill="#000000" d="M28.707 19.293L26 16.586V13a10.014 10.014 0 0 0-9-9.95V1h-2v2.05A10.014 10.014 0 0 0 6 13v3.586l-2.707 2.707A1 1 0 0 0 3 20v3a1 1 0 0 0 1 1h7v.777a5.152 5.152 0 0 0 4.5 5.199A5.006 5.006 0 0 0 21 25v-1h7a1 1 0 0 0 1-1v-3a1 1 0 0 0-.293-.707ZM19 25a3 3 0 0 1-6 0v-1h6Zm8-3H5v-1.586l2.707-2.707A1 1 0 0 0 8 17v-4a8 8 0 0 1 16 0v4a1 1 0 0 0 .293.707L27 20.414Z"></path>
                </svg>
            )}
            <p>{notiCount}</p>
        </div>
    )
}

export default NotificationButton