import ReactDom from 'react-dom/client'
import { RouterProvider } from 'react-router-dom'
import router from './router'

ReactDom.createRoot(document.getElementById('root')).render(
  <RouterProvider router={router}/>
)
