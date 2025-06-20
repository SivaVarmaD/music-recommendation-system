import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './DisplayUser.css'; // Import CSS file for styling

const DisplayUsers = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const response = await axios.get('http://localhost:8000/users');
        setUsers(response.data);
      } catch (error) {
        console.error('There was an error fetching the users!', error);
      }
    };

    fetchUsers();
  }, []);

  return (
    <div className="user-list">
      <h2>Users</h2>
      <div className='list-container'>
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            <p>ID: {user.id}</p>
            <p>Friends: {user.friends.join(', ')}</p>
            <p>Liked Music: {user.likedmusic.join(', ')}</p>
          </li>
        ))}
      </ul>
      </div>
    </div>
  );
};

export default DisplayUsers;
