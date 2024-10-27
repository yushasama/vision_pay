
"use client";
import React, { useRef, useState, useEffect } from "react";

export default function Home() {
  const videoRef = useRef<HTMLVideoElement | null>(null);
  const [cameraActive, setCameraActive] = useState(false);
  const [stream, setStream] = useState<MediaStream | null>(null);

  // Preset list of items with prices and initial quantity set to 0
  const [fruits, setFruits] = useState([
    { name: "Banana", description: "Fresh Banana", price: 0.5, quantity: 0 },
    { name: "Apple", description: "Fresh Apple", price: 0.75, quantity: 0 },
    { name: "Orange", description: "Fresh Orange", price: 0.6, quantity: 0 },
  ]);

  // State for the total amount
  const [totalAmount, setTotalAmount] = useState(0.00);

  useEffect(() => {
    // Calculate total amount when fruits state updates
    const total = fruits.reduce((sum, fruit) => sum + fruit.price * fruit.quantity, 0);
    setTotalAmount(total);
  }, [fruits]);

  useEffect(() => {
    const startCamera = async () => {
      if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        try {
          const videoStream = await navigator.mediaDevices.getUserMedia({
            video: true,
          });
          if (videoRef.current) {
            videoRef.current.srcObject = videoStream;
            setStream(videoStream);
          }
        } catch (error) {
          console.error("Error accessing camera:", error);
          alert("Could not access the camera. Please check your browser permissions.");
        }
      }
    };

    if (cameraActive) startCamera();
  }, [cameraActive]);

  const handleStartCamera = () => setCameraActive(true);

  const handleStopCamera = () => {
    if (stream) {
      stream.getTracks().forEach((track) => track.stop());
      setStream(null);
      setCameraActive(false);
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen">
      <div className="w-full md:w-11/12 max-w-5xl flex flex-col md:flex-row gap-8 px-4">
        {/* Left Container - Checkout Section */}
        <div className="w-full md:w-1/2 bg-white rounded-lg shadow-lg p-6 border border-gray-300 text-black">
          <h2 className="text-3xl font-bold mb-4">Checkout</h2>
          <ul className="space-y-4 mb-8">
            {fruits
              .filter((fruit) => fruit.quantity > 0) // Only display items with quantity > 0
              .map((fruit, index) => (
                <li key={index} className="text-lg text-black">
                  <span className="font-semibold">{fruit.name}</span>
                  <p className="text-sm text-black">{fruit.description}</p>
                  <p className="text-sm text-black">Price: ${fruit.price.toFixed(2)} x {fruit.quantity}</p>
                </li>
              ))}
          </ul>
          <div className="text-xl font-bold mt-8 text-black">Total: ${totalAmount.toFixed(2)}</div>
          <button className="w-full bg-black text-white py-3 mt-4 text-xl font-bold rounded-lg">
            Pay
          </button>
        </div>

        {/* Right Container - Cart Preview and Camera */}
        <div className="w-full md:w-1/2 bg-white rounded-lg shadow-lg p-6 border border-gray-300 flex flex-col items-center text-black">
          <h2 className="text-2xl font-bold mb-4 text-black">Checkout Your Items!</h2>
          
          <div className="w-full h-64 bg-gray-200 flex items-center justify-center rounded-lg mb-6 overflow-hidden">
            {cameraActive ? (
              <video
                ref={videoRef}
                autoPlay
                playsInline
                className="w-full h-full object-cover rounded-lg"
              ></video>
            ) : (
              <span className="text-gray-500 text-lg">[ Image Preview ]</span>
            )}
          </div>
          
          <div className="flex space-x-4">
            <button
              onClick={handleStartCamera}
              className="flex items-center justify-center bg-black text-white p-3 rounded-full"
            >
              {/* Camera Icon */}
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
                <path strokeLinecap="round" strokeLinejoin="round" d="M6.827 6.175A2.31 2.31 0 0 1 5.186 7.23c-.38.054-.757.112-1.134.175C2.999 7.58 2.25 8.507 2.25 9.574V18a2.25 2.25 0 0 0 2.25 2.25h15A2.25 2.25 0 0 0 21.75 18V9.574c0-1.067-.75-1.994-1.802-2.169a47.865 47.865 0 0 0-1.134-.175 2.31 2.31 0 0 1-1.64-1.055l-.822-1.316a2.192 2.192 0 0 0-1.736-1.039 48.774 48.774 0 0 0-5.232 0 2.192 2.192 0 0 0-1.736 1.039l-.821 1.316Z" />
                <path strokeLinecap="round" strokeLinejoin="round" d="M16.5 12.75a4.5 4.5 0 1 1-9 0 4.5 4.5 0 0 1 9 0ZM18.75 10.5h.008v.008h-.008V10.5Z" />
              </svg>
            </button>
            {!cameraActive ? (
              <button onClick={handleStartCamera} className="bg-blue-500 text-white px-4 py-2 rounded-lg">
                Start Camera
              </button>
            ) : (
              <button onClick={handleStopCamera} className="bg-red-500 text-white px-4 py-2 rounded-lg">
                Stop Camera
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}


// "use client";
// import React, { useRef, useState, useEffect } from 'react';

// export default function Home() {
//   const videoRef = useRef<HTMLVideoElement | null>(null);
//   const [cameraActive, setCameraActive] = useState(false);
//   const [stream, setStream] = useState<MediaStream | null>(null);

//   useEffect(() => {
//     const startCamera = async () => {
//       if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
//         try {
//           const videoStream = await navigator.mediaDevices.getUserMedia({ video: true });
//           if (videoRef.current) {
//             videoRef.current.srcObject = videoStream;
//             setStream(videoStream);
//           }
//         } catch (error) {
//           console.error("Error accessing camera:", error);
//           alert("Could not access the camera. Please check your browser permissions.");
//         }
//       }
//     };

//     if (cameraActive) startCamera();
//   }, [cameraActive]);

//   const handleStartCamera = () => setCameraActive(true);

//   const handleStopCamera = () => {
//     if (stream) {
//       stream.getTracks().forEach((track) => track.stop());
//       setStream(null);
//       setCameraActive(false);
//     }
//   };

//   return (
//     <div className="flex justify-center items-center min-h-screen">
//       <div className="w-full md:w-11/12 max-w-5xl flex flex-col md:flex-row gap-8 px-4">
//         {/* Left Container - Checkout Section */}
//         <div className="w-full md:w-1/2 bg-white rounded-lg shadow-lg p-6 border border-gray-300 text-black">
//           <h2 className="text-3xl font-bold mb-4">Checkout</h2>
//           <ul className="space-y-4 mb-8">
//             {[...Array(4)].map((_, index) => (
//               <li key={index} className="text-lg text-black">
//                 <span className="font-semibold">Fruit Name</span>
//                 <p className="text-sm text-black">Fruit description.</p>
//               </li>
//             ))}
//           </ul>
//           <div className="text-xl font-bold mt-8 text-black">Total:</div>
//           <button className="w-full bg-black text-white py-3 mt-4 text-xl font-bold rounded-lg">
//             Pay
//           </button>
//         </div>

//         {/* Right Container - Cart Preview and Camera */}
//         <div className="w-full md:w-1/2 bg-white rounded-lg shadow-lg p-6 border border-gray-300 flex flex-col items-center text-black">
//           <h2 className="text-2xl font-bold mb-4 text-black">Checkout Your Items!</h2>
          
//           <div className="w-full h-64 bg-gray-200 flex items-center justify-center rounded-lg mb-6 overflow-hidden">
//             {cameraActive ? (
//               <video
//                 ref={videoRef}
//                 autoPlay
//                 playsInline
//                 className="w-full h-full object-cover rounded-lg"
//               ></video>
//             ) : (
//               <span className="text-gray-500 text-lg">[ Image Preview ]</span>
//             )}
//           </div>
          
//           <div className="flex space-x-4">
//             <button
//               onClick={handleStartCamera}
//               className="flex items-center justify-center bg-black text-white p-3 rounded-full"
//             >
//               {/* Camera Icon from Heroicons */}
//               <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
//                 <path strokeLinecap="round" strokeLinejoin="round" d="M6.827 6.175A2.31 2.31 0 0 1 5.186 7.23c-.38.054-.757.112-1.134.175C2.999 7.58 2.25 8.507 2.25 9.574V18a2.25 2.25 0 0 0 2.25 2.25h15A2.25 2.25 0 0 0 21.75 18V9.574c0-1.067-.75-1.994-1.802-2.169a47.865 47.865 0 0 0-1.134-.175 2.31 2.31 0 0 1-1.64-1.055l-.822-1.316a2.192 2.192 0 0 0-1.736-1.039 48.774 48.774 0 0 0-5.232 0 2.192 2.192 0 0 0-1.736 1.039l-.821 1.316Z" />
//                 <path strokeLinecap="round" strokeLinejoin="round" d="M16.5 12.75a4.5 4.5 0 1 1-9 0 4.5 4.5 0 0 1 9 0ZM18.75 10.5h.008v.008h-.008V10.5Z" />
//               </svg>
//             </button>
//             {!cameraActive ? (
//               <button onClick={handleStartCamera} className="bg-blue-500 text-white px-4 py-2 rounded-lg">
//                 Start Camera
//               </button>
//             ) : (
//               <button onClick={handleStopCamera} className="bg-red-500 text-white px-4 py-2 rounded-lg">
//                 Stop Camera
//               </button>
//             )}
//           </div>
//         </div>
//       </div>
//     </div>
//   );
// }
