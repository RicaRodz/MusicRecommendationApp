import React from 'react';

interface HomeProps {
  message: string;
}

const Home = async (): Promise<React.ReactElement> => {
  const res = await fetch('http://localhost:8000/');
  const data = await res.json();

  return (
    <div>
      <h1>Frontend</h1>
      <p>{data.message}</p>
    </div>
  );
};

export default Home;