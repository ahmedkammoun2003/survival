import { useState } from "react";

const Chatbot = () => {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState("");
  const [error, setError] = useState(null);

  const reponse = async () => {
    try {
      const res = await fetch("http://localhost:3000/get_answer", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ question: input }),
      });
      const data = await res.json();
      return data.answer;
    } catch (error) {
      setError(error.message);
      return null;
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await reponse();
    if (response) {
      setMessages(response);
    }
  };

  return (
    <div>
      <input
        type="text"
        onChange={(e) => {
          setInput(e.target.value);
        }}
      />
      <button type="submit" onClick={handleSubmit}>
        ASK
      </button>
      {error ? (
        <div>
          <h1>Error: {error}</h1>
        </div>
      ) : (
        messages && (
          <div>
            <h6>Chat Bot Said:{messages}</h6>
          </div>
        ))}
      </div>)}
export default Chatbot