import {useForm} from 'react-hook-form'
import { createClient, deleteClient, updateClient, getClient } from '../api/clients.api';
import { useNavigate, useParams } from 'react-router-dom';
import { useEffect } from 'react';

export function ClientsFormPage() {

    const {
        register, 
        handleSubmit, 
        formState:{errors},
        setValue
    } = useForm()

    const navigate = useNavigate()
    const params = useParams()

    const onSubmit = handleSubmit(async data =>{

        if(params.id){
            await updateClient(params.id, data)
        }else {
            await createClient(data);
        }
        navigate('/clients')
        
    });

    useEffect(()=>{
        async function loadClients() {
            if(params.id){
                const res = await getClient(params.id)
                setValue('name', res.data.name)
                setValue('lastname', res.data.lastname)
                setValue('age', res.data.age)
                setValue('isActive', res.data.isActive)
                
            }
        }
        
        loadClients();
    },[]);

    return (
        <div>
            <form onSubmit={onSubmit}>

                <input type="text" placeholder="name" {...register("name",{required:true})}/>
                {errors.name && <span>This field is required</span>}

                <input type="text" placeholder="lastname" {...register("lastname",{required:true})}/>
                {errors.lastname && <span>This field is required</span>}

                <input type="integer" placeholder="age" {...register("age",{required:true})}/>
                {errors.age && <span>This field is required</span>}

                <input type="checkbox" defaultChecked="True" {...register("isActive")}/>
                

                <button>Save</button>

            </form>
            
            {params.id && <button onClick={async ()=>{

                const accepted =  window.confirm('Are you sure?')

                if(accepted){

                    await deleteClient(params.id)
                    navigate('/clients')
                    
                }
                
            }}>Delete</button>}
        </div>
    )

}