
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Navbar from './components/Navbar';
import ProductCard from './components/ProductCard';

function App() {
  const [products, setProducts] = useState<any[]>([]);
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/products').then(r => setProducts(r.data));
  }, []);
  return (
    <div className="font-sans">
      <Navbar />
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 p-4">
        {products.map(p => <ProductCard key={p.id} product={p} />)}
      </div>
    </div>
  );
}
export default App;
