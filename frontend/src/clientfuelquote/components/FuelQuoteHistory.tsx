import React from "react";
import styles from "./fqhist.module.css"
import Navbar from "../../Navbar/Navbar";

interface TableRow {
  gallonsRequested: number;
  deliveryAddress: string;
  deliveryDate: Date;
  Suggestedprice: number;
  AmountDue: number;
}

const Table: React.FC = () => {
  const tableData: TableRow[] = [
    { gallonsRequested: 1, deliveryAddress: "4361 cougar village dr", deliveryDate: new Date('2020-01-01'), Suggestedprice:2 ,AmountDue: 3}
    
  ];

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
        {tableData.map((row) => (
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
