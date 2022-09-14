import './App.css';
import Navigation from './UI/navigaton';
import { BrowserRouter, Routes, Route} from "react-router-dom";
import ActiveTagsList from './UI/Component/ActiveTag/activeTagsList';
import CarHistoryList from './UI/Component/CarHistory/carHistoryList';
import SysContext  from './UI/context/context';
import Main from './UI/main';
import io from 'socket.io-client';
import React from "react";


let endPoint = 'http://localhost:5000';
export let socket = io.connect(`${endPoint}`);


function App() {  
  return (
    <SysContext>
    <>
    <BrowserRouter>
    <div className='container'>

    <Navigation />
    <div className='text-center'>
    <Routes>
        <Route path="/" element={<Main />} />
        <Route path="active-tag" element={<ActiveTagsList />} />
        <Route path="cars-history" element={<CarHistoryList />} />
        </Routes>
    
    </div>
    </div>
    </BrowserRouter>
    </>
    </SysContext>
  );  
}

export default App;
