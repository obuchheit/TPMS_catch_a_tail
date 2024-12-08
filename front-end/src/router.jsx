import { createBrowserRouter } from "react-router-dom";
import App from './App';
import ConfigPage from "../pages/ConfigPage";
import RunPage from "../pages/RunPage";
import Error404Page from "../pages/Error404Page";

const router = createBrowserRouter([
    {
        path: '/',
        element: <App/>,
        children: [
            {
                index: true,
                element: <ConfigPage/>
            },
            {
                element: <RunPage/>,
                path: "/run"
            },
        ],
        errorElement: <Error404Page/>
    }
]);

export default router