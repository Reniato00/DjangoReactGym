export function ClientCard({client}){
    return (
        <div>
                <h1>{client.name + ' '+ client.lastname}</h1>
                <p>{client.age}</p>
            </div>
    );
}