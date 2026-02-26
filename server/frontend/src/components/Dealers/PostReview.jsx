import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import "./Dealers.css";
import "../assets/style.css";
import Header from '../Header/Header';

const PostReview = () => {

  const [dealer, setDealer] = useState({});
  const [review, setReview] = useState("");
  const [model, setModel] = useState("");
  const [year, setYear] = useState("");
  const [date, setDate] = useState("");
  const [carmodels, setCarmodels] = useState([]);

  let curr_url = window.location.href;
  let root_url = curr_url.substring(0, curr_url.indexOf("postreview"));
  let params = useParams();
  let id = params.id;

  let dealer_url = root_url + `djangoapp/dealer/${id}`;
  let review_url = root_url + `djangoapp/add_review`;
  let carmodels_url = root_url + `djangoapp/get_cars`;

  const postreview = async () => {

    let name = sessionStorage.getItem("firstname") + " " + sessionStorage.getItem("lastname");

    if (!name || name.includes("null")) {
      name = sessionStorage.getItem("username");
    }

    if (!model || !review || !date || !year) {
      alert("⚠️ All details are mandatory");
      return;
    }

    let model_split = model.split(" ");
    let make_chosen = model_split[0];
    let model_chosen = model_split[1];

    let jsoninput = JSON.stringify({
      "name": name,
      "dealership": parseInt(id),   // ✅ FIXED HERE
      "review": review,
      "purchase": true,
      "purchase_date": date,
      "car_make": make_chosen,
      "car_model": model_chosen,
      "car_year": year,
    });

    try {
      const res = await fetch(review_url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: jsoninput,
      });

      const json = await res.json();

      if (json.status === 200) {
        window.location.href = window.location.origin + "/dealer/" + id;
      } else {
        alert("❌ Failed to submit review");
      }

    } catch (error) {
      console.error("Error posting review:", error);
      alert("❌ Error submitting review");
    }
  };

  const get_dealer = async () => {
    try {
      const res = await fetch(dealer_url);
      const retobj = await res.json();

      if (retobj.status === 200) {
        let dealerobjs = Array.from(retobj.dealer);
        if (dealerobjs.length > 0)
          setDealer(dealerobjs[0]);
      }
    } catch (error) {
      console.error("Error fetching dealer:", error);
    }
  };

  const get_cars = async () => {
    try {
      const res = await fetch(carmodels_url);
      const retobj = await res.json();

      let carmodelsarr = Array.from(retobj.CarModels);
      setCarmodels(carmodelsarr);
    } catch (error) {
      console.error("Error fetching cars:", error);
    }
  };

  useEffect(() => {
    get_dealer();
    get_cars();
  }, []);

  return (
    <div>
      <Header />

      <div className="review-page-container">

        <h2>{dealer.full_name}</h2>

        <label>Write Your Review</label>
        <textarea
          rows="6"
          placeholder="Share your experience..."
          value={review}
          onChange={(e) => setReview(e.target.value)}
        />

        <label>Purchase Date</label>
        <input
          type="date"
          value={date}
          onChange={(e) => setDate(e.target.value)}
        />

        <label>Car Make & Model</label>
        <select
          value={model}
          onChange={(e) => setModel(e.target.value)}
        >
          <option value="" disabled hidden>
            Choose Car Make and Model
          </option>

          {carmodels.map((carmodel, index) => (
            <option
              key={index}
              value={carmodel.CarMake + " " + carmodel.CarModel}
            >
              {carmodel.CarMake} {carmodel.CarModel}
            </option>
          ))}
        </select>

        <label>Car Year</label>
        <input
          type="number"
          min="2015"
          max="2023"
          value={year}
          onChange={(e) => setYear(e.target.value)}
        />

        <button className="postreview" onClick={postreview}>
          🚗 Post Review
        </button>

      </div>
    </div>
  );
};

export default PostReview;