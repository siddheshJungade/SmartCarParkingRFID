import React from "react";

const ActiveTagItem = (props) => {
    return <>
        <tr>
      <td>{props.user_id}</td>
      <td>{props.balance}</td>
    </tr>
    </>
}

export default ActiveTagItem;