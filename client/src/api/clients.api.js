import axios from 'axios'

const clientsApi = axios.create({
    baseURL: 'http://127.0.0.1:8000/clients/api/v1/clients/'
})

export const getAllClients = () =>{
    return clientsApi.get('/');
}

export const createClient = (client) => {
    return clientsApi.post('/', client);
}

export const deleteClient = (id) =>  clientsApi.delete('/'+id)

export const updateClient = (id, client) => clientsApi.put('/'+id+'/', client)

export const getClient = (id) => clientsApi.get('/'+id+'/')