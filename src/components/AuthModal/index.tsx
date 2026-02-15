import React, { useState } from 'react';
import './AuthModalStyles.css'; // We'll create this separately

const AuthModal = ({ isOpen, onClose, onAuthSuccess }) => {
  const [isLogin, setIsLogin] = useState(true);
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    softwareBackground: '',
    hardwareBackground: ''
  });
  const [loading, setLoading] = useState(false);

  if (!isOpen) return null;

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const endpoint = isLogin 
        ? (process.env.REACT_APP_API_URL || 'http://localhost:8000') + '/api/auth/login'
        : (process.env.REACT_APP_API_URL || 'http://localhost:8000') + '/api/auth/register';
      
      const response = await fetch(endpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(
          isLogin 
            ? { email: formData.email, password: formData.password }
            : {
                email: formData.email,
                password: formData.password,
                software_background: formData.softwareBackground,
                hardware_background: formData.hardwareBackground
              }
        ),
      });

      const data = await response.json();

      if (response.ok) {
        // Store token in localStorage
        localStorage.setItem('access_token', data.access_token);
        onAuthSuccess();
        onClose();
      } else {
        alert(data.detail || 'Authentication failed');
      }
    } catch (error) {
      console.error('Authentication error:', error);
      alert('An error occurred during authentication');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-modal-overlay">
      <div className="auth-modal">
        <div className="auth-modal-header">
          <h2>{isLogin ? 'Sign In' : 'Sign Up'}</h2>
          <button className="auth-modal-close" onClick={onClose}>×</button>
        </div>
        
        <form onSubmit={handleSubmit} className="auth-form">
          <div className="auth-form-group">
            <label htmlFor="email">Email:</label>
            <input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
            />
          </div>
          
          <div className="auth-form-group">
            <label htmlFor="password">Password:</label>
            <input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              required
            />
          </div>
          
          {!isLogin && (
            <>
              <div className="auth-form-group">
                <label htmlFor="softwareBackground">Software Background:</label>
                <textarea
                  id="softwareBackground"
                  name="softwareBackground"
                  value={formData.softwareBackground}
                  onChange={handleChange}
                  placeholder="Describe your software development background..."
                />
              </div>
              
              <div className="auth-form-group">
                <label htmlFor="hardwareBackground">Hardware Background:</label>
                <textarea
                  id="hardwareBackground"
                  name="hardwareBackground"
                  value={formData.hardwareBackground}
                  onChange={handleChange}
                  placeholder="Describe your hardware/embedded systems background..."
                />
              </div>
            </>
          )}
          
          <button type="submit" disabled={loading} className="auth-submit-button">
            {loading ? 'Processing...' : (isLogin ? 'Sign In' : 'Sign Up')}
          </button>
        </form>
        
        <div className="auth-switch">
          <p>
            {isLogin ? "Don't have an account?" : "Already have an account?"}{' '}
            <button 
              type="button" 
              onClick={() => setIsLogin(!isLogin)}
              className="auth-switch-button"
            >
              {isLogin ? 'Sign Up' : 'Sign In'}
            </button>
          </p>
        </div>
      </div>
    </div>
  );
};

export default AuthModal;