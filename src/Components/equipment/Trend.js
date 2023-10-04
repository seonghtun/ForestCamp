import React from "react";
import styles from "./Trend.module.css";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
} from "recharts";
// import { ResponsiveLine } from '@nivo/line'
function Trend(props) {
  const data = props.trenddata;
  console.log(data);
  return (
    <div className={styles.wrapper}>
      <LineChart
        width={1024}
        height={400}
        data={data}
        margin={{
          top: 5,
          right: 30,
          left: 20,
          bottom: 5,
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="recentTime" />
        <YAxis domain={['auto', 'auto']} />
        <Tooltip />
        <Legend />
        <Line
          type="monotone"
          dataKey="recentPrc"
          stroke="#82ca9d"
        // activeDot={{ r: 8 }}
        />
      </LineChart>
    </div>
  );
}

export default Trend;

//     return (
//         <div className={styles.wrapper}>
//             <div className={styles.trendContainer}>
//                 <span>
//                     <img src="http://43.202.93.56:3000/Campingstore/trends?id=1010001" alt="img" className={styles.trend} ></img>
//                 </span>s
//             </div>
//         </div>
//     );
// };
