import ActiveTag from './activeTag';
import StartSys from './startSys';
import CarHistory from './carHistory';
import React from "react";

const Navigation =() => {
    return     <div className="container text-center my-3">
    <StartSys />
    <ActiveTag />
    <CarHistory />
</div>;
}
export default Navigation;