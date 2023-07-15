import React from "react";
import styles from "./fqhist.module.css"
import Navbar from "../../Navbar/Navbar";
import { getCookie, backendurl } from "../../utils";
import axios, { AxiosError } from 'axios';

interface TableRow {
  gallons_requested: number;
  delivery_address: string;
  delivery_date: string;
  suggested_price: number;
  total_amount_due: number;
}
const Table: React.FC = () => {
  const [fuelquotes, setFuelquotes] = React.useState<TableRow[]>([]);
  React.useEffect(() => {
    const username = getCookie('username'); 
    axios.get(`${backendurl}/fuelquote/getfuelquote/${username}`).then((response) => {
      setFuelquotes(response.data);
      console.log(response.data);
    });
  }, []);

  return (
    <>
    <Navbar/>
    <div className={styles.tablecontainer}>
    <h1>Fuel Quote History</h1>
    <table>
      <thead>
        <tr>
          <th>Gallons Requested</th>
          <th>Address</th>
          <th>date</th>
          <th>price</th>
          <th>amount due</th>
        </tr>
      </thead>
      <tbody>
  {fuelquotes.map((row) => (
    <tr key={row.deliveryDate.toDateString()}>
      <td>{row.gallonsRequested}</td>
      <td>{row.deliveryAddress}</td>
      <td>{row.deliveryDate.toDateString()}</td>
      <td>{row.Suggestedprice}</td>
      <td>{row.AmountDue}</td>
    </tr>
  ))}
</tbody>
    </table>
    </div>
    </>
  );
};

export default Table;
