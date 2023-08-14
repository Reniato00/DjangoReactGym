import { Link } from "react-router-dom"

export function Navigation() {
    return (
        <div>
            <h1>Gym App</h1>
            <ul>
                <li><Link to="/clients">Clients</Link></li>
                <li><Link to="/clients-create">Create Client</Link></li>
            </ul>
            
            
        </div> 
    )
}      

