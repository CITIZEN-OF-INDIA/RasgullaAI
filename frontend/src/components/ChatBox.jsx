import { useState, useRef } from "react";
import MessageBubble from "./MessageBubble";
import { askRasgullaAI } from "../services/api";
import TypingAnimation from "./TypingAnimation";

function ChatBox() {
  const [input, setInput] = useState("");

  const [messages, setMessages] = useState([]);

  const [loading, setLoading] = useState(false);

  const [showScrollBtn, setShowScrollBtn] =
    useState(false);

  const messagesRef = useRef(null);

  const suggestedPrompts = [
    "Tell me about Ritvik's projects",
    "What technologies does Ritvik know?",
    "Summarize Ritvik's resume"
  ];

  const handleScroll = () => {
    const element = messagesRef.current;

    if (!element) return;

    const distance =
      element.scrollHeight -
      element.scrollTop -
      element.clientHeight;

    setShowScrollBtn(distance > 250);
  };

  const scrollToBottom = () => {
    if (!messagesRef.current) return;

    messagesRef.current.scrollTo({
      top: messagesRef.current.scrollHeight,
      behavior: "smooth",
    });
  };

  const handleSend = async (customMessage) => {
  const text = customMessage || input;

  if (!text.trim()) return;

  const userMessage = {
    role: "user",
    content: text,
  };

  setMessages((prev) => [
    ...prev,
    userMessage,
  ]);

  setInput("");

  setLoading(true);

  try {
    const answer =
      await askRasgullaAI(text);

    setMessages((prev) => [
      ...prev,
      {
        role: "assistant",
        content: answer,
      },
    ]);
  } catch (error) {
    setMessages((prev) => [
      ...prev,
      {
        role: "assistant",
        content:
          error.message ||
          "Failed to connect to backend.",
      },
    ]);
  } finally {
    setLoading(false);

    setTimeout(() => {
      scrollToBottom();
    }, 100);
  }
};

  return (
    <div
      className="chat-container"
      style={{
        width: "100%",
        maxWidth: "1200px",
        height: "100%",
        margin: "0 auto",
        display: "flex",
        flexDirection: "column",
      }}
    >
      {/* MESSAGES */}

      <div
        ref={messagesRef}
        onScroll={handleScroll}
        style={{
          flex: 1,
          overflowY: messages.length === 0 ? "hidden" : "auto",
          padding: "40px 24px",
        }}
      >
        {messages.length === 0 ? (
          <div
            style={{
              maxWidth: "900px",
              margin: "80px auto",
              textAlign: "center",
            }}
          >
            <img
              className="rasgulla-welcome-avatar"
              src="/Rasgulla_Ai.png"
              alt="RasgullaAI"
            />

            <h1
              className="welcome-title"
              style={{
                fontSize: "3rem",
                fontWeight: 800,
                marginBottom: "14px",
              }}
            >
              Welcome to RasgullaAI
            </h1>

            <p
              className="welcome-subtitle"
              style={{
                color: "#b4b4c7",
                lineHeight: "1.8",
                marginBottom: "40px",
                maxWidth: "700px",
                marginInline: "auto",
              }}
            >
              Ask anything about skills,
              projects, experience,
              certifications and career
              journey.
            </p>

            <div
              className="prompt-grid"
              style={{
                display: "grid",
                gridTemplateColumns:
                  "repeat(auto-fit,minmax(250px,1fr))",
                gap: "16px",
              }}
            >
              {suggestedPrompts.map(
                (prompt, index) => (
                  <button
                    key={index}
                    onClick={() =>
                      handleSend(prompt)
                    }
                    className="glass-card"
                    style={{
                      padding: "18px",
                      color: "white",
                      textAlign: "left",
                      background:
                        "rgba(255,255,255,0.03)",
                    }}
                  >
                    {prompt}
                  </button>
                )
              )}
            </div>
          </div>
        ) : (
          <>
            {messages.map(
              (message, index) => (
                <MessageBubble
                  key={index}
                  message={message}
                />
              )
            )}

            {loading && (
              <TypingAnimation />
            )}
          </>
        )}
      </div>

      {/* SCROLL BUTTON */}

      {showScrollBtn && (
        <button
          onClick={scrollToBottom}
          style={{
            position: "fixed",
            bottom: "120px",
            right: "30px",

            width: "50px",
            height: "50px",

            borderRadius: "50%",

            background:
              "rgba(255,255,255,.08)",

            color: "white",

            border:
              "1px solid rgba(255,255,255,.1)",

            backdropFilter: "blur(20px)",

            zIndex: 999,
          }}
        >
          ↓
        </button>
      )}

      {/* INPUT */}

      <div
        style={{
          padding: "18px",
        }}
      >
        <div
          className="glass-card input-wrapper"
          style={{
            display: "flex",
            alignItems: "center",
            gap: "12px",
            padding: "12px",
          }}
        >
          <input
            className="chat-input"
            value={input}
            onChange={(e) =>
              setInput(e.target.value)
            }
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                handleSend();
              }
            }}
            placeholder="Ask RasgullaAI anything..."
            style={{
              flex: 1,
              background: "transparent",
              border: "none",
              outline: "none",
              color: "white",
              padding: "12px",
              fontSize: "1rem",
            }}
          />

          <button
            style={{
              width: "46px",
              height: "46px",

              borderRadius: "12px",

              background:
                "rgba(255,255,255,.06)",

              color: "white",
            }}
          >
            🎤
          </button>

          <button
            onClick={() =>
              handleSend()
            }
            style={{
              width: "50px",
              height: "50px",

              borderRadius: "14px",

              background:
                "linear-gradient(135deg,#7c5cff,#4f8cff)",

              color: "white",

              fontWeight: "700",

              fontSize: "1.2rem",
            }}
          >
            →
          </button>
        </div>
      </div>
    </div>
  );
}

export default ChatBox;
