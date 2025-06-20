import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './AddMusic.css'; // Import the CSS file

const AddMusic = () => {
  const [music, setMusic] = useState({
    id: '',
    name: '',
    date: '',
    author: '',
    language: '',
    genre: ''
  });
  const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setMusic({
      ...music,
      [name]: value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://localhost:8000/music', music);
      setSuccessMessage('Music added successfully');
      setMusic({
        id: '',
        name: '',
        date: '',
        author: '',
        language: '',
        genre: ''
      });
    } catch (error) {
      console.error('There was an error adding the music!', error);
      setErrorMessage('There was an error adding the music');
    }
  };

  useEffect(() => {
    if (successMessage) {
      const timer = setTimeout(() => setSuccessMessage(''), 3000);
      return () => clearTimeout(timer);
    }
  }, [successMessage]);

  return (
    <div className="form-container">
      <form onSubmit={handleSubmit}>
        <div>
          <label>ID:</label>
          <input type="number" name="id" value={music.id} onChange={handleChange} required />
        </div>
        <div>
          <label>Name:</label>
          <input type="text" name="name" value={music.name} onChange={handleChange} required />
        </div>
        <div>
          <label>Date:</label>
          <input type="date" name="date" value={music.date} onChange={handleChange} required />
        </div>
        <div>
          <label>Author:</label>
          <input type="text" name="author" value={music.author} onChange={handleChange} required />
        </div>
        <div>
          <label>Language:</label>
          <input type="text" name="language" value={music.language} onChange={handleChange} required />
        </div>
        <div>
          <label>Genre:</label>
          <input type="text" name="genre" value={music.genre} onChange={handleChange} required />
        </div>
        <button type="submit">Add Music</button>
      </form>
      {successMessage && <p className="success-message">{successMessage}</p>}
      {errorMessage && <p className="error-message">{errorMessage}</p>}
    </div>
  );
};

export default AddMusic;
