import React, { useEffect, useState } from 'react';
import io from 'socket.io-client';
import axios from 'axios';

const socket = io('http://localhost:5000'); // Adjust URL as needed

const RunPage = () => {
  const [data, setData] = useState(null);

  const start = () => {
    axios.post('/start').then((response) => alert(response.data.message));
  };

  const stop = () => {
    axios.post('/stop').then((response) => alert(response.data.message));
  };

  useEffect(() => {
    socket.on('data_response', (newData) => setData(newData));
    return () => socket.off('data_response');
  }, []);

  return (
    <div>
      <h1>Run Page</h1>
      <button onClick={start}>Start</button>
      <button onClick={stop}>Stop</button>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
};

export default RunPage;
