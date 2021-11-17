import React from 'react';
import './App.css';
import {BrowserRouter, Route, Routes} from 'react-router-dom';
import Navbar from './Components/Navbar';
import SearchBar from './Components/SearchBar';
import TorrentTable from './Components/Torrent_Table';

function App() {
  return (
    <div>
      <Navbar></Navbar>

      <SearchBar></SearchBar>

      <BrowserRouter>
        <Routes>
          <Route path="/torrents/:torrent" element={<TorrentTable/>}/>
        </Routes>
    </BrowserRouter>
    </div>

    

    
    
    
  );
}

export default App;