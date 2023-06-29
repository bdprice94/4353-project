import React, { useState } from "react";
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import './fqform.css';

const CalendarInput: React.FC<{ value: Date | null, onChange: (date: Date | null) => void }> = ({ value, onChange }) => {
  return (
    <DatePicker
      selected={value}
      onChange={onChange}
      dateFormat="MM/dd/yyyy"
      placeholderText="Select a date"
    />
  );
};

const FuelQuoteForm: React.FC = () => {
  const [quanity, setQuanity] = useState("");
  const [email, setEmail] = useState("");
  const [address, setAddress] = useState("");
  const [price, setPrice] = useState("");
  const [totalAmount, setTotalAmount] = useState("");
  const [deliveryDate, setDeliveryDate] = useState<Date | null>(null);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
  
    // Add your logic here to handle the form submission
  };

  return (
    <div className="form-container">
      <h1>Fuel Quote Form</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="quanity">Gallons Requested:</label>
          <input
            type="number"
            id="quanity"
            value={quanity}
            onChange={(e) => setQuanity(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="deliveryDate">Delivery Date:</label>
          <CalendarInput value={deliveryDate} onChange={setDeliveryDate} />
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
  );
};

export default FuelQuoteForm;
