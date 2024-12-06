import { createBrowserRouter } from 'react-router-dom'
import App from './App' 
import Config from '../pages/Config'
import RunPage from '../pages/RunPage';
import Error404Page from '../pages/Error404Page';

const router = createBrowserRouter([
    {
        path: '/',
        element: <App />,
        children: [
            {
                index: true,
                element: <Config/>
            },
            {
                path: '/run',
                element: <RunPage />
            }
        ],
        errorElement: <Error404Page />
    }
]);

export default router
