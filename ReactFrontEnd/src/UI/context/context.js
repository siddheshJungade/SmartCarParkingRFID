import { createContext, useState} from "react";
import React from "react";

export const AppContext = createContext();

const SysContext = ({ children }) => {
    const [activeTagData,SetActiveTagData] = useState([
        {
            "balance": 100,
            "user_id": 133255188585
        },
        {
            "balance": 100,
            "user_id": 584208811781
        }
    ])
    const handlerClickContextActiveTag = async () =>{
        const result = await fetch(`http://localhost:5000/active-tags`).then((response) => response.json()).then(actulData => actulData);
        SetActiveTagData(result)
    }

    const [carHistory,setCarHistory] = useState([])
    const handlerClickContextCarsHistory = async () => {
        const response = await fetch(`http://localhost:5000/cars-history`).then((response) => response.json()).then(actulData => actulData);
        setCarHistory(response)
    }

    const [ message, setMessage] = useState("");
 
    const handlerListningMessage = (msg) => {
        setMessage(msg)
    }


    return (<AppContext.Provider value={{activeTagData , handlerClickContextActiveTag,carHistory,handlerClickContextCarsHistory,message, handlerListningMessage}}>
        {children}
    </AppContext.Provider>)
}



export default SysContext
