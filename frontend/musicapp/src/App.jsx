// App.js

import React from 'react';
import MusicList from './Components/MusicList';
import AddMusic from './Components/AddMusic';
import DisplayUsers from './Components/DisplayUser';
import AddUser from './Components/AddUser';
import MusicSuggester from './Components/MusicSuggester';
import './App.css'; // Import the CSS file

function App() {
  return (
    <div className='app-container'>
      <h1>ListenX</h1>
      <div className="components-container">
        <div className="component">
          <AddMusic />
          <MusicList />
        </div>
        <div className="component">
          <AddUser />
          <DisplayUsers />
        </div>
        <div className="component">
          <MusicSuggester />
        </div>
      </div>
    </div>
  );
}

export default App;
