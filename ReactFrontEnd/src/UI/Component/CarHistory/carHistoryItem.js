import React from "react";


const CarHistoryItem = (props) => {
    return <>
            <tr>
      <td>{props.userId}</td>
      <td>{props.intime}</td>
      <td>{props.outtime}</td>
      <td>{props.duration}</td>
    </tr>
    </>
}


export default CarHistoryItem;