import React, { useState, useEffect } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import styles from "./FuelQuoteForm.module.css";
import Navbar from "./Navbar";
import { getCookie, backendurl } from "../authentication";
import axios, { AxiosError } from "axios";

const CalendarInput: React.FC<{
  value: Date;
  onChange: (date: Date) => void;
}> = ({ value, onChange }) => {
  return (
    <DatePicker
      selected={value}
      onChange={onChange}
      dateFormat="yyyy-mm-dd"
      placeholderText="Select a date"
    />
  );
};
const username = getCookie("username");

export interface FuelQuoteForm {
  gallons_requested: { value: number };
  delivery_address: { value: string };
  delivery_date: { value: string };
  suggested_price: { value: number };
  total_amount_due: { value: number };
}

export interface FuelQuote {
  gallons_requested: { value: number };
  delivery_address: { value: string };
  delivery_date: { value: Date };
  suggested_price: { value: number };
  total_amount_due: { value: number };
}
const convertFormToModel = (form: FuelQuoteForm) => {
  return {
    username: getCookie("username") as string,
    gallons_requested: form.gallons_requested.value,
    delivery_address: form.delivery_address.value,
    delivery_date: form.delivery_date.value,
    suggested_price: form.suggested_price.value,
    total_amount_due: form.total_amount_due.value,
  };
};

const FuelQuoteForm: React.FC = () => {
  const backendurl_profile = `${backendurl}/profile`;
  const [quanity, setQuanity] = useState("");
  const [address, setAddress] = useState("");
  const [price, setPrice] = useState("5");
  const [totalAmount, setTotalAmount] = useState("");
  const [deliveryDate, setDeliveryDate] = useState<Date>(new Date());

  const fetchUserAddress = async () => {
    const username = getCookie("username");
    try {
      const response = await axios.get(
        `${backendurl_profile}/profile/${username}`
      );
      setAddress(response.data.address_1);
    } catch (error) {
      console.error(error);
    }
  };
  useEffect(() => {
    fetchUserAddress();
  }, []);
  const calculateTotalAmount = (price: string, quanity: string) => {
    return Number(price) * Number(quanity);
  };

  const handleQuanityChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setQuanity(e.target.value);
    const newTotalAmount = calculateTotalAmount(price, e.target.value);
    setTotalAmount(newTotalAmount.toString());
  };
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const target = e.target as typeof e.target & FuelQuoteForm;
    const fuelquote = {
      gallons_requested: { value: Number(quanity) },
      delivery_address: { value: address },
      delivery_date: { value: deliveryDate.toDateString() },
      suggested_price: { value: Number(price) },
      total_amount_due: { value: Number(totalAmount) },
    };
    console.log(fuelquote);
    const fuelquoteModel = convertFormToModel(fuelquote);
    axios
      .post(`${backendurl}/fuelquote/fuelquote/${username}`, fuelquoteModel)
      .then((response) => {
        alert(`${username} your fuel quote has just been created!`);
      })
      .catch((e: AxiosError) => {
        let errString =
          "Sorry, we don't know what happened. Please verify information is correct";
        if ("response" in e && e.response !== undefined) {
          if (e.response.status === 422) {
            const data = e.response.data as { detail: Array<string> };
            errString = data.detail.map((err: any) => err.msg).join("\n");
          } else if (e.response.status === 404) {
            const data = e.response.data as { detail: string };
            errString = data.detail;
          } else {
            console.log(e.response.data);
          }
        } else {
          console.log(e);
        }
        alert(errString);
      });
  };

  return (
    <>
      <Navbar />
      <div className={styles.formcontainer}>
        <h1>Fuel Quote Form</h1>
        <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor="quanity">Gallons Requested:</label>
            <input
              type="number"
              id="quanity"
              value={quanity}
              onChange={handleQuanityChange}
            />
          </div>
          <div>
            <label htmlFor="deliveryDate">Delivery Date:</label>
            <input type="date" min="2020-01-01" max="2023-12-31"></input>
          </div>
          <div>
            <label htmlFor="address">Delivery Address:</label>
            <input
              type="text"
              id="address"
              value={address}
              onChange={(e) => setAddress(e.target.value)}
              readOnly
            />
          </div>
          <div>
            <label htmlFor="price">Suggested Price:</label>
            <input
              type="number"
              id="price"
              value={price}
              onChange={(e) => setPrice(e.target.value)}
              readOnly
            />
          </div>
          <div>
            <label htmlFor="totalAmount">Total Amount Due:</label>
            <input
              type="number"
              id="totalAmount"
              value={totalAmount}
              onChange={(e) => setTotalAmount(e.target.value)}
              readOnly
            />
          </div>
          <button type="submit">Submit</button>
        </form>
      </div>
    </>
  );
};

export default FuelQuoteForm;
