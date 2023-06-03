import React, {useEffect, useState} from "react";


function ShoesList(props){

  const handleDeleteShoe = async (event, shoeId) => {
    event.preventDefault();
    console.log(shoeId)
    const url = `http://localhost:8080/api/shoes/${shoeId}`;
    const fetchConfig = {
      method: "DELETE"
    }
    const response = await fetch(url, fetchConfig);
    if (response.ok){
      const reply = await response.json();
      console.log(reply);
      loadShoesandHats();

    }

}


return (
    <table className="table table-striped">
                <thead>
                <tr>
                    <th>Shoe</th>
                    <th>Manufacturer</th>
                    <th>Color</th>
                    <th>Picture</th>
                    <th>Location</th>
                    <th>Delete?</th>
                </tr>
                </thead>
                <tbody>
                {props.shoes.map(shoe => {
                  console.log(shoe)
                return (
                  <tr key={shoe.name}>
                    <td>{shoe.name}</td>
                    <td>{shoe.manufacturer}</td>
                    <td>{shoe.color}</td>
                    <td><img
                    src={shoe.picture_url}
                    width="100"
                    height="100"
                  />
                  </td>
                  <td>{shoe.bin.name}</td>
                    <td><button
                    className="delete button"
                    onClick={(event) => {
                      const confirmBox = window.confirm(
                        "Do you really want to delete this shoe?"
                      )
                      if (confirmBox === true) {
                        handleDeleteShoe(event, shoe.id)
                      }
                    }}>
                  Delete?</button></td>
                  </tr>
                );
              })}
                </tbody>
            </table>
        );
        }

    export default ShoesList
