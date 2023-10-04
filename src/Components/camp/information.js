import React from "react"
import Paper from '@mui/material/Paper';

const Information = (props) => {
    let str = props.info;
    // console.log("info", str)
    if (props.src) {
        var el = document.createElement('html');
        el.innerHTML = props.info
        var imgTag = el.getElementsByClassName('v_img'); // Live NodeList of your anchor elements
        imgTag[0].src = props.src;
        str = el.getElementsByClassName('tab_con active')[0].outerHTML
    }

    // console.log(el.getElementsByClassName('v_img')[0].src)
    return (
        <Paper>
            <div style={{ display: 'flex', justifyContent: 'center' }} dangerouslySetInnerHTML={{ __html: str }} >
            </div>
        </Paper >
    );
}

export default Information