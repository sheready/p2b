import {Routes, Route} from "react-router-dom";
import '../App.css';
import Header from "./Header";
import Footer from "./Footer";
import Home from "./Home";
import Plans from "./Plans";
import Courses from "./Courses";
import ContactUs from "./ContactUs";

function App() {
  return (
    <div className="App">
      <Header/>
      <Routes>
        <Route path="/" element={<Home title="Welcome to Passport To Business" />} />
        <Route path="plans" element={<Plans/>} />
        <Route path="courses" element={<Courses/>} />
        <Route path="contact-us" element={<ContactUs/>} />
        <Route
          path="*"
          element={<h1 className="not-found">Page Not Found</h1>}
        />
      </Routes>
      <Footer/>
    </div>
  );
}


export default App;
