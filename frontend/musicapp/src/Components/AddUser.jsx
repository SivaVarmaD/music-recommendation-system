import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './AddUser.css'; // Import the CSS file

const AddUser = () => {
  const [user, setUser] = useState({
    id: '',
    friends: '',
    likedmusic: ''
  });
  const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setUser({
      ...user,
      [name]: value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const formattedUser = {
        ...user,
        friends: user.friends.split(',').map(Number),
        likedmusic: user.likedmusic.split(',').map(Number)
      };
      await axios.post('http://localhost:8000/users', formattedUser);
      setSuccessMessage('User added successfully');
      setUser({
        id: '',
        friends: '',
        likedmusic: ''
      });
    } catch (error) {
      console.error('There was an error adding the user!', error);
      setErrorMessage('There was an error adding the user');
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
          <input type="number" name="id" value={user.id} onChange={handleChange} required />
        </div>
        <div>
          <label>Friends (comma-separated IDs):</label>
          <input type="text" name="friends" value={user.friends} onChange={handleChange} required />
        </div>
        <div>
          <label>Liked Music (comma-separated IDs):</label>
          <input type="text" name="likedmusic" value={user.likedmusic} onChange={handleChange} required />
        </div>
        <button type="submit">Add User</button>
      </form>
      {successMessage && <p className="success-message">{successMessage}</p>}
      {errorMessage && <p className="error-message">{errorMessage}</p>}
    </div>
  );
};

export default AddUser;
