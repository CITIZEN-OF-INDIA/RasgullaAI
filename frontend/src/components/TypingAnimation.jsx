function TypingAnimation() {
return (
<div
className="fade-in"
style={{
display: "flex",
alignItems: "center",
gap: "12px",
marginBottom: "25px",
}}
>
<div
style={{
width: "38px",
height: "38px",
borderRadius: "12px",

      background:
        "linear-gradient(135deg,#7c5cff,#9b7dff)",

      display: "flex",
      justifyContent: "center",
      alignItems: "center",
    }}
  >
    <img
      className="rasgulla-avatar"
      src="/Rasgulla_Ai.png"
      alt="RasgullaAI"
    />
  </div>

  <div
    style={{
      display: "flex",
      gap: "6px",
      padding: "10px 15px",
      background:
        "rgba(255,255,255,0.04)",
      borderRadius: "15px",
    }}
  >
    <div className="dot"></div>
    <div className="dot"></div>
    <div className="dot"></div>
  </div>
</div>

);
}

export default TypingAnimation;
