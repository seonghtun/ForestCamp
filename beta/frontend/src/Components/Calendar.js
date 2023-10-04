import React, { useState } from 'react';
import Paper from '@mui/material/Paper';
import styles from './Calnedar.module.css';



const RenderHeader = (props) => {

    const date = new Date(props.date)

    return (
        <div className={styles.head}>
            <h1 className={styles.head_title}>
                {date.getMonth() + 1}월
            </h1>
            <p className={styles.head_subtitle}>
                {date.getFullYear()}
            </p>
        </div>
    )
}

const TableCells = ({ date, able, state }) => {
    const startDate = new Date(date)
    const prevMonthDate = new Date(startDate.getFullYear(), startDate.getMonth(), 0)
    const endDate = new Date(startDate.getFullYear(), startDate.getMonth() + 1, 0)
    const today = new Date()
    const [isSelected, setIsSelected] = useState(false);
    const rows = [];
    let rowNum = 0;
    let days = [];
    let day = 1;
    let ableIndex = 0;
    let isAble = false;

    for (let i = startDate.getDay(); i > 0; i--) {
        days.push(<td className={`${styles.day_disabled} ${styles.cell}`} key={
            prevMonthDate.getFullYear() + '/' + prevMonthDate.getMonth() + '/' + (prevMonthDate.getDate() - i)}>
            {prevMonthDate.getDate() - i}</td >);
    }

    for (let i = startDate.getDay(); i < 7; i++) {
        if (able && ableIndex < able.length && parseInt(able[ableIndex].slice(-2)) === day) isAble = true;

        days.push(
            <td className={`${isSelected ? styles.seleted : styles.notSelected} ${styles.cell}`} key={
                startDate.getFullYear() + '/' + startDate.getMonth() + '/' + (day)}>
                <div>
                    <span>{day}</span>
                </div>
                <div><span className={`${styles.state}`}>{isAble ? state && state[ableIndex].join(' / ') : ""}</span></div>
            </td>
        );
        if (isAble) {
            ableIndex++;
            isAble = false;
        }
        day++;
    }

    rows.push(days);
    days = []

    while (day <= endDate.getDate()) {
        if (able && ableIndex < able.length && parseInt(able[ableIndex].slice(-2)) === day) isAble = true;

        days.push(
            <td className={`
                ${today.getMonth() === startDate.getMonth() &&
                    today.getDate() === day ? styles.today : ''}
                ${isSelected ? styles.seleted : styles.notSelected} 
                ${styles.cell}`}
                key={startDate.getFullYear() + '/' + startDate.getMonth() + '/' + (day)}
            >
                <div>{day}</div>
                <div><span className={styles.state}>{isAble ? state && state[ableIndex].join(' / ') : ""}</span></div>
            </td>
        );
        day++;
        if (isAble) {
            ableIndex++;
            isAble = false;
        }

        if (days.length === 7) {
            rows.push(days);
            days = [];
        }
    }
    rows.push(days)

    for (let i = endDate.getDay(); i < 7; i++) {
        rows[rows.length - 1].push(
            <td className={styles.day_disabled} key={`${i + 20} disable`}></td>
        )
    }

    return (
        <tbody key={'tableBody'}>
            {rows.map(row => {
                rowNum++;
                return (
                    <tr
                        key={`${rowNum}row`}
                    >
                        {row}
                    </tr>)
            })}
        </tbody>
    )
}

const TableHeader = () => {
    const days = [];
    const date = ['Sun', 'Mon', 'Thu', 'Wed', 'Thrs', 'Fri', 'Sat'];

    for (let i = 0; i < 7; i++) {
        days.push(
            <td className={styles.head_cell} key={date[i]}>{date[i]}</td>
        )
    }
    return days
}

function Calendar({ date, able, state }) {

    return (
        <div>
            <RenderHeader date={date} />
            <table className={styles.calendar} >
                <thead>
                    <tr>
                        <TableHeader />
                    </tr>
                </thead>
                <TableCells date={date} able={able} state={state} />
            </table >
        </div>
    );
}

export default Calendar;