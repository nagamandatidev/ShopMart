
import React from 'react';
export default function ProductCard({product}: any){
  return (
    <div className="border p-2 rounded shadow hover:shadow-lg">
      <img src={product.image} alt={product.name} className="h-32 w-full object-cover"/>
      <h2 className="font-semibold">{product.name}</h2>
      <p>${product.price}</p>
      <button className="bg-blue-600 text-white px-2 py-1 mt-2 rounded">Add to Cart</button>
    </div>
  );
}
