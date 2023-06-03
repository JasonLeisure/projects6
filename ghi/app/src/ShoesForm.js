import React, {useEffect, useState } from 'react';


function ShoesForm(){

    const [bins, setBins] = useState([]);
    const [name, setName] = useState('');
    const [color, setColor] = useState('');
    const [manufacturer, setManufacturer] = useState('');
    const [bin, setBin] = useState([]);
    const [picture, setPicture] = useState([]);

    const handleNameChange = (event) =>{
        const value = event.target.value;
        setName(value);
    }
    const handleColorChange = (event) =>{
        const value = event.target.value;
        setColor(value);
    }
    const handleManufacturerChange = (event) =>{
        const value = event.target.value;
        setManufacturer(value);
    }
    const handlePictureChange = (event) =>{
      const value = event.target.value;
      setPicture(value);
  }


  const handleBinChange = (event) =>{
      const value = event.target.value;
      setBin(value);
  }

    const handleSubmit = async (event) => {
        event.preventDefault();

        const data ={}

        data.color = color;
        data.name = name;
        data.manufacturer = manufacturer;
        data.bin = bin;
        data.picture_url = picture;

        console.log(data);

        const locationUrl = 'http://localhost:8080/api/shoes/';
        const fetchConfig = {
            method: "post",
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json',
            },
            };
            const response = await fetch(locationUrl, fetchConfig);
            if (response.ok) {
            const newShoe = await response.json();
            console.log(newShoe)
            event.target.reset();
            setName('');
            setManufacturer('');
            setColor('');
            setBin('');
            loadShoesandHats()
            }
    }

    const fetchData = async () =>{
      const url = 'http://localhost:8100/api/bins/'
      const response = await fetch(url);

      if (response.ok){
        const data = await response.json();
        setBins(data.bins);
        console.log(data.bins);



      }
    }

useEffect(() => {
  fetchData();
  }, []);


    return (
        <div className="row">
        <div className="offset-3 col-6">
          <div className="shadow p-4 mt-4">
            <h1>Create a new shoe!</h1>
            <form onSubmit={(event) => handleSubmit(event)} id="create-shoe-form">
              <div className="form-floating mb-3">
                <input value={name} onChange={handleNameChange} placeholder="Name" required type="text" name="name" id="name" className="form-control"/>
                <label htmlFor="name">Name</label>
              </div>
              <div className="form-floating mb-3">
                <input value={manufacturer} onChange={handleManufacturerChange} placeholder="Manufacturer" required type="text" name="manufacturer" id="manufacturer" className="form-control"/>
                <label htmlFor="manufacturer">Manufacturer</label>
              </div>
              <div className="form-floating mb-3">
                <input value={color} onChange={handleColorChange} placeholder="Color" required type="text" name="color" id="color" className="form-control"/>
                <label htmlFor="color">Color</label>
              </div>
              <div className="form-floating mb-3">
                <input value={picture} onChange={handlePictureChange} placeholder="Image" required type="url" name="picture" id="picture" className="form-control"/>
                <label htmlFor="picture">Image</label>
              </div>
              <div className="mb-3">
          <select onChange={handleBinChange} required id="bin" name="bin" className="form-select">
          <option value="">Choose a bin</option>
          {bins.map(bin =>{
            return (
                <option key={bin.id} value={bin.id}>
                    {bin.closet_name}
                </option>
            )
          })}
          </select>
            </div>
              <button className="btn btn-primary">Create</button>
            </form>
          </div>
        </div>
      </div>
    );
}

export default ShoesForm;
