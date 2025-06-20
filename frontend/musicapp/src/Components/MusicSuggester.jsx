import React, { useState, useEffect } from 'react';
import './MusicSuggester.css'; // Import the CSS file

function MusicSuggester() {
  const [users, setUsers] = useState([]);
  const [selectedUser1, setSelectedUser1] = useState('');
  const [selectedUser2, setSelectedUser2] = useState('');
  const [criteria, setCriteria] = useState('author');
  const [value, setValue] = useState('');
  const [suggestedMusic, setSuggestedMusic] = useState([]);
  const [errorMessage, setErrorMessage] = useState('');

  useEffect(() => {
    // Fetch users data from backend API
    fetch('http://localhost:8000/users')
      .then(response => response.json())
      .then(data => setUsers(data))
      .catch(error => console.error('Error fetching users:', error));
  }, []);

  const handleUser1Change = (event) => {
    setSelectedUser1(event.target.value);
  };

  const handleUser2Change = (event) => {
    setSelectedUser2(event.target.value);
  };

  const handleCriteriaChange = (event) => {
    setCriteria(event.target.value);
  };

  const handleValueChange = (event) => {
    setValue(event.target.value);
  };

  const handleSubmit = () => {
    if (!selectedUser1 || !selectedUser2 || !value) {
      setErrorMessage('Please select both users and provide a value for the criteria.');
      return;
    }
    
    // Make request to backend API to get suggested music based on selected users and criteria
    fetch(`http://localhost:8000/users/${selectedUser1}/suggest_song/${selectedUser2}?criteria=${criteria}&value=${value}`)
      .then(response => response.json())
      .then(data => {
        if (data.message) {
          setErrorMessage(data.message);
        } else {
          setSuggestedMusic(data);
          setErrorMessage('');
        }
      })
      .catch(error => console.error('Error fetching suggested music:', error));
  };

  return (
    <div className="form-container">
      <h2>Suggest Music</h2>
      <div>
        <label>User 1:</label>
        <select value={selectedUser1} onChange={handleUser1Change}>
          <option value="">Select User</option>
          {users.map(user => (
            <option key={user.id} value={user.id}>{user.id}</option>
          ))}
        </select>
      </div>
      <div>
        <label>User 2:</label>
        <select value={selectedUser2} onChange={handleUser2Change}>
          <option value="">Select User</option>
          {users.map(user => (
            <option key={user.id} value={user.id}>{user.id}</option>
          ))}
        </select>
      </div>
      <div>
        <label>Criteria:</label>
        <select value={criteria} onChange={handleCriteriaChange}>
          <option value="author">Author</option>
          <option value="language">Language</option>
          <option value="genre">Genre</option>
        </select>
      </div>
      <div>
        <label>Value:</label>
        <input type="text" value={value} onChange={handleValueChange} />
      </div>
      <button onClick={handleSubmit}>Submit</button>
      {errorMessage && <p className="error-message">{errorMessage}</p>}
      <div className="suggested-music">
        <h3>Suggested Music</h3>
        <ul>
          {suggestedMusic.map(music => (
            <li key={music.id}>{music.name} - {music.author}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default MusicSuggester;
