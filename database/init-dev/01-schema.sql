-- Customers Table
  CREATE TABLE IF NOT EXISTS customers (
      id SERIAL PRIMARY KEY,
      name VARCHAR(100) NOT NULL,
      email VARCHAR(255) NOT NULL UNIQUE,      
      company VARCHAR(100),
      created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
  );

  -- Orders Table
  CREATE TABLE IF NOT EXISTS orders (
      id SERIAL PRIMARY KEY,
      customer_id INTEGER NOT NULL,
      order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
      status VARCHAR(20) NOT NULL CHECK (status IN ('pending', 'processing', 'shipped', 'delivered', 'cancelled')),
      notes TEXT,
      CONSTRAINT fk_customer
          FOREIGN KEY (customer_id)
          REFERENCES customers(id)
          ON DELETE CASCADE
  );

  -- Order Items Table
  CREATE TABLE IF NOT EXISTS order_items (
      id SERIAL PRIMARY KEY,
      order_id INTEGER NOT NULL,
      product_name VARCHAR(200) NOT NULL,
      quantity INTEGER NOT NULL CHECK (quantity > 0),
      unit_price DECIMAL(10,2) NOT NULL CHECK (unit_price >= 0),
      CONSTRAINT fk_order
          FOREIGN KEY (order_id)
          REFERENCES orders(id)
          ON DELETE CASCADE
  );

  -- Indexes for foreign keys (standard practice)
  CREATE INDEX idx_orders_customer_id ON orders(customer_id);
  CREATE INDEX idx_order_items_order_id ON order_items(order_id);

  -- Index for email lookups
  CREATE INDEX idx_customers_email ON customers(email);