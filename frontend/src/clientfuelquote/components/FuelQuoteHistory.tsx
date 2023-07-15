import React from "react";
import styles from "./fqhist.module.css"
import Navbar from "../../Navbar/Navbar";
import { getCookie, backendurl } from "../../utils";
import axios, { AxiosError } from 'axios';

interface TableRow {
  gallonsRequested: number;
  deliveryAddress: string;
  deliveryDate: Date;
  Suggestedprice: number;
  AmountDue: number;
}
const Table: React.FC = () => {
  const [fuelquotes, setFuelquotes] = React.useState<TableRow[]>([]);
  React.useEffect(() => {
    const username = "someuser"; // change this to the actual username
    axios.get(`backendurl/fuelquote/fuelquote/${username}`).then((response) => {
      setFuelquotes(response.data);
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
