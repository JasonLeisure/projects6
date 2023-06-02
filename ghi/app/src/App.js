import { BrowserRouter, Routes, Route } from "react-router-dom";
import MainPage from "./MainPage";
import Nav from "./Nav";
import ShoesForm from "./ShoesForm";
import ShoesList from "./ShoesList";

import React from "react";

function App(props) {
  if (props.shoes === undefined && props.hats === undefined) {
    return null;
  }

  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="shoes">
            <Route index element={<ShoesList shoes={props.shoes} />} />
            <Route path="new" element={<ShoesForm />} />
          </Route>
          <Route path="hats" element={<HatsList hats={props.hats} />} />
          <Route path="hats/new" element={<HatsForm />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
