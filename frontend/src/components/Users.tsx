import { useEffect, useState } from "react";
import { fetchUsers } from "../services/userService";
import type { User } from "../types/user";

const Users = () => {
    // Usestae is like a memory for react to store information that can change.
    // React, remember the users for me.
    const [users, setUsers] = useState<User[]>([]);


// useState = React remembers data.
// setState = update that data and trigger a re-render.
// useEffect = perform side effects such as API calls in response to rendering/dependency changes.

    // Run this effect when the component is initially loaded.
    // Run this effect after the component is mounted, and don't re-run it because of state/prop changes.
    //useEffect is used when we want React to perform a side effect related to the component.
    // React, when this component mounts, perform this operation."
    useEffect(() => {
        const loadUsers = async () => {
            // Get the users from our backend.
            const data = await fetchUsers();
            // React, update the users you are remembering.
            setUsers(data);
        };

        loadUsers();
        // [] is the dependency array .
        // Run this effect after the component's initial mount, and don't re-run it due to later renders.
        // if we put [userId] then, react understands as Run this effect when userId changes.
    }, []);

    return (
        <div>
            <h2>Users</h2>
             {/* Concerts the array data to html */}
            {/* Go through every user in the users array and create something for each user.  */}
            {users.map((user) => (
                <div key={user.id}>
                    {user.email}
                </div>
            ))}
        </div>
    );
};

export default Users;