import React, { useState, useEffect } from 'react';
import Chatbot from '@site/src/components/Chatbot';
import AuthModal from '@site/src/components/AuthModal';

// Context to share auth state across components
export const AuthContext = React.createContext();

export default function Root({ children }) {
    const [isAuthModalOpen, setIsAuthModalOpen] = useState(false);
    const [isLoggedIn, setIsLoggedIn] = useState(false);

    // Check if user is logged in on component mount
    useEffect(() => {
        const token = localStorage.getItem('access_token');
        setIsLoggedIn(!!token);
    }, []);

    const handleAuthSuccess = () => {
        setIsLoggedIn(true);
        setIsAuthModalOpen(false);
    };

    const handleLogout = () => {
        localStorage.removeItem('access_token');
        setIsLoggedIn(false);
    };

    // Check if we're on the sign-in page to show the modal
    useEffect(() => {
        if (window.location.pathname === '/docs/intro' && !isLoggedIn) {
            setIsAuthModalOpen(true);
        }
    }, [isLoggedIn]);

    return (
        <AuthContext.Provider value={{ isLoggedIn, setIsLoggedIn, handleLogout }}>
            {children}
            <Chatbot />
            <AuthModal 
                isOpen={isAuthModalOpen} 
                onClose={() => setIsAuthModalOpen(false)} 
                onAuthSuccess={handleAuthSuccess}
            />
        </AuthContext.Provider>
    );
}
