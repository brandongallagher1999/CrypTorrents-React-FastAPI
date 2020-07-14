import React from 'react';
import './App.css';
import {BrowserRouter, Route, Switch} from 'react-router-dom';
import Navbar from './Components/Navbar';
import SearchBar from './Components/SearchBar';
import TorrentTable from './Components/Torrent_Table';

function App() {
  return (
    <div>
      <Navbar></Navbar>

      <SearchBar></SearchBar>

      <BrowserRouter>
      <div>
        <Switch>
          <Route path="/torrents/:torrent" component={TorrentTable}/>
        </Switch>
      </div>
    </BrowserRouter>
    </div>

    

    
    
    
  );
}

export default App;