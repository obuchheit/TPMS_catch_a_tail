import { useState, useEffect } from 'react';
import io from 'socket.io-client';

const socket = io('http://127.0.0.1:5000');


function RunPage(){
    const [message, setMessage] = useState('');

    useEffect(() => {
        socket.on('message', (data) => {
          setMessage(data.data)
        });
    
        return () => {
          socket.disconnect();
        };
      }, []);

    return(
        <>
            <h1>TPMS Catch A Tail</h1>
        </>
    );
};

export default RunPage