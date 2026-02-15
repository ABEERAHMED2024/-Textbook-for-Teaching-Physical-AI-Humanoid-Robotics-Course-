import React, { useContext, useEffect, useState } from 'react';
import BrowserOnly from '@docusaurus/BrowserOnly';
import { AuthContext } from '../Root';

// Client-only component for navbar auth button
const NavbarAuthButton = () => {
  const { isLoggedIn, handleLogout } = useContext(AuthContext);
  const [showButton, setShowButton] = useState(false);

  useEffect(() => {
    // Only show the button after client-side hydration
    setShowButton(true);
  }, []);

  if (!showButton) {
    // Render nothing during SSR
    return null;
  }

  return (
    <div className="navbar__item">
      {isLoggedIn ? (
        <button 
          className="button button--outline button--secondary navbar-auth-btn"
          onClick={handleLogout}
          style={{ textDecoration: 'none' }}
        >
          Sign Out
        </button>
      ) : (
        <a
          className="button button--outline button--secondary navbar-auth-btn"
          href="/docs/intro"
          style={{ textDecoration: 'none' }}
        >
          Sign In
        </a>
      )}
    </div>
  );
};

// Wrapper to ensure this only runs on the client
const ClientNavbarAuthButton = () => {
  return (
    <BrowserOnly>
      {() => <NavbarAuthButton />}
    </BrowserOnly>
  );
};

export default ClientNavbarAuthButton;