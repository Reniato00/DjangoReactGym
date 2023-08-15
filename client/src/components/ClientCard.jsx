import { useNavigate } from "react-router-dom";

export function ClientCard({client}){

    const navigate = useNavigate();



    return (
        <div 
        onClick={()=>{
            navigate('/clients/'+client.id);
        }}
        >

            <hr />
                <h1>{client.name + ' '+ client.lastname}</h1>
                <p>{client.age}</p>
                
            </div>
            
    );
}