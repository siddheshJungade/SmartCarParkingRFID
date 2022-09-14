import { useContext, useEffect} from "react";
import { socket } from "../App";
import React from "react";
import { AppContext } from "./context/context";
import Recharge from "./recharge";


const Main = () => {
    const {message, handlerListningMessage} = useContext(AppContext)
    useEffect(() => {
        getMessage()
    },[])


    const getMessage = () => {
        socket.on('message', (data) => {
            handlerListningMessage(data)
        })
    }
    return <>
        <h1>Smart Car Parking System</h1>
        <h4>{message}</h4>
        {
            message === 'recharge' ? <Recharge /> : " "
        }
    </>
}

export default Main;