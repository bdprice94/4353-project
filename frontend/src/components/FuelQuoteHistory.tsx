import React from "react";
import styles from "./FuelQuoteHistory.module.css";
import Navbar from "./Navbar";
import { getCookie, backendurl } from "../authentication";
import axios from "axios";

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
    const username = getCookie("username");
    axios
      .get(`${backendurl}/fuelquote/getfuelquote/${username}`, {
        withCredentials: true
      })
      .then((response) => {
        setFuelquotes(response.data);
        console.log(response.data);
      });
  }, []);

  return (
    <>
      <Navbar />
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
              <tr key={row.delivery_date.toString()}>
                <td>{row.gallons_requested}</td>
                <td>{row.delivery_address}</td>
                <td>{row.delivery_date.toString()}</td>
                <td>{row.suggested_price}</td>
                <td>{row.total_amount_due}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
};

export default Table;
