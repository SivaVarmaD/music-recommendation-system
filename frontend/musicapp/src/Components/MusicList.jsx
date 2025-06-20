import React, { useState, useEffect } from 'react';
import './MusicList.css'; // Import CSS file for styling

function MusicList() {
  const [musicList, setMusicList] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/music')
      .then(response => response.json())
      .then(data => {
        console.log(data); // Log fetched data
        setMusicList(data);
      })
      .catch(error => console.error('Error fetching music:', error));
  }, []);

  return (
    <div className="music-list">
      <h2>Music List</h2>
      <ul>
        {musicList.map(music => (
          <li key={music.id}>{music.id} - {music.name} - {music.author}</li>
        ))}
      </ul>
    </div>
  );
}

export default MusicList;
