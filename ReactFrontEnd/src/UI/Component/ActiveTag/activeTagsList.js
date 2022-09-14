import ActiveTagItem from "./activeTagItem";
import { useContext } from "react";
import { AppContext } from "../../context/context";

import React from "react";


const ActiveTagsList = () => {
  const {activeTagData} = useContext(AppContext)

    return <>
     <div>
      <table className="table">
        <thead>
          <tr>
            <th scope="col">TAG NO</th>
            <th scope="col">Balance</th>
          </tr>
        </thead>
        <tbody>
        {activeTagData.map(item => {
            const {user_id,balance} = item
            return <ActiveTagItem key={user_id} user_id={user_id} balance={balance} />
          })
       
          }
            
        </tbody>
      </table>
    </div>
    </>
}

export default ActiveTagsList;