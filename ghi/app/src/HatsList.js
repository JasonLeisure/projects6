import Nav from './Nav';

function HatList(props) {
    const [items, setItems] = React.useState(props.hats);
    const deleteItem = (id) => async ()
    return (
        <table className="table table-striped">
            <thead>
                <tr>
                    <th>Fabric</th>
                    <th>Style</th>
                    <th>Color</th>
                    <th>Location</th>
                    <th>Picture</th>
                </tr>
            </thead>
            <tbody>
                {}
                {props.hats.map(hat => {
                    return (
                        <tr key={location.href}
                    )
                })}
            </tbody>
        </table>
    )
}

export default HatList;
