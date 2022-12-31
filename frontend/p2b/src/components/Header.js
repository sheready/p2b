import React from 'react';

import { Link, NavLink } from "react-router-dom";
import logo from "../assets/P2B-Logo-490x109.png";

function Header() {
  const getClass = ({ isActive }) => (isActive ? "nav-active" : null);

  return (
    <header className="container-header">
      <Link to="/">
        <img
          className="logo"
          src={logo}
          alt="Passport To Business logo"
          title="Passport To Business | Home"
        />
      </Link>

      <nav>
        <NavLink to="/plans" className={getClass}>
          Plans
        </NavLink>
        <NavLink to="/courses" className={getClass}>
          Courses
        </NavLink>
        <NavLink to="/contact-us" className={getClass}>
          Contact Us
        </NavLink>

      </nav>
    </header>
  );
}



export default Header;