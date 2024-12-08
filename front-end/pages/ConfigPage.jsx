import { useState } from 'react';
import axios from 'axios';

const ConfigPage = () => {
    const [config, setConfig] = useState({ gps: true, make_csv: true, make_kml: true });

    const handleSubmit = async () => {
        await axios.post('http://localhost:5000/config', config);
        alert('Config updated!');
    };

    return (
        <div>
            <h1>Config Page</h1>
            <label>
                GPS Configured with GPSD:
                <input
                    type="checkbox"
                    checked={config.gps}
                    onChange={(e) => setConfig({ ...config, gps: e.target.checked })}
                />
            </label>

            
            <button onClick={handleSubmit}>Save Config</button>
        </div>
    );
};

export default ConfigPage;
