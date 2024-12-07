import { useState } from "react";
import axios from 'axios';

function Config() {
    const [config, setConfig] = useState({
        gps: true,
        make_csv: true,
        make_kml: true,
        csv_name: '',
        kml_name: '',
      });
    
      const updateConfig = () => {
        axios.post('/update_config', config).then((response) => {
          alert(response.data.message);
        });
      };

    return(
        <>
            <h1>Configuration Page</h1>
            <label>GPS:</label>
            <input type="checkbox" checked={config.gps} onChange={(e) => setConfig({ ...config, gps: e.target.checked })}></input>

            <label>Google Earth CSV:</label>
            <input type="checkbox" checked={config.make_csv} onChange={(e) => setConfig({ ...config, make_csv: e.target.checked })}/>
            <input type="text" placeholder="CSV Output Filename" value={config.csv_name} onChange={(e) => setConfig({ ...config, csv_name: e.target.value})}/>

            <label>Route Overlay KML:</label>
            <input type="checkbox" checked={config.make_kml} onChange={(e) => setConfig({ ...config, make_kml: e.target.checked })}/>
            <input type="text" placeholder="KML Output Filename" value={config.kml_name} onChange={(e) => setConfig({ ...config, kml_name: e.target.value})}/>


            <button onClick={updateConfig}>Update Config</button>
        </>
    );
};

export default Config