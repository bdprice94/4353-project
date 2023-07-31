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

export interface FuelQuoteForm {
  gallons_requested: { value: number };
  delivery_address: { value: string };
  delivery_date: { value: string };
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
  };
};

const FuelQuoteForm: React.FC = () => {
  const backendurl_profile = `${backendurl}/profile`;
  const [quantity, setQuantity] = useState("1");
  const [address, setAddress] = useState("");
  const [price, setPrice] = useState("5");
  const [totalAmount, setTotalAmount] = useState("");
  const [deliveryDate, setDeliveryDate] = useState<Date>(new Date());

  const username = getCookie("username");
  const fetchUserAddress = async () => {
    if (address !== "") {
      return;
    }
    const username = getCookie("username");
    try {
      const response = await axios.get(`${backendurl_profile}/${username}`);
      setAddress(response.data.address_1);
    } catch (error) {
      console.error(error);
    }
  };

  const getFuelForm = () => {
    return {
      gallons_requested: { value: Number(quantity) },
      delivery_address: { value: address },
      delivery_date: { value: deliveryDate.toDateString() },
      suggested_price: { value: Number(price) },
      total_amount_due: { value: Number(totalAmount) },
    };
  }

  const handleQuantityChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    if (Number(e.target.value) < 1) {
      setQuantity("1")
      return
    }

    setQuantity(e.target.value);

    const fuelquoteModel = convertFormToModel(getFuelForm());
    fuelquoteModel.gallons_requested = Number(e.target.value);

    const preliminaryCost = await axios
      .post<FuelQuote>(`${backendurl}/fuel_quote/price`, fuelquoteModel)
      .catch((e: AxiosError) => {
        let errString =
          "Make sure your profile is setup";
        if ("response" in e && e.response !== undefined) {
          if (e.response.status === 422) {
            const data = e.response.data as { detail: Array<string> };
            errString = data.detail.map((err: any) => err.msg).join("\n");
          } else if (e.response.status === 404 || e.response.status === 403 || e.response.status === 400) {
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


    if (preliminaryCost) {
      const data = preliminaryCost.data
      setPrice(String(data.suggested_price))
      setTotalAmount(String(data.total_amount_due))
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const fuelquoteModel = convertFormToModel(getFuelForm());
    axios
      .post(`${backendurl}/fuel_quote/`, fuelquoteModel)
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

  useEffect(() => {
    fetchUserAddress();
  }, []);

  return (
    <>
      <Navbar />
      <div className={styles.formcontainer}>
        <h1>Fuel Quote Form</h1>
        <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor="quantity">Gallons Requested:</label>
            <input
              type="number"
              id="quantity"
              value={quantity}
              onChange={handleQuantityChange}
            />
          </div>
          <div>
            <label htmlFor="deliveryDate">Delivery Date:</label>
            <input type="date" min="2020-01-01" max="2023-12-31" />
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
              readOnly
              disabled
            />
          </div>
          <div>
            <label htmlFor="totalAmount">Total Amount Due:</label>
            <input
              type="number"
              id="totalAmount"
              value={totalAmount}
              readOnly
              disabled
            />
          </div>
          <button type="submit">Submit</button>
        </form>
      </div>
    </>
  );
};

export default FuelQuoteForm;
