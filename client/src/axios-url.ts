import axios from "axios";

const instance = axios.create({
  baseURL: "http://0.0.0.0:8080/api/v1",
  withCredentials: true,
});

export default instance;
