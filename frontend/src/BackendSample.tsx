import React, { useEffect, useState } from 'react';
import axios from 'axios';

export interface User {
    id: number;
    email: string;
}

const BackendSample: React.FunctionComponent = () => {
    const [users, setUsers] = useState<User[]>([]);

    useEffect(() => {
        const fetchUsers = async () => {
            try {
                console.log("Hehe")
                const response = await axios.get('http://localhost:8000/api/users');
                const data = await response.data;
                console.log(data)
                setUsers(data);
            } catch (error) {
                console.error('Error fetching users:', error);
            }
        };

        fetchUsers();
    }, []);

    return (
        <div>
            <h2>User List</h2>
            {
                users.length === 0 ? (<p>No users</p>)
                    :
                    (<ul>
                        {users.map((user) => (
                            <li key={user.id} >
                                <strong>ID:</strong> {user.id}, <strong>Email:</strong> {user.email}
                            </li>
                        ))}
                    </ul>)
            }
        </div >
    )
};

export default BackendSample;
