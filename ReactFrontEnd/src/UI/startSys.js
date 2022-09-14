
import React, { useState } from "react";
import { socket } from "../App";
import { useNavigate } from "react-router-dom";

const StartSys = () => {
    let navigate = useNavigate();

    const [sysStatus,setSystemStatus] = useState(false)
    const startSysHadler = async () => {
        setSystemStatus(true);
        socket.emit('message',"lissining.....")
        const response = await fetch(`http://localhost:5000/start-sys`).then((response) => response.text()).then(actulData => actulData);
        console.log(response,sysStatus)
    }


    return <>
        { sysStatus ? <button type="button" className="btn btn-danger" onClick={() => navigate('/')}>Home</button> 
        : <button type="button" className="btn btn-primary" onClick={startSysHadler}>Start</button> }
        
        
    </>
}

export default StartSys;