import { useContext } from "react";
import { AppContext } from "./context/context";
import { useNavigate } from "react-router-dom";
import React from "react";


const CarHistory = () => {
    let navigate = useNavigate();
    const {handlerClickContextCarsHistory} = useContext(AppContext);

    return  <button type="button" className="btn btn-warning" onClick={() => {
        handlerClickContextCarsHistory()
        navigate('/cars-history')
    }}>Car History</button>;
}

export default CarHistory;