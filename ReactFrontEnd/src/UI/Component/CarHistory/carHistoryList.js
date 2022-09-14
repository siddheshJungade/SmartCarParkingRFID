import CarHistoryItem from "./carHistoryItem";
import CARHISTORY from '../../../car_history.json'
import React from "react";


const CarHistoryList = () => {
    return <>
        <div>
      <table className="table">
        <thead>
          <tr>
            <th scope="col">TAG NO</th>   
            <th scope="col">InTime</th>
            <th scope="col">OutTime</th>
            <th scope="col">Duration</th>
          </tr>
        </thead>
        <tbody>
          {CARHISTORY.map((item ,id) => {
            const {user_id,intime,outtime,duration} = item
            return <CarHistoryItem key={id} userId={user_id} intime={intime} outtime={outtime} duration={duration} />
          })
       
          }
        </tbody>
      </table>
    </div>
    </>
}

export default CarHistoryList;