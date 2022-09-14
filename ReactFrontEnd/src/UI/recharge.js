
import { socket } from "../App";
import React from "react";

const Recharge = () => {




    const noRecharge = async () => {
        console.log("norecharge")
        const response = await fetch(`http://localhost:5000/no-recharge`).then((response) => response.text()).then(actulData => actulData);
        console.log(response)
    }

    const rechargeHandler = async () => {
        socket.emit('message',"Tap to Recharge")
        const response = await fetch(`http://localhost:5000/recharge`).then((response) => response.text()).then(actulData => actulData);
        console.log(response)
    }
    return (<div>
        <button type="button" className="btn btn-danger mx-2" onClick={()=> {
            noRecharge()
        }}>No</button>
        <button type="button" className="btn btn-success mx-4" onClick={()=> {
           rechargeHandler()
       }}>yes</button>
    </div> );
}

export default Recharge;