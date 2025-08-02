import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [prediction, setPrediction] = useState("");

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("http://localhost:8000/predict/", formData);
      setPrediction(res.data.prediction);
    } catch (err) {
      console.error("Upload failed", err);
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Image Prediction</h1>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Predict</button>
      {prediction && <h2>Prediction: {prediction}</h2>}
    </div>
  );
}

export default App;
