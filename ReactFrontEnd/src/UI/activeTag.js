import { useContext } from "react";
import { AppContext } from "./context/context";
import { useNavigate } from "react-router-dom";
import React from "react";

const ActiveTag = () => {
    let navigate = useNavigate();
    const { handlerClickContextActiveTag } = useContext(AppContext)

    return  <button type="button" className="btn btn-success mx-4" onClick={()=> {
           handlerClickContextActiveTag()
           navigate("/active-tag")
       }}>Active Tag</button>;

}

export default ActiveTag;