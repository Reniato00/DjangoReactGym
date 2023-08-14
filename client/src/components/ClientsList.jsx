import { useEffect, useState } from "react"
import { getAllClients } from "../api/clients.api";
import { ClientCard } from "./ClientCard";
export function ClientsList() {
const [clients, setClients] = useState([]);

useEffect(()=>{
        async function loadClients() {
            const res = await getAllClients()
            setClients(res.data)
        }
        loadClients();



},[]);
    return <div>
        {clients.map(client =>(
            <ClientCard key={client.id} client={client}/>
        ))}
    </div>;
}