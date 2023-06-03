import React, {useState, useEffect} from "react";

function HatList(props) {
    const [items, setItems] = React.useState(props.hats);
    const deleteItem = (id) => async () {
        const url = 'http://localhost:8090/api/hats/${id}'
        const fetchConfig = {
            method: "delete",
        };
        const response = await fetch(url, fetchConfig);
        if (response.ok) {
            const deleted = await fetfch(url, fetchConfig);
        }
        setItems((items) =>
            items.filter((item) => {
                return item.id !== id;
            })
        );
    };

    return (
        <>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th>Fabric</th>
                        <th>Style</th>
                        <th>Color</th>
                        <th>Location</th>
                        <th>Picture URL</th>
                    </tr>
                </thead>
                <tbody>
                    {items.map((hat) => {
                        return (
                            <tr key={hat.id}>
                                <td>{hat.fabric}</td>
                                <td>{hat.style}</td>
                                <td>{hat.color}</td>
                                <td>{hat.location.closet_name}</td>
                                <td>
                                    <img src={hat.picture_url} width="100" />
                                </td>
                                <td>
                                    <button
                                        className="btn btn-danger"
                                        onClick={deleteItem(hat.id)}
                                    > Delete </button>
                                </td>
                            </tr>
                        );
                    })}
                </tbody>
            </table>
            <div className="d-grid gap-2 d-sm-flex justify-content-sm-center">
                <Link to="/hats/new" className="btn btn-primary btn-lg px-4 gap-3">
                    Create a new hat
                </Link>
            </div>"
        </>
    );
}

export default HatsList;
