import { useState } from "react";

import Axios from "../../axios-url";
import "./FeedbackPage.css";
import Feedback from "../../components/Forms/Feedback/Feedback";
import { toast } from "react-toastify";

const FeedbackPage = () => {
  const [loading, setLoading] = useState(false);

  const createFeedback = async (
    person_name: string,
    email: string,
    message: string
  ) => {
    try {
      setLoading(true);
      const { data } = await Axios.post(`/feedback/create`, {
        person_name,
        email,
        message,
      });
      setLoading(false);
      toast(
        `Hello! ${data.person_name}.Your feedback is successfully submitted`
      );
    } catch (error: any) {
      setLoading(false);
      toast(
        `${error.response.data.detail[0].loc[1]}: ${error.response.data.detail[0].msg}`
      );
    }
  };
  return (
    <div className="feedback">
      <Feedback createFeedback={createFeedback} loading={loading} />
    </div>
  );
};

export default FeedbackPage;
