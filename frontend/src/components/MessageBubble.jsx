import useTypewriter from "../hooks/useTypewriter";

function MessageBubble({ message }) {
  const isUser = message.role === "user";

  const typedContent = useTypewriter(
    message.content,
    20
  );

  const content = isUser
    ? message.content
    : typedContent;

  return (
    <div
      className="fade-in"
      style={{
        width: "100%",
        marginBottom: "32px",
      }}
    >
      {/* Header */}

      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: "12px",
          marginBottom: "12px",
        }}
      >
        <div
          style={{
            width: "40px",
            height: "40px",
            borderRadius: "12px",

            display: "flex",
            alignItems: "center",
            justifyContent: "center",

            flexShrink: 0,

            background: isUser
              ? "linear-gradient(135deg,#2563eb,#3b82f6)"
              : "linear-gradient(135deg,#7c5cff,#9b7dff)",

            boxShadow: isUser
              ? "0 8px 20px rgba(59,130,246,.25)"
              : "0 8px 20px rgba(124,92,255,.25)",
          }}
        >
          {isUser ? (
            "👤"
          ) : (
            <img
              className="rasgulla-avatar"
              src="/Rasgulla_Ai.png"
              alt="RasgullaAI"
            />
          )}
        </div>

        <div>
          <div
            style={{
              fontWeight: 700,
              fontSize: ".95rem",
            }}
          >
            {isUser ? "You" : "RasgullaAI"}
          </div>

          <div
            style={{
              color: "#888",
              fontSize: ".8rem",
            }}
          >
            {isUser
              ? "User"
              : "AI Assistant"}
          </div>
        </div>
      </div>

      {/* Message */}

      <div
        className="message-content"
        style={{
          marginLeft: "52px",

          background:
            "rgba(255,255,255,0.03)",

          border:
            "1px solid rgba(255,255,255,0.06)",

          borderRadius: "20px",

          padding: "18px 22px",

          color: "#f5f5f5",

          fontSize: "1rem",

          lineHeight: "1.9",

          wordBreak: "break-word",

          backdropFilter: "blur(20px)",
        }}
      >
        {content}
      </div>
    </div>
  );
}

export default MessageBubble;
