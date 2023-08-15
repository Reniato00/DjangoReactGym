import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom'
import { ClientsPage } from './pages/ClientsPage'
import { ClientsFormPage } from './pages/ClientsFormPage'
import { Navigation } from './components/Navigation'
function App() {
  return (
    <BrowserRouter>
      <Navigation/>
      <Routes>
        <Route path='/' element={<Navigate to="/clients"/>}/>
        <Route path='/clients' element={<ClientsPage/>}/>
        <Route path='/clients-create' element={<ClientsFormPage/>}/>
        <Route path='/clients/:id' element={<ClientsFormPage/>}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App