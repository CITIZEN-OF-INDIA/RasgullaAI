import Navbar from "../components/Navbar";
import ChatBox from "../components/ChatBox";

function Home() {
  return (
    <div className="home-container">
      <Navbar />

      <main className="main-content">
        <ChatBox />
      </main>
    </div>
  );
}

export default Home;