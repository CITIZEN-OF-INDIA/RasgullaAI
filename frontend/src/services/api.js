import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
  headers: {
    "Content-Type": "application/json",
  },
  timeout: 30000,
});

export const askRasgullaAI = async (question) => {
  try {
    const response = await api.post("/chat", {
      question,
    });

    return response.data.answer;
  } catch (error) {
    console.error(error);

    if (error.response) {
      throw new Error(
        error.response.data.detail ||
          "Backend returned an error."
      );
    }

    if (error.request) {
      throw new Error(
        "Cannot connect to RasgullaAI backend."
      );
    }

    throw new Error("Something went wrong.");
  }
};

export default api;