import axios from "axios";

const api = axios.create({
  baseURL: "https://rasgullaai.onrender.com",
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
          "Backend returned an error.",
        { cause: error }
      );
    }

    if (error.request) {
      throw new Error(
        "Cannot connect to RasgullaAI backend.",
        { cause: error }
      );
    }

    throw new Error("Something went wrong.", {
      cause: error,
    });
  }
};

export default api;
