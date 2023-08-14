import axios from 'axios'
export const getAllClients = () =>{
    return axios.get('http://127.0.0.1:8000/clients/api/v1/clients/')
}