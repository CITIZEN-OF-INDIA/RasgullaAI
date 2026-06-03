function Navbar() {
return (
<nav
className="navbar"
style={{
display: "flex",
justifyContent: "space-between",
alignItems: "center",

    padding: "18px 30px",

    borderBottom:
      "1px solid rgba(255,255,255,0.08)",

    backdropFilter: "blur(20px)",
  }}
>
  <div className="navbar-brand">
    <h1
      className="brand-title"
      style={{
        display: "flex",
        alignItems: "center",
        gap: "10px",
        fontSize: "1.5rem",
        fontWeight: 700,
      }}
    >
      <img
        className="rasgulla-brand-avatar"
        src="/Rasgulla_Ai.png"
        alt="RasgullaAI"
      />
      RasgullaAI
    </h1>

    <p
      style={{
        color: "#b4b4c7",
        marginTop: "4px",
        fontSize: ".9rem",
      }}
    >
      Personal AI Clone of Ritvik Arora
    </p>
  </div>

  <div
    className="navbar-right"
    style={{
      display: "flex",
      gap: "12px",
    }}
  >
    <button className="nav-btn">
      Resume
    </button>

    <button className="nav-btn">
      GitHub
    </button>

    <button className="nav-btn">
      LinkedIn
    </button>

    <button
      className="new-chat-btn"
      style={{
        padding: "12px 18px",

        borderRadius: "12px",

        background:
          "linear-gradient(135deg,#7c5cff,#4f8cff)",

        color: "white",

        fontWeight: 600,
      }}
    >
      + New Chat
    </button>
  </div>
</nav>

);
}

export default Navbar;
