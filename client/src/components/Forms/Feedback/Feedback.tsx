import React, { SyntheticEvent, useState } from "react";

import "./Feedback.css";

type PropsType = {
  createFeedback: (
    person_name: string,
    email: string,
    message: string
  ) => Promise<void>;

  loading: boolean;
};

const Feedback: React.FC<PropsType> = ({ createFeedback, loading }) => {
  const [person_name, setPersonName] = useState("");
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = (e: SyntheticEvent) => {
    e.preventDefault();
    createFeedback(person_name, email, message);
    setPersonName("");
    setEmail("");
    setMessage("");
  };

  return (
    <form className="form" onSubmit={handleSubmit}>
      <h1>Feedback</h1>
      <label>Person Name</label>
      <input
        type="text"
        placeholder="Write your full name"
        value={person_name}
        onChange={(e) => setPersonName(e.target.value)}
        minLength={2}
        maxLength={255}
        required
      />

      <label>Email</label>
      <input
        type="email"
        placeholder="Write your email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      />

      <label>Message</label>
      <textarea
        placeholder="Write your feedback message"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        required
      ></textarea>

      <button type="submit">{!loading ? "Submit" : "Loading"}</button>
    </form>
  );
};

export default Feedback;
