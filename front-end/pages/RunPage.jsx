import { useState, useEffect } from 'react';
import axios from 'axios';
import { io } from 'socket.io-client';

const RunPage = () => {
    const [data, setData] = useState([]);

    const socket = io("http://localhost:5000", {
        transports: ["websocket", "polling"], // Ensure compatibility with multiple transports
      });
      
    useEffect(() => {
        socket.on('data', (newData) => {
            setData((prev) => [...prev, newData]);
        });
        return () => socket.disconnect();
    }, []);

    const handleStart = async () => {
        await axios.post('http://localhost:5000/run/start');
        alert('Main started!');
    };

    const handleStop = async () => {
        await axios.post('http://localhost:5000/run/stop');
        alert('Main stopped!');
    };

    return (
        <div>
            <h1>Run Page</h1>
            <button onClick={handleStart}>Start</button>
            <button onClick={handleStop}>Stop</button>
            <h2>Data:</h2>
            <ul>
                {data.map((item, index) => (
                    <li key={index}>ID: {item.id}, RSSI: {item.rssi}</li>
                ))}
            </ul>
        </div>
    );
};

export default RunPage;
