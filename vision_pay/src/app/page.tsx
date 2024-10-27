import { useState, useRef } from 'react';

export default function Home() {
  return (
    <div className="flex justify-center items-center min-h-screen">
      {/* Container */}
      <div className="w-3/4 max-w-screen-lg flex space-x-6">
        
        {/* Left Container - Checkout Section */}
        <div className="w-1/2 bg-white rounded-lg shadow-lg p-6 border border-gray-300">
          <h2 className="text-3xl font-bold mb-4">Checkout</h2>
          <ul className="space-y-4 mb-8">
            {[...Array(4)].map((_, index) => (
              <li key={index} className="text-lg">
                <span className="font-semibold">Fruit Name</span>
                <p className="text-gray-600 text-sm">Fruit description.</p>
              </li>
            ))}
          </ul>
          <div className="text-xl font-bold mt-8">Total:</div>
          <button className="w-full bg-black text-white py-3 mt-4 text-xl font-bold rounded-lg">
            Pay
          </button>
        </div>

        {/* Right Container - Cart Preview and Camera */}
        <div className="w-1/2 bg-white rounded-lg shadow-lg p-6 border border-gray-300 flex flex-col items-center">
          <h2 className="text-2xl font-bold mb-4">Checkout Your Items!</h2>
          <div className="w-full h-64 bg-gray-200 flex items-center justify-center rounded-lg mb-6">
            {/* Placeholder for image */}
            <span className="text-gray-500 text-lg">[ Image Preview ]</span>
          </div>
          <div className="flex space-x-4">
            <button className="flex items-center justify-center bg-black text-white p-3 rounded-full">
              {/* Camera Icon */}
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-6">
                <path strokeLinecap="round" strokeLinejoin="round" d="M6.827 6.175A2.31 2.31 0 0 1 5.186 7.23c-.38.054-.757.112-1.134.175C2.999 7.58 2.25 8.507 2.25 9.574V18a2.25 2.25 0 0 0 2.25 2.25h15A2.25 2.25 0 0 0 21.75 18V9.574c0-1.067-.75-1.994-1.802-2.169a47.865 47.865 0 0 0-1.134-.175 2.31 2.31 0 0 1-1.64-1.055l-.822-1.316a2.192 2.192 0 0 0-1.736-1.039 48.774 48.774 0 0 0-5.232 0 2.192 2.192 0 0 0-1.736 1.039l-.821 1.316Z" />
                <path strokeLinecap="round" strokeLinejoin="round" d="M16.5 12.75a4.5 4.5 0 1 1-9 0 4.5 4.5 0 0 1 9 0ZM18.75 10.5h.008v.008h-.008V10.5Z" />
              </svg>
            </button>
            <button className="bg-blue-500 text-white px-4 py-2 rounded-lg">
              Start Camera
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
