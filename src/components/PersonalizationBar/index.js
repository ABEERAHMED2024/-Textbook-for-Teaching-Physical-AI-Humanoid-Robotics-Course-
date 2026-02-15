import React, { useState, useContext, useEffect } from 'react';
import { AuthContext } from '../theme/Root';
import ContentService from '../../services/personalizationService'; // Updated import name
import './PersonalizationBar.css';

const PersonalizationBar = ({ chapterTitle, children }) => {
  const { isLoggedIn } = useContext(AuthContext);
  const [isPersonalized, setIsPersonalized] = useState(false);
  const [isTranslated, setIsTranslated] = useState(false);
  const [userBackground, setUserBackground] = useState(null);
  const [translatedContent, setTranslatedContent] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    if (isLoggedIn) {
      loadUserBackground();
    }
  }, [isLoggedIn]);

  const loadUserBackground = async () => {
    try {
      const background = await ContentService.getUserBackground();
      setUserBackground(background);
    } catch (error) {
      console.error('Error loading user background:', error);
    }
  };

  const handlePersonalize = async () => {
    if (!isLoggedIn) {
      alert('Please sign in to personalize content');
      return;
    }

    if (!isPersonalized) {
      // Apply personalization
      try {
        setIsLoading(true);
        
        // Get personalized content from backend
        const personalizedContent = await ContentService.personalizeContent(
          typeof children === 'string' ? children : children?.props?.children || ''
        );
        
        // Update the content to show personalized version
        // Note: In a real implementation, we'd need to render the personalized content properly
        setIsPersonalized(true);
        alert(`Content personalized based on your background: ${userBackground?.background || 'Not specified'}`);
      } catch (error) {
        console.error('Error personalizing content:', error);
        alert('Failed to personalize content');
      } finally {
        setIsLoading(false);
      }
    } else {
      // Revert to original content
      setIsPersonalized(false);
    }
  };

  const handleTranslate = async () => {
    if (!isLoggedIn) {
      alert('Please sign in to translate content');
      return;
    }

    if (!isTranslated) {
      // Apply translation
      try {
        setIsLoading(true);
        
        // Get translated content from backend
        const translated = await ContentService.translateToUrdu(
          typeof children === 'string' ? children : children?.props?.children || ''
        );
        
        setTranslatedContent(translated);
        setIsTranslated(true);
      } catch (error) {
        console.error('Error translating content:', error);
        alert('Failed to translate content to Urdu');
      } finally {
        setIsLoading(false);
      }
    } else {
      // Revert to original content
      setIsTranslated(false);
      setTranslatedContent(null);
    }
  };

  return (
    <div className="personalization-bar">
      {isLoggedIn && (
        <>
          <button
            className={`personalize-btn ${isPersonalized ? 'active' : ''} ${isLoading ? 'loading' : ''}`}
            onClick={handlePersonalize}
            title={isPersonalized ? 'Disable personalization' : 'Personalize content based on your profile'}
            disabled={isLoading}
          >
            {isPersonalized ? '✅ Personalized' : '🎨 Personalize Content'}
          </button>
          <button
            className={`translate-btn ${isTranslated ? 'active' : ''} ${isLoading ? 'loading' : ''}`}
            onClick={handleTranslate}
            title={isTranslated ? 'Disable Urdu translation' : 'Translate to Urdu'}
            disabled={isLoading}
          >
            {isTranslated ? '🇺🇦 Urdu' : '🇵🇰 Translate to Urdu'}
          </button>
        </>
      )}
      {!isLoggedIn && (
        <div className="auth-prompt">
          <span>Sign in to personalize content and translate to Urdu</span>
        </div>
      )}
      {/* Render the content, potentially personalized or translated */}
      <div className="content-container">
        {isLoading ? (
          <div className="loading-indicator">Processing...</div>
        ) : isTranslated ? (
          <div className="translated-content">
            <h3>اردو ترجمہ / Urdu Translation</h3>
            <div dangerouslySetInnerHTML={{ __html: translatedContent }} />
          </div>
        ) : isPersonalized ? (
          <div className="personalized-content">
            <p>Personalized content based on your background: {userBackground?.background || 'Not specified'}</p>
            {children}
          </div>
        ) : (
          children
        )}
      </div>
    </div>
  );
};

export default PersonalizationBar;