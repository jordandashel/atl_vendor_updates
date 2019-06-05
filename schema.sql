DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
  key integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  id integer NOT NULL,
  first_name text NOT NULL,
  last_name text NOT NULL,
  street_address text NOT NULL,
  state text NOT NULL,
  zip_code text NOT NULL,
  purchase_status text NOT NULL,
  product_id integer NOT NULL,
  product_name text NOT NULL,
  item_price text NOT NULL,
  date_time text NOT NULL
);
