import React, { useState, useEffect } from 'react';
import Navbar from '@theme-original/Navbar';
import Link from '@docusaurus/Link';
import { AuthContext } from '../theme/Root';

const CustomNavbar = (props) => {
  const { isLoggedIn, handleLogout } = React.useContext(AuthContext);

  return (
    <>
      <Navbar {...props} />
      <div style={{
        position: 'absolute', 
        right: '1rem', 
        top: '0.5rem',
        display: 'flex',
        alignItems: 'center',
        gap: '1rem'
      }}>
        {isLoggedIn ? (
          <button 
            className="button button--outline button--secondary navbar-auth-btn"
            onClick={handleLogout}
            style={{ 
              textDecoration: 'none',
              height: '2.5rem',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center'
            }}
          >
            Sign Out
          </button>
        ) : (
          <Link
            className="button button--outline button--secondary navbar-auth-btn"
            to="/docs/intro"
            style={{ 
              textDecoration: 'none',
              height: '2.5rem',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center'
            }}
          >
            Sign In
          </Link>
        )}
      </div>
    </>
  );
};

export default CustomNavbar;